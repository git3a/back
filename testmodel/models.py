from django.db import models

# Create your models here.
class recipe(models.Model):
	recipe_name = models.TextField()
	img_html = models.TextField()
	ingredient_name = models.TextField()
	ingredient_quantity = models.TextField()
	setp_text = models.TextField()
