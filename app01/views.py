from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse

from app01 import models


def pie(request):
    """ 饼图

    :param request:
    :return:
    """
    return render(request, 'pie.html')


def pie_data(request):
    """ 获取饼状数据
    构造数据结构
        [
            {'name':'销售','y':4},
            {'name':'运营','y':24},
            {'name':'运维','y':14},
        ]

    :param request:
    :return:
    """
    result = models.Server.objects.values('depart__title').annotate(y=Count('depart_id'))
    data = [{'y': item['y'], 'name': item['depart__title']} for item in result]
    print(data)
    return JsonResponse(data, safe=False)
