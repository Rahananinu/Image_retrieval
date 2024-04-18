from flask import*
from database import*

public=Blueprint('public',__name__)


@public.route('/')
def home():
    return render_template("index.html")



@public.route('/login',methods=['get','post'])
def login():
    if'sub'in request.form:
        username=request.form['uname']
        password=request.form['pass']
        
        qry="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(qry)
        
        if res:
            session['log']=res[0]['login_id']
        
            if res[0]['usertype']=='admin':
                return ("<script>alert('WELCOME ADMIN');window.location='/adminhome'</script>")
            
            if res[0]['usertype']=='station':
                qry1="select * from station where login_id='%s'"%(session['log'])
                res1=select(qry1)
                if res1:
                    session['station']=res1[0]['station_id']
                    return ("<script>alert('WELCOME STATION');window.location='/police_station_home'</script>")
            if res[0]['usertype']=='staff':
                qry1="select * from staff where login_id='%s'"%(session['log'])
                res1=select(qry1)
                if res1:
                    session['staff']=res1[0]['staff_id']
                    return ("<script>alert('WELCOME STAFF');window.location='/staffhome'</script>")
        else:
            return ("<script>alert('invalid username or password');window.location='/login'</script>")


         
    return render_template("login.html")




