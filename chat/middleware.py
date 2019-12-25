from django.utils.deprecation import MiddlewareMixin
from .models import Room

ASSERT_ERRROR = 'The %s requires authentication middleware to be installed.'


class RoomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        room = request.session.get('room', None)
        if room is None:
            request.room = Room.objects.first()
        elif room != request.room:
            try:
                request.room = Room.objects.get(slug=request.session.get('room'))
            except Room.DoesNotExist:
                pass
