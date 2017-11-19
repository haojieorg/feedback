from flask import Blueprint

admin = Blueprint('admin',__name__)

from .views import FeedbackPost

from .views import FeedbackList

admin.add_url_rule('/post/',view_func=FeedbackPost.as_view('post'))
admin.add_url_rule('/list/',view_func=FeedbackList.as_view('list'))