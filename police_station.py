from flask import *
from database import*

police_station=Blueprint('police_station',__name__)



@police_station.route('/police_station_home')
def police_station_home():
    return render_template("police_station_home.html")



@police_station.route('/police_view_staff')
def police_view_staff():
    data={}
    qry2="select * from staff inner join station using(station_id)"
    res=select(qry2)
    if res:
        data['view']=res
        
    return render_template("police_view_staff.html",data=data)


@police_station.route('/police_add_case',methods=['get','post'])
def police_add_case():
    data={}
    qry="select * from registered_cases"
    res=select(qry)
    if res:
        data['view']=res
    if'submit' in request.form:
        case_name=request.form['case_name']
        details=request.form['details']
        
        qry="insert into registered_cases values(null,'%s','%s','%s',curdate(),'pending')"%(session['station'],case_name,details)
        insert(qry)
        return ("<script>alert('CASE ADDED');window.location='/police_add_case'</script>")

    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']
        if action=='assign_case':
            qry3="select * from staff where station_id='%s'"%(session['station']) 
            res3=select(qry3)
            if res3:
                data['staff']=res3   
                
                if 'assign' in request.form:
                    
                    qr="select * from assigned_cases where case_id='%s'"%(id)
                    re=select(qr)
                    if re:
                        return ("<script>alert('ALREADY ASSIGNED');window.location='/police_add_case'</script>")

                    else:
                        staff=request.form['staff']
                        qry4="insert into assigned_cases values(null,'%s','%s',curdate(),'pending')"%(id,staff)
                        insert(qry4)
                        return ("<script>alert('CASE ASSIGNED');window.location='/police_add_case'</script>")

                        
      
    return render_template("police_add_case.html",data=data)




@police_station.route('/police_station_com',methods=['get','post'])
def police_station_com():
    data={}
    qry1="select * from complaints where sender_id=(select station_id from station where login_id='%s')"%(session['log'])
    res1=select(qry1)
    if res1:
        data['view']=res1
    if'submit' in request.form:
        title=request.form['title']
        description=request.form['description']
        qry="insert into complaints values(null,'%s','%s','%s','pending',curdate())"%(session['log'],title,description)
        insert(qry)
        return ("<script>alert('COMPLAINT SEND');window.location='/police_station_com'</script>")

    return render_template("police_complaint.html",data=data)


@police_station.route('/view_cases')
def view_cases():
    data={}
    qry="select * from registered_cases inner join assigned_cases using(case_id)"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("station_view_cases.html",data=data)



@police_station.route('/police_case_status')
def police_case_status():
    id=request.args['id']
    data={}
    qry="select * from case_status where assigned_id='%s'"%(id)
    res=select(qry)
    if res:
        data['view']=res
    return render_template("police_case_status.html",data=data)





