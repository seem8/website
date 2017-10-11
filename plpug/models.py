from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Project(models.Model):
    '''
    Project model for page projects/projekty.
    '''
    name = models.CharField(max_length=254,
                            verbose_name=_("Project name"),
                            )
    website = models.CharField(max_length=254,
                              verbose_name=_("Project website"),
                              )
    owner_name = models.CharField(max_length=254,
                                 verbose_name=_("Project owner"),
                                 )
    owner_email = models.EmailField(max_length=254,
                                  verbose_name=_("Owner email"),
                                  )
    creation_date = models.DateTimeField(auto_now=True,
                                        )

