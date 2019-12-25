from datetime import timedelta
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from .models import User

ASSERT_ERRROR = 'The %s requires authentication middleware to be installed.'


class UpdateLastActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), ASSERT_ERRROR % self.__class__.__name__
        if request.user.is_authenticated and request.user.last_activity + timedelta(minutes=14) < timezone.now():
            User.objects.filter(id=request.user.id).update(last_activity=timezone.now())
