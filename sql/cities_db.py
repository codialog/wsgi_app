import sqlite3

from sql.base_db import BaseDB


class CityDB(BaseDB):

    def __init__(self):
        BaseDB.__init__(self)
        self.table_name = 'city'

    def create_db_if_not_exists(self):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS {}(
                city_id INTEGER PRIMARY KEY,
                country_id INTEGER NOT NULL,
                region_id INTEGER NOT NULL ,
                name TEXT NOT NULL)
        """.format(self.table_name)
        cursor.execute(query)
        connect.commit()
        connect.close()

    def fill_city_table(self, data):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            INSERT INTO {}(
                city_id, country_id, region_id, name
                ) 
                VALUES (?, ?, ?, ?)
        """.format(self.table_name)
        try:
            for cities in data:
                for city in cities:
                    cursor.execute(query, city)
                connect.commit()
        except Exception as ex:
            print(ex)
        finally:
            connect.close()
