from django.shortcuts import render, get_object_or_404
from .models import Request
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'myapp/home.html')  # Create a home.html template

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'myapp/request_list.html', {'requests': requests})  # Create a request_list.html template

def request_detail(request, request_id):
    request_item = get_object_or_404(Request, request_id=request_id)
    return render(request, 'myapp/request_detail.html', {'request': request_item})  # Create a request_detail.html template

from django.shortcuts import render, get_object_or_404
from .models import User

def request_detail(request, request_id):
    request_detail = get_object_or_404(Request, request_id=request_id)
    user = request_detail.user_id  # Get the associated user
    context = {
        'request': request_detail,
        'user': user,
    }
    return render(request, 'myapp/request_detail.html', context)

def request_form(request):
    if request.method == 'POST':
        description = request.POST.get('request_description')
        # Assuming you have user_id from session or passed in context
        user_id = request.user.user_id  # Adjust based on your logic
        Request.objects.create(user_id_id=user_id, request_description=description)
        return redirect('request_list')
    return render(request, 'myapp/request_form.html')

def user_form(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, user_id=user_id)
    else:
        user = None

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        academic_email = request.POST.get('academic_email')
        academic_year = request.POST.get('academic_year')

        if user:
            user.user_name = user_name
            user.academic_email = academic_email
            user.academic_year = academic_year
            user.save()
        else:
            User.objects.create(user_name=user_name, academic_email=academic_email, academic_year=academic_year)

        return redirect('user_list')

    return render(request, 'myapp/user_form.html', {'user': user})

def user_list(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})

def user_profile(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    requests = Request.objects.filter(user_id=user)  # Fetch requests for this user
    context = {
        'user': user,
        'requests': requests,
    }
    return render(request, 'myapp/user_profile.html', context)