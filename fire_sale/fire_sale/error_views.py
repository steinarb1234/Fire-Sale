from django.shortcuts import render
from django.views.defaults import permission_denied


def permission_denied_view(request, exception):
    return render(request, 'error_pages/not_authorized.html', status=403)


def page_not_found_view(request, exception=None):
    return render(request, 'error_pages/page_not_found.html', status=404)

