from flask import Flask, render_template, request, url_for, redirect
from hymnal import hymn
from functions import InputSong
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    try:
        mysql = pymysql.connect(
            host="bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com",
            user="u28owjanx91fbbgg",
            passwd="Hib9YhOmKLh3xa3MMPMZ",
            db="bj7l3xtoftrlpschwtah",
            port=3306
        )

        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM visual_db")
        
        data = cursor.fetchall()
        main_list = data
    
    except pymysql.Error as e: 
        return f"<h1>{e}</h1>"
    
    finally:
        if mysql.open:
            mysql.close()

    return render_template('index.html', canciones=main_list)


@app.route('/selector')
def selector():
    try:
        mysql = pymysql.connect(
            host="bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com",
            user="u28owjanx91fbbgg",
            passwd="Hib9YhOmKLh3xa3MMPMZ",
            db="bj7l3xtoftrlpschwtah",
            port=3306
        )

        cursor = mysql.cursor()
        cursor.execute("select * from select_db")
        
        data = cursor.fetchall()
        main_list = data
    
    except pymysql.Error as e: 
        return f"<h1>{e}</h1>"
    
    finally:
        if mysql:
            mysql.close()

    return render_template('selector.html', myData=main_list)


@app.route('/search')
def search():
    return render_template('search.html')

# PROCESS --------------------------------------------------------------------------------------
@app.route('/add', methods=['GET','POST'])
def add_song():
    if request.method=='POST':
        song_name = request.form['songInput']

        mysql = pymysql.connect(
            host="bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com",
            user="u28owjanx91fbbgg",
            passwd="Hib9YhOmKLh3xa3MMPMZ",
            db="bj7l3xtoftrlpschwtah",
            port=3306
        )
        
        try:
            cursor = mysql.cursor()
            cursor.execute(f"INSERT INTO select_db VALUES (0, '{song_name}');")
            mysql.commit()

        except pymysql.Error as e: 
            return f"<h1>{e}</h1>"
    
        finally:
            if mysql:
                mysql.close()

        return redirect(url_for("selector"))


@app.route('/delete', methods=['GET','POST'])
def delete_song():
    if request.method=='POST':
        song_name = request.form['song-deleted']

        mysql = pymysql.connect(
            host="bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com",
            user="u28owjanx91fbbgg",
            passwd="Hib9YhOmKLh3xa3MMPMZ",
            db="bj7l3xtoftrlpschwtah",
            port=3306
        )
        
        try:
            cursor = mysql.cursor()
            cursor.execute(f"DELETE FROM select_db WHERE name='{song_name}'")
            mysql.commit()
        
        except pymysql.Error as e: 
            return f"<h1>{e}</h1>"
    
        finally:
            if mysql:
                mysql.close()
            
        return redirect(url_for("selector"))


@app.route('/update', methods=['GET','POST'])
def update_song():
    if request.method=='POST':
        song_indx = request.form['indx-change']
        song_name = request.form['songInput']

        mysql = pymysql.connect(
            host="bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com",
            user="u28owjanx91fbbgg",
            passwd="Hib9YhOmKLh3xa3MMPMZ",
            db="bj7l3xtoftrlpschwtah",
            port=3306
        )
        
        try:
            cursor = mysql.cursor()
            cursor.execute(f"UPDATE select_db SET name='{song_name}' WHERE songId={song_indx}")
            mysql.commit()
        
        except pymysql.Error as e: 
            return f"<h1>{e}</h1>"
    
        finally:
            if mysql:
                mysql.close()
            
        return redirect(url_for("selector"))


@app.route('/delete_all', methods=['GET','POST'])
def delete_table():
    if request.method=='POST':
        key_word = request.form['delete-response']

        if key_word == "si":
            mysql = pymysql.connect(
                host="bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com",
                user="u28owjanx91fbbgg",
                passwd="Hib9YhOmKLh3xa3MMPMZ",
                db="bj7l3xtoftrlpschwtah",
                port=3306
            )
            
            try:
                cursor = mysql.cursor()
                cursor.execute(f"TRUNCATE TABLE select_db")
                mysql.commit()
            
            except pymysql.Error as e: 
                return f"<h1>{e}</h1>"
        
            finally:
                if mysql:
                    mysql.close()
                
            return redirect(url_for("selector"))
        
        else:
            return redirect(url_for("selector"))


@app.route('/add_changes', methods=['GET','POST'])
def add_data():
    if request.method=='POST':
        data = request.form['save-changes']
        separate = data.split(',')
        
        mysql = pymysql.connect(
            host="bj7l3xtoftrlpschwtah-mysql.services.clever-cloud.com",
            user="u28owjanx91fbbgg",
            passwd="Hib9YhOmKLh3xa3MMPMZ",
            db="bj7l3xtoftrlpschwtah",
            port=3306
        )

        try:
            cursor = mysql.cursor()
            cursor.execute(f"TRUNCATE TABLE visual_db")
            mysql.commit()

            for x in separate:
                cursor.execute(f"INSERT INTO visual_db VALUES ('{x}')")
                mysql.commit()
        
        except pymysql.Error as e: 
            return f"<h1>{e}</h1>"
    
        finally:
            if mysql:
                mysql.close()
            
        return redirect(url_for("index"))
    
    else:
        return redirect(url_for("selector"))


# -----------------------------------------------------------------------------------------------
@app.route('/song', methods=['GET','POST'])
def songs():
    if request.method=='POST':
        song_name = request.form['songInput']
        
        sheet = hymn['song'][song_name]
        # main_image = hymn['song'][song_name]['chord_image']
            
        return render_template('song.html', ts=sheet) #, img=main_image)


@app.route('/tone', methods=['GET','POST'])
def change():
    if request.method=='POST':
        song_name = request.form['song_name_id']
        song_tone = request.form['song_tone_id']
        tone_selected = request.form['tones']

        sheet = hymn['song'][song_name.lower()]
        change_process = InputSong.inputs(song_name, tone_selected)

        num = len(change_process)

        message = [song_name, song_tone, tone_selected]
        set_new_tones = change_process[-1]
        
        for x, y in enumerate(set_new_tones):
            replace_symbol = str(y).replace("#","S")
            set_new_tones[x] = replace_symbol

        return render_template('change.html', msg=list(message), chp=change_process[:num-1],
                            ts=sheet, snt=set_new_tones)
    
    return "<h1>Seccion de cambio de tono...</h1>"


if __name__=='__main__':
    app.run(debug=True)