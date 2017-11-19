from datetime import datetime
from flask import render_template,request,redirect,url_for
from flask.views import MethodView
from .forms import PostForm
from .models import db,Employee



class FeedbackPost(MethodView):
    def get(self):
        from .models import Department
        form = PostForm()
        form.departmentid.choices=[(d.id,d.name) for d in Department.query.all()]

        return render_template('feedback-post.html', form=form)
    def post(self):
        from .models import Employee
        form=PostForm(request.form)
        emp = Employee()
        form.populate_obj(emp)
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('admin.list'))

class FeedbackList(MethodView):
    def get(self):
        from .models import Employee
        form = Employee.query.limit(10)
        return render_template('feedback_list.html',form=form)
    def post(self):
        pass

