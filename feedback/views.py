from datetime import datetime
from flask import render_template,request,redirect,url_for
from flask.views import MethodView
from .forms import PostForm
from .models import db,Employee,Department



class FeedbackPost(MethodView):
    def get(self):

        form = PostForm()
        form.departmentid.choices=[(d.id,d.name) for d in Department.query.all()]

        return render_template('feedback-post.html', form=form)
    def post(self):
        form=PostForm(request.form)
        emp = Employee()
        form.populate_obj(emp)
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('admin.emplist'))

class FeedbackList(MethodView):
    def get(self,page=1):
        form = Employee.query.paginate(page,per_page=10)
        return render_template('feedback_list.html',form=form)
    def post(self):
        pass

class FeedbackDel(MethodView):
    def get(self,id):
        emp = Employee.query.get(id)
        db.session.delete(emp)
        db.session.commit()
        return redirect(url_for('admin.emplist'))

class FeedbackEdit(MethodView):
    def get(self,id=None):
        emp = Employee.query.get(id)
        form = PostForm(request.form,obj=emp)
        form.departmentid.choices = [(d.id, d.name) for d in Department.query.all()]
        return render_template('feedback-post.html',form=form)

    def post(self,id=None):
        form = PostForm(request.form)
        emp = Employee.query.get(id)
        form.populate_obj(emp)
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('admin.emplist'))

