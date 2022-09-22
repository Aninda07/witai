from django.shortcuts import render
import json, requests, random, re
from pprint import pprint
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
import json
from . import tests
from jsonfield import JSONField
from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
import numpy as np
from rest_framework import serializers
from datetime import datetime, date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import pandas as pd
from django.urls import path
from PIL import Image, ImageDraw, ImageFont, ImageOps
from django.conf import settings
import face_recognition
import requests
from django.shortcuts import render
from django import forms
import random
import requests


class Montact(models.Model):
    Chat = models.CharField(max_length=200, default="null")
    Intent = models.CharField(max_length=200, default="null")
    Sender_ID = models.CharField(max_length=200, default='10000')

    def __str__(self):
        return self.Intent

class Contact(models.Model):
    Utterance = models.CharField(max_length=200, default="null")
    Entities = models.CharField(max_length=500, default="null")
    Traits = models.CharField(max_length=500, default="null")
    Shrug = models.ForeignKey(Montact, null=True, on_delete=models.SET_NULL)
    Details = models.JSONField()











