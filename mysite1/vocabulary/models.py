from django.db import models

"""翻译表"""
class WordsInfo(models.Model):
    words=models.CharField(verbose_name="原单词",max_length=32)
    translation=models.CharField(verbose_name="译文",max_length=64)
    additon=models.CharField(verbose_name="备注",max_length=64,null=True,blank=True)
"""查询表"""
class Lookup(models.Model):
    title=models.CharField(verbose_name="标题",max_length=32)
    words=models.CharField(verbose_name="原单词",max_length=32)
    translation=models.CharField(verbose_name="译文",max_length=64)
    additon=models.CharField(verbose_name="备注",max_length=64,null=True,blank=True)
    add_time=models.DateTimeField(verbose_name="添加时间",)



    