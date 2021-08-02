from os.path import isfile
from sqlite3 import connect
import asyncio

__version__ = "0.0.2"

class DB:
    """Defines a database instance"""
    __slots__ = ("db_path", "build_path", "connection", "cursor")

    def __init__(self, db_path: str, build_path: None):
        self.db_path = db_path
        self.build_path = build_path
        self.connection = connect(db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def test(self):
        """Test if the database is valid"""
        print(self.connection)
        print(self.cursor)
        print(self.db_path)
        print(self.build_path)

    def build(self):
        if isfile(self.build_path):
            with open(self.build_path, "r", encoding="utf-8") as script:
                self.cursor.executescript(script.read())
    
    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def field(self, command, *values):
        self.cursor.execute(command, tuple(values))

        if (fetch := self.cursor.fetchone()) is not None:
            return fetch[0]

    def record(self, command, *values):
        self.cursor.execute(command, tuple(values))

        return self.cursor.fetchone()

    def records(self, command, *values):
        self.cursor.execute(command, tuple(values))

        return self.cursor.fetchall()

    def column(self, command, *values):
        self.cursor.execute(command, tuple(values))

        return [item[0] for item in self.cursor.fetchall()]
    
    def execute(self, command, *values):
        self.cursor.execute(command, tuple(values))

    def multiexec(self, command, valueset):
        self.cursor.executemany(command, valueset)