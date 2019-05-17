from django.http import HttpResponse
from testmodel.models import password

def insert(requese):
	data = password(account = 'aaa', password = '123');
	data.save()
	return HttpResponse("insert compelite")