from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['auteur', 'commentaire']

        widgets = {
            'auteur' : forms.TextInput(attrs=
                    {
                        'class' : 'fst-italic',
                        'placeholder' : 'Votre nom'
                    }),
            'commentaire': forms.Textarea(attrs=
                    {
                        'class': 'fst-italic',
                        'placeholder' : 'Votre commentaire',
                        'rows' : 10,
                        'cols' : 80,
                    }),
        }

