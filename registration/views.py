from django.shortcuts import render

# Create your views here.
from registration.models import Member # with capital S for Student because it's a class

from django.http import Http404

def home(request): 

    members = Member.objects.all()

    return render(request,'home.html',{'members':members,})


def member_detail(request, member_id):

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        raise Http404('Sorry, Member not found!')

    return render(request,'member_detail.html',{'member':member})

def about(request):

    module_name = 'Mission'
    return render(request,'about.html',{'module_name':module_name})
