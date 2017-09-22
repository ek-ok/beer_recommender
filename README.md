# Beer Recommender

This application is running here [http://recommend.beer](http://www.recommend.beer/)

# What is your new favorite beer?

I always wonder what beer to get at a bar. There are way too many choices for a casual beer drinker and I usually know 
just a few beers out of the dozens of choices there. Thus, I decided to build a beer recommendation engine based on 
online user reviews, which were scraped from one of the most popular beer review sites. Running multithreaded Python 
web crawlers on an Ubuntu server for a few days, pretty much the entire site was successfully scraped and the data was 
temporary stored into MongoDB, because the data was unstructured. For example, some seasonal beers had extra rating 
fields and they were unknown until they were scraped. At the end, in the NoSQL, there were 6,899,254 reviews, 319,483 
beer data, and 362,602 user info. Finally, after significant data mungging, these raw data was migrated to PostgreSQL 
from MongoDB for machine learning and analysis purposes.