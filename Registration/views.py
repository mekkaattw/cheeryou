from datetime import datetime
from django.shortcuts import render
	def Registration(request):
		return render(request,
		'Registration.html',
		{'current_time': datetime.now()})
