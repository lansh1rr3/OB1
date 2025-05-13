from rest_framework import serializers
from .models import Section, Material, Test, TestResult


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'description', 'created_by']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'section', 'title', 'content', 'created_by']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'material', 'question', 'correct_answer', 'created_by']


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ['id', 'test', 'student', 'answer', 'is_correct', 'submitted_at']
