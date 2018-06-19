from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

# User Authentication & Authorization
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin

import logging
logging.basicConfig(level=logging.DEBUG)

class LoginView(generic.TemplateView):
	template_name = 'app/login.html'

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(request, username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect(reverse('app:index'))
	else:
		return HttpResponseRedirect(reverse('app:loginView'))
	# logging.debug("username: "+username+" password: "+password)
	
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('app:loginView'))

class IndexView(LoginRequiredMixin, generic.TemplateView):
	login_url = 'app:loginView'
	redirect_field_name = 'redirect_to'
	template_name = 'app/index.html'

def patientReceptionPost(request):
	logging.debug(request.POST)
	return HttpResponseRedirect(reverse("app:index"))

class patientReceptionView(generic.TemplateView):
	template_name = 'app/patient_reception.html'

class diagnoseView(generic.TemplateView):
	template_name = 'app/diagnose_wizard.html'

# class ExerciseGoalFormView(generic.TemplateView):
# 	template_name = 'app/exercise_goal_form.html'

# class ExerciseGoalsView(generic.TemplateView):
# 	template_name = 'app/exercise_goal_form.html'
		
		
# def index(request):
#     return render(request, 'app/index.html')

# def gentella_html(request):
#     logging.debug("gentella_html")
#     context = {}
#     # The template to be loaded as per gentelella.
#     # All resource paths for gentelella end in .html.

#     # Pick out the html file name from the url. And load that template.
#     load_template = request.path.split('/')[-1]
#     template = loader.get_template('app/' + load_template)
#     return HttpResponse(template.render(context, request))