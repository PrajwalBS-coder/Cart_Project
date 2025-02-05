from rest_framework.validators import ValidationError
from django.core.validators import validate_email

class Email_Validators:
    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError('Invalid Email')