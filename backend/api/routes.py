from rest_framework import routers
from api.viewsets.studentViewsets import StudentListViewset
from api.viewsets.lecturerViewsets import LecturerListViewset

routes = routers.SimpleRouter()

routes.register('student', StudentListViewset, basename='Student')
routes.register('lecturer', LecturerListViewset, basename='Lecturer')

urlpatterns = routes.urls

#API URL configuration
# localhost:8000/api/students