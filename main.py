from flask import Flask, request, render_template, jsonify
import utils

app = Flask(__name__)


@app.route("/")  # Добавить поиск на главную, а не через url
def main_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/post/<int:postid>")
def post_by_id(postid):
    post = utils.get_post_by_pk(postid)
    comments = utils.get_comments_by_post_id(postid)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search/")
def post_search():
    s = request.args.get('s')
    posts = utils.search_for_posts(s)
    return render_template('search.html', posts=posts, s=s)


@app.route("/users/<username>")
def post_search_by_users(username):
    posts = utils.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


@app.route("/api/posts")
def json_post_giver():
    data = utils.get_posts_all()
    return jsonify(data)


@app.route("/api/posts/<post_id>")
def json_post_giver_by_id(post_id):
    data = utils.get_post_by_pk(post_id)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
