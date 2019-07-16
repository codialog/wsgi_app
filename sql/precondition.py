import logging
import os

from sql.countries_db import CountryDB
from sql.cities_db import CityDB
from sql.db import location
from sql.feedack_db import FeedbackDB
from sql.regions_db import RegionDB


def prepare_feedback_db():
    try:
        feedback_db = FeedbackDB()
        if not os.path.isfile(feedback_db.db_path):
            feedback_db.create_db_if_not_exists()
    except:
        logging.debug('Fail in prepare "feedback" DB')


def prepare_country_db():
    try:
        country_bd = CountryDB()
        if not os.path.isfile(country_bd.db_path):
            country_bd.create_db_if_not_exists()
            country_bd.fill_country_table(location.countries)
    except:
        logging.debug('Fail in prepare "country" DB')


def prepare_region_db():
    try:
        region_db = RegionDB()
        if not os.path.isfile(region_db.db_path):
            region_db.create_db_if_not_exists()
            region_db.fill_region_table(location.regions)
    except:
        logging.debug('Fail in prepare "region" DB')


def prepare_city_db():
    try:
        city_db = CityDB()
        if not os.path.isfile(city_db.db_path):
            city_db.create_db_if_not_exists()
            city_db.fill_city_table(location.cities)
    except:
        logging.debug('Fail in prepare "city" DB')


def prepare_db():
    prepare_feedback_db()
    prepare_country_db()
    prepare_region_db()
    prepare_city_db()