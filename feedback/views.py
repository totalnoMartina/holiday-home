from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Feedback
from .forms import FeedbackForm




def see_feedbacks(request):
    """ A posting of feedback for guests """
    feedbacks = Feedback.objects.order_by('-date_posted')
    context = {   
        'feedbacks': feedbacks
    }
    return render(request, 'feedback/feedback.html', context)

@login_required
def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback submitted successfully')
            return redirect('home')
    else:
        form = FeedbackForm()
    context = {'form': form}

    return render(request, 'feedback/add_feed.html', context)
