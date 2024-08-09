from flask import Flask, render_template # type: ignore
from models import db
from config import Config
from controllers.area_controller import area_bp
from controllers.location_controller import location_bp
from controllers.person_controller import person_bp
from controllers.category_controller import category_bp
from controllers.field_controller import field_bp
from controllers.country_controller import country_bp
from controllers.district_controller import district_bp
from controllers.district_advisory_board_lay_controller import district_advisory_board_lay_bp
from controllers.district_advisory_board_ministerial_controller import district_advisory_board_ministerial_bp
from controllers.elders_deacons_controller import elders_deacons_bp
from controllers.local_controller import local_bp
from controllers.missionary_controller import missionary_bp
from controllers.missionaries_adicional_information_controller import missionaries_adicional_information_bp
from controllers.missionary_home_assignment_details_controller import missionary_home_assignment_details_bp
from controllers.region_controller import region_bp
from controllers.regional_advisory_council_controller import regional_advisory_council_bp
from controllers.regional_advisory_council_member_at_large_controller import regional_advisory_council_member_at_large_bp
from controllers.region_and_field_contact_information_controller import region_and_field_contact_information_bp
from controllers.schools_controller import schools_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Register blueprints
app.register_blueprint(area_bp, url_prefix='/api')
app.register_blueprint(location_bp, url_prefix='/api')
app.register_blueprint(person_bp, url_prefix='/api')
app.register_blueprint(category_bp, url_prefix='/api')
app.register_blueprint(field_bp, url_prefix='/api')
app.register_blueprint(country_bp, url_prefix='/api')
app.register_blueprint(district_bp, url_prefix='/api')
app.register_blueprint(district_advisory_board_lay_bp, url_prefix='/api')
app.register_blueprint(district_advisory_board_ministerial_bp, url_prefix='/api')
app.register_blueprint(elders_deacons_bp, url_prefix='/api')
app.register_blueprint(local_bp, url_prefix='/api')
app.register_blueprint(missionary_bp, url_prefix='/api')
app.register_blueprint(missionaries_adicional_information_bp, url_prefix='/api')
app.register_blueprint(missionary_home_assignment_details_bp, url_prefix='/api')
app.register_blueprint(region_bp, url_prefix='/api')
app.register_blueprint(regional_advisory_council_bp, url_prefix='/api')
app.register_blueprint(regional_advisory_council_member_at_large_bp, url_prefix='/api')
app.register_blueprint(region_and_field_contact_information_bp, url_prefix='/api')
app.register_blueprint(schools_bp, url_prefix='/api')

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/content/<page>')
def content(page):
    return render_template(f'{page}')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
