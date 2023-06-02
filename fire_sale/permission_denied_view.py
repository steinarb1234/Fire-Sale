from django.shortcuts import render
from django.views.defaults import permission_denied


def permission_denied_view(request, exception):
    return render(request, 'error_pages/not_authorized.html', status=403)