from django.urls import path
from.import views
urlpatterns=[
    path('',views.entry_page,name="entry_page"),
    path('home',views.home, name="home"),
    path('login', views.login, name="login"),
    path('admin_register_login', views.admin_register_login, name="admin_register_login"),
    path('admin_register', views.admin_register, name="admin_register"),
    path('staff_register_login', views.staff_register_login, name="staff_register_login"),
    path('staff_register', views.staff_register, name="staff_register"),
    path('student_register_login', views.student_register_login, name="student_register_login"),
    path('student_register', views.student_register, name="student_register"),
]