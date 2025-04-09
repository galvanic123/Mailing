from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

from users.models import CustomsUser


@login_required
def block_user(self, pk):
    user = CustomsUser.objects.get(pk=pk)
    user.is_active = {user.is_active: False, not user.is_active: True}[True]
    user.save()
    return redirect(reverse("users:user_list"))