from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.index , name = 'index'),
    path('about',views.about, name ='about'),
    path('contact',views.contact,name='contact'),
    path('show_comment',views.show_comment,name='show_comment'),
    path('survey',views.survey,name='survey'),
    path('sondageglob',views.sondageglob,name='sondageglob'),
    path('vote/<sondage_id>/',views.vote,name='vote'),
    path('result/<sondage_id>/',views.result,name='result'),
    path('home_sondage',views.home_sondage,name='home_sondage'),
    path('create_result',views.create_result,name='create_result'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('product/', views.productDetail, name='product'),


    ###########################################################################
    path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
    path('student-exam', views.student_exam_view,name='student-exam'),
    path('admin-add-course', views.admin_add_course_view,name='admin-add-course'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view', views.admin_view,name='admin-view'),
    path('delete-survey/<int:pk>', views.delete_survey,name='delete-survey'),
    path('see-question/<int:pk>', views.see_question_view,name='see-question'),
    path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
    path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
    path('view-result', views.view_result_view,name='view-result'),
    path('test', views.test,name='test'),
    # path('testt', views.test2,name='testt'),


 


 








  
]