from django.db import models
from djangotoolbox.fields import ListField
from conjugate.forms import StringListField



class CategoryField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)


class Verb(models.Model):
    verb = models.CharField(max_length=255)
    regularity = models.CharField(max_length=255)
    verbal_noun = models.CharField(max_length=255)
    verbal_adjective = models.CharField(max_length=255)
    past = CategoryField()
    present = CategoryField()
    habitual_present = CategoryField()
    habitual_present.null = True
    future = CategoryField()
    conditional = CategoryField()
    past_habitual = CategoryField()
    subjunctive = CategoryField()
    past_subjunctive = CategoryField()
    imperative = CategoryField()

    def __unicode__(self):
        return self.verb
