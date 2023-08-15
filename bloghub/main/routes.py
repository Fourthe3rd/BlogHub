from flask import render_template, request, Blueprint
from bloghub.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 3
    skip = (page - 1) * per_page
    posts = Post.objects().order_by('-date_posted').skip(skip).limit(per_page)
    total_posts = Post.objects().count()
    return render_template('home.html', posts=posts, total_posts=total_posts, per_page=per_page, page=page)

@main.route("/about")
def about():
    return render_template('about.html', title='About')