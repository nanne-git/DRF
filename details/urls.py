from django.urls import path, include
from details import views
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("studentsearch/<str:name>", views.StudentSearch.as_view(), name="studentsearch"),
    path("teachersearch/<str:name>", views.TeacherSearch.as_view(), name="teachersearch"),
    path("oninputstudent", views.on_input_student, name="oninputstundet"),
    path("oninputteacher", views.on_input_teacher, name="oninputteacher"),
    path("searchbymarks/<str:marks>", views.SearchByMarks.as_view(), name="searchbymarks"),
]
























# path("listview", views.ListStudentGenerics.as_view(), name="listview"),
    # path("updateview/<int:pk>", views.RDStudentGenerics.as_view(), name="listview"),
    # path("students", views.StudentsMixin.as_view(), name="students"),
    # path("studentscrud/<int:pk>", views.StudentsCRUDMixin.as_view(), name="studentscrudview"),
    # path("searchstudent/<str:name>", views.searchstudent, name='search'),
    # path("liststudents/",views.ListStudents.as_view(),name="studentlist"),
    # path("detailed/<int:idnum>/",views.DetailedStudent.as_view(),name="detailed"),