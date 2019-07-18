import cgi


class BaseOdject():

    def __init__(self):
        self.fields = []

    def db_object_factory(self, cursor, row):
        for idx, col in enumerate(cursor.description):
            name, value = (col[0], row[idx])
            self.set_field(name, value)
        return self

    def env_object_factory(self, environ):
        form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=True,
            )
        for key in form.keys():
            self.set_field(key, form[key].value)
        return self

    def set_field(self, name, value):
        dict.__setattr__(self, name, value)

    def get_field(self, name):
        return getattr(self, name)

