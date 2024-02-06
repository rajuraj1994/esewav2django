from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userspage.auth import admin_only

# Create your views here.
@login_required
@admin_only
def admin_home(request):
    return render(request,'admins/dashboard.html')