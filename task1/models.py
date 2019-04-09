from django.db import models
from collections import Counter
from django.template.defaultfilters import linebreaksbr

class Note(models.Model):
    note = models.TextField(max_length=1000, blank=False, null=False, default=None)
    is_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.CharField(max_length=20, blank=False, null=False)
    unique_words = models.IntegerField(blank=True, default=-1)

    def save(self, *args, **kwargs):
        try:
            self.unique_words = len(Counter(str(self.note).split(" ")))
            super(Note, self).save(*args, **kwargs)
        except: ValueError("BLYA")

    def __str__(self):

            return '%s ' % self.note

    class Meta:
         verbose_name= "Note"
         verbose_name_plural = "Notes"