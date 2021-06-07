from django.shortcuts import render, redirect
from chat.models import Message

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room_name = request.POST.get('code')
        return redirect('/chat/' + room_name + '?username='+username)

    return render(request, template_name='index.html')

def room_detail(request, room_name):
    username = request.GET.get('username')
    messages = Message.objects.filter(room=room_name)[0:25]
    return render(request, template_name='room.html', context={'room_name':room_name, 'username':username, 'messages':messages})