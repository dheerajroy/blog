from django.views.generic import ListView, DetailView
from markdown import markdown
from .models import Article

class ListArticlesView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 20
    q = None
    heading = 'Articles'

    def get_queryset(self):
        self.q = self.request.GET.get('q')
        if self.q:
            self.heading = 'Search Results'
            return Article.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-updated_at')
        return Article.objects.order_by('-updated_at')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({'q': self.q, 'heading': self.heading})
        return data

class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        content = markdown(self.object.content)
        data.update({'content': content})
        return data
