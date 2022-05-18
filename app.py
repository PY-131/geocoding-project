import os
from dotenv import dotenv_values
from flask import Flask, jsonify, render_template, request
server = Flask(__name__)
from utils import get_coordinates

ENV = dotenv_values()  


"""
EXERCISE: 
Turn your program for the cesear cipher (exercise 3 from earlier)
into a little flask app that takes a string input, and returns the 
encrypted text to the user 
""" 


@server.route("/", methods=['GET', 'POST'])
def index():
    """
    main page with input fields
    """

    if request.method == "POST":

      results = {} 
      results['address'] = request.form["address"]

      lat, lon = get_coordinates(results['address'], ENV['URL'], ENV['PRIVATE_TOKEN'])
      results['lat'] = lat
      results['lon'] = lon

      return render_template("results.html", **results)
       
    return render_template("index.html")

if __name__ == '__main__':
    server.run(host=ENV['HOST'],port=ENV['PORT'], debug=True)