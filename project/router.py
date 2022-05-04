from rest_framework import routers
from users.api import CustomerViewSet, OrderViewSet, CarViewSet

router = routers.DefaultRouter()
router.register('customer', CustomerViewSet, 'api_customer')
router.register('car', CarViewSet, 'api_car')
router.register('order', OrderViewSet, 'api_order')

urlpatterns = router.urls