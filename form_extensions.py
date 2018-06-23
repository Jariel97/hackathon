from flask_security.forms import ConfirmRegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ExtendedRegisterForm(ConfirmRegisterForm):
    company_name = StringField('Company Name', [DataRequired()])
    full_name = StringField('Full Name', [DataRequired()])

    def validate(self):
        res = super(ExtendedRegisterForm, self).validate()
        return res
