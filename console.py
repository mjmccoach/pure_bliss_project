import pdb

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.bucketlist_repository as bucketlist_repository

country_repository.delete_all()
city_repository.delete_all()

country1 = Country("Germany", "Europe")
country_repository.save(country1)

country2 = Country("South Korea", "Asia")
country_repository.save(country2)

country3 = Country("New Zealand", "Oceania")
country_repository.save(country3)

# country_repository.delete(1)
# country_repository.select_all()
# country_repository.select(1)

# country_repository.update(country1)
city1 = City("Busan", country2)
city_repository.save(city1)

city2 = City("Cologne", country1)
city_repository.save(city2)

city3 = City("Christchurch", country3)
city_repository.save(city3)

# city_repository.update(city1)

# city_repository.delete(0)
# city_repository.select_all()

pdb.set_trace()
