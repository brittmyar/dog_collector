from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Blu', 'great dane', 'sweet lil baby', 6),
  Dog('Auggy', 'vizslador', 'absolute madman and scruffy', 3),
  Dog('Torree', 'pit-bull', 'sweet lion', 7)
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })