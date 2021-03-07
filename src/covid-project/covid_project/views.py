from django.shortcuts import render
import pickle as pkl
import pandas as pd
import numpy as np
from fbprophet import Prophet
import datetime as dt
import os
cwd = os.getcwd()

# Create your views here.
from django.http import HttpResponse

def index(request):
	return render(request,"InitialPage.html")

def output(request):
	if request.method == "GET":
		fname = request.GET.get('fname')
		date = request.GET.get('date')
		request.session['name'] = fname
		future = pd.read_csv(cwd + '/simulate_future.csv')
		with open(cwd+'/final_model.sav','rb') as file:
			model = pkl.load(file)
		result = model.predict(future)
		result[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
		dimension = result.shape
		length = dimension[0]
		cases = []
		datey = int(date.split('-')[0])
		datem = int(date.split('-')[1])
		dated = int(date.split('-')[2])
		dateymd = dt.date(datey,datem,dated)
		for i in range(0,length):
 		    if result.iloc[i]['ds'] == dateymd :
 			    cases.append(result.iloc[i]['yhat'])
 			    cases.append(result.iloc[i]['yhat_lower'])
 			    cases.append(result.iloc[i]['yhat_upper'])
		resultdic = {
			'date' : dateymd,
			'cases': int(cases[0]),
			'cases_lower': int(cases[1]),
			'cases_upper': int(cases[2])
		}
		return render(request, "FinalPage.html",resultdic)
	else:
		return render(request,"error-404.html")

def report(request):
	if request.method == "GET":
		return render(request, "form_two.html")
	else:
		return render(request,"error-404.html")
