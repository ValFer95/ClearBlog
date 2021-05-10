from django.shortcuts import render
#from django.http import HttpResponse

from blog.models import Post, PostCategory
from blog import model_helpers
from blog import navigation
from blog import forms


def accueil(request):
     nav_items = navigation.navigation_items(navigation.NAV_WELCOME)
     context = {
          "nav_items" : nav_items
     }
     return render(request, 'blog/accueil.html', context)


def articles_categorie(request, category_name=''):
     category_name, articles = model_helpers.get_category_and_posts(category_name)
     category_nb_articles = model_helpers.get_nb_posts_category()
     nav_items = navigation.navigation_items(navigation.NAV_POSTS)

     context = {
          "articles": articles,
          "category": category_name,
          "categories" : category_nb_articles,
          "nav_items" : nav_items
     }
     return render(request, 'blog/index.html', context)

def article(request, article_id):
     nav_items = navigation.navigation_items(navigation.NAV_POSTS)
     article_info = model_helpers.get_article(article_id)
     article_titles = model_helpers.get_titles_article(article_info.category, article_id)
     comment_form = forms.CommentForm()
     comment_data = model_helpers.get_comment(article_id)

     if request.method == 'POST':
          comment_get_data = forms.CommentForm(request.POST)

          if comment_get_data.is_valid():
               comment = comment_get_data.save(commit=False)
               comment.post = article_info
               comment.save()
               message = "Votre commentaire est enregistré !"

     else:
          message = ''

     context = {
          "id_article": article_id,
          "article" : article_info,
          "nav_items": nav_items,
          'article_titles' : article_titles,
          "comment_form" : comment_form,
          'comment_data' : comment_data,
          'message' : message,
     }
     return render(request, 'blog/article.html', context)


def about(request):
     nav_items = navigation.navigation_items(navigation.NAV_ABOUT)
     context = {
          "nav_items" : nav_items
     }
     return render(request, 'blog/about.html', context)
