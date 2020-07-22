from django.shortcuts import render
from .models import contactdata
from .forms import contactform
from django.http.response import HttpResponse

# Create your views here.


def contact_display(request):
    if request.method == 'POST':
        cform = contactform(request.POST)
        if cform.is_valid():
            name1 = request.POST.get('name')
            mobile1 = request.POST.get('mobile')
            email1 = request.POST.get('email')
            course1 = request.POST.get('course')
            location1 = request.POST.get('location')

            sunil = contactdata(
                name=name1,
                mobile=mobile1,
                email=email1,
                course=course1,
                location=location1
            )
            sunil.save()
            cform = contactform()
            return render(request, 'contactform.html', {'cform': cform})
        else:
            return HttpResponse('Invalid')
    else:
        cform = contactform()
        return render(request, 'contactform.html', {'cform': cform})