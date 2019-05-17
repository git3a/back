from django.http import HttpResponse
from testmodel.models import password
import json

class ResultJSON():
    '''
    结果对象
    '''

    def __init__(self, code, msg, body):
        self.code = code
        self.body = body
        self.msg = msg

def toResultJson(code, body, msg):
    '''
    转Json返回码对象
    :param code: 
    :param body: 
    :return: 
    '''
    return json.dumps(ResultJSON(code=code, msg=msg, body=list(body)).__dict__, ensure_ascii=False)

def get(request):
	response = ""
	response1 = ""
	
	data = password.objects.filter(id = 1)
	for var in data:
		response += var.account + ' ' + var.password
	return HttpResponse(json.dumps(response))
	