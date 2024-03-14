from sqlfunction import *



def classinSql():
    """
    Attempts to create databases named CLASS_1 to CLASS_12 (inclusive) in the connected MySQL server.

    This function connects to the MySQL server using `mysql_connect` (function not shown),
    creates a cursor object for executing queries, and iterates through a loop from 1 to 12.
    For each iteration, it constructs a database name in the format 'CLASS_{number}' and attempts
    to create that database using `CREATE DATABASE`.

    **Note:** This function catches any exceptions (errors) during the creation operation but does not
    print them by default. Consider uncommenting the `print(Error)` line for debugging purposes.

    Returns:
        None (no specific return value)
    """

    connection = mysql_connect()  # Connect to MySQL server (function not shown)
    cursor = connection.cursor()  # Create a cursor object

    for number in range(1, 13):  # Loop through numbers 1 to 12
        classno = f'CLASS_{number}'  # Construct database name

        try:
            cursor.execute(f'CREATE DATABASE {classno};')  # Attempt to create the database
        except Exception as Error:
            pass  # Silently handle exceptions (consider uncommenting print(Error) for debugging)



def tablesinsql():
    """
    Creates tables named "Students" in all previously created databases (CLASS_1 to CLASS_12).

    This function calls `classinSql` (presumably defined elsewhere) to ensure the databases
    exist before creating tables. It then connects to the MySQL server (assuming `mysql_connect`
    establishes a connection) and creates a cursor object for executing queries.

    The function iterates through a loop from 1 to 12, constructing database names in the
    format 'CLASS_{number}'. Inside the loop:

    1. It attempts to create a table named "Students" within the current database using
       `CREATE TABLE`.
    2. The table definition includes columns:
       - Rollno (INT, PRIMARY KEY): Unique integer identifier for students.
       - Name (varchar(50), NOT NULL): Student's name (cannot be empty).
       - DOB (DATE, NOT NULL): Student's date of birth (cannot be empty).
       - LOC (VARCHAR(50)): Student's location (optional).
    3. After creating the table, the function commits the changes using `cursor.commit()`.

    **Note:** This function catches any exceptions (errors) during the table creation but does not
    print them by default. Consider uncommenting the `#print(Error)` line for debugging purposes.

    Returns:
        None (no specific return value)
    """

    classinSql()  # Call function to create databases (assumed to exist before creating tables)

    connection = mysql_connect()  # Connect to MySQL server (function not shown)
    cursor = connection.cursor()  # Create a cursor object

    for number in range(1, 13):  # Loop through numbers 1 to 12
        classno = f'CLASS_{number}'  # Construct database name

        try:
            cursor.execute(f'CREATE TABLE {classno}.Students (Rollno INT PRIMARY KEY, Name varchar(50) NOT NULL, DOB DATE NOT NULL, LOC VARCHAR (50));')
            cursor.commit()  # Commit changes after table creation
        except Exception as Error:
            pass  # Silently handle exceptions (consider uncommenting print(Error) for debugging)



def dataintable(tablename):
    """
    Inserts sample student data into the specified table named "tablename".

    This function assumes `tablesinsql` (defined elsewhere) has already created the tables.
    It connects to the MySQL server (assuming `mysql_connect` establishes a connection)
    and creates a cursor object for executing queries.

    The function defines a list `Studentlist` containing sample student data tuples.
    Each tuple represents a student record with values for:
        - Rollno (INT)
        - Name (varchar(50))
        - DOB (DATE) in YYYY-MM-DD format
        - LOC (VARCHAR(50)) (optional)

    The function iterates through the `Studentlist`, unpacking each tuple (`element`).
    Inside the loop:

    1. It constructs an `INSERT INTO` statement dynamically using f-strings to insert
       the current student data (`element`) into the specified table (`tablename`).
    2. The function then executes the constructed `INSERT INTO` statement using `cursor.execute`.
    3. Finally, after iterating through all students, the function commits the changes using
       `connection.commit`.

    **Note:** The commented-out `#print(element)` line can be used for debugging purposes
    to see the individual student data being inserted.

    Args:
        tablename (str): The name of the table to insert data into.

    Returns:
        None (no specific return value)
    """

    tablesinsql()  # Call function to ensure table exists (assumed)

    connection = mysql_connect()  # Connect to MySQL server (function not shown)
    cursor = connection.cursor()  # Create a cursor object

    Studentlist = ((1, 'Kim Jisoo', '1995-01-03', 'South Korea'),
                   (2, 'Jennie Kim', '1995-01-03', 'South Korea'),
                   (3, 'Park Chaeyoung', '1997-02-11', 'New Zealand'),
                   (4, 'Lalisa Manoban', '1997-03-27', 'South Korea'),)

    for element in Studentlist:
        # print(element)  # Uncomment for debugging (optional)
        cursor.execute(f'INSERT INTO {tablename}.Students VALUES {element}')

    connection.commit()  # Commit changes after inserting all student data



def writeinsql():
    """
    Iterates through class names (CLASS_1 to CLASS_12) and inserts sample student data into
    corresponding tables in the MySQL database.

    This function iterates through a loop from 1 to 12, constructing class names (databases)
    in the format 'CLASS_{number}'. Inside the loop:

    1. It attempts to insert sample student data into the corresponding table using the
       `dataintable` function (assumed to be defined elsewhere). The table name is passed
       as the `tablename` argument to `dataintable`.
    2. The function uses a `try-except` block to handle any exceptions (errors) that might occur
       during the data insertion process. By default, exceptions are silently passed (not printed).
       Consider uncommenting `#print(Error)` for debugging purposes.

    Returns:
        None (no specific return value)
    """

    for number in range(1, 13):
        classno = f'CLASS_{number}'  # Construct class name (database name)

        try:
            dataintable(tablename=classno)  # Call function to insert data into corresponding table
        except Exception as Error:
            pass  # Silently handle exceptions (consider uncommenting print(Error) for debugging)