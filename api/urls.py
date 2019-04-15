from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.viewsets import *

router = DefaultRouter()
router.register(r'student',StudentEducationViewset)

urlpatterns = [
	
	path('',include(router.urls)),

]