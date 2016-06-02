from django.db import models

class Category(models.Model):
	category = models.TextField(max_length = 75)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# def __unicode__(self):
	# 	return self.category 

class Quote(models.Model):
	quote = models.TextField(max_length = 1000)
	author = models.TextField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	category_id = models.ForeignKey('Category')
	# def __unicode__(self):
	# 	return self.quote
