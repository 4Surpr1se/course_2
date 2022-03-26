import pytest

from main import app


def test_posts_api():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list, "Тип данных неверен"
    assert list(response.json[0].keys()) == ['content', 'likes_count', 'pic', 'pk',
                                             'poster_avatar', 'poster_name', 'views_count'], "неверные ключи"


def test_posts_api_by_id():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict, "Тип данных неверен"
    assert list(response.json.keys()) == ['content', 'likes_count', 'pic', 'pk',
                                          'poster_avatar', 'poster_name', 'views_count'], "неверные ключи"
