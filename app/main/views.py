from flask import render_template, request, redirect, url_for, abort
from ..models import User, Post, Country,Comment
from . import main
from flask_login import login_required, current_user
from .forms import UpdateProfile,PostForm,CommentForm
from .. import db,photos
from datetime import datetime
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
    commentForm=CommentForm()
    posts = Post.query.filter_by(country_name=name).order_by(Post.posted.desc()).all()
    title = f'{name}'
    print(name)

    return render_template('post.html',title = title,posts = posts,form=commentForm)

@main.route('/post/new/<country_name>',methods = ['GET','POST'])
@login_required
def new_post(country_name):
    '''
    A function that saves the post added
    '''
    post_form = PostForm()

    if post_form.validate_on_submit():
        title = post_form.title.data
        body = post_form.content.data
        
        title = post_form.title.data

        new_post = Post(post_title=title, post_content=body, country_name = country_name, user = current_user)
        new_post.save_post()

        return redirect(url_for('main.index'))


    title = 'New post | The World Board'

    return render_template('newpost.html', title = title, postform = post_form)

@main.route('/comment/<int:post_id>', methods = ['POST','GET'])
@login_required
def comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id, post_id = post_id)
        new_comment.save_comment()
        return redirect(url_for('.posts', name = post.country_name))
    return render_template('comment.html', form = form, post = post,all_comments = all_comments)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update_profile',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    form = UpdateProfile()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)

    
@main.route('/user/<uname>/update/profile',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))