from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wellcome(request):
    return render(request, "pack_login/wellcome.html")  
# end def

 






 