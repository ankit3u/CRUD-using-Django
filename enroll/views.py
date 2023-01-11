
from django.shortcuts import render,HttpResponsePermanentRedirect

from .models import User
from .forms import CourseDetails

#Create your views here.
def add_show(request):
    if request.method =='POST':
        fm=CourseDetails(request.POST)
        if fm.is_valid():
            fm.save()
            fm=CourseDetails()
    else:
        fm=CourseDetails()
    stud=User.objects.all()

    return render(request,'enroll/addandshow.html',{'form':fm,'stud':stud})

def update(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=CourseDetails(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=CourseDetails(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')

    

