from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse

# User Authentication & Authorization
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import Survey, Patient
from django.core.files.base import ContentFile

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
	patient_name = request.POST['patient-name']
	patient_gender = request.POST['patient-gender']
	patient_birthday = request.POST['patient-birthday']
	patient_age = request.POST['patient-age']
	patient_height = request.POST['patient-height']
	patient_weight = request.POST['patient-weight']
	patient_receiving_date = request.POST['patient-receiving-date']
	patient_surgical_history = request.POST['patient-surgical-history']
	patient_medicine_history = request.POST['patient-medicine-history']

	print(request.POST['patient-birthday'])
	
	# p = Patient(
	# 	name = patient_name,
	# 	gender = patient_gender,
	# 	# ...
	# )

	survey_list = []
	for key, value in request.POST.items():
		try:
			kind, category, question = key.split("-")
		except ValueError as e:
			print(e)
			continue
		target_survey = [item for item in survey_list if 'category' in item and item['category'] == category]		
		
		if len(target_survey) > 0:
			for a_survey in target_survey:
				target_statement = [item for item in a_survey['statement'] if 'question' in item and item['question'] == question]
				if len(target_statement) > 0:
					for a_statement in target_statement:
						if kind == 'frequency':
							a_statement['frequency'] = int(value)
						elif kind == 'strength':
							a_statement['strength'] = int(value)
				else:
					new_statement_dict ={}
					new_statement_dict['question'] = question
					if kind == 'frequency':
						new_statement_dict['frequency'] = int(value)
					elif kind == 'strength':
						new_statement_dict['strength'] = int(value)
					a_survey['statement'].append(new_statement_dict)
		else:
			new_survey_dict = {}
			new_survey_dict['category'] = category
			new_statement_dict = {}
			new_statement_dict['question'] = question
			if kind == 'frequency':
				new_statement_dict[' jfrequency'] = int(value)
			elif kind == 'strength':
				new_statement_dict['strength'] = int(value)
			new_survey_dict['statement'] = []
			new_survey_dict['statement'].append(new_statement_dict)
			survey_list.append(new_survey_dict)
	survey = {}
	survey['survey'] = survey_list
	s = Survey(survey_json=survey)
	s.save()
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