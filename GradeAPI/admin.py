from django.contrib import admin
from . import models

admin.site.register(models.Candidate)
admin.site.register(models.Recruiter)
admin.site.register(models.Task)
admin.site.register(models.Grade)