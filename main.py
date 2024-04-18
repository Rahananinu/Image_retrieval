from flask import*
from database import*
from public import public
from admin import admin
from police_station import police_station
from police_staff import police_staff

app=Flask(__name__,template_folder="templates")
app.secret_key="image"

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(police_station)
app.register_blueprint(police_staff)
app.run(debug=True,port=5007)