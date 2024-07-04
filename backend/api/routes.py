from rest_framework import routers
from api.viewsets.studentViewsets import StudentListViewset

routes = routers.SimpleRouter()

routes.register('student', StudentListViewset, basename='Players')

urlpatterns = routes.urls

#API URL configuration
# localhost:8000/api/students