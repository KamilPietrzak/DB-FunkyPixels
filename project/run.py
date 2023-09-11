# Import packages
from dotenv import load_dotenv  # Import load_dotenv from the python-dotenv package.
from colorama import just_fix_windows_console, init # Import just_fix_windows_console and init from the colorama package.
# Import files
from db_operations import OperationsDatabase # Import class OperationsDatabase from the db_operations.py file.
import hey # Import all from the hey.py file.


# This code start only when variable __name__ has the '__main__' value, for the run.py file. 
if __name__ == '__main__':
    load_dotenv() # Parse a .env file and then load all the variables found as environment variables.
    just_fix_windows_console() # Reportedly, this code  is used to make sure the colorama works the same on both Linux and Windows.
    init(autoreset=True) # Init autostart style for colorama. Every prints have reset styles.

    hey.dog() # Call function dog() from hey.py file.
    OperationsDatabase() # Call class OperationsDatabase() from db_operations.py file.