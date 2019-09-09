import logging
import pandas
import pymysql
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.sql import text


class DatabaseConnection(object):
    """ This is an object for a database connection
	"""

    def __init__(
        self,
        username,
        password,
        host,
        port,
        database,
        dialect="mysql",
        driver="pymysql",
        logpath="database.log",
    ):
        """ Initializes db conn object
		"""
        self.dialect = dialect
        self.driver = driver
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.logpath = logpath
        logging.basicConfig(
            filename=logpath,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
        )
        self.logger = logging.getLogger("DatabaseConnection")
        self.logger.info("Ready to connect to DB")

    def connect(self):
        """ Function to connect to database
		"""
        try:
            self.engine = create_engine(
                self.dialect
                + "+"
                + self.driver
                + "://"
                + self.username
                + ":"
                + self.password
                + "@"
                + self.host
                + ":"
                + self.port
                + "/"
                + self.database
            )
            self.conn = self.engine.connect()
            self.logger.info(
                "Connected to "
                + self.host
                + " as "
                + self.username
                + " on port "
                + self.port
                + " using database "
                + self.database
            )
        except:
            print("Could not connect")
            self.logger.error("Could not connect, try reinitializing connection INFO")

    def disconnect_db(self):
        """ Function to disconnect from current connection
        """
        self.conn.close()
        self.logger.info(
            "Disconnected from "
            + self.host
            + " as "
            + self.username
            + " on port "
            + self.port
            + " and on database "
            + self.database
        )

    def execute_query(self, query):
        """ Execute execute_query
        """
        try:
            self.conn.execute(query)
            self.logger.info("Ran query " + query)
        except StatementError:
            self.logger.error("Ran into error on " + query)

    def write_to_sql(self, data, tablename, if_exists="append"):
        """ Write to sql table
        """
        data.to_sql(tablename, self.engine, if_exists=if_exists, index=False)
