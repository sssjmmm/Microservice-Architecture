from django.http import JsonResponse
import json

# 导入 city 
from common.models import Citylog

def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_city':
        return listcities(request)
    elif action == 'add_city':
        return addcity(request)
    elif action == 'modify_city':
        return modifycity(request)
    elif action == 'del_city':
        return deletecity(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

def listcities(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Citylog.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})

def addcity(request):

    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象 
    record = Citylog.objects.create(key=info['key'] ,
                            time=info['time'])

    return JsonResponse({'ret': 0, 'id':record.id})


def modifycity(request):

    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    
    cityid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        city = Citylog.objects.get(id=cityid)
    except Citylog.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{cityid}`的城市不存在'
        }


    if 'key' in  newdata:
        city.key = newdata['key']
    if 'time' in newdata:
        city.time = newdata['time']

    # 注意，一定要执行save才能将修改信息保存到数据库
    city.save()

    return JsonResponse({'ret': 0})

def deletecity(request):

    cityname = request.params['key']

    try:
        # 根据 key 从数据库中找到相应的城市记录
        cityinfo = Citylog.objects.get(key=cityname)
    except Citylog.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'key 为`{cityname}`的城市不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    cityinfo.delete()

    return JsonResponse({'ret': 0})