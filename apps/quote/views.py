from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Category, Quote
from django.utils import timezone


def index(request):
	
 	try:#make the assumption session exists first 
 		if (request.session['count'] < request.session['counter1']):
			request.session['count'] = request.session['count'] + 1
			print request.session['counter1']
		else:
			request.session['count'] = 1
			# request.session['counter1'] = Quote.objects.count()
	except:#this will only happens one, if you don't have this the first time the page will not render
		request.session['count'] = 1

	firstq = Quote.objects.get(id=request.session['count'])

 	context = {
 		"quote" : firstq,
 	}
	return render(request, 'quote/index.html', context)

def new(request):
	#brings back all the categroies and display it drop down list
	allcategories = Category.objects.all()
	context = {
		'categories' : allcategories,
	}
	return render(request, 'quote/new.html', context)

def addNew(request):
	#read in from - request.POST is request.form
	qouteforme = request.POST['quote']
	authorforme = request.POST['author']
	#I was not able to use the category id directly ... 
	catid = request.POST.get("categid", "")
	#...therefore I needed to call its instance before inserting to table
	catidInsert = Category.objects.get(id=catid)
	#create what to insert into Quote table
	newquote = Quote(quote=qouteforme, author=authorforme, category_id=catidInsert, created_at=timezone.now(), updated_at=timezone.now())
	#the actul insert statment
	newquote.save()
	#update the counter1 the number of records in the db
	request.session['counter1'] = Quote.objects.count()
	return redirect ('/')


def edit(request):
	editq = Quote.objects.get(id=request.session['count'])
	#trying to preselect the category as a default that was assigned to the quote
	# selected_cat = Category.objects.all().filter(category=editq.category_id.category)
	# selected_cat = Category.objects.get(id=editq.category_id.category)
	# print selected_cat
	# selected_cat = Category.objects.get(id=6)
	# selected_cat = 6
	# print ("*" *20)
	# print selected_cat
	# print ("*" *20)
	allcategories = Category.objects.all()
	context = {
 		'quote' : editq,
 		# 'selected_category' : selected_cat,
 		'categories' : allcategories,

 	}
	return render(request, 'quote/edit.html', context)


# def showOne(request):
# 	print ("*" *20)
# 	print 'I am inside the redirect'
# 	print ("*" *20)
# 	return render(request, 'quote/showOne.html')

def clear(request):
	del request.session['count']
	return redirect('/')