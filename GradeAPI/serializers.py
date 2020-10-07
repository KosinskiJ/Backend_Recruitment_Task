from rest_framework import serializers
from .models import Grade, Candidate

class AddMarkSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Grade
        fields = ('value', 'task', 'candidate', 'recruiter')
        extra_kwargs = {'value' : {'required' : False}}


class GradeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Grade
        fields = ('value',)

class CandidateListSerializer(serializers.ModelSerializer) :
    grades = GradeSerializer(many = True, read_only = True)
    avg_grade = serializers.DecimalField(max_digits = 4, decimal_places = 2)

    class Meta :
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'avg_grade', 'grades')
