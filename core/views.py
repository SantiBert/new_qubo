import secrets
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django import forms
from django.views import View
from django.db.models import Q
from django.urls import reverse_lazy

from .forms import ProfileForm, EmailForm, NameUpdateForm
from .models import Profile
from blog.models import BlogCategory, BlogEntry


class IndexView(View):
    def get(self, request, *args, **kwargs):
        all_note = list(BlogEntry.objects.filter(active=True))
        featureds = BlogEntry.objects.filter(active=True, featured=True)
        recents = BlogEntry.objects.filter(
            active=True).order_by('-created_date')[:4]
        categories = BlogCategory.objects.filter(is_active=True)
        secure_random = secrets.SystemRandom()
        list_of_random_items = secure_random.sample(all_note, 4)
        context = {
            'ramdoms': list_of_random_items,
            'featureds': featureds,
            'recents': recents,
            'categories': categories

        }
        return render(request, "index.html", context)


class SearchView(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        categories = BlogCategory.objects.filter(is_active=True)
        featured = BlogEntry.objects.filter(
            active=True, featured=True).order_by('-created_date')
        if queryset:
            posts = BlogEntry.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset),
                active=True
            ).distinct().order_by('-created_date')

        context = {
            'categories': categories,
            'featured': featured,
            'object_list': posts,
        }
        return render(request, 'results.html', context)


@method_decorator(login_required, name='dispatch')
class AdministrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "administration.html", )


@method_decorator(login_required, name='dispatch')
# Actualiza o crea los datos de un usuario para un perfil
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):  # Permite editar el e-mail de un usuario
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form


@method_decorator(login_required, name='dispatch')
class NameUpdate(UpdateView):  # Permite editar el e-mail de un usuario
    form_class = NameUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_name_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(NameUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'})
        return form
