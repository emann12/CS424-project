from django.shortcuts import render
from members.models import Member
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from IPython import embed

from members.forms import MemberForm


# Create your views here.

def member(request,member_id):
    member = Member.objects.get(id=member_id)
    
    context={"member": member}
    
    response = render(request,'members/member_detail.html', context )
  
    return response



def member_list(request):
    
    member_list = Member.objects.all()        
    context={"member_list": member_list}
    response = render(request,'members/member_list.html', context )
    
    return response

# Lets a member update their details
def member_update(request,member_id):
    member = Member.objects.get(id=member_id)
    if request.method=="POST":
        form = MemberForm(request.POST, instance=member) # populates the form fields with POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_profile',kwargs={'member_id':member_id}))
        else:
            return HttpResponseRedirect('/')

    form = MemberForm()
    return render(request,'members/member_update.html',{
            'form':form
        })