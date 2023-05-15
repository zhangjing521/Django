from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.shortcuts import render,HttpResponse,redirect
from vocabulary.models import Lookup,WordsInfo
from vocabulary import models
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from vocabulary.utils.pagination import Pagination
from django.http.request import QueryDict
import copy
import datetime
import json

def words_translate(request):
    return render(request,"words_translate.html")

def words_list(request):
    """单词列表"""
    data_dict = {}
    # 如果是空字典,表示获取所有
    # 不加后面的 "", 首次访问浏览器,搜索框中不会显示前端页面中的 placeholder="Search for..." 属性
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["words__contains"] = search_data 
    
    queryset = Lookup.objects.filter(**data_dict)
    print(queryset[0])

    ### 引入封装的 Pagination 类并初始化
    # 初始化
    page_object = Pagination(request, queryset, page_size=10, page_param="page")
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "pretty_data": page_queryset,   # 分页的数据
        "search_data": search_data,     # 搜索的内容
        "page_string": page_string,     # 页码
        "head_page": head_page,         # 首页
        "end_page": end_page,           # 尾页
    }

    return render(request, "words_list.html", context)

def words_add(request):
    """添加单词"""
    if request.method=="GET":
        return render(request,"words_add.html")
    #获取POST提交过来的数据
    words=request.POST.get("words")
    translation=request.POST.get("translation")
    additon=request.POST.get("additon")
    add_time = datetime.date.today()
    add_time = add_time.strftime("%Y-%m-%d-%H-%M-%s") # 修改时间格式

    #保存到数据库
    models.Lookup.objects.create(
        words=words,
        translation=translation,
        additon=additon,
        add_time=add_time
    )

    #重定向回部门列表
    return redirect("/words/list/")

def words_delete(request):
    """删除单词"""
    nid=request.GET.get("nid")
    models.Lookup.objects.filter(id=nid).delete()
    #重定向回部门列表
    return redirect("/words/list/")

class AddModelForm(forms.ModelForm):
    """添加单词"""
    class Meta:
        model = models.Lookup
        fields = ["words","translation","additon","add_time"]
        #exclude = ["paichu"]
        # fields = "__all__"
    def __init__(self, *args, **kwargs):
        #继承另一个类的参数
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class" : "form-control", "placeholder" : field.label}
    
    def clean_words(self):
        txt_words = self.cleaned_data["words"]
        exists =models.Lookup.objects.filter(words = txt_words).exists()
        if exists:
            raise ValidationError("单词已存在")
        return txt_words
def words_model_form_add(request):
    if request.method=="GET":
        form = AddModelForm()
        return render(request, "words_model_form_add.html" , {"form": form})
    #POST提交数据，数据校验
    form = AddModelForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect("/words/list/")
    else:
        return render(request, "words_model_form_add.html" , {"form": form})

class EditModelForm(forms.ModelForm):
    class Meta:
        model = models.Lookup
        fields = ["words","translation","additon","add_time"]
        #exclude = ["paichu"]
        # fields = "__all__"
    def __init__(self, *args, **kwargs):
        #继承另一个类的参数
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class" : "form-control", "placeholder" : field.label}

    def clean_words(self):
        txt_words = self.cleaned_data["words"]
        exists = models.Lookup.objects.exclude(id = self.instance.pk).filter(words=txt_words).exists()
        if exists:
            raise ValidationError("单词已存在")
        return txt_words

def words_edit(request, nid):
    """修改单词"""
    row_object=models.Lookup.objects.filter(id=nid).first()
    if request.method=="GET":
        #根据nid获取数据

        form = EditModelForm(instance = row_object)

        return render(request, "words_edit.html" , {"form": form})
    
    form = EditModelForm(data = request.POST,instance = row_object)

    if form.is_valid():
        form.save()
        return redirect("/words/list/")
    else:
        return render(request, "words_edit.html" , {"form": form})
    
    # return Json object
    # {
    #     'status_code':200, 400, 404 , 500,
    #     'error_msg':'数据库连接错误| 服务器异常',
    #     'data':[
    #         'wordInfo':{
    #             'words': 'he',
    #             'translate':'str'
    #         },
    #         'wordInfo':{}
    #     ]|{}
    # }