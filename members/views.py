from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from members.models import member


def show_all_members(request):
    all_members = member.objects.all()
    context = {
        'all_members':all_members,
    }
    return render(request,"all_members.html",context)
def member_detail(request,id):
    req_member=member.objects.get(id=id)
    context={
        "req_member": req_member,
    }
    return render(request,"member_detail.html",context)


# Create your views here.
