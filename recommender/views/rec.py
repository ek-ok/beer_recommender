#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Defines the recommend view
"""

from flask import Blueprint, render_template, request
from recommender import db

rec = Blueprint('rec', __name__, template_folder='/../templates')

@rec.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        query = """
        SELECT
            beer_id,
            beer_name
        FROM rec.beer;
        """
        beers = db.fetch_data(query)

        return render_template('rec_input.html', active_page='recommend', beers=beers)

    elif request.method == 'POST':
        input_beers = request.form['beers']
        if input_beers:
            query = """
            WITH org AS (
                SELECT beer_id1, beer_id2, distance
                FROM rec.distance
                WHERE beer_id1 IN (%s)
            ),
            rec AS (
                SELECT
                    beer_id2,
                    SUM(distance) AS total_dist
                FROM org
                GROUP BY beer_id2
            ),
            rec10 AS (
                SELECT
                    ROW_NUMBER() OVER(ORDER BY total_dist DESC) rn,
                    beer_id2,
                total_dist
            FROM rec
            )

            SELECT
                rn,
                total_dist AS similarity,
                beer_id,
                beer_name,
                brewer_name,
                country_name,
                style_name,
                seasonal,
                weighted_avg,
                abv,
                est_calories
            FROM rec.beer
            INNER JOIN rec10
                ON rec.beer.beer_id = rec10.beer_id2
            WHERE rn <= 10
            ORDER BY rn;
            """ % input_beers

            output_beers = []
            for beer in db.fetch_data(query):
                tmp_dict = {}
                tmp_dict['rank'] = beer[0]
                tmp_dict['similarity'] = beer[1]
                tmp_dict['beer_id'] = beer[2]
                tmp_dict['beer_name'] = beer[3]
                tmp_dict['brewer_name'] = beer[4]
                tmp_dict['country_name'] = beer[5]
                tmp_dict['style_name'] = beer[6]
                tmp_dict['seasonal'] = beer[7]
                tmp_dict['weighted_avg'] = beer[8]
                tmp_dict['abv'] = beer[9]
                tmp_dict['est_calories'] = beer[10]
                output_beers.append(tmp_dict)

            return render_template('rec_result.html', beers=output_beers, active_page='recommend')
        else:
            return render_template('404.html')
