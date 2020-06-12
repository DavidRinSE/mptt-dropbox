from django.shortcuts import render
from .models import Node_Model
# Create your views here.
def index(request):
    return render(request, "index.html", {"file_system": Node_Model.objects.all()})