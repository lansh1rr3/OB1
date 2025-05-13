from django.db import models
from users.models import CustomUser


class Section(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.title


class Material(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Test(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='tests')
    question = models.TextField()
    correct_answer = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.test.question}"
