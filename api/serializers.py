from rest_framework import serializers
from api.models import *

class StudentEducationSerializer(serializers.ModelSerializer):
	class Meta:

		model = StudentEducation
		fields = "__all__"
		