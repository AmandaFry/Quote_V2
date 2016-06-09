from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Category, Quote
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


def index(request):
	#this try - exept is for to see if the session count exists
	try:#make the assumption session exists first 
 		if (request.session['count'] < request.session['counter1']):
			request.session['count'] = request.session['count'] + 1
			print 'I am ', request.session['count'], ' of ', request.session['counter1'], ' of quotes'
		else:
			request.session['count'] = 1

	except:#this will only happens one, if you don't have this the first time the page will not render
		request.session['count'] = 1
		
	#this try - exept is for see if the record exists, if not then increase the count
	# and redirect 
	try:
		secondq = Quote.objects.get(id=request.session['count'])
		pass
		context = {
 		"quote" : secondq,
 		}
		return render(request, 'quote/index.html', context)
	except:
		print 'I got to except'
		request.session['count'] + 1
		return redirect ('/')


def clear(request):
	#returns to first record
	del request.session['count']
	return redirect('/')


def new(request):
	#brings back all the categroies and display it drop down list
	request.session['is_new'] = True
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
	print request.session['counter1']
	#counterModified is needed in the successAE view
	request.session['counterModified'] = request.session['counter1']
	print request.session['counterModified']
	return redirect ('/successAE')


def edit(request):
	#render the edit page 
	if request.session['is_new'] == True:
		editq = Quote.objects.latest('id')
	else:
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
 	request.session['is_new'] = False
	return render(request, 'quote/edit.html', context)


def addEdit(request):
	#Make sure I work with the correct record
	updatequote = Quote.objects.get(id=request.session['count'])
	#Read in from the form quote and author
	qouteforme = request.POST['quote']
	authorforme = request.POST['author']
	#Read in the category id
	catid = request.POST.get("categid", "")
	catidInsert = Category.objects.get(id=catid)
	# First step I update every line, later I can see if anythign changed
	updatequote.quote = qouteforme
	updatequote.author = authorforme
	updatequote.category_id = catidInsert
	updatequoteupdated_at = timezone.now()
	updatequote.save()
	request.session['counterModified'] = request.session['count']
	return redirect ('/successAE')


def successAE(request):
	#when add or edit record it will show the effected record in the home page
	#Note this works fine for edit, but not for new not sure why.
	if request.session['is_new'] == True:
		sucq = Quote.objects.latest('id')
	else:
		sucq = Quote.objects.get(pk=request.session['counterModified'])
	print ('%' * 25)
	print "inside successAE"
	print request.session['counterModified']
	print sucq
	print ('%' * 25)
 	context = {
 		"quote" : sucq,
 	}
	return render(request, 'quote/index.html', context)


def favorite(request):
	print "I am in the favorite"
 	lastFive = Quote.objects.order_by('id')[:3]
 	context = {
 		'quote' : lastFive,
 	}
	return render(request, 'quote/Favorite.html', context)



