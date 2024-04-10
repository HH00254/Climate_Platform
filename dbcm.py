"""
Description: Database Context Manager
Author: Lance Fuentes, Al Hochbaum, Christian Requerme
Section Number: FTO01
Date Created: 03/21/24
Credit:
Updates:
"""
<<<<<<< HEAD


import sqlite3
from contextlib import ContextDecorator
=======
from contextlib import ContextDecorator
import sqlite3
from prod_util import ProdUtil
>>>>>>> 1a34288dbee26ff68c9996da2b45bad0589e4f24

class DBCM(ContextDecorator):
    """
    A context manager for managing SQLite database connections.

    Usage:
    ```
    with DBCM('database.db') as cursor:
        cursor.execute("SELECT * FROM table_name")
        result = cursor.fetchall()
    ```

    When exiting the context, the changes are committed if no exceptions occurred, otherwise,
      they are rolled back.
    """

    def __init__(self, db_name):
        """
        Initialize the DBCM context manager.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """
        Enter the context and establish a connection to the SQLite database.

        Returns:
            sqlite3.Cursor: A cursor object for executing SQL queries.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            return self.cursor
<<<<<<< HEAD
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)
=======

        except sqlite3.Error as e:
            ProdUtil.system_log(e, e.args)
            print("Error connecting to the database:", e)

>>>>>>> 1a34288dbee26ff68c9996da2b45bad0589e4f24
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the context and commit or rollback changes to the database.

        Args:
            exc_type (type): The type of the exception that occurred, if any.
            exc_value (Exception): The exception instance that occurred, if any.
            traceback (traceback): The traceback object associated with the exception, if any.
        """
        if exc_type is not None:
            print("Exception occured, rollback changes:", exc_value)
            self.conn.rollback()
<<<<<<< HEAD
=======

>>>>>>> 1a34288dbee26ff68c9996da2b45bad0589e4f24
        else:
            try:
                self.conn.commit()
            except sqlite3.Error as e:
<<<<<<< HEAD
                print("Error commiting changes to the database:", e)
                self.conn.rollback()
                print("Rollback changes.")
        self.cursor.close()
        self.conn.close()
=======
                ProdUtil.system_log(e, e.args)
                print("Error commiting changes to the database:", e)

                self.conn.rollback()
                print("Rollback changes.")

        self.cursor.close()
        self.conn.close()
>>>>>>> 1a34288dbee26ff68c9996da2b45bad0589e4f24
