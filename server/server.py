from flask import Flask, render_template, request, url_for,redirect, session
import pandas as pd
import os


app = Flask(__name__)
app.secret_key = os.urandom(16)

def get_lyrics(song_title):
    pd.set_option('display.max_colwidth', -1)
    song_title = song_title.lower()
    file = pd.read_csv("/Users/shubhamsharan09/Downloads/songdata.csv") 
    return(file[file["song"].str.lower() == song_title]["text"])

@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        #session['lyrics'] = request.form['search-bar']
        if request.form['search-button'] == 'search':
            #session["lyrics"] = request.form["search-bar"]
            return redirect(url_for('songs'))
    else:
        return render_template('index.html')

@app.route('/songs', methods=['POST'])
def songs():
    #words = get_lyrics("billie jean")
    song_title = get_lyrics(request.form["search-bar"])
    return render_template('songs.html',lyrics=song_title)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





