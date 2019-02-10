from flask import Flask, render_template, request, url_for,redirect, session
import pandas as pd
import os
from get_lyrics import get_lyrics
from process_lyrics import substitute_words

app = Flask(__name__)
app.secret_key = os.urandom(16)

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
    song_original_lyrics = get_lyrics(request.form["search-bar"])
    song_new_lyrics = substitute_words(request.form["search-bar"])
    return render_template('songs.html',
            old_lyrics=song_original_lyrics,
            new_lyrics=song_new_lyrics, 
            song_title=request.form["search-bar"])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





