from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path(route="", view=views.landing_page_view,
         name="landing_page"),  # Landing page
    path("signin/", views.signin_view, name="signin"),  # URL name
    path("survey/", views.survey_view, name="survey"),
    path("completion/", views.completion_view, name="completion"),
]
