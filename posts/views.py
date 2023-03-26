from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from accounts.models import Account
from posts.forms import PostForm
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


class PostCreateView(CreateView):
    template_name = 'post_add_view.html'
    form_class = PostForm
    model = Post

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            form.instance.author = user
            form.save()
            return redirect('index')
            # return redirect('profile', pk=user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('index')
        # return reverse('profile', kwargs={'pk': self.request.user.pk})
