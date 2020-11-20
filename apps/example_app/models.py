from django.db import models
from django.utils.translation import gettext_lazy as _


class ExampleModel(models.Model):
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('example model')
        verbose_name_plural = _('example models')

    def __str__(self):
        return self.name
