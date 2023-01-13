from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import todoform

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class tlv(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class tdv(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class tuv(UpdateView):
    model = Task
    template_name = 'updates.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('tdv',kwargs={'pk':self.object.id})

class tdel(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tlv')

# Create your views here.
def demo(request):
    task1 = Task.objects.all()
    if request.method=="POST":
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':task1})

# def details(request):
#     return render(request,'details.html',)

def update(request,id):
    task = Task.objects.get(id=id)
    f = todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html',{'f': f, 'task': task})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


