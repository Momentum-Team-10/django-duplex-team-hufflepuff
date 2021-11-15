from django.shortcuts import render
from .models import Snippet

# Create your views here.

def home_page(request):
  snippets = Snippet.objects.all()[0:5]
  return render(request, 'code_snips/home.html', {"snippets": snippets})

def user_page(request):
  return render(request, 'code_snips/user_page.html')