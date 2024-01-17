from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Main page accessed')
    return render(request, 'mainpg.html')


def about(request):
    logger.info(f'About page was visited')
    return render(request, 'aboutme.html')
