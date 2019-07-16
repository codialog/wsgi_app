import sqlite3

from sql.base_db import BaseDB


class RegionDB(BaseDB):

    def __init__(self):
        BaseDB.__init__(self)
        self.table_name = 'region'

    def create_db_if_not_exists(self):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS {}(
                region_id INTEGER PRIMARY KEY NOT NULL,
                country_id INTEGER NOT NULL,
                city_id INTEGER NOT NULL ,
                name TEXT NOT NULL)
        """.format(self.table_name)
        cursor.execute(query)
        connect.commit()
        connect.close()

    def fill_region_table(self, data):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            INSERT INTO {}(
                region_id, country_id, city_id, name
                ) 
                VALUES (?, ?, ?, ?)
        """.format(self.table_name)
        try:
            for region in data:
                cursor.execute(query, region)
                connect.commit()
        except Exception as ex:
            print(ex)
        finally:
            connect.close()
