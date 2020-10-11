from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import TemplateView

from numpy.random import permutation
from gensim.models import word2vec
import pandas as pd
import json

# class IndexTemplateView(TemplateView):

#     def get_template_names(self):
#         template_name = 'index.html'
#         return template_name

#     def get_context_data(self, **kwargs):
#         context = super(IndexTemplateView, self).get_context_data(**kwargs)
#         titles = ["--", "\u5176\u4ed6\u707d\u60c5", "\u571f\u77f3\u707d\u60c5",
#                   "\u5ee3\u544a\u62db\u724c\u707d\u60c5",
#                   "\u5efa\u7269\u6bc0\u640d", "\u6a4b\u6881\u707d\u60c5", "\u6c34\u5229\u8a2d\u65bd\u707d\u60c5",
#                   "\u706b\u707d", "\u74b0\u5883\u6c59\u67d3", "\u7a4d\u6df9\u6c34\u707d\u60c5",
#                   "\u8def\u6a39\u707d\u60c5",
#                   "\u8eca\u8f1b\u3001\u4ea4\u901a\u4e8b\u6545", "\u9053\u8def\u3001\u96a7\u9053\u707d\u60c5",
#                   "\u9435\u8def\u3001\u9ad8\u9435\u6377\u904b\u707d\u60c5"]
#         subtitles = ["--", "\u9053\u8def\u7a4d\u6df9\u6c34", "\u8def\u6a39\u5012\u584c", "\u8def\u57fa\u6d41\u5931",
#                      "\u5ee3\u544a\u62db\u724c\u6389\u843d", "\u6a4b\u6881\u65b7\u88c2", "\u5176\u4ed6",
#                      "\u5830\u585e\u6e56",
#                      "\u6cb3\u5ddd\u6c34\u4f4d\u9054\u8b66\u6212\u6c34\u4f4d\u53ca\u5c01\u9589\u6a4b\u6881",
#                      "\u8def\u6a39\u50be\u659c", "\u5730\u5340\u7a4d\u6df9\u6c34",
#                      "\u5ee3\u544a\u62db\u724c\u6b32\u589c",
#                      "\u571f\u77f3\u6d41\u963b\u65b7", "\u623f\u5c4b\u7a4d\u6df9\u6c34",
#                      "\u5730\u4e0b\u9053\u6df9\u6c34",
#                      "\u9053\u8def\u843d\u77f3", "\u6a4b\u58a9\u57fa\u790e\u6c96\u5237",
#                      "\u6551\u8b77\u9001\u91ab\u6848\u4ef6",
#                      "\u8acb\u6c42\uff08\u5354\u52a9\uff09\u758f\u6563\u64a4\u96e2", "\u571f\u77f3\u5d29\u843d",
#                      "\u571f\u77f3\u6d41", "\u6f01\u8239(\u7b4f)\u6bc0\u640d", "\u5824\u9632\u6bc0\u640d",
#                      "\u6eaa\u6c34\u66b4\u6f32", "\u8eca\u798d", "\u74b0\u5883\u6c59\u67d3", "\u908a\u5761\u574d\u65b9",
#                      "\u5de5\u5340\u53ca\u5468\u908a\u5340\u57df\u640d\u58de", "\u5efa\u7269\u8f15\u5fae\u53d7\u640d",
#                      "\u516c\u5171\u5834\u6240", "\u6c34\u9598\u9580\u6545\u969c", "\u9053\u8def\u4e2d\u65b7",
#                      "\u5efa\u7bc9\u7269"]
#         departments = ['災情查報', '網路災情通報', '119消防署派遣系統']
#         context['titles'] = titles
#         context['subtitles'] = subtitles
#         context['departments'] = departments
#         return context
        
# Create your views here.
def home(request):
    data = {"a": [3,5,6]}
    return render(request, "DupDetector/home.html")
    # return JsonResponse(data, safe=False)


def about(request):
    # data = {"a": [3,5,6]}
    return render(request, 'DupDetector/about.html')