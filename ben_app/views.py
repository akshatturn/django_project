from django.shortcuts import render
from ben_app.forms import NewMessage
from ben_app.models import Message
# Create your views here.
def index(request):
    form = NewMessage()
    if request.method =='POST':
        form = NewMessage(request.POST)

        if form.is_valid():
            name = request.POST.get('name','')
            message = request.POST.get('message','')
            msg_obj = Message(name = name, message = message)
            msg_obj.save()

            print("Thank You!!")
        else:
            print("ERROR")
    return render(request, 'ben_app/index.html', {'form':form})

def about(request):
    return render(request, 'ben_app/about.html')
