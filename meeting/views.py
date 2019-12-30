from django.shortcuts import redirect
from django.views import generic
from .models import Album, Photo


class AlbumList(generic.ListView):
    model = Album


class PhotoList(generic.ListView):
    model = Photo

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        photo = self.model.objects.filter(album__date__day=day, album__date__month=month,
                                          album__date__year=year).first()
        return redirect('photo', pk=photo.id)


class PhotoDetail(generic.DetailView):
    model = Photo

    def get(self, request, *args, **kwargs):
        if request.GET.get('pk'):
            return redirect('photo', pk=request.GET['pk'])
        return super(PhotoDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PhotoDetail, self).get_context_data(**kwargs)
        item = context['object']

        context.update({
            'photo_list': item.album.photos.all(),
            'prev_photo': item.album.photos.filter(my_order__lt=item.my_order).order_by('-my_order').first(),
            'next_photo': item.album.photos.filter(my_order__gt=item.my_order).order_by('my_order').first(),
        })
        return context
