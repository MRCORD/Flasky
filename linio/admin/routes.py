from flask import render_template, session, request, redirect, url_for, flash
from linio import app, db, bcrypt
from .models import Usuario
from .forms import RegistrationForm, LoginForm
import os 

@app.route('/')
def home():
    return render_template('admin/index.html', title = 'Inicio')

@app.route('/registro', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        usuario = Usuario(nombre=form.nombre.data, username=form.username.data, email =form.email.data,
                            password =hash_password, telefono=form.telefono.data, distrito=form.distrito.data, 
                            direccion=form.direccion.data, tarjeta=form.tarjeta.data)
        db.session.add(usuario)
        db.session.commit()
        flash(f' Bienvenido {form.nombre.data} Gracias por registrarte', 'aprobado')
        return redirect(url_for('home')) 
    return render_template('admin/registro.html', form=form, title = 'Pagina registro')
    
@app.route('/inicio-sesion', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Bienvenido {form.email.data} Iniciaste sesion', 'exito')
            return redirect(request.args.get('next') or url_for('home'))
        else: 
            flash('Email o contraseña erroneo', 'error')

    return render_template('admin/inicio-sesion.html', form=form, title= 'Pagina inicio sesion')