from flask import *
from database import*

admin=Blueprint('admin',__name__)



@admin.route('/adminhome')
def adminhome():
    return render_template("admin_home.html")



@admin.route('/manage_division',methods=['get','post'])
def manage_division():
    data={}
    qry1="select * from division"
    res1=select(qry1)
    if res1:
        data['view']=res1
    if'submit' in request.form:
        div=request.form['div']
        qry="insert into division values(null,'%s')"%(div)
        insert(qry)
        return ("<script>alert('ADDED SUCCESSFULLY');window.location='/manage_division'</script>")
    if'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='update':
            qry3="select * from division where division_id='%s'"%(id)
            res3=select(qry3)
            if res3:
                data['up']=res3
                
                if 'update' in request.form:
                    div=request.form['div']
                    qry4="update division set division_name='%s' where division_id='%s'"%(div,id)
                    update(qry4)
                    return ("<script>alert('updated SUCCESSFULLY');window.location='/manage_division'</script>")
                
                
        if action=='delete':
            qry5="delete from division  where division_id='%s'"%(id)
            delete(qry5)
            return ("<script>alert('DELETED SUCCESSFULLY');window.location='/manage_division'</script>")

            

    return render_template("admin_manage_division.html",data=data)


@admin.route('/manage_station',methods=['get','post'])
def manage_station():
    data={}
    qry3="select * from division"
    res3=select(qry3)
    if res3:
        data['view']=res3
    qry4="select * from station"
    res4=select(qry4)
    if res4:
        data['station']=res4
    if'submit' in request.form:
        div_id=request.form['div_id']
        name=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        
        qry="insert into login values(null,'%s','%s','station')"%(username,password)
        res=insert(qry)
        
        qry1="insert into station values(null,'%s','%s','%s','%s','%s','%s')"%(res,div_id,name,place,phone,email)
        insert(qry1)
        return ("<script>alert('REGSITERED SUCCESSFULLY');window.location='/manage_station'</script>")

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='update':
            qry3="select * from station where station_id='%s'"%(id)
            res3=select(qry3)
            if res3:
                data['up']=res3
                
                if 'update' in request.form:
                    name=request.form['name']
                    place=request.form['place']
                    phone=request.form['phone']
                    email=request.form['email']
                    qry4="update station set station_name='%s',place='%s',phone='%s',email='%s' where station_id='%s'"%(name,place,phone,email,id)
                    update(qry4)
                    return ("<script>alert('updated SUCCESSFULLY');window.location='/manage_station'</script>")
                
                
        if action=='delete':
            qry5="delete from station where station_id='%s'"%(id)
            delete(qry5)
            return ("<script>alert('DELETED SUCCESSFULLY');window.location='/manage_station'</script>")

            
        
    return render_template("admin_manage_station.html",data=data)




@admin.route('/manage_staff',methods=['get','post'])
def manage_staff():
    data={}
    qry="select * from staff inner join station using(station_id)"
    data['view']=select(qry)

    qry4="select * from station"
    res4=select(qry4)
    if res4:
        data['station']=res4
    if'submit' in request.form:
        station=request.form['station']
        name=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        desig=request.form['desig']
        username=request.form['uname']
        password=request.form['pass']
        
        qry="insert into login values(null,'%s','%s','staff')"%(username,password)
        res=insert(qry)
        
        qry1="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,station,name,place,phone,email,desig)
        insert(qry1)
        return ("<script>alert('REGSITERED SUCCESSFULLY');window.location='/manage_staff'</script>")

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        
        if action=='update':
            qry3="select * from staff where staff_id='%s'"%(id)
            res3=select(qry3)
            if res3:
                data['up']=res3
                
                if 'update' in request.form:
                    station=request.form['station']
                    name=request.form['name']
                    place=request.form['place']
                    phone=request.form['phone']
                    email=request.form['email']
                    desig=request.form['desig']
                    qry4="update staff set staff_name='%s',place='%s',phone='%s',email='%s',designation='%s' where station_id='%s'"%(name,place,phone,email,desig,id)
                    update(qry4)
                    return ("<script>alert('updated SUCCESSFULLY');window.location='/manage_staff'</script>")
                
                
        if action=='delete':
            qry5="delete from staff where staff_id='%s'"%(id)
            delete(qry5)
            return ("<script>alert('DELETED SUCCESSFULLY');window.location='/manage_staff'</script>")

            
        
    return render_template("admin_manage_staff.html",data=data)



@admin.route('/admin_view_complaint',methods=['get','post'])
def admin_view_complaint():
    data={}
    qry="select * from complaints"
    data['view']=select(qry)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='reply':
        qry1="select * from complaints where complaint_id='%s'"%(id)
        data['reply']=select(qry1)
    if 'submit' in request.form:
        reply=request.form['reply']
        
        qry2="update complaints set reply='%s' where complaint_id='%s'"%(reply,id)
        update(qry2)
        return ("<script>alert('REPLY SENT');window.location='/admin_view_complaint'</script>")

    return render_template("admin_view_complaint.html",data=data)


@admin.route("/admin_view_regcase")
def admin_view_regcase():
    data={}
    qry="select * from registered_cases inner join station using(station_id)"
    data['view']=select(qry)
    return render_template("admin_view_regcase.html",data=data)