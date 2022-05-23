import os
from dotenv import dotenv_values
from flask import Flask, jsonify, render_template, request
server = Flask(__name__)
from utils import get_coordinates, get_iss_location, get_iss_people

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


@server.route("/iss_location")
def iss_location():
  res = get_iss_location(ENV['ISS_URL'])
  return jsonify(res)


@server.route("/iss_people")
def iss_people():
  res = get_iss_people(ENV['ISS_URL'])
  return jsonify(res)


@server.route("/iss_info")
def iss_info():

  people = get_iss_people(ENV['ISS_URL'])
  location = get_iss_location(ENV['ISS_URL'])

  people.update(location)
  return jsonify(people)


if __name__ == '__main__':
    server.run(host=ENV['HOST'],port=ENV['PORT'], debug=True)
