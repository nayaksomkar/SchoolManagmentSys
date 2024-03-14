import mysql.connector as con  # Import the mysql.connector library and assign it an alias `con`



def mysql_connect(user='root', password='password'):
    """
    Establishes a connection to a MySQL database.

    This function attempts to connect to a MySQL database using the provided credentials.
    If successful, it returns the connection object. Otherwise, it returns None.

    Returns:
        A MySQL connection object if successful, otherwise None.
    """

    try:
        connection = con.connect(
        user=user,  # Username for the MySQL database (replace with your actual username)
        password=password,  # Password for the MySQL database (replace with your actual password)
        #host="localhost",  # Hostname of the MySQL server (uncomment if using a remote server)
        #database="mysql"  # Database name to connect to (uncomment if using a specific database)
        )

        if connection.is_connected():
            return connection

    except Exception as Error:
        pass
        #print("Error connecting to MySQL database:", Error)
        


def showdb():
    """
    Fetches a list of available databases on the connected MySQL server,
    excluding default system databases.

    This function connects to the MySQL server (using `mysql_connect`),
    executes a query to show all databases, and then filters out some
    predefined default system databases. The filtered list is returned.

    **Note:** This function modifies the retrieved list in-place.

    Returns:
        A list of tuples, where each tuple represents a non-default database name.
    """

    database = mysql_connect()  # Attempt to connect to the MySQL database

    if database:
        cursor = database.cursor()  # Create a cursor object to execute queries
        cursor.execute('SHOW DATABASES')  # Execute the query to list databases
        result = cursor.fetchall()  # Retrieve the query results

        # Predefined list of default system database names (modify if needed)
        defaultdb = [('information_schema',), ('my_database',), ('mysql',),
                     ('performance_schema',), ('sys',)]

        # Remove default databases from the results (modifies result in-place)
        for db in defaultdb:
            result.remove(db)

        return result  # Return the filtered list of database names
  
    

def userconnect():
    """
    Prompts the user for username and password, attempts to connect to the MySQL database
    using those credentials, and returns the connection object if successful.

    Returns:
        A MySQL connection object if successful, otherwise None (refer to mysql_connect documentation).
    """

    username = input('Enter the username : ')  # Prompt user for username
    password = input('Enter the password : ')  # Prompt user for password

    connection = mysql_connect(user=username, password=password)  # Attempt connection using user input

    return connection



def freshStart():
    """
    Attempts to drop all databases named CLASS_1 to CLASS_12 (inclusive) from the connected MySQL server.

    This function connects to the MySQL server using `mysql_connect` (function not shown),
    creates a cursor object for executing queries, and iterates through a loop from 1 to 12.
    For each iteration, it constructs a database name in the format 'CLASS_{number}' and attempts
    to drop that database using `DROP DATABASE`. 

    **Note:** This function catches any exceptions (errors) during the drop operation but does not
    print them by default. Consider uncommenting the `print(Error)` line for debugging purposes.

    Returns:
        None (no specific return value)
    """

    connection = mysql_connect()  # Connect to MySQL server (function not shown)
    cursor = connection.cursor()  # Create a cursor object

    for number in range(1, 13):  # Loop through numbers 1 to 12
        classno = f'CLASS_{number}'  # Construct database name

        try:
            cursor.execute(f'DROP DATABASE {classno};')  # Attempt to drop the database
        except Exception as Error:
            pass  # Silently handle exceptions (consider uncommenting print(Error) for debugging)

def showtableall(database_name):
    connection = mysql_connect()  # Connect to MySQL server (function not shown)
    cursor = connection.cursor()  # Create a cursor object

    try:
        cursor.execute(f'SELECT * FROM {database_name}.Students;')  # Attempt to drop the database
        return cursor.fetchall()
    
    except Exception as Error:
        print(Error)
        pass  # Silently handle exceptions (consider uncommenting print(Error) for debugging)