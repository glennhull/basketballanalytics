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

TODO

# Authors

<a href="https://github.com/attfarhan"><img src="https://avatars0.githubusercontent.com/u/16265452?v=3&s=460" align="left" height="30px"></a> **** - [[courier-new]](https://github.com/courier-new)

<a href="https://github.com/glennhull"><img src="https://avatars3.githubusercontent.com/u/10781869?v=3&s=460" align="left" height="30px"></a> **Glen Hull** -  [[auberginekenobi]](https://github.com/auberginekenobi)

<a href="https://github.com/jackhuang19"><img src="https://avatars0.githubusercontent.com/u/25134347?v=3&s=460" align="left" height="30px"></a> **Jack Huang** - [[courier-new]](https://github.com/patrickshao)


# License

This code base is released under the [MIT](/LICENSE) license.
