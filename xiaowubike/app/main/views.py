from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    后台管理系统
    """
    return render_template('index.html')
