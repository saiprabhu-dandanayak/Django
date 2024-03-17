import datetime

from django.shortcuts import render

# Create your views here.

def template(request):
    return render(request,'testapp/index.html')
def template_view(request):
    return render(request,'testapp/signin.html')

def result_view(request):
    dt = datetime.datetime.now()
    name = 'Saiprabhu'
    rollno = 124
    marks = 88
    my_dict = {'date': dt, 'name': name, 'rollno': rollno, 'marks': marks}
    return render(request, 'testapp/results.html', my_dict)

def user_details_view(request):
    user = {
        'name': 'Saiprabhu',
        'email': 'saiprabhu@gmail.com',
        'age': 23,
        'country': 'INDIA'
    }
    context = {'user': user}
    return render(request, 'testapp/details.html', context)