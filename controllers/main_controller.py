from flask import Blueprint, render_template, request, redirect, url_for, flash

main_bp = Blueprint('main', __name__)

@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Adicione a lógica de signup aqui
        flash('Sign up successful!')
        return redirect(url_for('main.signup'))
    return render_template('signup.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Adicione a lógica de login aqui
        return redirect(url_for('dashboard'))
    return render_template('login.html')
