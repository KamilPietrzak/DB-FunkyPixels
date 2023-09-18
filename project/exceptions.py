from sys import exit # Import exit function from sys.
from colorama import * # Import all from the colorama package.

# This defined Exception has a message that provides information about .env file error or database error.
# This class is called when psycopg2 is trying to connect with the database and raises the OperationalError exception. 
# Situations in which when psycopg2 raises the OperationalError exception for psycopg2.connect() function:
# - the .env file is not exist,
# - some rquired variables is missed,
# - some of the variable values are incorrect,
# - the database doesn't exist.
# The __executexception() method is used to display the error message and terminate the program immediately.
class ConnectOperationalError(Exception):
    def __init__(self):
        self.message = f"""{Back.RED}{Fore.BLACK}Error:{Back.RESET}{Fore.RED} Something went wrong. It's possible that the .env file doesn't exist or that some required variables are missing, 
        or that the database doesn't exist.\n
        - Please make sure that there is .env file in the project folder.
        - Please make sure thet there are required variables, like HOST, PORT, USER and PASSWORD, in there .env file.
        - Please make sure that the environments value is correct.
        - Please make sure that the database called 'dbfunkypixels' exists on your server.
        \nExample project\.env file:\n{Fore.YELLOW}
        HOST = '127.0.0.1'
        PORT = 5432
        USER= 'postgres'
        PASSWORD = 'password'
        """
        self.__executexception()

    def __executexception(self):
        print(self.message)
        return exit(1) #Terminate the program immediately.

# This defined Exception has a message that provides information about unexpected exceptions.
# This class is called when psycopg2 is trying to connect with the database and raises any Exception except the OperationalError exception.
# The __executexception() method is used to display the error message and terminate the program immediately.
class ConnectSomethingWentWrong(Exception):
    def __init__(self, error):
        self.message = f"{Back.RED}{Fore.BLACK}Error:{Back.RESET}{Fore.RED} {str(error)}"
        self.__executexception()

    def __executexception(self):
        print(self.message)
        return exit(1) #Terminate the program immediately.
    
# This defined Exception has a message that provides information about certain problems encountered during the creation of certain extensions.
# This class is called when __extensioninit() encounters problems while creating certain extensions.
# The message includes information about which extension wasn't created and the full text of the error.
class InitExtensionError(Exception):
    def __init__(self, error, extension):
        self.message = f"""{Back.RED}{Fore.BLACK}Error:{Back.RESET}{Fore.RED} During the attempt to create the {extension} extension, 
        something went wrong. Here is the full text of the error: \n {str(error)}"""
        self.__executexception()

    # The __executexception() method is used to display the error message and terminate the program immediately.
    def __executexception(self):
        print(self.message)
        return exit(1) #Terminate the program immediately.
    
# This defined Exception has a message that provides information about certain problems encountered during the creation of certain tables.
# This class is called when __tableinit() encounters problems while creating certain tables.
# The message includes information about which table wasn't created and the full text of the error.    
class InitTableError(Exception):
    def __init__(self, error, table):
        self.message = f"""{Back.RED}{Fore.BLACK}Error:{Back.RESET}{Fore.RED} During the attempt to create the {table} table, something went wrong. 
        Here is the full text of the error: \n {str(error)}"""
        self.__executexception()

    # The __executexception() method is used to display the error message and terminate the program immediately.
    def __executexception(self):
        print(self.message)
        return exit(1) #Terminate the program immediately.