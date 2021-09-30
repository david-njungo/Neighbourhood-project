from django.shortcuts import render
from .models import Neighhood,Business,Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses= Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
