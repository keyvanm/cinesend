from django.shortcuts import redirect

__author__ = 'k1'


def homepage(request):
    if request.user.is_authenticated():
        return redirect('asset-list')
    else:
        return redirect('account_login')
