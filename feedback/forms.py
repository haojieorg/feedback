from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,RadioField


class PostForm(FlaskForm):
    name= StringField('姓名')
    gender = RadioField('性别',choices=[('男','男'),('女','女')])
    mobile=StringField('电话')
    address = StringField('地址')
    departmentid = SelectField('热力公司')
    text = TextAreaField('反馈问题')

class AddDepartment(FlaskForm):
    name = StringField('公司名称')