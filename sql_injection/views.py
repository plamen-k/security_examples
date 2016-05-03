from django.shortcuts import render, render_to_response
from django.db import connection
from django.template import RequestContext
from csrf.models import Payment
# Create your views here.

def inject(request):
    result = ''
    if request.method == "POST":
        cursor = connection.cursor()
        query = 'SELECT count(*) FROM csrf_payment where receiver="' + request.POST.get('search') + '"'
        print query
        cursor.executescript( query )
        result = cursor.fetchall()[0]
        
    return render_to_response('inject.html', {'result' : result}, context_instance=RequestContext(request))

def payments(request):
    payments = Payment.objects.all()
    return render_to_response('payments.html', {'payments': payments})