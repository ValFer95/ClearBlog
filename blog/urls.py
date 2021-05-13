from django.urls import path

from blog import views

urlpatterns = [
    path('accueil/', views.accueil, name="accueil"),
    path('articles/', views.articles_categorie, name="articles"),
    path('articles/<str:category_name>', views.articles_categorie, name="articles_liste"),
    path('article/<int:article_id>', views.article, name="article"),
    path('propos/', views.about, name="a_propos"),

    path('', views.accueil, name="index"),
]



