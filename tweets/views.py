from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import TweetModelForm
from .models import Tweet

class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()


class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/tweet/create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)



# Create your views here.
# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         'object': obj
#     }
#     return render(request, "tweets/detail_view.html", context)
#
#
# def tweet_list_view(request, id=1):
#     query_set = Tweet.objects.all()
#     print(query_set)
#
#     context = {
#         'object_list': query_set
#     }
#     return render(request, "tweets/list_view.html", context)