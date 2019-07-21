import sqlite3

from cgi_bin.feedback import Feedback
from sql.base_db import BaseDB


class FeedbackDB(BaseDB):

    def __init__(self):
        BaseDB.__init__(self)
        self.table_name = 'feedback'

    def create_db_if_not_exists(self):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS {}(
                feedback_id INTEGER PRIMARY KEY, 
                s_name text NOT NULL,
                name text NOT NULL,
                m_name text,
                region text,
                city text,
                phone text,
                email text,
                comment text NOT NULL)
        """.format(self.table_name)
        cursor.execute(query)
        connect.commit()
        connect.close()
        print('Preparing "Feedback" DB: SUCCESSFULLY')

    def set(self, feedback):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            INSERT INTO {}(
                s_name, name, m_name, region, city, phone, email, comment
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """.format(self.table_name)
        try:
            cursor.execute(query, (feedback.__get_field('s_name'),
                                  feedback.__get_field('name'),
                                  feedback.__get_field('m_name'),
                                  feedback.__get_field('region'),
                                  feedback.__get_field('city'),
                                  feedback.__get_field('phone'),
                                  feedback.__get_field('email'),
                                  feedback.__get_field('comment')))
        except Exception as ex:
            print(ex)
        connect.commit()
        connect.close()

    def get_all(self):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            SELECT * FROM {}
        """.format(self.table_name)
        cursor.execute(query)
        all_rows = cursor.fetchall()
        all_feedback = []
        for row in all_rows:
            all_feedback.append(Feedback().db_object_factory(cursor, row))
        connect.commit()
        connect.close()
        return all_feedback

    def get_region_list_by_region(self, min_count_comment):
        all_feedback = self.get_all()
        all_regions = {}
        for feedback in all_feedback:
            cur_region = feedback['region']
            count = all_regions.get(cur_region)
            count = 0 if not count else count
            all_regions.update({cur_region: count+1})

    def delete(self, feedback):
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        query = """
            DELETE FROM {db_file}
            WHERE surname={surname},
                name={name},
                comment={connect}
        """.format(
                db_file=self.table_name,
                surname=feedback.surname,
                name=feedback.name,
                connect=feedback.comment)
        cursor.execute(query)
        all_rows = cursor.fetchall()
        connect.commit()
        connect.close()
        return all_rows