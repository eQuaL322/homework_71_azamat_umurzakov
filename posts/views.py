from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from accounts.models import Account
from posts.models import Post


class PostListView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return context
        user: Account = self.request.user
        # subscriptions = user.subscriptions.all()
        posts = Post.objects.all()
        # subscriptions_posts = posts.filter(author__in=subscriptions)
        context['posts'] = posts
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_add_view.html'
    model = Post
    fields = ['image', 'description']

    def form_valid(self, form):
        self.object: Post = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('account_detail', kwargs={'username': self.request.user.username})


class PostDetailView(DetailView):
    template_name = 'post_detail_view.html'
    model = Post
    context_object_name = 'post'
