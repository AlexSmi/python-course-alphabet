from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.shortcuts import render

from account.models import Profile
from account.forms import ProfileForm, UserForm


class ProfileDetailView(DetailView):
    template_name = 'account/profile.html'
    model = Profile
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'


class StartView(ListView):
    model = Profile
    template_name = 'start.html'


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', profile_form.instance.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/form.html', {
        'profile_form': profile_form
    })


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Create user
        created_user = form.save()
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, authenticated_user)
        return redirect('profile', created_user.profile.user_id)
