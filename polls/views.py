from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone
from django.core import serializers


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html',context)

# def detail(request, question_id):
#     # try:
#     #     # question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})


class IndexView(generic.ListView):
    template_name ='polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]


# class IndexView(generic.list.ListView):
#     model = Question
#     template_name = 'polls/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_question_list'] = Question.objects.filter(
#             pub_date__lte = timezone.now()
#         ).order_by('-pub_date')[:5]
#         return context

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question

    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'errormessage': "Yor did not select a choice.",
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # F方法会覆盖标准的Python运算符来创建一个封装的SQL表达式
        selected_choice.votes = F('votes') + 1 # 数据库递增由selected_choice.votes表示的数据库字段
        selected_choice.save()
        
        
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def testjson(request):
    objs = serializers.serialize("json", Question.objects.all()) 

    # return JsonResponse(['zhangsan',25,'11111'], safe=False)

    return JsonResponse({
        'obj': objs
    })