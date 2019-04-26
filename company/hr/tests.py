import json

from django.urls import reverse
from rest_framework.test import APITestCase

from hr.models import Department, Employee
from hr.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListViewTestCase(APITestCase):
    url = reverse("department_list")

    def test_create_department(self):
        response = self.client.post(self.url, {"name": "IT"})
        self.assertEqual(201, response.status_code)

    def test_list_departments(self):
        Department.objects.create(name="Marketing")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Department.objects.count())


class DepartmentDetailViewTestCase(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="IT")
        self.url = reverse("department_detail", kwargs={'id': self.department.id})

    def test_retrieve_department(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        department_serializer_data = DepartmentSerializer(instance=self.department).data
        response_data = json.loads(response.content)
        self.assertEqual(department_serializer_data, response_data)

    def test_update_department(self):
        response = self.client.put(self.url, {"name": "Marketing"})
        response_data = json.loads(response.content)
        department = Department.objects.get(id=self.department.id)
        self.assertEqual(response_data.get("name"), department.name)

    def test_delete_department(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)


class EmployeeListViewTestCase(APITestCase):

    def setUp(self):
        self.url = reverse("employee_list")
        self.department = Department.objects.create(name="IT")

    def test_create_employee(self):
        response = self.client.post(self.url, {"name": "Jose", "email": "jose@company.com", "department": 1})
        self.assertEqual(201, response.status_code)

    def test_list_employees(self):
        Employee.objects.create(name="Jose", email="jose@company.com", department_id=1)
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Employee.objects.count())


class EmployeeDetailViewTestCase(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="IT")
        self.employee = Employee.objects.create(name="Jose", email="jose@company.com", department_id=1)
        self.url = reverse("employee_detail", kwargs={'id': self.employee.id})

    def test_retrieve_employee(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        employee_serializer_data = EmployeeSerializer(instance=self.employee).data
        response_data = json.loads(response.content)
        self.assertEqual(employee_serializer_data, response_data)

    def test_patch_employee(self):
        response = self.client.patch(self.url, {"name": "Jose Escobar"})
        response_data = json.loads(response.content)
        employee = Employee.objects.get(id=self.employee.id)
        self.assertEqual(response_data.get("name"), employee.name)

    def test_update_employee(self):
        response = self.client.patch(self.url, {"name": "Jose Escobar", "email": "jose.escobar@company.com", "department": 1})
        response_data = json.loads(response.content)
        employee = Employee.objects.get(id=self.employee.id)
        self.assertEqual(response_data.get("name"), employee.name)
        self.assertEqual(response_data.get("email"), employee.email)
        self.assertEqual(response_data.get("department"), employee.department_id)

    def test_delete_employee(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
