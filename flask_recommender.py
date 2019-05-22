import pandas as pd
from flask import request
import csv
import sqlite3
from flask import Flask, g
movie_data = pd.read_csv('movie_data.csv')

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/choose', methods=['POST'])
def choose():
    # Get the database connection
    import sqlite3
    conn = sqlite3.connect('movie.db')#建table
    c = conn.cursor()#創一個cursor物件

    model_name = request.form.get('model_name')
    movie_title = request.form.get('movie_title')
    try:
        movieid = movie_data[movie_data['title']==movie_title].iloc[0]['movieid']
    except:
        return '<p>There is no movie!</p>'
########################################combine##############################################
    if model_name == 'combine':
        try:
            cursor = c.execute('select movieout from movierecommenderlist where moviein =\'{}\''.format(movie_title))
            a = cursor.fetchall()
            b = list(map(lambda x :str(x).replace(',','').replace('(','').replace(')','').replace('\'',''),a))   
            c = str(b).replace(',','\n').replace('[','').replace(']','')
            return '<p>%s</p>'%(c)
        except:
            return '<p>%s</p>'%(movie_title)
#########################################als###########################################################    
    elif model_name == 'als':
        try:
            cursor = c.execute('SELECT * FROM movie_als WHERE movieid =\'{}\''.format(movieid))
            a = cursor.fetchall()
            b = []
            for i in a[0][1:]:
                i = movie_data[movie_data['movieid']==i].iloc[0]['title']
                b.append(i)
            return '<p>%s</p>'%(b)
        except:
            return '<p>%s</p>'%(movieid)
#########################################cosine#########################################################
    elif model_name == 'cosine':
        try:
            cursor = c.execute('SELECT * FROM movie_cosine WHERE movieid =\'{}\''.format(movieid))
            a = cursor.fetchall()
            b = []
            for i in a[0][1:]:
                i = movie_data[movie_data['movieid']==i].iloc[0]['title']
                b.append(i)
            return '<p>%s</p>'%(b)
        except:
            return '<p>%s</p>'%(movieid)
########################################bm25#########################################################
    elif model_name == 'bm25':
        try:
            cursor = c.execute('SELECT * FROM movie_bm25 WHERE movieid =\'{}\''.format(movieid))
            a = cursor.fetchall()
            b = []
            for i in a[0][1:]:
                i = movie_data[movie_data['movieid']==i].iloc[0]['title']
                b.append(i)
            return '<p>%s</p>'%(b)
        except:
            return '<p>%s</p>'%(movieid)
###########################################bpr#########################################################
    elif model_name == 'bpr':
        try:
            cursor = c.execute('SELECT * FROM movie_bpr WHERE movieid =\'{}\''.format(movieid))
            a = cursor.fetchall()
            b = []
            for i in a[0][1:]:
                i = movie_data[movie_data['movieid']==i].iloc[0]['title']
                b.append(i)
            return '<p>%s</p>'%(b)
        except:
            return '<p>%s</p>'%(movieid)
########################################TFIDF######################################################
    elif model_name == 'TFIDF':
        try:
            cursor = c.execute('SELECT * FROM movie_TFIDF WHERE movieid =\'{}\''.format(movieid))
            a = cursor.fetchall()
            b = []
            for i in a[0][1:]:
                i = movie_data[movie_data['movieid']==i].iloc[0]['title']
                b.append(i)
            return '<p>%s</p>'%(b)
        except:
            return '<p>%s</p>'%(movieid)
#########################################################################################################
if __name__ == '__main__':
    app.run()
