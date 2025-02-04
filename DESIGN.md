Design Document: Email Editing and Undo System

Overview
This project is an Email Editing and Undo system built using Flask as the backend framework, SQLite for data storage, Bootstrap for styling, and JavaScript for interactivity. It allows users to send emails, edit them within a 10-minute window, and unsend emails within the same timeframe. The system includes a version history feature to track all changes made to an email, ensuring transparency.

The project is designed as a controlled simulation of how such features could work in real-world email systems, such as Gmail.

Features
1. Send Emails:
   - Users can compose and send emails with fields for the sender, recipient, subject, and content.
   - Emails are stored in an SQLite database, with a timestamp indicating when they were sent.

2. Edit Emails:
   - Users can edit emails within a 10-minute window after sending.
   - All edits are tracked in a `version_history` table for accountability.
   - A countdown timer is displayed on the editing page to show the time remaining.

3. Unsend Emails:
   - Users can unsend emails within the editable window.
   - Unsending deletes the email and all its associated version history from the database.

4. View Emails:
   - Users can view the details of a sent email, including its version history.

---

Technical Implementation

1. Backend Design
The backend is implemented using Flask, a lightweight Python web framework. Key components include:

Routes
- `/`: Displays a list of all sent emails.
- `/send`: Handles the creation and storage of new emails.
- `/edit/<email_id>`: Allows users to edit an email within the 10-minute editable window.
- `/delete/<email_id>`: Allows users to unsend an email within the editable window.
- `/view/<email_id>`: Displays the details of a single email and its version history.

Database Design
-Emails Table:
  Stores all emails sent by users, including:
  - `id` (Primary Key)
  - `sender`
  - `recipient`
  - `subject`
  - `content`
  - `timestamp`
  - `editable_until` (10 minutes after `timestamp`)

- Version History Table:
  Tracks all edits made to emails:
  - `id` (Primary Key)
  - `email_id` (Foreign Key referencing `Emails`)
  - `version` (Content of the email at a given point)
  - `timestamp` (Time when the version was saved)

Logic
- Editable Window: Enforced by comparing the current timestamp with the `editable_until` field in the `emails` table. Attempts to edit or delete emails after this window result in an error.
- Version Tracking: Each edit appends a new entry to the `version_history` table with the updated content and timestamp.

---

2. Frontend Design
The frontend is implemented using HTML, Bootstrap, and JavaScript.

HTML and Bootstrap**
Bootstrap is used to style the application for a clean and responsive design. Key UI elements include:
- Forms: For sending and editing emails.
- Tables and Lists: To display emails and version histories.
Buttons: Styled with Bootstrap classes for actions like edit, view, and unsend.

JavaScript
- A countdown timer is implemented on the email editing page using JavaScript to dynamically display the remaining editable time. Once the time expires, the form is disabled to prevent further edits.

Design Decisions

Why Flask?
Flask was chosen for its simplicity and flexibility. Its minimalistic design allows for quick development, making it ideal for a project focused on showcasing functionality rather than complex infrastructure.

Why SQLite?
SQLite is lightweight and easy to integrate with Flask. Its simplicity ensures that data persistence is handled efficiently without requiring a separate database server, which aligns with the project’s scope.

Why Bootstrap?
Bootstrap was used to simplify the styling process and ensure that the application is mobile-friendly and visually appealing without requiring extensive custom CSS.

Why JavaScript?
JavaScript was added for dynamic interactivity, such as the countdown timer on the editing page and confirmation dialogs for unsending emails. These features enhance the user experience and align with modern web application standards.

Challenges and Solutions
1. Editable Window Enforcement:
   - Challenge: Ensuring emails could only be edited or unsent within the 10-minute window.
   - Solution: A `timestamp` comparison is implemented in both the backend logic and the frontend timer.

2. Version History:
   -Challenge: Tracking changes without overwriting previous versions.
   - Solution: A separate `version_history` table was introduced to store each version of the email content.

3. Error Handling
   - Challenge: Informing users when actions fail (e.g., editing or deleting after the window).
   - Solution: Flask returns clear error messages, and the frontend displays them appropriately.

Limitations and Future Improvements
Limitations
- No User Authentication:
  - Emails are not tied to specific users, so there’s no privacy or security mechanism.
- No Real Email Delivery:
  - This system only simulates email functionality and does not send real emails.

Future Improvements
1. User Authentication:
   - Add login functionality to tie emails to specific users.
2.Soft Deletes:
   - Instead of permanently deleting emails, implement a "soft delete" system where emails are recoverable for a limited time.
3. Mock API:
   - Simulate integration with a real email service (e.g., Gmail) using a mock API.

---

Conclusion
This project demonstrates how an email editing and undo system can be implemented in a controlled environment. The use of Flask, SQLite, Bootstrap, and JavaScript showcases a combination of backend and frontend development skills, meeting the scope and complexity expected of a CS50 final project. It is a proof-of-concept for features that could be integrated into real-world email systems.
