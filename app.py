from flask import Flask, render_template
from flask_restful import Resource, Api
from db import get_all_posts, find_post_by_id, delete_post
import re
from jinja2 import evalcontextfilter, Markup, escape

from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a9SQqcH7tD8Gms4WqnX9G2ZEJQDNWuWd'

login_manager = LoginManager()
login_manager.init_app(app)

api = Api(app)

class PostRes(Resource):
  def delete(self, post_id):
    post = find_post_by_id(post_id)
    if post is None:
      return {
        'success': 0,
        'message': 'Post not found',
      }
    else:
      delete_post(post_id)
      return {
        'success': 1,
        'message': 'Post was deleted',
      }

@app.route('/')
def index():
    posts = get_all_posts()
    return render_template("index.html", posts=posts)

@app.route('/admin')
@login_required
def admin():
  posts = get_all_posts()
  return render_template('admin.html', posts=posts)

@app.route('/login')
def login():
  return render_template('login.html')

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@app.template_filter()
@evalcontextfilter
def nl2br (eval_ctx, value):
    result = u'\n\n'.join(u'<span>%s</span>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result

api.add_resource(PostRes, '/posts/<post_id>')

if __name__ == '__main__':
  app.run(debug=True)
