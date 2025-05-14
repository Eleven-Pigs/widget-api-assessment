from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Widget


class WidgetAPITestCase(APITestCase):
    def setUp(self):
        self.widget_data = {"name": "Test Widget", "number_of_parts": 5}
        self.widget = Widget.objects.create(**self.widget_data)

    def test_list_widgets(self):
        response = self.client.get(reverse("widget-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_get_single_widget(self):
        response = self.client.get(reverse("widget-detail", args=[self.widget.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.widget.name)

    def test_create_widget(self):
        new_widget = {"name": "New Gadget", "number_of_parts": 10}
        response = self.client.post(reverse("widget-list"), new_widget)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], new_widget["name"])

    def test_update_widget(self):
        update_data = {"name": "Updated Widget", "number_of_parts": 15}
        response = self.client.put(
            reverse("widget-detail", args=[self.widget.id]), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], update_data["name"])

    def test_delete_widget(self):
        response = self.client.delete(reverse("widget-detail", args=[self.widget.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Widget.objects.filter(id=self.widget.id).exists())
