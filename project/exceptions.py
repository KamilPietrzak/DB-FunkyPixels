from colorama import * # Import all from the colorama package.

# This defined Exception has a message that provides information about .env file error.
# This class is called when psycopg2 is trying to connect with the database and raises the OperationalError exception. 
# Situations in which when psycopg2 raises the OperationalError exception for psycopg2.connect() function:
# - the .env file is not exist,
# - some rquired variables is missed,
# - some of the variable values are incorrect.. 
class ConnectOperationalError(Exception):
    def __init__(self):
        self.message = Back.RED + Fore.BLACK + "Error:" + Back.RESET + Fore.RED + """ Something went wrong. Probably the .env file isn't exists or some required variables are lacking. \n
        - Please make sure that there is .env file in the project folder.
        - Please make sure thet there are required variables, like HOST, PORT, USER and PASSWORD, in there .env file.
        - Please make sure that the environments value is correct.
        \nExample project\.env file:\n""" + Fore.YELLOW + """
        HOST = '127.0.0.1'
        PORT = 5432
        USER= 'postgres'
        PASSWORD = 'password'
        """
        super().__init__(self.message) # Call the __init__() method in the parent class (Exception) and pass the variable 'self.message'.

# This defined Exception has a message that provides information about unexpected exceptions.
# This class is called when psycopg2 is trying to connect with the database and raises any Exception except the OperationalError exception.
class ConnectSomethingWentWrong(Exception):
    def __init__(self, error):
        self.message = Back.RED + Fore.BLACK + "Error:" + Back.RESET + Fore.RED + " " + str(error)
        super().__init__(self.message) # Call the __init__() method in the parent class (Exception) and pass the variable 'self.message'.

# This defined Exception is raised when psycopg2 attempts to connect with the database, and the database connection attempt is successful.
# This class has a variable called 'connect,' which includes a connection class from psycopg2.
class ConnectSuccess(Exception):
    def __init__(self, connect):
        self.connect=connect
        super().__init__(self.connect) # Call the __init__() method in the parent class (Exception) and pass the variable 'self.connect'.