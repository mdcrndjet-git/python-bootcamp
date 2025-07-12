"""
Build a Simple Shopping List Web App with Flask

In this lab session, you will create a simple Shopping List application where users can:
    Add shopping items.
    Mark items as bought.
    Delete items.
    View the current shopping list.

You will use Flask to build the application. The data will be stored in-memory (no need for a database).
Items will persist for the duration of the session, but once the server is restarted, all items will be lost.

Requirements:
    Flask: You will use Flask to build the web application.
    HTML and Forms: Use HTML forms to handle item input and actions.

Step 1: Setup Flask Application
-------------------------------
Create a Flask app named app.py:

    Initialize a Flask app and set up basic routes (/ for the homepage, /add for adding items, /bought for marking as bought, /delete for deleting items).
    Use an in-memory list to store the items (e.g., shopping_list = []).

Step 2: Display Items
---------------------
On the home page, display the current list of shopping items in a list format.

    Each item should have a checkbox or button to mark it as bought.
    Each item should also have a delete button to remove it from the list.

Step 3: Add a New Item
----------------------
Create a form where users can add a new item. When the form is submitted, add the item to the list.

    The form should take a single input (item name).
    After adding the item, redirect the user back to the homepage.

Step 4: Mark Item as Bought
---------------------------
Next to each item, provide a button or checkbox that lets the user mark it as bought.

    When the button is clicked, update the item in the list to mark it as bought.

Step 5: Delete an Item
----------------------
Each item should have a button to delete it. When clicked, remove the item from the list.

Step 6: Basic Styling (Optional)
--------------------------------
Add some simple styling to make the app look clean. You can use an external CSS file or inline styles.

Additional Features (Optional):
-------------------------------
    Allow the user to filter items (e.g., show only bought items, or show only unbought items).
    Persist the items to a file (e.g., a JSON file) so that items are saved even when the app restarts.
"""
