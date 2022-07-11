from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Object


class ListObjectView(ListView):
    model = Object
    template_name = 'index.html'
    context_object_name = "objects"




list_objects = ListObjectView.as_view()


class AddObject(CreateView):
    model = Object
    fields = "__all__"
    template_name = 'add.html'
    success_url = reverse_lazy('list')




add_object = AddObject.as_view()


class UpdateObject(UpdateView):
    model = Object
    fields = '__all__'
    template_name = 'add.html'
    success_url = reverse_lazy("list")




update_object = UpdateObject.as_view()


class DeleteObject(DeleteView):
    model = Object
    success_url = reverse_lazy("list")
    template_name = 'delete.html'




delete_object = DeleteObject.as_view()
