import forms

from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.utils.http import is_safe_url
from django.utils.translation import LANGUAGE_SESSION_KEY, check_for_language

from generic_views import LoginMixin, MessageView


class DashboardView(LoginMixin, TemplateView):
    template_name = 'dashboard.html'
    title = _('Welcome')
    view_name = 'dashboard'


class ChangeLanguage(View):
    def get(self, request, code):
        redirect = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=redirect, host=request.get_host()):
            redirect = '/'
        if code and check_for_language(code):
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = code
        return HttpResponseRedirect(redirect)


class UserProfileEdit(UpdateView, MessageView):
    form_class = forms.UserForm
    view_name = 'user_edit'
    template_name = 'user_edit.html'
    title = _('Change user information')
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        self.add_message(_('Profile changed.'), messages.SUCCESS)
        return HttpResponseRedirect('/')


class PasswordChangeDone(MessageView, View):
    """
        Redirect page that adds success message
    """
    def get(self, request):
        self.add_message(_('Password changed successfully.'), messages.SUCCESS)
        return HttpResponseRedirect('/')
