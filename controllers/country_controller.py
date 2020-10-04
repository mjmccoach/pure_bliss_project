from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries",__name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)


@countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    return render_template("countries/new.html")

@countries_blueprint.route("/countries", methods=["POST"])
def add_country():
    
    name = request.form["name"]
    continent = request.form["continent"]
    
    country = Country(name, continent)

    country_repository.save(country)
    return redirect ("/countries")