from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core.exceptions import ValidationError
from script.models import CategoryGroup, Script
from django.urls import reverse

#Tests de Modelos
class CategoryGroupModelTest(TestCase):
    def CategoryGroupModelTest(self):
        group = CategoryGroup.objects.create(name='Baneos')
        self.assertEqual(str(group), "Baneos")


    def CategoryGroupCreationModelTest(self):
        group = CategoryGroup.objects.create(name='Baneos')
        self.assertEqual(group.name, "Baneos")


    def test_name_max_length(self):
        long_name = 'test' * 210
        group = CategoryGroup.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            group.full_clean()

#Tests de Vistas

class CategoryGroupViewTests(TestCase):
    def setUp(self):
        self.group = CategoryGroup.objects.create(name='Baneos')

    def test_category_group_list_view(self):
        response = self.client.get(reverse('script:category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.group, response.context['object_list'])

    def test_categorygroup_create_view_get(self):
        url = reverse("script:category_create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "script/category_form.html")

    def test_category_create_view_post(self):
        url = reverse("script:category_create")
        response = self.client.post(url, {
            "name": "Baneos",
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(CategoryGroup.objects.filter(name="Baneos").exists())
