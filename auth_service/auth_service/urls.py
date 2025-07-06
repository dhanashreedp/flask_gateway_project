from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse # Import HttpResponse

def test_view(request):
    return HttpResponse("This is a test view!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('test-loading/', test_view), # <-- ADD THIS TEMPORARY LINE
]