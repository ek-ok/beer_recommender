#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Defines the recommend view
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
import pandas as pd
import numpy as np
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
        df = db.fetch_data(query)
        beers = df.values.tolist()

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

            df = db.fetch_data(query)
            output_beers = [df.ix[i].to_dict() for i in df.index]

            return render_template('rec_result.html', beers=output_beers, active_page='recommend')
        else:
            return render_template('404.html')
