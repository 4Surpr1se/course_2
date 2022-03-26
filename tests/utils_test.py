import utils
import pytest
#  import sys


data_id_3 = [{
    "poster_name": "hank",
    "poster_avatar": "https://randus.org/avatars/m/383c7e7e3c3c1818.png",
    "pic": "https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
    "content": "Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.",
    "views_count": 187,
    "likes_count": 67,
    "pk": 3
  }]
comment_id_1 = [{
    "post_id": 1,
    "commenter_name": "hanna",
    "comment": "Очень здорово!",
    "pk": 1
  }]


def test_get_posts_all():
    info = utils.get_posts_all()
    assert info[2] == data_id_3[0], 'ошибка при передаче постов'


def test_get_posts_by_user():
    info = utils.get_posts_by_user('hank')
    assert info[0] == data_id_3[0], 'ошибка при поиске поста по имени '


def test_get_comments_by_post_id():
    info = utils.get_comments_by_post_id(1)
    assert info[0] == comment_id_1[0], 'ошибка при комментах'


def test_search_for_posts():
    info = utils.search_for_posts('ржавые')
    assert info == data_id_3, 'ошибка при поиске постов по значению'


def test_get_post_by_pk():
    info = utils.get_post_by_pk(3)
    assert info == data_id_3[0], 'ошибка при поиске по pk'
