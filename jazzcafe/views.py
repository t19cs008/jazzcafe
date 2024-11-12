from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.db import transaction
from django.utils import timezone
from django.conf import settings  

from .forms import *
from .models import *

import csv
import pytz

# Create your views here.
class NewOrderView(generic.CreateView):
    template_name = "jazzcafe/new_order.html"
    form_class = NewOrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.register_datetime = timezone.now()
        instance.table_number = self.kwargs.get("table_number")
        instance.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("jazzcafe:done_new_order", args=[self.object.pk])

class DoneNewOrderView(generic.DeleteView):
    template_name = "jazzcafe/done_new_order.html"
    model = Order
    context_object_name = "order"

class StaffMainPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "jazzcafe/staff_main_page.html"

class AddDrinkView(LoginRequiredMixin, generic.CreateView):
    template_name = "jazzcafe/add_drink.html"
    form_class = AddDrinkForm
    success_url = reverse_lazy("jazzcafe:done_add_drink")

class DoneAddDrinkView(LoginRequiredMixin, generic.TemplateView):
    template_name = "jazzcafe/done_add_drink.html"

class ChangeDrinkStackStatusView(LoginRequiredMixin, generic.ListView):
    template_name = "jazzcafe/change_drink_stack_status.html"
    model = Drink
    context_object_name = "drinks"

class UpdateDrinkStackStatusView(LoginRequiredMixin, generic.UpdateView):
    def post(self, request: HttpRequest, *args: str, **kwargs: reverse_lazy) -> HttpResponse:
        selected_item_ids = request.POST.getlist('selected_items')
        Drink.objects.filter(id__in=selected_item_ids).update(is_out_of_order=True)
        Drink.objects.exclude(id__in=selected_item_ids).update(is_out_of_order=False)
        return redirect('jazzcafe:change_drink_stack_status')

class AddTreatView(LoginRequiredMixin, generic.CreateView):
    template_name = "jazzcafe/add_treat.html"
    form_class = AddTreatForm
    success_url = reverse_lazy("jazzcafe:done_add_treat")

class DoneAddTreatView(LoginRequiredMixin, generic.TemplateView):
    template_name = "jazzcafe/done_add_treat.html"

class ChangeTreatStackStatusView(LoginRequiredMixin, generic.ListView):
    template_name = "jazzcafe/change_treat_stack_status.html"
    model = Treat
    context_object_name = "treats"

class UpdateTreatStackStatusView(LoginRequiredMixin, generic.UpdateView):
    def post(self, request: HttpRequest, *args: str, **kwargs: reverse_lazy) -> HttpResponse:
        selected_item_ids = request.POST.getlist('selected_items')
        Treat.objects.filter(id__in=selected_item_ids).update(is_out_of_order=True)
        Treat.objects.exclude(id__in=selected_item_ids).update(is_out_of_order=False)
        return redirect('jazzcafe:change_treat_stack_status')

class ImcompleteOrderListView(LoginRequiredMixin, generic.ListView):
    template_name = "jazzcafe/imcomplete_order_list.html"
    model = Order
    context_object_name = "orders"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_served = False).order_by("register_datetime")
        return queryset

class UpdateOrderStatusView(LoginRequiredMixin, generic.UpdateView):
    success_url = "jazzcafe:imcomplete_order_list"

    def post(self, request: HttpRequest, *args: str, **kwargs: reverse_lazy) -> HttpResponse:
        selected_item_ids = request.POST.getlist('selected_items')
        Order.objects.filter(id__in=selected_item_ids).update(is_served=True)
        return redirect('jazzcafe:imcomplete_order_list')

class CompleteOrderListView(LoginRequiredMixin, generic.ListView):
    template_name = "jazzcafe/complete_order_list.html"
    model = Order
    context_object_name = "orders"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_served = True).order_by("register_datetime")
        return queryset

class OutputOrderListView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="order_list.csv"'

        writer = csv.writer(response)
        writer.writerow(["受付時間", "テーブル番号", "飲み物", "砂糖", "ミルク", "スイーツ"])

        jst = pytz.timezone(settings.TIME_ZONE)

        for order in Order.objects.all():
            jst_datetime = timezone.localtime(order.register_datetime, jst)
            writer.writerow([jst_datetime.strftime('%Y-%m-%d %H:%M:%S'), order.table_number, order.drink, order.is_suger, order.is_milk, order.treat])

        return response