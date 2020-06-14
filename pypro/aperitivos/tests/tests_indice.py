import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'slug',
    [
        'Video Aperitivo: Video_Aula_Vimeo',
        'Segundo Video Aula Python: Video_2_Vimeo',
    ]
)
def test_titulo_video(resp, slug):
    assert_contains(resp, slug)


@pytest.mark.parametrize(
    'slug',
    [
        'Video_Aula_Vimeo',
        'Video_2_Vimeo',
    ]
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
