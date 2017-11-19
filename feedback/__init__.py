from flask import Blueprint

admin = Blueprint('admin',__name__)

from .views import FeedbackPost
from .views import FeedbackList
from .views import FeedbackDel
from .views import FeedbackEdit

fblist=FeedbackList.as_view('emplist')
admin.add_url_rule('/list/',view_func=fblist)
admin.add_url_rule('/list/<int:page>/',view_func=fblist)

admin.add_url_rule('/post/',view_func=FeedbackPost.as_view('post'))
admin.add_url_rule('/del/<int:id>/',view_func=FeedbackDel.as_view(('del')))
admin.add_url_rule('/edit/<int:id>/',view_func=FeedbackEdit.as_view('edit'))


