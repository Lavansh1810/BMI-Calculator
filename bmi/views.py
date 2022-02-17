from asyncio.windows_events import NULL
from enum import Flag
from pickle import DICT
import re
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm


def bmi_calc(weight, feet, inch):
    height = (feet+(inch/12))*0.3048
    if(height == 0):
        return 0
    ans = weight / (height*height)
    return round(ans, 2)


def bmi(request):
    result = 0
    flag = 0
    str = ' '
    if request.method == 'POST':
        flag = 1
        weight = request.POST['weight']
        feet = request.POST['feet']
        inch = request.POST['inch']
        result = bmi_calc(int(weight), int(feet), int(inch))

        if result < 15:
            str = ' You are very severely underweight.'

        elif result >= 15 and result <= 16:
            str = ' You are severely underweight.'

        elif result > 16 and result <= 18.5:
            str = ' You are underweight.'

        elif result > 18.5 and result <= 25:
            str = ' You are Normal (healthy weight).'

        elif result > 25 and result <= 30:
            str = ' You are overweight.'

        elif result > 30 and result <= 35:
            str = ' You are moderately obese.'

        elif result > 35 and result <= 40:
            str = ' You are severely obese.'

        elif result > 40:
            str = ' You are very severely obese.'

    dict = {'result': result, 'flag': flag, 'str': str}

    return render(request, 'main.html', dict)
