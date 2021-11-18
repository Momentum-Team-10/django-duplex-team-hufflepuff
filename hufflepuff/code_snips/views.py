from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Snippet, Comment
from .forms import SnippetForm, CommentForm
import datetime
# Create your views here.

def home_page(request):
  user = request.user
  snippets = Snippet.objects.all()[0:5]
  return render(request, 'code_snips/home.html', {"snippets": snippets, "user":user})

@login_required
def user_page(request):
  favorites=Snippet.objects.filter(favorited=True)
  authored = Snippet.objects.filter(created_by=request.user)
  return render(request, 'code_snips/user_page.html', {"favorites": favorites, "authored": authored})

def code_view(request, pk):
  snippet = get_object_or_404(Snippet, pk=pk)
  comments = Comment.objects.filter(snippet=snippet).order_by('-created_at')
  user = request.user
  if request.method == 'GET':
    form = CommentForm()
  else:
    form = CommentForm(data=request.POST)
    if form.is_valid():
      comment_form = form.save(commit=False)
      comment_form.user = request.user
      comment_form.snippet = snippet
      comment_form.save()
  return render(request, 'code_snips/code_view.html', {"snippet": snippet, "comments": comments, "form": form, "user": user, "pk":pk,})

@login_required
def add_snip(request):
  if request.method == 'GET':
    form = SnippetForm()
  else:
    form = SnippetForm(data=request.POST)
    if form.is_valid():
      snippet_form = form.save(commit=False)
      snippet_form.created_by = request.user
      snippet_form.save()
      return redirect('user_page')
  return render(request, 'code_snips/add_snip.html', {'form': form})

@login_required
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

@login_required
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

@login_required
def favorite_snippet(request, pk):
  user = request.user
  snippet = get_object_or_404(Snippet, pk=pk)
  
  if request.method == "DELETE":
    snippet.favorited.remove(user)
    favorited = False
  elif request.method == "POST":
    snippet.favorited.add(user)
    favorited = True

  # Lazy non-seperated check if request is ajax
  if(request.headers.get("x-requested-with") == "XMLHttpRequest"):
    return JsonResponse({ "favorited": favorited })

  return redirect("code_view", pk=pk)

@login_required
def clone_snippet(request, pk):
  # retrieve snippet and user info
  user = request.user
  snippet = get_object_or_404(Snippet, pk=pk)
  # create clone and edit data to asociate user
  snippet.created_by = user
  snippet.created_at = datetime.datetime.now()
  snippet.pk = None
  # save clone as new snippet by user and redirect user to their new snippet
  snippet.save()
  new_pk = snippet.pk
  # attach MtM relationship

  return redirect('code_view', pk=new_pk)