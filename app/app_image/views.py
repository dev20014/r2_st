from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import ModelSerializer
from .models import Document, PrivateDocument
from rest_framework.viewsets import ModelViewSet

def hello_world(request):
    return render(request, 'hello_world.html', {})




# @method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class PrivateDocumentCreateView(CreateView):
    model = PrivateDocument
    fields = ['upload', ]
    success_url = reverse_lazy('profile')


# serializers.py
class PrivateDocumentSerializer(ModelSerializer):
    class Meta:
        model = PrivateDocument
        fields = '__all__'

# views.py
class PrivateDocumentViewSet(ModelViewSet):
    queryset = PrivateDocument.objects.all()
    serializer_class = PrivateDocumentSerializer