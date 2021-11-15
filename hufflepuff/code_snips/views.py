from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet
from .forms import SnippetForm

# Create your views here.

def home_page(request):
  snippets = Snippet.objects.all()[0:5]
  return render(request, 'code_snips/home.html', {"snippets": snippets})

def user_page(request):
  return render(request, 'code_snips/user_page.html')

def code_view(request, pk):
  snippet = get_object_or_404(Snippet, pk=pk)
  return render(request, 'code_snips/code_view.html', {"snippet": snippet})

def add_snip(request):
  if request.method == 'GET':
    form = SnippetForm()
  else:
    form = SnippetForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('user_page')
  return render(request, 'code_snips/add_snip.html', {'form': form})

def edit_snip(request, pk):
  snippet = get_object_or_404(Snippet, pk=pk)
  if request.method == 'GET':
    form = SnippetForm(instance=snippet)
  else:
    form = SnippetForm(data=request.POST, instance=snippet)
    if form.is_valid():
      form.save()
      return redirect('user_page')
  return render(request, 'code_snips/edit_snip.html', {'form': form, 'snippet': snippet})

def delete_snip(request, pk):
  snippet = get_object_or_404(Snippet, pk=pk)
  if request.method == 'POST':
    snippet.delete()
    return redirect('user_page')
  return render(request, 'code_snips/delete_snip.html', {'snippet': snippet})
