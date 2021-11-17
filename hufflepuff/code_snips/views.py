from django.db.models import query
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Snippet, Comment
from .forms import SnippetForm, CommentForm

# Create your views here.

def home_page(request):
  user = request.user
  snippets = Snippet.objects.all()[0:5]
  return render(request, 'code_snips/home.html', {"snippets": snippets, "user":user})

@login_required
def user_page(request):
  snippets=Snippet.objects.filter(favorited=True)
  return render(request, 'code_snips/user_page.html', {"snippets": snippets})

def code_view(request, pk):
  snippet = get_object_or_404(Snippet, pk=pk)
  comments = Comment.objects.filter(snippet=snippet).order_by('-created_at')
  if request.method == 'GET':
    form = CommentForm()
  else:
    form = CommentForm(data=request.POST)
    if form.is_valid():
      comment_form = form.save(commit=False)
      comment_form.user = request.user
      comment_form.snippet = snippet
      comment_form.save()
  return render(request, 'code_snips/code_view.html', {"snippet": snippet, "comments": comments, "form": form})

def add_snip(request):
  if request.method == 'GET':
    form = SnippetForm()
  else:
    form = SnippetForm(data=request.POST)
    if form.is_valid():
      snippet_form = form.save(commit=False)
      snippet_form.user = request.user
      snippet_form.save()
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

def filter_by_tag(request, tag):
  snippets=Snippet.objects.filter(tags__name=tag)
  snippets.order_by('-created_at')
  return render(request, 'code_snips/filtered_page.html', {"snippets":snippets, "tag":tag})

def filter_by_language(request, language):
  snippets=Snippet.objects.filter(language__name=language)
  snippets.order_by('-created_at')
  return render(request, 'code_snips/by_language.html', {"snippets":snippets, "language":language})

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
  results = Snippet.objects.filter(tags__name__icontains=query)
  return render(request, "code_snips/home.html", {"snippets": results})

def search_by_user(request):
  query = request.GET.get("q")
  results = Snippet.objects.filter(created_by__username__icontains=query)
  return render(request, "code_snips/home.html", {"snippets": results})