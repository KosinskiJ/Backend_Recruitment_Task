from django.db import models
from django.contrib.auth.models import  User

class Candidate(models.Model) :
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

class Recruiter(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

class Task(models.Model) :
    title = models.CharField(max_length = 200)


class Grade(models.Model) :
    value = models.IntegerField(null = True)
    task = models.ForeignKey(Task, on_delete = models.SET_NULL, null = True)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE, related_name = 'grades')
    recruiter = models.ForeignKey(Recruiter, on_delete= models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(value__gte=1) & models.Q(value__lte=10),
            name = "A value is valid between 1-10",
                                   )
        ]



