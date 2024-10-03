from django.shortcuts import render, redirect, get_object_or_404
from .models import UserDetails
from .forms import UserDetailsForm

# Create or Add a new User
def create_user(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserDetailsForm()
    return render(request, 'crud_app/create_user.html', {'form': form})

# Read or List all Users
def user_list(request):
    users = UserDetails.objects.all()
    return render(request, 'crud_app/user_list.html', {'users': users})

# Update User Details
def update_user(request, user_id):
    user = get_object_or_404(UserDetails, pk=user_id)
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserDetailsForm(instance=user)
    return render(request, 'crud_app/update_user.html', {'form': form})

# Delete a User
def delete_user(request, user_id):
    user = get_object_or_404(UserDetails, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'crud_app/delete_user.html', {'user': user})

