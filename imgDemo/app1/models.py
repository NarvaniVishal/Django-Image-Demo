# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stu(models.Model):
	stu_name=models.CharField(max_length=200)
	stu_img=models.ImageField(upload_to='img')