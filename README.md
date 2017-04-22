# Project Name

basketballanalytics

# Description

The purpose of the site is to create the most engaging basketball analytics website. There has been a large increase in interest over the past couple years in how analytics can be used to better understand players,outcomes of games, and best strategies. The front-end will have four main parts (not including the signup/login page). 

The first part will be a player dashboard. This will show recent updates on the player (injury updates, trades, etc.) and data visualizations of their performance. 

The second part will be the same as the player dashboard but for teams as a whole. 

The third part of the front-end will be a feed where a person can select which teams and players they want to follow. This feed will be similar to Facebook/Twitter in layout and whenever there is a new update to someone they follow that person/team will be put on top. 

The fourth and final part of the front-end is focused on predictive models. This page will show interactive player projections for the next upcoming game, and for the rest of their career. The data visualizations will be done in d3.js.

The data needed for all of this is available from an API called Stattleship. We are going to write a script that copies the necessary data from their API to our database so we are not constantly sending requests to their API. 

Our database will have tables for players and their statistics for individual games, along with a table with team statistics. We are still figuring out the exact layout of the database. Further, we will have a table for users and the people who they follow. The backend will be responsible for handling all the queries/creation of the database. Aside from that, it will be primarily responsible for the predictive models.

# Usage

To run the development server, run `python manage.py runserver` in this directory.  It will run on port 8000 by default.  Navigate to http://127.0.0.1:8000/.

# Development 

To create a new 'app' (a python package that is essentially a new separate of the web app that would require different templates, etc.), run 'python manage.py startapp your_app_name_here' and your_app_name_here into the INSTALLED_APPS array in settings.py.

For templates, you need to first create a new `templates` direct in the app directory (for example, in the player app, a folder called templates), and then create a subdirectory named identically to the app's name in the templates directory (so in player directory: player/templates/player).  You should put your templates in the subdirectory.

To link to other pages within Django templates, make sure you set the namespaces properly for both the app and the view.  In app/urls.py, set the app_name variable and use the name field for each url object.  In server/urls.py, set the names field for the url object to be the relevant app name. 

# Authors

<a href="https://github.com/attfarhan"><img src="https://avatars0.githubusercontent.com/u/16265452?v=3&s=460" align="left" height="30px"></a> **Farhan Attamimi** 
<a href="https://github.com/glennhull"><img src="https://avatars3.githubusercontent.com/u/10781869?v=3&s=460" align="left" height="30px"></a> **Glen Hull** 

<a href="https://github.com/jackhuang19"><img src="https://avatars0.githubusercontent.com/u/25134347?v=3&s=460" align="left" height="30px"></a> **Jack Huang** 

# License

This code base is released under the [MIT](/LICENSE) license.
