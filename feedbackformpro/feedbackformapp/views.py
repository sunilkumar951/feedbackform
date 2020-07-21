from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt

date1 = dt.datetime.now()


def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')

            data = FeedbackData(
                name=name1,
                date=date1,
                rating=rating1,
                feedback=feedback1
            )
            data.save()
            form = FeedbackForm()
            feedbacks = FeedbackData.objects.all()
            return render(request, 'feedbackdata.html', {'form': form, 'feedbacks': feedbacks})
        else:
            return HttpResponse("Invalid Data")
    else:
        form = FeedbackForm()
        feedbacks = FeedbackData.objects.all()
        return render(request, 'feedbackdata.html', {'form': form, 'feedbacks': feedbacks})
