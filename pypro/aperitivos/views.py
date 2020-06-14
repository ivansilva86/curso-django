from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.vimeo_id = vimeo_id
        self.titulo = titulo
        self.slug = slug

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('Video_Aula_Vimeo', 'Video Aperitivo: Video_Aula_Vimeo', 428174309),
    Video('Video_2_Vimeo', 'Segundo Video Aula Python: Video_2_Vimeo', 428995779),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
