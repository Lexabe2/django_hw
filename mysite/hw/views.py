from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

name = 'User Alex'

def index(request):
    logger.info(f"{name} I went to the main page")
    return render(request, 'hw/index.html')

def about_me(request):
    logger.info(f"{name} Went to the main page about me")
    return render(request, 'hw/about_me.html')