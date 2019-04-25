from django.urls import path

from hr.views import DepartmentListView, EmployeeListView, EmployeeDetailView, DepartmentDetailView

urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('departments/<int:id>', DepartmentDetailView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('employees/<int:id>', EmployeeDetailView.as_view()),
]
