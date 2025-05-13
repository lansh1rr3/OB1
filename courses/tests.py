from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from users.models import CustomUser
from courses.models import Section, Material, Test, TestResult


class CourseTests(APITestCase):
    def setUp(self):
        self.teacher = CustomUser.objects.create_user(
            username='teacher', password='testpass', role='teacher'
        )
        self.student = CustomUser.objects.create_user(
            username='student', password='testpass', role='student'
        )
        self.token = AccessToken.for_user(self.teacher)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.section = Section.objects.create(title="Test Section", description="Description", created_by=self.teacher)
        self.material = Material.objects.create(title="Test Material", section=self.section, created_by=self.teacher)
        self.test = Test.objects.create(title="Test", section=self.section, created_by=self.teacher)

    def test_create_section_as_teacher(self):
        url = reverse('section-list')
        data = {'title': 'New Section', 'description': 'Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_submit_test_answer(self):
        url = reverse('testresult-list')
        data = {'test': self.test.id, 'student': self.student.id, 'answer': 'Answer', 'score': 0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
