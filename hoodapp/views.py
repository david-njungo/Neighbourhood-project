from django.shortcuts import render,redirect
from .models import Neighhood,Business,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
# Create your views here.

def home(request):
    hoods = Neighhood.objects.all()
    return render(request, 'home.html',{"hoods" : hoods})

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

@login_required(login_url='/accounts/login/')
def profile_page(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)          
        return redirect('myprofile')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})