#views.py
from django.shortcuts import render


# Create your views here.
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from login.models import *
from login.fileProcess import *
from login.displayObject import *
 
@csrf_protect
def register(request):
	
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def fileupload_success(request):
	
	content=''
	with open("temp.html", "r") as infile:
        	for line in infile:
                	content+=line

	list = content.split("<DT><A HREF=");

	print len(list)

	displayList = []

	for index in range(len(list)):
        	if(index !=0 ):
                	sublist = list[index].split('"')
                	titlelist = list[index].split('>')
                	title=titlelist[1]
                	#actualTitle=title[:len(title)-3]
                	displayList.append(DisplayObject(sublist[1],sublist[3],title[:len(title)-3]))

	#for item in displayList:
        #	print item.link+" --- "+item.adddate+" --- "+item.title


	return render_to_response(
	'fileUpload/success.html',{'displayList':displayList}
	) 

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



 
@login_required
@csrf_protect
def home(request):
    #form = DocumentForm()
    #if request.method == 'POST':
    #	form = DocumentForm(request.POST, request.FILES)
    #	if form.is_valid():
    #		newdoc = Document(docfile=request.FILES['docfile'])
    #		newdoc.save()
    #		return HttpResponseRedirect('/register/success')

    #else:
    #    form = DocumentForm()
    #variables = RequestContext(request, {
    #'form': form
    #})

    
    #return render_to_response(
    #'home.html',
    #{ 'user': request.user }
    #)
	print 'post ?'
	if request.method == 'POST':
		form = DocumentFileForm(request.POST, request.FILES)
    		if form.is_valid():
			print 'file process'
			process_uploaded_file(request.FILES['file'])
    			# Redirect to the document list after POST
			return HttpResponseRedirect('/fileUpload/success')
        else:
		form = DocumentFileForm() # A empty, unbound form
   
   
	# Render list page with the documents and the form
	return render(request, 'home.html', {'form': form})
