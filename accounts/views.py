from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView

from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm
from accounts.models import Account


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        email: str = form.cleaned_data.get('email')
        password: str = form.cleaned_data.get('password')
        user = authenticate(request=request, email=email, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


# class ProfileView(LoginRequiredMixin, DetailView):
#     model = get_user_model()
#     template_name = 'user_detail.html'
#     context_object_name = 'user_obj'
#     paginate_related_by = 3
#     paginate_related_orphans = 0
#
#     def get_context_data(self, **kwargs):
#         articles = self.object.articles.order_by('-created_at')
#         paginator = Paginator(articles, self.paginate_related_by, orphans=self.paginate_related_orphans)
#         page_number = self.request.GET.get('page', 1)
#         page = paginator.get_page(page_number)
#         kwargs['page_obj'] = page
#         kwargs['articles'] = page.object_list
#         kwargs['is_paginated'] = page.has_other_pages()
#         return super().get_context_data(**kwargs)


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class SearchAccountListView(ListView):
    template_name: str = 'accounts_search.html'
    model = Account
    context_object_name = 'accounts'

    def get(self, request, *args, **kwargs):
        self.search_value = request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(first_name__iregex=self.search_value) | Q(email__iregex=self.search_value) | Q(
                    username__iregex=self.search_value)
            )
        return queryset


class AccountDetailView(DetailView):
    model = Account
    template_name = 'user_profile.html'
    context_object_name = 'profile'
    slug_field = 'username'
    slug_url_kwarg = 'username'

