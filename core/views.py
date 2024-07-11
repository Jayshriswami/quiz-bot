from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def chat(request):
    try:
        if not request.session.session_key:
            request.session.create()

        context = {
            'user': request.user,
            'session_key': request.session.session_key
        }
        
        return render(request, 'chat.html', context)
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
