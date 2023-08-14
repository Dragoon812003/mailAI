from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.http import JsonResponse
import joblib, os, mimetypes
from mail_checker import settings
from sendfile import sendfile
from datetime import datetime
from .utils import model, feature_extraction, format_developer_names
from .models import *

# Create your views here.

def index(request):
    developers = Developer.objects.all()
    current_year = datetime.now().year
    formatted_names = format_developer_names([(developer.name, developer.linkedin_link) for developer in developers])
    return render(request, 'main/index.html', {"developers": developers, "year": current_year, "names": formatted_names})

def submit_mail(request):
    if request.method == "POST":
        user_input = request.POST.get('mail')

        input_data_features = feature_extraction.transform([user_input])
        prediction = model.predict(input_data_features)
        return JsonResponse({"prediction": bool(prediction[0] == 0)}, safe=False)
    return redirect(reverse('index'))

def serve_developer_profile_pic(request, timestamp):
    developer = get_object_or_404(Developer, timestamp=timestamp)
    image = developer.profile_pic
    image_name = image.name.split('/')[-1]
    image_path = os.path.join(settings.MEDIA_ROOT, 'profile_pic', timestamp, image_name)
    mimetype = mimetypes.guess_type(image_path)[0]
    return sendfile(request, image_path, mimetype=mimetype)
