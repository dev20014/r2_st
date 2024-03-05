from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Document, PrivateDocument


def hello_world(request):
    return render(request, 'hello_world.html', {})




# @method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class PrivateDocumentCreateView(CreateView):
    model = PrivateDocument
    fields = ['upload', ]
    success_url = reverse_lazy('profile')