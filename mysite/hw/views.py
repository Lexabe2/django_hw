from django.shortcuts import render, redirect
import logging
from datetime import datetime, timedelta
from .models import Order
from .forms import AddPhoto

logger = logging.getLogger(__name__)

name = 'User Alex'


def index(request):
    now = datetime.now()

    orders_7_days = Order.objects.filter(date__gte=now - timedelta(days=7))

    orders_30_days = Order.objects.filter(date__gte=now - timedelta(days=30))

    orders_365_days = Order.objects.filter(date__gte=now - timedelta(days=365))

    return render(request, 'hw/index.html', {
        'orders_7_days': orders_7_days,
        'orders_30_days': orders_30_days,
        'orders_365_days': orders_365_days,
    })


def add_photo(request):
    if request.method == 'POST':
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddPhoto()

    return render(request, 'hw/add_photo.html', {'form': form})


def about_me(request):
    logger.info(f"{name} Went to the main page about me")
    return render(request, 'hw/about_me.html')
