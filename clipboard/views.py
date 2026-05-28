from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from .models import Snippet

def home(request):
    if request.method == 'POST':
        new_text = request.POST.get('clipboard_text')
        # Check if the user ticked the "Keep Permanently" box
        keep_permanently = request.POST.get('keep_permanently') == 'on'
        
        if new_text:
            Snippet.objects.create(
                content=new_text, 
                keep_permanently=keep_permanently
            )
            return redirect('home')

    # THE 7-DAY LOGIC
    # 1. Figure out exactly what time it was 7 days ago
    time_threshold = timezone.now() - timedelta(days=7)
    
    # 2. Tell the database to only give us snippets that were created AFTER the threshold, 
    # OR snippets where keep_permanently is True.
    snippets = Snippet.objects.filter(
        Q(created_at__gte=time_threshold) | Q(keep_permanently=True)
    ).order_by('-created_at')
    
    return render(request, 'clipboard/home.html', {'snippets': snippets})