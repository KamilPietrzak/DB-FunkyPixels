# Import packages
from os import getenv # Import getenv function from os.
from colorama import * # Import all from the colorama package.
import psycopg2 # Import all from the psycopg2 package.
import json # Import all from the json package.
# Import files
from exceptions import * # Import exceptions function from exceptions.py.

# A function used to execute a database connection and raise the appropriate exception with specified parameters.
# If psycopg2.connect() raises an OperationalError, then the connect() function raises a ConnectOperationalError without parameters.
# If psycopg2.connect() raises any Exception except for OperationalError,
# then the connect() function raises a ConnectSomethingWentWrong exception with a parameter called 'error', 
# including the raised Exception from psycopg2.connect().
# If psycopg2.connect() doesn't raise any Exception, then that means the connection is successful. 
# The connect() function return connection class.
def connect():
    try:
      return psycopg2.connect(host=getenv('HOST'), port=getenv('PORT'), user=getenv('USER'), password=getenv('PASSWORD'), dbname="dbfunkypixels")
    except psycopg2.OperationalError:
        raise ConnectOperationalError()
    except Exception as error:
        raise ConnectSomethingWentWrong(error)

# A class OperationsDatabase used to execute all required operations, such as 'CREATE TABLE', to create a database.
class OperationsDatabase():

    # The init() method first calls the __connect() method in order to obtain the connection class. After that, 
    # the method calls the __run() method in order to execute the next step.
    def __init__(self):
        self.con=self.__connect()
        self.cur=self.con.cursor()
        self.data=self.__getquery()
        self.__run()

    # The __connect() method execute the connect() function, set autocommit on True and return the variable colled 'conn' as the connection class.
    def __connect(self):
        with connect() as conn:
            conn.autocommit = True
            return conn
    
    # The __getquery() method is used to get query database from jeson file.
    def __getquery(self):
        with open('query.json') as file:
            return json.load(file)

    # The __extensioninit() method is used to create all the required postgreSQL extensions.
    # If an exception occurs, the method rolls back all changes, calls the __close() method and raises an InitExtensionError.  
    def __extensioninit(self):
        for extension in self.data['extensions']:
            try:
                self.cur.execute(extension['query'])
            except Exception as error:
                self.con.rollback() # Back all changes.
                self.__close()
                raise InitTableError(error=error, table=extension['name'])
        del data # Del data variable.
        print(f"{Back.GREEN}{Fore.BLACK}SUCCESS:{Back.RESET}{Fore.GREEN} Created all tables is successful.")
        

    # The __tableinit() method is used to create all the required tables. 
    # If an exception occurs, the method rolls back all changes, calls the __close() method, and raises an InitTableError.   
    def __tableinit(self):
        for table in self.data['tables']:
            try:
                self.cur.execute(table['query'])
            except Exception as error:
                self.con.rollback() # Back all changes.
                self.__close()
                raise InitTableError(error=error, table=table['name'])
        del data # Del data variable.
        print(f"{Back.GREEN}{Fore.BLACK}SUCCESS:{Back.RESET}{Fore.GREEN} Created all tables is successful.")

    # The __close() method is used to close the cursor and connection with the database server.
    def __close(self):
        self.cur.close()
        self.con.close()
    
    def __run(self):
        self.__extensioninit()
        self.__tableinit()
        self.__close()