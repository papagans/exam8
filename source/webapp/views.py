from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product, Otziv
from django.shortcuts import reverse, redirect, get_object_or_404

class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)

        return context

class ProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'



class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = ('name', 'category', 'description', 'photo')
    # permission_required = 'webapp.add_product', 'webapp.can_have_piece_of_pizza'
    # permission_denied_message = '403 Доступ запрещён!'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    fields = ('name', 'category', 'description', 'photo')
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    context_key = 'product'
    success_url = reverse_lazy('index')
    context_object_name = 'product'
    redirect_url = reverse_lazy('project_index')

    # def delete(self, request, *args, **kwargs):
    #     product = self.object = self.get_object()
    #     product.in_order = False
    #     product.save()
    #     return HttpResponseRedirect(self.get_success_url())

# Create your views here.
