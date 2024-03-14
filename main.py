# Import necessary modules (assuming they provide MySQL-related functions)
from sqlfunction import *  # Import all functions for MySQL operations
from writeinSql import *  # Import functions related to writing SQL data
from terminalsql import *  # Import functions for terminal-based SQL interactions

# Initiate database connection with user authentication
connection = userconnect()
while connection == None:
    print('Login failed, enter the details again . . .')  # Notify user of failed attempt
    connection = userconnect()  # Retry connection

# Proceed with operations if connection is successful
if connection:
    # Write initial data to the database (functionality assumed in writeinsql())
    writeinsql()

    # Offer additional options to the user within a loop
    choice = ''
    while choice != True:  # Loop continues until user doesn't want more options
        choice = input("\n Choose do you want more options 'Y\\n' : ")

        if choice.lower() in ['yes', 'y']:
            # Display a menu of available options (defined in showoptions())
            showoptions()
            # Handle user's choice of action (implemented in optioninsql())
            optioninsql()
        else:
            break  # Exit the loop if user doesn't want more options