from django.core.exceptions import ValidationError
# running validation directly on the field of the model.
# could be used to prevent profanity or whatever
def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("content cannot be blank")
    return value