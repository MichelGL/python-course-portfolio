from django.views.generic import ListView

from author.models import Author


class AthorView(ListView):
    model = Author
    template_name = "author/author.html"
