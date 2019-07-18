from cgi_bin.base_object import BaseOdject

class Feedback(BaseOdject):

    def to_dict(self):
        return {'s_name': self.get_field('s_name'),
                'name': self.get_field('name'),
                'm_name': self.get_field('middle_name'),
                'region': self.get_field('region'),
                'city': self.get_field('city'),
                'phone': self.get_field('phone'),
                'email': self.get_field('email'),
                'comment': self.get_field('comment')
                }

    def to_list(self):
        return (self.get_field('s_name'),
                self.get_field('name'),
                self.get_field('middle_name'),
                self.get_field('region'),
                self.get_field('city'),
                self.get_field('phone'),
                self.get_field('email'),
                self.get_field('comment')
                )
