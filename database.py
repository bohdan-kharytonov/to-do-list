# This Python file uses the following encoding: utf-8
import sqlite3
import os.path

class database:
    def __init__(self):
        self.database_name = "todo.db"
#        if(os.path.isfile(self.database_name)):
        self.create_table()

    def create_table(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks(
        id INTEGER PRIMARY KEY,
        Content TEXT NOT NULL,
        Date TEXT NOT NULL
        )
        ''')

        connection.commit()
        connection.close()

    def get_data_from_database(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Tasks')
        tasks = cursor.fetchall()
        print(len(tasks))
        for task in tasks:
            print(task)

        connection.close()
        return tasks

    def input_data_to_database(self, content, date):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Tasks (Content, Date) VALUES (?, ?)', (str(content), str(date)))

        connection.commit()
        connection.close()
