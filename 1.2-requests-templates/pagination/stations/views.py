from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('pagination/data-398-2018-08-30.csv', newline='\n', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        CONTENT = [name for name in reader]
        param_page = int(request.GET.get('page', 1))
        content = Paginator(CONTENT, 10)
        stations = content.get_page(param_page)
        page = content.get_page(param_page)
        context = {
            'bus_stations': stations,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
