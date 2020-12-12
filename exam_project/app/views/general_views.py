from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


class MasterData(TemplateView):
    template_name = 'master_data.html'
