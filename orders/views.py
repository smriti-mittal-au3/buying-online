from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from billing.models import BillingProfile
from .models import Order

class OrderListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		return Order.objects.by_request(self.request)

class OrderDetailView(LoginRequiredMixin, DetailView):

	def get_queryset(self):
		return Order.objects.by_request(self.request)

	def get_object(self):
		qs=self.get_queryset().filter(order_id=self.kwargs.get('order_id'))
		if qs.count() ==1:
			return qs.first()
		raise Http404
