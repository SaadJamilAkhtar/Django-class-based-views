from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Object


class ListObjectView(ListView):
    model = Object
    template_name = 'index.html'
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "All Item"
        return data

    def get_queryset(self):
        return super().get_queryset().order_by("-id")


list_objects = ListObjectView.as_view()


class AddObject(CreateView):
    model = Object
    fields = "__all__"
    template_name = 'add.html'
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Add Item"
        data["heading"] = "Add Item"
        data["button"] = "Add +"
        return data


add_object = AddObject.as_view()


class UpdateObject(UpdateView):
    model = Object
    fields = '__all__'
    template_name = 'add.html'
    success_url = reverse_lazy("list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Update Item"
        data["heading"] = "Update Item"
        data["button"] = "Update"
        return data


update_object = UpdateObject.as_view()


class DeleteObject(DeleteView):
    model = Object
    success_url = reverse_lazy("list")
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Delete Item"
        data["heading"] = "Delete Item"
        return data


delete_object = DeleteObject.as_view()
