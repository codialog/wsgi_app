import logging

from sql.countries_db import CountryDB
from sql.cities_db import CityDB
from sql.db import location
from sql.feedack_db import FeedbackDB
from sql.regions_db import RegionDB


def prepare_db():
    FeedbackDB().create_db_if_not_exists()
    CountryDB().prepare_country_db(location.countries)
    RegionDB().prepare_region_db(location.regions)
    CityDB().prepare_city_db(location.cities)
