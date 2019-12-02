import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def add(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            num = json.loads(request.body)
            A_first = num['A']
            B_second = num['B']
            if type(A_first) == int and type(B_second) == int:
                A_and_B_total = A_first + B_second
                return JsonResponse({'answer': A_and_B_total})
            else:
                response = JsonResponse({'error': 'Need integer(Где чила)'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response


@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            num = json.loads(request.body)
            A_num = num['A']
            B_num = num['B']
            if type(A_num) == int and type(B_num) == int:
                A_and_B_total = A_num + B_num
                return JsonResponse({'answer': A_and_B_total})  # ВЕРНУЛА ДЕЙСТВИЕ СЛОЖЕНИЕ
            else:
                response = JsonResponse({'error': 'Need integer(Где чила)'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response


def multiply(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            num = json.loads(request.body)
            A_num = num['A']
            B_num = num['B']
            if type(A_num) == int and type(B_num) == int:
                A_and_B_total = A_num * B_num
                return JsonResponse({'answer': A_and_B_total})
            else:
                response = JsonResponse({'error': 'Need integer(Где чила)'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response


def divide(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            num = json.loads(request.body)
            A_num = num['A']
            B_num = num['B']
            if type(A_num) == int and type(B_num) == int:
                A_and_B_total = A_num / B_num
                return JsonResponse({'answer': A_and_B_total})
            else:
                response = JsonResponse({'error': 'Need integer(Где чила)'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'No data provided'})
            response.status_code = 400
            return response
