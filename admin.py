from flask import *
from database import *

admin=Blueprint('admin',__name__)


@admin.route('/admin_home')
def admin_homee():
	return render_template('sub_officer_home.html')