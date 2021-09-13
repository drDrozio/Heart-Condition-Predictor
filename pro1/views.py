# Create your views here.
from django.shortcuts import render, redirect
from .mlprocessing.heart_disease import heart_disease_ml


# Create your views here.
def heart_disease(request):
	if request.method == 'POST':
		dic = request.POST
		X_encoded = heart_disease_ml.preprocess(dic)
		pred = heart_disease_ml.predict_disease(X_encoded)

		if pred<=1:
			advise = 'Your heart seems to be in good condition. You are good to go!'
		elif pred>=3:
			advise = 'Your heart is not in a good condition. You are advised to consult a Physician'
		else:
			advise = 'Your heart is still OK but we advise you to take care and stay healthy'

		context = {'pred':pred, 'advise' : advise}
		print("Prediction : ",pred)
		return render(request,'pro1/result.html',context)

	context = {}
	return render(request,'pro1/heart_disease.html',context)