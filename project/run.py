from dotenv import load_dotenv
from colorama import just_fix_windows_console, init
from db_operations import OperationDataBase
import hey

if __name__ == '__main__':
    load_dotenv() 
    just_fix_windows_console()
    init(autoreset=True)

    hey.dog()
    test=OperationDataBase.test()


