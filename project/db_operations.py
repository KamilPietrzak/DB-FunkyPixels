from os import getenv # Import getenv function from os.
from sys import exit # Import exit function from sys.
from exceptions import * # Import exceptions function from exceptions.py.
import psycopg2 # Import all from the psycopg2 package.

# A function used to execute a database connection and raise the appropriate exception with specified parameters.
# If psycopg2.connect() raises an OperationalError, then the connect() function raises a ConnectOperationalError without parameters.
# If psycopg2.connect() raises any Exception except for OperationalError,
# then the connect() function raises a ConnectSomethingWentWrong exception with a parameter called 'error', 
# including the raised Exception from psycopg2.connect().
# If psycopg2.connect() doesn't raise any Exception, then that means the connection is successful. 
# The connect() function set autocommit on True and raises a ConnectSuccess exception with a variable called 'connect,' indicating a connection class.
def connect():
    try:
      connect=psycopg2.connect(host=getenv('HOST'), port=getenv('PORT'), user=getenv('USER'), password=getenv('PASSWORD'))
    except psycopg2.OperationalError:
        raise ConnectOperationalError()
    except Exception as error:
        raise ConnectSomethingWentWrong(error)
    else:
        raise ConnectSuccess(connect)

# A class OperationsDatabase used to execute all required operations, such as 'CREATE TABLE', to create a database.
class OperationsDatabase():

    # The init() method first calls the __connect() method in order to obtain the connection class. After that, 
    # the method calls the __run() method in order to execute the next step.
    def __init__(self):
        self.cur=self.__connect()
        self.__run()

    # The __connect() method tries to execute the connect() function. If the method encounters a ConnectOperationalError exception or a ConnectSomethingWentWrong exception,
    # then the method prints an error message and immediately terminates the program. Otherwise, it returns the connection class.
    def __connect(self):
        try:
            connect()
        except (ConnectOperationalError or ConnectSomethingWentWrong) as e:
            print(e.message)
            return exit(1) # Immediately terminates the program.
        except ConnectSuccess as e:
            return e.connect.cursor()
    
    def __run(self):
        pass #Next step