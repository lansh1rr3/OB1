from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from courses.views import SectionViewSet, MaterialViewSet, TestViewSet, TestResultViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Self-Learning Platform API",
        default_version='v1',
        description="API for self-learning platform",
    ),
    public=True,
)

router = DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'tests', TestViewSet)
router.register(r'test-results', TestResultViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
