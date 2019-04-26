from django.urls import path

from hr.views import DepartmentListView, EmployeeListView, EmployeeDetailView, DepartmentDetailView

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name="department_list"),
    path('departments/<int:id>', DepartmentDetailView.as_view(), name="department_detail"),
    path('employees/', EmployeeListView.as_view(), name="employee_list"),
    path('employees/<int:id>', EmployeeDetailView.as_view(), name="employee_detail"),
]
