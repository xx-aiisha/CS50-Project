Email Editing and Undo System
Overview
This project is a web-based Email Editing and Undo System. It allows users to:
- Compose and send emails.
- Edit sent emails within a 10-minute window.
- Unsend emails during the same timeframe.
- View sent emails along with their version history.
This system is a simulation of how email editing and unsending might work in a real-world application, implemented using Flask for the backend, SQLite for data storage, Bootstrap for styling, and JavaScript for interactivity.

features
1.Send Emails:
- Fill out a form with sender, recipient, subject, and content fields.
- Click "Send" to save the email in the database.
2. Edit Emails:
- Edit email content within a 10-minute window.
- A countdown timer on the editing page shows the time remaining to make changes.
- All edits are tracked in a version history for transparency.
3. Unsend Emails:
- Delete emails within the editable window.
- Once unsent, the email and its version history are permanently removed.
4. View Emails:
- View email details, including sender, recipient, subject, and content.
- Review the email’s version history, which records all edits made.

Installation and Setup
Requirements
- Python 3.7 or later
- Flask (Python web framework)
- SQLite (built into Python)
Installation Steps
1. Clone the Repository:
bash
 git clone <repository-url>
 cd <repository-name>

2. Install Dependencies:
 Install Flask and any other required libraries
 bash
  pip install flask

3. Initialize the Database:
  Run the application to automatically create the SQLite database:
  bash
   python app.py

4.Run the Application:
  Start the Flask development server:
  bash
   python app.py

How to Use
1. Sending an Email
- Navigate to the "Send New Email" page.
- Fill out the form with:
- Sender: Your email address.
- Recipient: The recipient's email address.
- Subject: The subject of the email.
- Content: The body of the email.
- Click "Send Email" to save the email in the database. You will be redirected to the home page, where you can see the list of all sent emails.


2. Editing an Email
- Click "Edit" next to an email on the home page.
- Modify the email content in the text box provided.
- A countdown timer will show the time remaining for editing.
- Once the time expires, the form will be disabled, and further edits will not be allowed.
- Click "Save Changes" to update the email. The changes will be saved to the database, and the previous content will be added to the version history.

3. Unsending an Email
- Click "Unsend" next to an email on the home page or on the email’s details page.
- Confirm the action in the dialog box.
- If the unsend window has not expired, the email will be permanently deleted from the database along with its version history.


4. Viewing an Email
- Click "View" next to an email on the home page.
- See details such as sender, recipient, subject, and content.
- Scroll down to view the version history of the email, which shows all past edits with timestamps.

Project Structure


- `app.py`: The main Flask application containing routes, database logic, and application logic.


-`templates/`:


 - `index.html`: Displays the list of sent emails.


 - `send_email.html`: A form for composing and sending new emails.


 - `edit_email.html`: A form for editing an email within the editable window.


 - `view_email.html`: Displays email details and version history.


- `emails.db`: SQLite database file storing emails and version history (auto-created).



Database Design


1. Emails Table:


  - `id`: Primary key for each email.


  - `sender`: Sender’s email address.


  - `recipient`: Recipient’s email address.


  - `subject`: Subject of the email.


  - `content`: Body of the email.


  - `timestamp`: Time the email was sent.


  - `editable_until`: Time until which the email can be edited or unsent.





2. Version History Table:


  - `id`: Primary key for each version.


  - `email_id`: Foreign key referencing the associated email.


  - `version`: Content of the email at a specific time.


  - `timestamp`: Time the version was saved.


Limitations


- No Authentication: Any user can access and manage emails. Future implementations could include user accounts for privacy.


- No Real Email Sending: This project simulates email functionality but does not send real emails.


- Hardcoded Editable Window: The 10-minute window is fixed in this implementation but could be made configurable.



Troubleshooting


- Error: `TemplateNotFound`**:


 - Ensure all templates are in a `templates/` folder in the same directory as `app.py`.


- Error: `Method Not Allowed`**:


 - Ensure "Unsend" uses a form with the `POST` method.


- Database Not Updating:


 - Check if `emails.db` exists in the project directory.


 - If not, restart the server to auto-create the database.

Future Work


- Add user authentication to tie emails to individual accounts.


- Implement soft-deletes for recoverable unsending.


- Enhance frontend interactivity with JavaScript or AJAX for real-time updates.

Author
Aisha Ahmed
CS50 Final Project, December 2024

