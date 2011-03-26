import os
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()

def index(request):
    return HttpResponse("You are at the index")

def thanks(request):
    return HttpResponse("Your file has been successfully uploaded")

def upload_file(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponseRedirect('/listManager/thanks/')
        else:
            form = UploadFileForm()
        
        return render_to_response('listManager/upload.html', {'form':form}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
    # hint for os.path.dirname... came from http://stackoverflow.com/questions/550632/favorite-django-tips-features
    destination = open( os.path.dirname(__file__) +'/uploadedFiles/'+ f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()