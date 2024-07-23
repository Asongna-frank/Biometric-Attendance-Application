from rest_framework import routers
from api.viewsets.studentViewsets import StudentListViewset
from api.viewsets.lecturerViewsets import LecturerListViewset
from api.viewsets.courseViewsets import CourseListViewset, StudentCoursesView, LecturerCoursesView
from api.viewsets.teachesViewsets import TeachesListViewset
from api.viewsets.attendanceViewsets import AttendanceListViewset, StudentAttendanceView, LecturerAttendanceView
from api.viewsets.enrollsViewsets import EnrollsListViewset
from api.viewsets.usersViewsets import UsersListViewset, StudentLoginView, LecturerLoginView
from api.viewsets.timetableViewsets import TimetableViewset, StudentTimetableView, LecturerTimetableView
from api.viewsets.classrosterViewsets import ClassRosterView


routes = routers.SimpleRouter()

routes.register('student', StudentListViewset, basename='Student')
routes.register('lecturer', LecturerListViewset, basename='Lecturer')
routes.register('course', CourseListViewset, basename='Course')
routes.register('teaches', TeachesListViewset, basename='Teaches')
routes.register('attendance', AttendanceListViewset, basename='Attendance')
routes.register('enrolls', EnrollsListViewset, basename='Enrolls')
routes.register('users', UsersListViewset, basename='Users')
routes.register('timetable', TimetableViewset, basename='Timetable')
routes.register('auth/login/student', StudentLoginView, basename='Student_Login')
routes.register('auth/login/lecturer', LecturerLoginView, basename='Lecturer_Login')

routes.register('timetable/student', StudentTimetableView, basename='Student_Timetable')
routes.register('timetable/lecturer', LecturerTimetableView, basename='Lecturer_Timetable')
routes.register('attendance/student', StudentAttendanceView, basename='Student_Attendance')
routes.register('attendance/lecturer', LecturerAttendanceView, basename='Lecturer_Attendance')
routes.register('courses/student', StudentCoursesView, basename='Student_Courses')
routes.register('courses/lecturer', LecturerCoursesView, basename='Lecturer_Courses')
routes.register('classroster', ClassRosterView, basename='Class_Roster')

urlpatterns = routes.urls
