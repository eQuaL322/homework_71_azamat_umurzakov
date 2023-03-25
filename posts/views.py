from django.views.generic import ListView

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
        print(self.request.user.is_authenticated)
        user: Account = self.request.user
        subscriptions = user.subscriptions.all()
        posts = Post.objects.all()
        subscriptions_posts = posts.filter(author__in=subscriptions)
        context['posts'] = subscriptions_posts

        return context
