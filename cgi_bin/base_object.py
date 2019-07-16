import cgi


class BaseOdject():

    def __init__(self):
        self.fields = []

    def db_object_factory(self, cursor, row):
        for idx, col in enumerate(cursor.description):
            name, value = (col[0], row[idx])
            self.__add_field(name, value)
        return self

    def env_object_factory(self, environ):
        form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=True,
            )
        for key in form.keys():
            self.__add_field(key, form[key].value)
        return self

    def __add_field(self, name, value):
        self.fields.append(name)
        setattr(self, name, value)

    def __to_tuple(self):
        return tuple([getattr(self, x) for x in self.fields])

