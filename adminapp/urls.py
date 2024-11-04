from django.urls import path, include
from . import views
from . import views
urlpatterns=[
    path('',views.projecthomepage,name='projecthomepage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),

    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randompagelogic/',views.randompagelogic,name='randompagelogic'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
    path('calculatorpagelogic/',views.calculatorpagelogic,name='calculatorpagelogic'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('add_task/',views.add_task,name='add_task'),
    path('delete_task/',views.delete_task,name='delete_task'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('add_task/',views.add_task,name='add_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),

    path('loginpagecall/',views.loginpagecall,name='loginpagecall'),
    path('loginpagelogic/',views.loginpagelogic,name='loginpagelogic'),
    path('logout/', views.logoutpagelogic, name='logout'),
    path('upload_file/', views.upload_file, name='upload_file'),

path('add_student_page_call',views.add_student_page_call,name='add_student_page_call'),
path('feedback', views.feedback_view, name='feedback'),
path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),

]