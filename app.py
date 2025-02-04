from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import time

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect("emails.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            recipient TEXT,
            subject TEXT,
            content TEXT,
            timestamp INTEGER,
            editable_until INTEGER
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS version_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_id INTEGER,
            version TEXT,
            timestamp INTEGER,
            FOREIGN KEY (email_id) REFERENCES emails(id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper function to connect to the database
def query_db(query, args=(), one=False):
    conn = sqlite3.connect("emails.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def index():
    """Home page showing all sent emails."""
    emails = query_db("SELECT * FROM emails")
    return render_template("index.html", emails=emails)

@app.route("/send", methods=["GET", "POST"])
def send_email():
    """Route to send a new email."""
    if request.method == "POST":
        sender = request.form["sender"]
        recipient = request.form["recipient"]
        subject = request.form["subject"]
        content = request.form["content"]
        timestamp = int(time.time())
        editable_until = timestamp + 600  # Editable for 10 minutes

        conn = sqlite3.connect("emails.db")
        c = conn.cursor()
        c.execute("INSERT INTO emails (sender, recipient, subject, content, timestamp, editable_until) VALUES (?, ?, ?, ?, ?, ?)",
                  (sender, recipient, subject, content, timestamp, editable_until))
        email_id = c.lastrowid
        c.execute("INSERT INTO version_history (email_id, version, timestamp) VALUES (?, ?, ?)",
                  (email_id, content, timestamp))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))
    return render_template("send_email.html")

@app.route("/edit/<int:email_id>", methods=["GET", "POST"])
def edit_email(email_id):
    """Route to edit an existing email."""
    email = query_db("SELECT * FROM emails WHERE id = ?", [email_id], one=True)
    if not email:
        return "Email not found!", 404

    current_time = int(time.time())
    if current_time > email["editable_until"]:
        return "The editable window has expired!", 403

    if request.method == "POST":
        new_content = request.form["content"]
        timestamp = int(time.time())

        conn = sqlite3.connect("emails.db")
        c = conn.cursor()
        c.execute("UPDATE emails SET content = ? WHERE id = ?", (new_content, email_id))
        c.execute("INSERT INTO version_history (email_id, version, timestamp) VALUES (?, ?, ?)",
                  (email_id, new_content, timestamp))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("edit_email.html", email=email)

@app.route("/view/<int:email_id>")
def view_email(email_id):
    """Route to view email details."""
    email = query_db("SELECT * FROM emails WHERE id = ?", [email_id], one=True)
    version_history = query_db("SELECT version, timestamp FROM version_history WHERE email_id = ?", [email_id])
    if not email:
        return "Email not found!", 404
    return render_template("view_email.html", email=email, version_history=version_history)

@app.route("/delete/<int:email_id>", methods=["GET", "POST"])
def delete_email(email_id):
    """Route to delete an email (simulate unsend)."""
    email = query_db("SELECT * FROM emails WHERE id = ?", [email_id], one=True)
    if not email:
        return "Email not found!", 404

    current_time = int(time.time())
    if current_time > email["editable_until"]:
        return "The unsend window has expired!", 403

    query_db("DELETE FROM emails WHERE id = ?", [email_id])
    query_db("DELETE FROM version_history WHERE email_id = ?", [email_id])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
    
