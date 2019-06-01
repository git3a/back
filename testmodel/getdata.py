from django.http import HttpResponse
from testmodel.models import recipe
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
	response = {}
	
	data = recipe.objects.all()[:1]
	for var in data:
		#print(var.recipe_name)
		#response = var.recipe_name
		response['recipe_name'] = var.recipe_name
		response['img_html'] = var.img_html
		response['ingredient_name'] = var.ingredient_name
		response['ingredient_quantity'] = var.ingredient_quantity
		response['setp_text'] = var.setp_text
	print(response['recipe_name'])
	return HttpResponse(json.dumps(response, ensure_ascii=False))
	