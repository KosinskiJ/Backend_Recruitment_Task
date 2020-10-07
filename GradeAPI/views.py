from django.db.models import Avg
from rest_framework import viewsets, status
from rest_framework.response import Response, SimpleTemplateResponse

from . import models, serializers

class AddMarkView(viewsets.ModelViewSet) :
    queryset = models.Grade.objects.all()
    serializer_class = serializers.AddMarkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        candidate_task = models.Grade.objects.filter(candidate = serializer.validated_data['candidate'])
        if not candidate_task.filter(task = serializer.validated_data['task']):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(data="The value of this task is already created for this candidate",
                            status=status.HTTP_403_FORBIDDEN)



class CandidateListView(viewsets.ModelViewSet) :
    serializer_class = serializers.CandidateListSerializer
    queryset = models.Candidate.objects.all()

    def get_queryset(self) :
        return models.Candidate.objects.annotate(
            avg_grade = Avg('grades__value'),
        )