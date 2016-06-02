from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.contrib.auth.models import User # 유저모델 가져오기
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Project_comnet.forms import *
# Create your views here.
