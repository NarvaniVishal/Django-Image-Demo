# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import Stu

# Create your views here.
def index(request):
	obj= Stu.objects.all()
	return render(request,'app1/index.html',{'data':obj})
