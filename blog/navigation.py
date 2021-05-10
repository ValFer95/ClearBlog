from django.urls import reverse_lazy

NAV_WELCOME = 'Accueil'
NAV_POSTS = 'Articles'
NAV_ABOUT = 'A propos...'

NAV_ITEMS = (
    (NAV_WELCOME, reverse_lazy('accueil')),
    (NAV_POSTS, reverse_lazy('articles')),
    (NAV_ABOUT, reverse_lazy('a_propos')),
)


def navigation_items(selected_item):
    nav_items = []
    for name, url in NAV_ITEMS:
        nav_items.append({
            'name': name,
            'url': url,
            'active': True if selected_item == name else False
        })

    return nav_items