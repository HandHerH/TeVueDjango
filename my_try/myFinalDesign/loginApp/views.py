import json
import random

from django.core.cache import caches
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import User
from .tools.verify import VerifyForm
from .tools import info


# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login_window.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # name = request.POST.get('name')
        # phone = request.POST.get('phone')

        if not all([username, password]):
            return JsonResponse({'code': 400, 'message': '认证失败'}, status=400)

        # if not VerifyForm.verify('phone', phone):
        #     return JsonResponse({'code': 400, 'message': '认证失败'}, status=400)

        # obj = User(username=username, password=password, name=name, phone=phone)
        # obj.save()


class SendInfoView(View):
    def get(self):
        return HttpResponse('找不到页面', status=404)

    def post(self, request):
        data = json.loads(request.body)
        phone = data.get('phone')
        verify_code = random.randint(1000, 9999)
        if not info.send_verify_code(phone, verify_code):
            return JsonResponse({'code': 400, 'message': '验证码发送失败'}, status=400)

        cache = caches['phone']
        cache.set(phone, verify_code, timeout=60 * 10)
        return JsonResponse({'code': 200, 'message': '验证码已发送'}, status=200)


class RegisterView(View):
    def get(self, request):
        return render(request, 'register_page.html')

    def post(self, request):
        pass
