from colorama import *

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
        super().__init__(self.message)

class ConnectSomthingWentWrong(Exception):
    def __init__(self, error):
        self.message = Back.RED + Fore.BLACK + "Error:" + Back.RESET + Fore.RED + " " + str(error)
        super().__init__(self.message)

class ConnectSuccess(Exception):
    def __init__(self, connect):
        self.connect=connect
        super().__init__(self.connect)