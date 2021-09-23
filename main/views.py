from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

BASE_CONTEXT = {"title": "Neurothrone"}


class HomeView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "main/index.html", BASE_CONTEXT)
