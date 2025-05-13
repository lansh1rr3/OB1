from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from users.models import CustomUser
from .models import Section, Material, Test, TestResult


class CourseTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = CustomUser.objects.create_user(username='admin', password='admin123', role='admin')
        self.teacher = CustomUser.objects.create_user(username='teacher', password='teacher123', role='teacher')
        self.student = CustomUser.objects.create_user(username='student', password='student123', role='student')
        self.section = Section.objects.create(title='Test Section', created_by=self.teacher)
        self.material = Material.objects.create(section=self.section, title='Test Material', content='Content',
                                                created_by=self.teacher)
        self.test = Test.objects.create(material=self.material, question='What?', correct_answer='Answer',
                                        created_by=self.teacher)

    def test_create_section_as_teacher(self):
        self.client.login(username='teacher', password='teacher123')
        response = self.client.post('/api/sections/',
                                    {'title': 'New Section', 'description': 'Desc', 'created_by': self.teacher.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_submit_test_answer(self):
        self.client.login(username='student', password='student123')
        response = self.client.post(f'/api/tests/{self.test.id}/submit_answer/', {'answer': 'Answer'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(TestResult.objects.filter(student=self.student, is_correct=True).exists())
