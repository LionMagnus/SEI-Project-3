from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Event, Comment, User
#from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def events_index(request):
  events = Event.objects.all()
  return render(request, 'events/index.html', {
    'events': events
  })

def events_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  comments_form = CommentForm()
  return render(request, 'events/detail.html', {
    'event': event,
    'comments_form': comments_form,
  })

def events_comments(request, event_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.user = request.user
    new_comment.event_id = event_id 
    new_comment.save()
  return redirect('detail', event_id = event_id) 
  

class EventCreate(CreateView):
  model = Event
  fields = ['eventTitle', 'description', 'date', 'evtLocation']
  def form_valid(self, form):
    print(self.request.user)
    form.instance.organizer = User.objects.get(username=self.request.user)
    return super().form_valid(form)

class EventUpdate(UpdateView):
  model = Event
  fields = ['eventTitle', 'description', 'date', 'evtLocation']

class EventDelete(DeleteView):
  model = Event
  success_url = '/events'

class CommentCreate(CreateView):
  model = Comment
  fields = ['__all__']


class CommentUpdate(UpdateView):
  model = Comment
  fields = ['comment']
  

class CommentDelete(DeleteView):
  model = Comment
  success_url = '/events'