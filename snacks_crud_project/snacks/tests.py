from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.test import Client
from django.contrib.auth import get_user_model


class SnackTest(TestCase):
    def tests_home_page_status(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_view(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test", email="test@test.com", password="123"
        )
        self.Snack = Snack.objects.create(
            title="test", purchaser=self.user, description="test"
        )

    def test_Update(self):
        url = reverse("snack_update", kwargs={"pk": self.Snack.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_Update_view(self):
        url = reverse("snack_update", kwargs={"pk": self.Snack.pk})
        response = self.client.post(url)
        self.assertTemplateUsed(response, "snack_update.html")

    def test_delete_status(self):
        url = reverse("snack_delete", kwargs={"pk": self.Snack.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):
        url = reverse("snack_delete", kwargs={"pk": self.Snack.pk})
        response = self.client.post(url)
        url2 = reverse("snack_list")
        self.assertRedirects(response, url2)
        self.assertEqual(response.status_code, 302)

    def test_str(self):
        self.assertEqual(str(self.Snack), "test")

    def test_snack_detail_status(self):
        url = reverse("snack_detail", kwargs={"pk": self.Snack.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_view(self):
        url = reverse("snack_detail", kwargs={"pk": self.Snack.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_create_status(self):
        url = reverse("snack_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
