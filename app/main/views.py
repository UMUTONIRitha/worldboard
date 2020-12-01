from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Post, Country
from .. import db
from datetime import datetime
from .forms import PostForm
from ..requests import get_countries

@main.route('/')
def index():
    all_countries=get_countries()
    title="The World Board"
    return render_template('index.html', title = title, all_countries=all_countries)

@main.route('/country/<name>')
def posts(name):

    '''
    View movie page function that returns the movie details page and its data
    '''
    posts = Post.query.filter_by(country_name=name).order_by(Post.posted.desc()).all()
    title = f'{name}'
    print(name)

    return render_template('post.html',title = title,posts = posts)

@main.route('/post/new',methods = ['GET','POST'])
@login_required
def new_post():
    '''
    A function that saves the post added
    '''
    post_form = PostForm()

    if post_form.validate_on_submit():
        title = post_form.title.data
        body = post_form.content.data
        country_name = post_form.country_name.data
        title = post_form.title.data

        new_post = Post(post_title=title, post_content=body, country_name = country_name, user = current_user)
        new_post.save_post()

        return redirect(url_for('main.index'))


    title = 'New post | The World Board'
    return render_template('newpost.html', title = title, postform = post_form)