from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    # Here i replaced 'Post.query.all()' with 'Post.query.paginate(per_page)' to get only a specific no. of posts.
    # The 'per_page' arguement in above line is used to get that specific no. of posts i talked about in above comment.
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')