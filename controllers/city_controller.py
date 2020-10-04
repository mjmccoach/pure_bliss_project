from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities",__name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

@cities_blueprint.route("/cities/new", methods=["GET"])
def new_city():
    countries = country_repository.select_all()
    return render_template("/cities/new.html", all_countries = countries)

@cities_blueprint.route("/cities", methods=["POST"])
def add_city():
    name = request.form['name']
    country_id = request.form["country_id"]
    visited = request.form["visited"]

    country = country_repository.select(country_id)
    city = City(name, country, visited)
    
    city_repository.save(city)
    
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect ("/cities")