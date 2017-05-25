from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

#inline model validation
from .validators import validate_content

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators=[validate_content])
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True, )


    def __str__(self):
        return str(self.content)

    # this is for a model validation, not necesarily for a field.
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("content cannot be abc")
    #     return super(Tweet, self).clean(*args, **kwargs)
