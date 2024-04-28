from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def userslogin(request):
    msg=''
    if request.method == 'POST':

        name=request.POST.get('name'),
        email=request.POST.get('email'),
        usercreate = User.object.create_user(request,name,email)
        usercreate.save()
        msg="success"
    else:
        msg="some thing is wrong"

    return render(request,'userlogin.html',{'msg':msg})
