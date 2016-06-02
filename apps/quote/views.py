from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Category, Quote



def index(request):
	
 	try:#make the assumption session exists first 
 		if (request.session['count'] < request.session['counter1']):
			request.session['count'] = request.session['count'] + 1
			print request.session['counter1']
		else:
			request.session['count'] = 1
			request.session['counter1'] = Quote.objects.count()
	except:#this will only happens one, if you don't have this the first time the page will not render
		request.session['count'] = 1

	secondq = Quote.objects.get(id=request.session['count'])

 	context = {
 		"quote" : secondq,
 	}
	return render(request, 'quote/index.html', context)

# def updateMe(request):
# 	request.session['counter1'] = Quote.objects.count()
# 	print ("&" *20)
# 	print request.session['counter1']
# 	print ("&" *20)
# 	return redirect('/')

def new(request):
	allcategories = Category.objects.all()
	context = {
		'categories' : allcategories,
	}
	return render(request, 'quote/new.html', context)

def addNew(request):
	qouteforme = request.POST['quote']
	authorforme = request.POST['author']
	# catid = request.POST.get("categid", "")
	print ("*" *20)
	print 'I read from the form'
	print qouteforme
	print authorforme
	# print catid
	print ("%" *20)
	return redirect ('/')

# def showOne(request):
# 	print ("*" *20)
# 	print 'I am inside the redirect'
# 	print ("*" *20)
# 	return render(request, 'quote/showOne.html')

def clear(request):
	del request.session['count']
	return redirect('/')