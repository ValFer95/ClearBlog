from blog.models import Post, PostCategory, Comment

def get_category_and_posts(category_name):
    articles = Post.objects.filter(published=True)

    if category_name == '':
        category = ''
    else:
        try:
            category = PostCategory.objects.get(name__iexact=category_name)
            articles = articles.filter(category = category)
        except PostCategory.DoesNotExist:
            category = PostCategory(name=category_name)
            articles = Post.objects.none()

    articles = articles.order_by("-created_at")
    return category, articles


def get_nb_posts_category():
    categories = PostCategory.objects.all().order_by('name')
    list_category_nb_articles = []

    for c in categories:
        #nb_articles = PostCategory.objects.filter(name=c.name).count()
        nb_articles = Post.objects.filter(category__name=c.name).count()
        list_category_nb_articles.append((c.name, nb_articles))

    return list_category_nb_articles


def get_article(article_id):
    article_info = Post.objects.get(id=article_id)
    return article_info

def get_titles_article(category_name, article_id):
    article_titles = Post.objects.filter(published=True, category__name=category_name)
    article_titles = article_titles.exclude(id=article_id)
    return article_titles


def get_comment(article_id):
    comment_data = Comment.objects.filter(post__id=article_id).exclude(status=Comment.STATUS_HIDDEN).order_by('-created_at')
    return comment_data