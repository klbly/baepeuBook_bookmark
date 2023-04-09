from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy 

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6
    # 기본값은 왜 "bookmark/bookmark_list.html" 이냐?
    # → venv/Lib/site-packages/django/views/generic/list.py 163행 template_name_suffix = '_list'
    
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'
    # template_name 기본값 = "bookmark/bookmark_form.html"
    # → venv/Lib/site-packages/django/views/generic/eidt.py 179행 template_name_suffix = '_form'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    # template_name 기본값 = "bookmark/bookmark_confirm_delete.html"
    # → venv/Lib/site-packages/django/views/generic/eidt.py 241행 template_name_suffix = '_confirm_delete'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    # template_name 기본값 = "bookmark/bookmark_form.html"
    # → venv/Lib/site-packages/django/views/generic/eidt.py 199행 template_name_suffix = '_form'
    
class BookmarkDetailView(DetailView):
    model = Bookmark
    # template_name 기본값 = "bookmark/bookmark_detail.html"
    # → venv/Lib/site-packages/django/views/generic/detail.py 113행 template_name_suffix = '_detail'