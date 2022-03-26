import json


def get_posts_all():
    with open("data/data.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data


def get_posts_by_user(user_name):
    posts_by_user = []
    posts_all = get_posts_all()
    for post in posts_all:
        if post['poster_name'] == user_name:
            posts_by_user.append(post)
    return posts_by_user


def get_comments_by_post_id(post_id):
    post_id = int(post_id)
    comments_by_post = []
    with open("data/comments.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        for comment in data:
            if comment['post_id'] == post_id:
                comments_by_post.append(comment)
    return comments_by_post


def search_for_posts(query):
    post_with_query = []
    posts_all = get_posts_all()
    for post in posts_all:
        if query.lower() in post['content'].lower():
            post_with_query.append(post)
    return post_with_query


def get_post_by_pk(pk):
    pk = int(pk)
    posts_all = get_posts_all()
    for post in posts_all:
        if post['pk'] == pk:
            return post
