
from flask import Blueprint

from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm, UserSearchForm)
from flaskblog.users.utils import save_picture, send_reset_email


users = Blueprint('users',__name__)


@users.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your Account has been Updated !!','success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':    
        form.username.data = current_user.username 
        form.email.data = current_user.email 

    image_file = url_for('static',filename='profile_pics/'+ current_user.image_file)
    return render_template('account.html',
                            title='Account', 
                            image_file=image_file, 
                            form=form)



@users.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Dear {form.username.data},Your Account has been Created!!','success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register Page', form=form)

@users.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            
            # if user access some page & not login then he will be redirected to login
            # after that he will be redirected to next page he wanted to access
            next_page = request.args.get('next')
            
            flash('Logged In','success')
            if next_page:
                return redirect(next_page) 
            else:
                return redirect(url_for('main.home'))
            #return redirect(url_for('main.home'))
        else:
            flash('Login Failed. Please check Email ID & Pass','danger')
    return render_template('login.html', title='Login Page',form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('users.login'))



@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page',1, type=int)

    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
                    .order_by(Post.date_posted.desc())\
                    .paginate(page=page, per_page=4)
    return render_template('user_post.html', posts=posts, user=user)


@users.route('/user/search', methods=['GET','POST'])
@login_required
def search_user():
    form = UserSearchForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            flash('User Not Found. Please check the username !!','danger')
            return redirect(url_for('users.search_user'))
 
        flash(f'Search results..','success')
        return redirect(url_for('users.user_posts',username=user.username))
    return render_template('search_user.html',form=form,title='Search User')


@users.route('/reset_password', methods=['GET','POST'])
def reset_request():
    # if the user is login he will be redirect to the Home Page
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been send to reset the password','info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route('/reset_password/<token>', methods=['GET','POST'])
def reset_token(token):
    # if the user is login he will be redirect to the Home Page
    # to make sure the user is LoggedOut
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Invalid Token or Expired Token','warning')
        return redirect(url_for('users.reset_request'))
    
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pass
        db.session.commit()
        flash(f'Your Paasword has been Reset!!','success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
