from django.urls import re_path
from .views import RecipientAutocomplete


urlpatterns = [
    re_path(
        r'^recipient-autocomplete/$',
        RecipientAutocomplete.as_view(create_field='email'),
        name='recipient-autocomplete',
    ),
]