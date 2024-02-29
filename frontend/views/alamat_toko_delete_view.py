from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from store.models import UserStoreAddress

from .base_view import FrontPage


@method_decorator(csrf_exempt, name="dispatch")
class DeleteAlamatToko(FrontPage):
    def post(self, request, id, id_alamat):
        userprofileaddress = UserStoreAddress.objects.get(pk=id_alamat)
        userprofileaddress.delete()
        return redirect(reverse("alamat_toko", id))
