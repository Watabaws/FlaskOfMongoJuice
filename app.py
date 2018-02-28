from flask import Flask, render_template, request, redirect, flash, Markup, url_for, jsonify
import requests, os
import daytabays

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.args["title"]:
        movie = daytabays.get_title(request.args["title"])
    elif request.args["director"]:
        movie = daytabays.get_director(request.args["director"])
    elif request.args['year']:
        movie = daytabays.get_year(int(request.args['year']))
    elif request.args["genre"]:
        movie = daytabays.get_genre(request.args["genre"])
    else:
        return redirect(url_for("home"))
    return render_template("results.html", movie= movie)
    '''
    try:
        title = request.args['title']
        movie = daytabays.get_title(title)
        return render_template("results.html", movie)
    except:
            try:
                drector = request.args['director']
                movie = daytabays.get_director(drector)
                return render_template("results.html", movie)
            except:
                try:

                except:
                    try:
                        gen = request.args['genre']
                        movie = daytabays.get_genre(gen)
                        return render_template("results.html", movie)
                    except:
                        return render_template("error.html")
                        '''




if __name__ == "__main__":
    app.debug = True
    app.run()
