from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
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

# class PostCreateView(CreateView):
#     template_name = 'post_add_view.html'
#     form_class = PostForm
#     model = Post
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = self.request.user.username
#             post.save()
#             return redirect('account_detail', username=post.author.username)
#         context = {}
#         context['form'] = form
#         return self.render_to_response(context)
#
#     def get_success_url(self):
#         return reverse('account_detail', kwargs={'username': self.request.user.username})
