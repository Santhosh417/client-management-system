from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from.models import models
from .models import Vehicle

from django.urls import reverse_lazy

class VehicleListView(LoginRequiredMixin,ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'

class VehicleDetailView(LoginRequiredMixin,DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'

class VehicleUpdateView(LoginRequiredMixin,UpdateView):
    model = Vehicle
    fields = ('year', 'make', 'car_model', 'vin_number', 'price')
    template_name = 'vehicle_edit.html'

class VehicleDeleteView(LoginRequiredMixin,DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleCreateView(LoginRequiredMixin,CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('year', 'make', 'car_model', 'vin_number', 'price')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
