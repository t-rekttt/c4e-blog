from flask import Flask, render_template
from db import get_all_posts
import re
from jinja2 import evalcontextfilter, Markup, escape

app = Flask(__name__)

@app.route('/')
def index():
    posts = get_all_posts()
    return render_template("index.html", posts=posts)

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@app.template_filter()
@evalcontextfilter
def nl2br (eval_ctx, value):
    result = u'\n\n'.join(u'<span>%s</span>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


if __name__ == '__main__':
  app.run(debug=True)
