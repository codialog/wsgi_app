from cgi_bin.base_object import BaseOdject

class Feedback(BaseOdject):

    def to_dict(self):
        return {'surname': self.surname,
                'name': self.name,
                'middle_name': self.middle_name,
                'region': self.region,
                'city': self.city,
                'phone': self.phone,
                'email': self.email,
                'comment': self.comment
                }
