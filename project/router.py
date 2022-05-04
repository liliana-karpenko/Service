from rest_framework import routers
from users.api import CustomerViewSet

router = routers.DefaultRouter()
router.register('api/customer', CustomerViewSet, 'todo')

urlpatterns = router.urls