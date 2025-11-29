from django.test import TestCase
from script.models import CategoryGroup, Script
from django.core.exceptions import ValidationError
from django.urls import reverse

class ScriptModelTests(TestCase):
    def setUp(self):
        self.CategoryGroup = CategoryGroup.objects.create(name='Baneos')

    def ScriptModelTest(self):
        group = CategoryGroup.objects.create(name='Baneos')
        script = Script.objects.create(group, name='Respuesta de baneo', content='Su cuenta ha sido baneada por hackear')
        self.assertEqual(str(script), "Respuesta de baneo Su cuenta ha sido baneada por hackear")


    def ScriptCategoryModelTest(self):
        group = CategoryGroup.objects.create(name='Baneos')
        script = Script.objects.create(group, name="prueba", content="Prueba")
        self.assertEqual(script.CategoryGroup, group)

    def test_name_max_length(self):
        long_content = 'test' * 1005
        script = Script(CategoryGroup=self.CategoryGroup, name="Test", content=long_content)

        with self.assertRaises(ValidationError):
            script.full_clean()

class ScriptModelViewTests(TestCase):
    def setUp(self):
        self.group = CategoryGroup.objects.create(name='Baneos')
        self.script = Script.objects.create(CategoryGroup=self.group, name="Prueba", content="ContenidoPrueba")

    def test_script_list_view(self):
        url = reverse('script:script_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.script, response.context['object_list'])

    def test_script_detail_view(self):
        url = reverse('script:script_detail', args=[self.script.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], self.script)

    def test_script_create_view(self):
        url = reverse('script:script_create')

        response = self.client.post(url,
        {
            "CategoryGroup" : self.group.pk,
            "name": "Nuevo script",
            "content": "ContenidoPrueba"
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Script.objects.filter(CategoryGroup=self.group, name="Nuevo script").exists())


