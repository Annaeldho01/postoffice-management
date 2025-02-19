from flask import *
from database import *

public = Blueprint('public',__name__)


@public.route('/')
def public_homee():
	return render_template('public_home.html') 


@public.route('/login',methods=['get','post'])
def login():
	if 'submitbutton' in request.form:
		uname=request.form['uname']
		pwd=request.form['password']
		fg="select * from login where username='%s' and password='%s'"%(uname,pwd)
		ds=select(fg)
		if ds:
      
			session['login_id']=ds[0]['login_id']

			if ds[0]['usertype']=='user':
				kk="select * from user where login_id='%s'"%(session['login_id'])
				fv=select(kk)
				if fv:
					session['u_id']=fv[0]['user_id']
				flash('login success........!')
				return redirect(url_for('user.user_home'))

			elif ds[0]['usertype']=='branch_employee':
				flash("login success........!")
				return redirect(url_for('branch_employee.branchemployee_home'))

			elif ds[0]['usertype']=='admin':
				flash("login success........!")
				return redirect(url_for('admin.admin_homee'))

		else:
			flash("invalid username or password........!")
			return redirect(url_for('public.login'))      

	return render_template('login.html')