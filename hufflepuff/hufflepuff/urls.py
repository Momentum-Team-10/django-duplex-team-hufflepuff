"""hufflepuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar
from code_snips import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('user_page/', views.user_page, name='user_page'),
    path('code_view/<int:pk>/', views.code_view, name='code_view'),
    path('snips/add/', views.add_snip, name='add_snip'),
    path('snips/<int:pk>/edit/', views.edit_snip, name='edit_snip'),
    path('snips/<int:pk>/delete/', views.delete_snip, name='delete_snip'),
    path('snippets/<str:tag>/', views.filter_by_tag, name='filter_by_tag'),
    path('snippets/language/<str:language>/', views.filter_by_language, name='filter_by_language'),
    path('title_search/', views.search_by_title, name='search_by_title'),
    path('language_search/', views.search_by_language, name='search_by_language'),
    path('tag_search/', views.search_by_tag, name='search_by_tag'),
    path('user_search/', views.search_by_user, name='search_by_user'),
    path("code_view/<int:pk>/favorite/", views.favorite_snippet, name="favorite_snippet"),
    path("code_view/<int:pk>/clone/", views.clone_snippet, name="clone_snippet"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))] + urlpatterns