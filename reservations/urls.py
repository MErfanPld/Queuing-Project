from django.urls import path
from .views import *

urlpatterns = [
    path('', AppointmentCreateView.as_view(), name='create_appointment'),
    path('update-appointment-status/', update_appointment_status, name='update_appointment_status'),
    # path('employee/<int:employee_id>/appointments/', EmployeeAppointmentListView.as_view(), name='employee_appointments'),
]
