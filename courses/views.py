from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Section, Material, Test, TestResult
from .serializers import SectionSerializer, MaterialSerializer, TestSerializer, TestResultSerializer


class IsAdminOrTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'teacher']


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin' or obj.created_by == request.user


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTeacher]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTeacher]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTeacher]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def submit_answer(self, request, pk=None):
        test = Test.objects.get(pk=pk)
        answer = request.data.get('answer')
        result = TestResult.objects.create(
            test=test,
            student=request.user,
            answer=answer,
            is_correct=(answer.lower() == test.correct_answer.lower())
        )
        serializer = TestResultSerializer(result)
        return Response(serializer.data)
