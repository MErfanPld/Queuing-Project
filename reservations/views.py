import json
from django.http import JsonResponse
from django.views import View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from acl.mixins import PermissionMixin
from business.models import Service
from .models import Appointment, Schedule
from payments.models import Wallet, Transaction, UserWithdrawalRequests
from .forms import AppointmentForm, UpdateAppointmentStatusForm
from decimal import Decimal
from business.models import Employee


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'reservations/reservation.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'pending'
        response = super().form_valid(form)

        # ایجاد تراکنش و افزودن مبلغ به کیف پول کاربر
        wallet, created = Wallet.objects.get_or_create(user=self.request.user)
        service = form.instance.service
        Transaction.objects.create(
            wallet=wallet, amount=service.price, appointment=form.instance)
        wallet.balance += Decimal(service.price)
        wallet.save()

        # ایجاد درخواست برداشت برای ادمین
        UserWithdrawalRequests.objects.create(
            user=self.request.user, appointment=form.instance)

        # هدایت به صفحه پرداخت
        return redirect(reverse('payment', kwargs={'appointment_id': form.instance.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()  # نمایش لیست خدمات برای انتخاب
        return context


@require_POST
def update_appointment_status(request):
    appointment_id = request.POST.get('appointment_id')
    status = request.POST.get('status')
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = status
        appointment.save()
        return JsonResponse({'success': True, 'message': 'وضعیت به‌روزرسانی شد.'})
    except Appointment.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'رزرو یافت نشد.'})

# class EmployeeAppointmentListView(ListView):
#     model = Appointment
#     template_name = 'reservations/reservation_list.html'
#     context_object_name = 'appointments'

#     def get_queryset(self):
#         employee_id = self.kwargs.get('employee_id')
#         employee = get_object_or_404(Employee, id=employee_id)
#         return Appointment.objects.filter(employee=employee)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['employee'] = get_object_or_404(Employee, id=self.kwargs.get('employee_id'))
#         return context
