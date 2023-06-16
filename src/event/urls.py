from rest_framework import routers
from event.views import (EvenViewSet, BookingViewSet)

router = routers.SimpleRouter()
router.register(r'event', EvenViewSet, basename='event')
router.register(r'booking', BookingViewSet, basename='event')

urlpatterns = router.urls