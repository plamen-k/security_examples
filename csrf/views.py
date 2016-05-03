from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def secure(request):
    return render_to_response('secure.html')

@csrf_exempt
def insecure(request):
    if request.method == 'POST':
        return render_to_response('insecure_owned.html')    

    return render_to_response('insecure.html')
    
    