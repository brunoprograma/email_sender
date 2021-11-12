from dal import autocomplete
from django.core.validators import validate_email, ValidationError
from .models import Recipient


class RecipientAutocomplete(autocomplete.Select2QuerySetView):
    """
    Retrieves the recipients to the admin.EmailMessageAdmin form
    """
    def get_queryset(self):
        if not (self.request.user.is_staff or self.request.user.is_superuser):
            return Recipient.objects.none()

        qs = Recipient.objects.all()

        if self.q:
            qs = qs.filter(email__istartswith=self.q)

        return qs

    def get_create_option(self, context, q):
        if q:
            try:
                validate_email(q)
            except ValidationError:
                return []
        return super().get_create_option(context, q)

