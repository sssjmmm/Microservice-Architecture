from django.db import models

# Create your models here.
from django.db import models

class Citylog(models.Model):
    # 关键词
    key = models.CharField(max_length=200)

    # 搜索时间
    time = models.CharField(max_length=200)
