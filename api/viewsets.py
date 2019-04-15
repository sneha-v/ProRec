from rest_framework import viewsets
from rest_framework.response import Response
from api.models import *
from api.serializers import *

class StudentEducationViewset(viewsets.ModelViewSet):

	queryset = StudentEducation.objects.all()
	serializer_class = StudentEducationSerializer
