from django.db.models import query
from django.shortcuts import render, get_object_or_404
from .models import Snippet

# Create your views here.

def home_page(request):
  snippets = Snippet.objects.all()[0:5]
  return render(request, 'code_snips/home.html', {"snippets": snippets})

def user_page(request):
  return render(request, 'code_snips/user_page.html')

def code_view(request, pk):
  snippet = get_object_or_404(Snippet, pk=pk)
  return render(request, 'code_snips/code_view.html', {"snippet": snippet})

def search_by_title(request):
    # get the search term from the query params
    query = request.GET.get("q")
    # use that search term to make a db query, save it to a variable
    results = Snippet.objects.filter(title__icontains=query)
    # send back a response that includes the data from the query

    return render(request, "code_snips/home.html", {"snippets": results})

def search_by_language(request):
  query = request.GET.get("q")
  results = Snippet.objects.filter(language__name__icontains=query)
  return render(request, "code_snips/home.html", {"snippets": results})

def search_by_tag(request):
  query = request.GET.get("q")
  results = Snippet.objects.filter(tag__name__icontains=query)
  return render(request, "code_snips/home.html", {"snippets": results})

def search_by_user(request):
  query = request.GET.get("q")
  results = Snippet.objects.filter(created_by__icontains=query)
  return render(request, "code_snips/home.html", {"snippets": results})