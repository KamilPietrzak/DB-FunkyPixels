from os import getenv # Import getenv function from os.
from exceptions import * # Import exceptions function from exceptions.py.
import psycopg2 # Import all from the psycopg2 package.

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
        self.__run()

    # The __connect() method execute the connect() function, set autocommit on True and return the variable colled 'conn' as the connection class.
    def __connect(self):
        with connect() as conn:
            conn.autocommit = True
            return conn

    # The __close() method is used to close the cursor and connection with the database server.
    def __close(self):
        self.cur.close()
        self.con.close()
    
    def __run(self):
        #Next step
        self.__close()