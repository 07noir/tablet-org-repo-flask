from flask import Flask,redirect,render_template,request
import mysql.connector 


app = Flask(__name__, template_folder='template')
connection_string = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'db_org',
}

@app.route('/overview')
def overview():
    conn  = mysql.connector.connect(**connection_string)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT CONCAT(tbl_student_info.first_name, ' ', tbl_student_info.last_name) AS Name, tbl_student_info.student_info_id,
                    tbl_course.course_name FROM tbl_student_info,tbl_student_course,tbl_course WHERE tbl_student_info.student_info_id = 
                    tbl_student_course.student_info_id AND tbl_course.course_id = tbl_student_course.course_id;""")
        Student = cursor.fetchall()
        
        cursor.execute("SELECT tbl_org.org_name,tbl_org.status,tbl_org.org_abbv FROM tbl_org;")
        org = cursor.fetchall()
        
        cursor.execute("SELECT COUNT(*) FROM tbl_student_info")
        stud_total = cursor.fetchall()
        stud_count = stud_total[0][0]
        
        cursor.execute("SELECT COUNT(*) FROM tbl_org")
        total_orgs = cursor.fetchall()
        orgs_count = total_orgs[0][0]
        cursor.close()
        conn.commit()
        return render_template('overview.html', student = Student, organization = org, studCount = int(stud_count), orgs_count = int(orgs_count))
    
    else:
        return "There was an error"
    
@app.route('/organizations')
def org():
    conn  = mysql.connector.connect(**connection_string)
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tbl_org")
        org = cursor.fetchall()
        cursor.close()
        conn.commit()
        return render_template('organization.html', organization=org)
    else:
        return "error"
    
@app.route('/archieved')
def archieved():
    return render_template('archieved.html')



@app.route('/add_organization', methods=['POST','GET'])
def add_organization():
    conn  = mysql.connector.connect(**connection_string)
    if request.method == 'POST':
        org_name = request.form['organization']
        abbreviation = request.form['abbreviation']
        status = request.form['status']
        adviser = request.form['adviser']
        president = request.form['president']
        
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tbl_org(org_name, org_abbv, status, adviser, president) VALUES(%s, %s, %s, %s, %s)", (org_name, abbreviation, status, adviser, president))
            cursor.close()
            conn.commit()
            conn.close()
            return redirect('/organizations')
        except:
            return "Error"




@app.route('/org_delete/<int:id>')
def delete(id):
    try:
        
        conn = mysql.connector.connect(**connection_string)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_org WHERE org_id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect('/organizations')

    except:
        return "Error deleting organization"
        
    
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/statistic')
def stat():
    return render_template('statistic.html')

def exit_button():
    if request.method == 'POST':
        return redirect('/organizations') 
    else:
        return "Method not allowed", 405
    
    
    
    
    
    
#================================================================================================================================================================================================
#officer's end ui 


@app.route('/officer_dashboard')
def officers_db():
    return render_template('officer_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port= 81)