from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Request
from .forms import RequestForm
from .models import User, Request  
from .models import User
from .forms import UserForm # Add Proof here
from .forms import RequestForm
from django.shortcuts import render, redirect
from django.contrib import messages 


def home(request):
    return render(request, 'myapp/home.html')  # Create a home.html template

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'myapp/request_list.html', {'requests': requests})  # Create a request_list.html template

def request_detail(request, request_id):
    request_item = get_object_or_404(Request, request_id=request_id)
    user = request_item.user_id  # Get the associated user
    context = {
        'request': request_item,
        'user': user,
    }
    return render(request, 'myapp/request_detail.html', context)


def request_form(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_instance = form.save(commit=False)
            request_instance.user_id = request.user  # Associate the request with the logged-in user
            request_instance.save()
            messages.success(request, 'Request created successfully!')  # Success message
            return redirect('user_profile')  # Redirect to user profile after saving
    else:
        form = RequestForm()
    
    return render(request, 'myapp/request_form.html', {'form': form})


def user_form(request, user_id=None):
    user = get_object_or_404(User, user_id=user_id) if user_id else None

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)  # Use the form with the instance
        if form.is_valid():
            form.save()  # Save the changes to the user
            return redirect('user_list')  # Redirect after saving
    else:
        form = UserForm(instance=user)  # Prepopulate the form with user data

    return render(request, 'myapp/user_form.html', {'form': form, 'user': user})


def user_list(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})

# myapp/views.py



def user_profile(request):
    user = request.user  # Get the logged-in user
    requests = Request.objects.filter(user_id=user)  # Get the user's requests
    if request.method == 'POST':
        request_form = RequestForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if request_form.is_valid():
            request_instance = request_form.save(commit=False)
            request_instance.user_id = user  # Associate the request with the user
            request_instance.save()
            return redirect('user_profile')  # Redirect to the profile page after saving
    else:
        request_form = RequestForm()

    return render(request, 'myapp/user_profile.html', {
        'user': user,
        'requests': requests,
        'request_form': request_form  # Pass the form to the template
    })
