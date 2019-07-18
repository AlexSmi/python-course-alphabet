from django.contrib import messages
from account.models import Profile


class FormMessageMixin(object):

    form_invalid_message = 'Please correct the errors below.'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            profile = Profile.objects
            if profile.filter(user=self.request.user):
                get_profile = profile.get(user=self.request.user)
                form.instance.author = get_profile
        messages.success(self.request, self.form_valid_message)
        return super(FormMessageMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.form_invalid_message)
        return super(FormMessageMixin, self).form_invalid(form)
