from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    buying_for = models.ManyToManyField(User,
                                        blank=True,
                                        null=True,
                                        related_name='gifter')

    def __unicode__(self):
        return unicode(self.user)


admin.site.register(UserProfile)


class Gift(models.Model):
    wisher = models.ForeignKey(User, related_name='wishing_for')
    buyer = models.ForeignKey(User, related_name='buying', blank=True, null=True)
    bought = models.BooleanField(default=False)
    name = models.CharField(max_length=400)

    def __unicode__(self):
        return unicode(self.name)


admin.site.register(Gift)
