from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    name= StringField('姓名',validators=[DataRequired])
    mobile=StringField('电话',validators=[DataRequired])
    address = StringField('地址',validators=[DataRequired])
    text = TextAreaField('反馈问题')


class AddDepartment(FlaskForm):
    name = StringField('公司名称',validators=[DataRequired])