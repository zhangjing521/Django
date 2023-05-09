from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import WordInfo
import datetime
import json


# Create your views here.
def index(request):
    data = {}
    words_data = WordInfo.objects.all()
    data['data'] = json.loads(serializers.serialize('json', words_data))
    return JsonResponse(data)

def add_word(request):
    if request.method == 'GET':
        return render(request, 'words/add.html')
    else:
        params = request.POST
        word = params.get('word')

        word_set = WordInfo.objects.filter(word=word)
        if len(word_set) == 0:
            translate_info = params.get('translate_info')
            extra_info = params.get('extra_info')
            time = datetime.date.today()

            try:
                new_word = WordInfo.objects.create(
                    word = word,
                    translate_info = translate_info,
                    extra_info = extra_info,
                    time = time
                )
                new_word.save()
            except Exception as e:
                return HttpResponse(e.args[1])
        else:
            return render(request, 'words/word_exist.html', context={
                'word': word
            })
        return HttpResponse('pass successful')