from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
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
        # context['total'] = total
        # print(otzivi)
        # for tot in
        return context

class ProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        total = 0
        ocenka = 0
        pk = self.kwargs.get('pk')
        product = Otziv.objects.all().filter(product_id=pk)
        for i in product:
            ocenka += i.ocenka
            total += 1
        obsh = ocenka / total
        print(obsh)
        context = super().get_context_data(**kwargs)
        context['otziv'] = Otziv.objects.all().filter(product_id=pk)
        context['obsh'] = int(obsh)
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = ('name', 'category', 'description', 'photo')
    permission_required = 'webapp.add_product'
    permission_denied_message = '403 Доступ запрещён!'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin,UpdateView):
    model = Product
    template_name = 'product/update.html'
    fields = ('name', 'category', 'description', 'photo')
    context_object_name = 'product'
    permission_required = 'webapp.change_product'
    permission_denied_message = '403 Доступ запрещён!'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    context_key = 'product'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'product'
    redirect_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'
    permission_denied_message = '403 Доступ запрещён!'


class OtzivCreateView(LoginRequiredMixin, CreateView):
    model = Otziv
    template_name = 'otziv/otziv_create.html'
    fields = ('description', 'ocenka')
    permission_required = 'webapp.add_otziv'
    permission_denied_message = '403 Доступ запрещён!'

    def form_valid(self, form):
        description = form.cleaned_data.pop('description')
        pk = self.kwargs.get('pk')
        print(pk, )
        user = self.request.user
        # product = Product.objects.all().filter(id=pk)
        product = get_object_or_404(Product.objects.all().filter(id=pk))
        # pk = self.object.pk
        Otziv.objects.create(user=user, product=product, description=description)
        return redirect('webapp:product_detail', pk)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['pk'] = pk
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class OtzivUpdateView(PermissionRequiredMixin, UpdateView):
    model = Otziv
    # context_object_name = 'otziv'
    template_name = 'otziv/otziv_update.html'
    fields = ('description', 'ocenka')
    context_object_name = 'otziv'
    permission_required = 'webapp.change_otziv'
    permission_denied_message = '403 Доступ запрещён!'

    def get_success_url(self):
        return reverse('webapp:index')

class OtzivDeleteView(PermissionRequiredMixin, DeleteView):
    model = Otziv
    template_name = 'otziv/otziv_delete.html'
    context_key = 'otziv'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'otziv'
    redirect_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_otziv'
    permission_denied_message = '403 Доступ запрещён!'