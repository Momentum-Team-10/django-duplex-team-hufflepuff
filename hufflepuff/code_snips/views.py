from django.shortcuts import render, get_object_or_404
from .models import Snippet

# Create your views here.

def home_page(request):
  return render(request, 'code_snips/home.html')

def user_page(request):
  return render(request, 'code_snips/user_page.html')

def code_view(request, pk):
  snippet = get_object_or_404(Snippet, pk=pk)
  return render(request, 'code_snips/code_view.html', {"snippet": snippet})