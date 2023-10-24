from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from  common.models import Citylog

def listlogs(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Citylog.objects.values()

    # 检查url中是否有参数key
    ph = request.GET.get('key',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(key=ph)

    # 定义返回字符串
    retStr = ''
    for citylog in  qs:
        for key,value in citylog.items():
            retStr += f'{key} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)