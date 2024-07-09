from rest_framework import routers
from api.viewsets.studentViewsets import StudentListViewset
from api.viewsets.lecturerViewsets import LecturerListViewset
from api.viewsets.courseViewsets import CourseListViewset
from api.viewsets.teachesViewsets import TeachesListViewset
from api.viewsets.attendanceViewsets import AttendanceListViewset
from api.viewsets.enrollsViewsets import EnrollsListViewset
from api.viewsets.usersViewsets import UsersListViewset

routes = routers.SimpleRouter()

routes.register('student', StudentListViewset, basename='Student')
routes.register('lecturer', LecturerListViewset, basename='Lecturer')
routes.register('course', CourseListViewset, basename='Course')
routes.register('teaches', TeachesListViewset, basename='Teaches')
routes.register('attendance', AttendanceListViewset, basename='Attendance')
routes.register('enrolls', EnrollsListViewset, basename='Enrolls')
routes.register('users', UsersListViewset, basename='Users')

urlpatterns = routes.urls

#API URL configuration
# localhost:8000/api/students