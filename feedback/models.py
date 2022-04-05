from django.db import models


class Feedback(models.Model):
    """ Guests who are logged in and have visited
    can give feedback about their stay """
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback #{self.id}'

    class Meta:
        """ A name rendering for plural """
        verbose_name_plural = 'feedbacks'
