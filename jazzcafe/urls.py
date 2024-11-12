from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "jazzcafe"

urlpatterns = [
    # お客様用
    path('new_order/<int:table_number>', views.NewOrderView.as_view(), name='new_order'),
    path('done_new_order/<int:pk>/', views.DoneNewOrderView.as_view(), name='done_new_order'),

    # スタッフ用
    path('staff_main_page/', views.StaffMainPageView.as_view(), name='staff_main_page'),

    path('imcomplete_order_list/', views.ImcompleteOrderListView.as_view(), name='imcomplete_order_list'),
    path('update_order_status/', views.UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('complete_order_list/', views.CompleteOrderListView.as_view(), name='complete_order_list'),
    path('output_order_list/', views.OutputOrderListView.as_view(), name='output_order_list'),

    path('add_drink/', views.AddDrinkView.as_view(), name='add_drink'),
    path('done_add_drink/', views.DoneAddDrinkView.as_view(), name='done_add_drink'),
    path('change_drink_stack_status/', views.ChangeDrinkStackStatusView.as_view(), name='change_drink_stack_status'),
    path('update_drink_stack_status/', views.UpdateDrinkStackStatusView.as_view(), name='update_drink_stack_status'),

    path('add_treat/', views.AddTreatView.as_view(), name='add_treat'),
    path('done_add_treat/', views.DoneAddTreatView.as_view(), name='done_add_treat'),
    path('change_treat_stack_status/', views.ChangeTreatStackStatusView.as_view(), name='change_treat_stack_status'),
    path('update_treat_stack_status/', views.UpdateTreatStackStatusView.as_view(), name='update_treat_stack_status'),
]
