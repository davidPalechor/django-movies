from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('user:login')
    redirect_field_name = 'next'
    template_name = 'dashboard.html'