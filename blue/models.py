from turtle import title
from django.db import models
from django.utils.translation import gettext_lazy as _


class Blue(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    content = models.CharField(_('Content'), max_length=50)
    app_name = models.CharField(_('App name'), max_length=50)

    def __str__(self):
        return self.title
