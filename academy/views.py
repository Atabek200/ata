from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from django.http import FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View, TemplateView
from django.utils.deprecation import MiddlewareMixin
from django.core.files.uploadhandler import MemoryFileUploadHandler
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class MyView(TemplateView):
    template_name = 'my_template.html'

    @method_decorator(csp_exempt, name='dispatch')
    def dispatch(self, request):
        return super().dispatch(request)


class ImageUploadView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = '/login/'
    permission_required = 'userAlbum.upload_image'

    def __get__(self, request):
        return render(request, 'upload_image.html')

    def post(self, request):
        return render(request, 'upload_success.html')


class CustomFileUploadHandler(MemoryFileUploadHandler):
    def file_allowed(self, file_name):
        allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
        extension = file_name.split('.')[-1].lower()

        if extension == 'exe':
            raise ValidationError("Загрузка файлов с расширением .exe запрещена.")

        return extension in allowed_extensions


class SecurityMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['X-XSS-Protection'] = '1; mode=block'
        response['Content-Security-Policy'] = "default-src 'self'"
        return response


class MyView(LoginRequiredMixin, View):
    def __get__(self, request):
        return HttpResponse("GET request processed.")

    def post(self, request):
        return HttpResponse("POST request processed.")


@login_required
@csrf_protect
def my_view(request):
    if request.method == 'GET':
        # Ваша логика обработки GET-запроса
        return HttpResponse("GET request processed.")
    elif request.method == 'POST':
        # Ваша логика обработки POST-запроса
        return HttpResponse("POST request processed.")
    else:
        return HttpResponse("Method not allowed.", status=405)


def get_user(request):
    username = request.GET.get('username')
    query = f"SELECT * FROM users WHERE username = '{username}'"


def get_users(request):
    username = request.GET.get('username')
    user = get_object_or_404(User, username=username)


class MyFileView(APIView):
    def __get__(self, request):
        file_path = 'academy'
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
        return response


def index(request):
    return render(request, 'index.com.html')


def layout(request):
    return render(request, 'layout.com.html')

