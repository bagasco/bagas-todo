from django.shortcuts import redirect, render
from .models import Todo
# Create your views here.

def index(request):
    if request.POST:
        kegiatan = request.POST['kegiatan']
        if kegiatan:
            todo = Todo(kegiatan=kegiatan)
            todo.save()
        return redirect('index')
    else:
        try:
            data = Todo.objects.all().order_by('-id')
        except:
            data = 0
        context = {
            'data':data
        }
        return render(request,'home.html',context)

def delete(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')