import json

from django.urls import reverse
from rest_framework.test import APITestCase

from hr.models import Department
from hr.serializers import DepartmentSerializer


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
