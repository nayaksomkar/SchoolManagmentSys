# Import all functions from the sqlfunction module (replace with specific imports if needed)
from sqlfunction import *  # Assuming this imports necessary MySQL functions

def showoptions():
    """
    Presents a menu of options to the user for interacting with student databases.
    """
    print(f'''
          ------------- OPTIONS -------------
          1. Show class databases
          2. Show all student's records (from a chosen database)
          3. Add a student's record (to a chosen database)
          4. Exit from options
          ''')

def optioninsql():
    """
    Handles user input for choosing an option and performs the selected action.
    """
    option = input('Choose an option : ')

    if option in ['1', '2', '3']:
        # Retrieve available class databases
        databases = showdb()  # Assuming this function retrieves database names

        print('\n', 10 * ' ', '------ CLASS DATABASES ------', sep='')
        for database in databases:
            print(16 * ' ', database[0])  # Assuming databases is a list of tuples

    if option in ['2', '3']:
        # Get database selection from user
        database = input('\nChoose a database from the following databases : ')

        while (database.upper(),) not in databases:  # Validate chosen database
            print('\n', 10 * ' ', '------ CLASS DATABASES ------', sep='')
            for database in databases:
                print(16 * ' ', database[0])
            database = input('\nChoose a database from the following databases : ')

    # Handle specific options based on user selection

    elif option == '2':
        # Show all student records (existing functionality)
        records = showtableall(database_name=database.upper())  # Assuming this retrieves records
        print('Rollno.', 'Name', 'DOB', 'LOC', sep=' '*8)
        for record in records:
            print(record)

    elif option == '3':
        # Add a student's record (existing functionality)
        connection = mysql_connect()  # Connect to MySQL server (function not shown)
        cursor = connection.cursor()  # Create a cursor object

        print("\nEnter details to add in the student's record . . .")
        Rollno = input('Enter the Rollno. : ')
        Name = input('Enter the Name : ')
        DOB = input('Enter the DOB : ')
        LOC = input('Enter the LOC : ')

        value = (int(Rollno), Name, DOB, LOC)
        cursor.execute(f'INSERT INTO {database.upper()}.Students VALUES {value}')
        print('Record added successfully.')
        connection.commit()  # Commit changes

        # Refresh records for display
        records = showtableall(database_name=database.upper())
        print('Rollno.', 'Name', 'DOB', 'LOC', sep=' '*8)
        for record in records:
            print(record)

    else:
        pass  # Handle invalid options (already exists)