from rest_framework.routers import SimpleRouter

from habits.views import HabitViewSet

app_name = "habits"

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = [] + router.urls
