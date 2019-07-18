import os
from jinja2 import Environment, FileSystemLoader

from cgi_bin.feedback import Feedback
from core.common import get_root_dir
from sql import feedack_db
from sql.feedack_db import FeedbackDB


def render_template(template_name, **kwargs):
    template_folder = os.path.join(get_root_dir(), 'static', 'templates')
    file_loader = FileSystemLoader(template_folder, encoding='utf-8')
    env = Environment(loader=file_loader)
    try:
        template = env.get_template('{}.html'.format(template_name))
        return template.render(**kwargs)
    except Exception as ex:
        print(ex)
        template = env.get_template('error.html')
        return template.render()

def not_found(environ):
    return render_template('not_found', title='404 Not Found')

def home_handler(environ):
    return render_template('index', title='Главная')

def comment_handler(environ):
    if environ['REQUEST_METHOD'] == 'POST':
        feedback = Feedback().env_object_factory(environ)
        FeedbackDB().add_feedback(feedback)
        return notify_handler(feedback)
    return render_template('comment', title='Обратная связь')

def view_handler(environ):
    all_feedback = feedack_db.FeedbackDB().get_all_feedback()
    return render_template('view', title='Обзор отзывов',
                           all_feedback=all_feedback)

def notify_handler(feedback):
    return render_template('comment_saved', title='Уведомление',
                           name=feedback.name,
                           comment=feedback.comment)

