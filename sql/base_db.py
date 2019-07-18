import os
import sqlite3

from core.common import get_root_dir


class BaseDB():

    def __init__(self):
        self.db_name = 'wsgi_app'
        self.db_file = '{}.db'.format(self.db_name)
        self.db_path = os.path.join(get_root_dir(), 'sql', 'db', self.db_file)
        self.table_name = ''
