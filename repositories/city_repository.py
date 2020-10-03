from db.run_sql import run_sql

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT into cities(name) VALUES (%s) RETURNING id"
    values = [city.name]
    results = run_sql(sql, values)
    city.id = results[0]['id']

    return city

def select_all():
    city_list = []
    
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        # country = country_repository.select(row["id"])
        city = City(["name"], [id], ['visited'])
        city_list.append(city)
    return city_list

def delete_all():
    
    sql = "DELETE FROM cities"
    results = run_sql(sql)

def delete(id):

    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)


def update(city):
    
    sql = "SET cities name = %s WHERE id = %s"
    values = [city.name, city.id]
    result = run_sql(sql, values)