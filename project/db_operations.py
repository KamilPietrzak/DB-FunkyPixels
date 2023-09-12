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

    # The __extensioninit() method is used to create all the required postgreSQL extensions.
    # If an exception occurs, the method rolls back all changes, calls the __close() method and raises an InitExtensionError.  
    def __extensioninit(self):

        # Try to create the uuid-ossp extension.
        try:
            self.cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitExtensionError(error=error, extension="uuid-ossp")
        

    # The __tableinit() method is used to create all the required tables. 
    # If an exception occurs, the method rolls back all changes, calls the __close() method, and raises an InitTableError.   
    def __tableinit(self):

        # Try to create the users table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
	            id serial NOT NULL UNIQUE PRIMARY KEY,
	            UID UUID NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
	            username varchar(256) NOT NULL UNIQUE,
	            email varchar(256) NOT NULL UNIQUE,
	            password varchar(256) NOT NULL,
	            created date DEFAULT CURRENT_DATE
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="user")
        
        # Try to create the roles table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS roles(
	            id smallserial NOT NULL UNIQUE PRIMARY KEY,
	            role varchar(255) NOT NULL UNIQUE
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="roles")
        
        # Try to create the admins table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS admins(
	            id smallserial NOT NULL UNIQUE PRIMARY KEY,
	            AID UUID NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
	            role_id smallint NOT NULL REFERENCES roles(id),
	            user_id integer NOT NULL UNIQUE REFERENCES users(id),
	            password varchar(256) NOT NULL,
	            created date DEFAULT CURRENT_DATE
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="admins")
        
        # Try to create the bans table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS bans(
	            id serial NOT NULL UNIQUE PRIMARY KEY,
	            user_id integer NOT NULL UNIQUE REFERENCES users(id),
	            comment varchar(256) NOT NULL,
	            deadline date DEFAULT CURRENT_DATE
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="bans")
        
        # Try to create the posts table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS posts(
	            id serial NOT NULL UNIQUE PRIMARY KEY,
	            PID UUID NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
	            author_id integer NOT NULL REFERENCES users(id),
	            title varchar(256) NOT NULL,
	            created timestamp DEFAULT NOW()
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="posts")
        
        # Try to create the comments table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS comments(
	            id serial NOT NULL UNIQUE PRIMARY KEY,
	            CID UUID NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
				post_id integer NOT NULL REFERENCES posts(id),
	            author_id integer NOT NULL REFERENCES users(id),
	            body varchar(256) NOT NULL,
	            created timestamp DEFAULT NOW()
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="comments")
        
        # Try to create the replies table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS replies(
	            id serial NOT NULL UNIQUE PRIMARY KEY,
	            RID UUID NOT NULL UNIQUE DEFAULT uuid_generate_v1(),
				comment_id integer NOT NULL REFERENCES comments(id),
	            author_id integer NOT NULL REFERENCES users(id),
	            body varchar(256) NOT NULL,
	            created timestamp DEFAULT NOW()
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="replies")
        
        # Try to create the tags table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS tags(
	            id serial NOT NULL UNIQUE PRIMARY KEY,
	            tag varchar(256) NOT NULL
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="tags")
        
        # Try to create the tag_relations table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS tag_relations(
				tag_id integer NOT NULL REFERENCES tags(id),
	            post_id integer NOT NULL REFERENCES posts(id)
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="tag_relations")
        
        # Try to create the likes table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS likes(
				post_id integer NOT NULL REFERENCES posts(id),
	            user_id integer NOT NULL REFERENCES users(id)
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="likes")
        
        # Try to create the follows table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS follows(
				follower_id integer NOT NULL REFERENCES users(id),
	            followed_id integer NOT NULL REFERENCES users(id)
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="follows")
        
        # Try to create the icons table.
        try:
            self.cur.execute("""
            CREATE TABLE IF NOT EXISTS icons(
	            id smallserial NOT NULL UNIQUE PRIMARY KEY,
	            address varchar(256) NOT NULL
            );""")
        except Exception as error:
            self.con.rollback() # Back all changes.
            self.__close()
            raise InitTableError(error=error, table="icons")

    # The __close() method is used to close the cursor and connection with the database server.
    def __close(self):
        self.cur.close()
        self.con.close()
    
    def __run(self):
        self.__extensioninit()
        self.__tableinit()
        self.__close()