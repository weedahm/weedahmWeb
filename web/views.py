from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse

# User Authentication & Authorization
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin

import os
import logging
import json
logging.basicConfig(level=logging.DEBUG)

class LoginView(TemplateView):
	template_name = 'app/login.html'

class LoginRequired(LoginRequiredMixin):
	login_url = 'app:loginView'
	redirect_field_name = 'redirect_to'

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

class IndexView(LoginRequired, TemplateView):
	template_name = 'app/index.html'

def patientReceptionPost(request):
	logging.debug(request.POST)
	return HttpResponseRedirect(reverse("app:index"))

class patientReceptionView(LoginRequired, TemplateView):
	template_name = 'app/patient_reception.html'
	def get_context_data(self, **kwargs):
		context = super(patientReceptionView, self).get_context_data(**kwargs)
		PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
		survey_json_data = open(PROJECT_PATH+"/utils/survey.json", "r", encoding='euc-kr').read()
		survey_json = json.loads(survey_json_data)
		context['survey_json'] = survey_json
		return context

class diagnoseView(LoginRequired, TemplateView):
	template_name = 'app/diagnose_wizard.html'

# class ExerciseGoalFormView(TemplateView):
# 	template_name = 'app/exercise_goal_form.html'

# class ExerciseGoalsView(TemplateView):
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