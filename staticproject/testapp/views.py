from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render

def wish(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    if h < 12:
        msg = 'Hello Guest !!!! Very Very Good Morning!!!'
    elif h < 16:
        msg = 'Hello Guest !!!! Very Very Good Afternoon!!!'
    elif h < 21:
        msg = 'Hello Guest !!!! Very Very Good Evening!!!'
    else:
        msg = 'Hello Guest !!!! Very Very Good Night!!!'
    my_dict = {'insert_date': date, 'insert_msg': msg}
    return render(request, 'testapp/user.html', my_dict)
