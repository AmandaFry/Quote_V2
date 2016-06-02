from django.contrib import admin
from .models import Category, Quote
from django.db import models

class QuoteAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'quote')
	# def __str__(self):
	# 	return self.quote

admin.site.register(Category)
admin.site.register(Quote, QuoteAdmin)


# class Quote():
# 	def __unicode__(self):
# 		return self.quote
