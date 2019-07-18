
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View
)

from article.models import Article, Comments
from article.mixins import FormMessageMixin
from article.forms import ArticleForm, CommentsForm


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('title').reverse()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All title'
        return context


class CommentArticleCreate(View):

    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            app_label, model = form.cleaned_data['model_name'].lower().split(
                '.')
            Comments.objects.create(
                author=getattr(request.user, 'profile', None),
                content_type=ContentType.objects.get(
                    app_label=app_label, model=model),
                object_id=int(form.cleaned_data['object_id']),
                comment=form.cleaned_data['comment'],
            )
        else:
            # todo: error handling
            pass

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ArticleCreateView(FormMessageMixin, CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm
    form_valid_message = 'Article created success'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = timezone.now()
        context['comments'] = Comments.objects.all()
        for field in context['article']._meta.get_fields():
            if field.name == 'title':
                context['title_name'] = field.name
            if field.name == 'description':
                context['description_name'] = field.name
        return context


class ArticleUpdateView(FormMessageMixin, UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'
    form_valid_message = 'Updated successfully!'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDeleteView(DeleteView):
    model = Article
    pk_url_kwarg = 'article_id'
    template_name = 'article/confirm_delete.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('index')
