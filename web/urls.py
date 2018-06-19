from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    # url(r'^.*\.html', views.gentella_html, name='gentella'),
    # url(r'^$', views.index, name='index'),

    # path('', views.index, name='index'),
    path('', views.LoginView.as_view(), name='loginView'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.IndexView.as_view(), name='index'),

    path('patientReceptionPost/', views.patientReceptionPost, name='patientReceptionPost'),
    path('patientReception/', views.patientReceptionView.as_view(), name='patientReception'),
    path('diagnose/', views.diagnoseView.as_view(), name='diagnose'),
    # path('exerciseGoalForm/', views.ExerciseGoalFormView.as_view(), name='exerciseGoalForm'),
    # path('exerciseLogView/', views.ExerciseLogView.as_view(), name='exerciseLog'),

    # path('exerciseGoalForm/enroll/', views.enrollExerciseGoal, name='enrollExerciseGoal'),
]