from __future__ import unicode_literals
from team.models import Team
from stattlepy import Stattleship

New_query = Stattleship()
Token = New_query.set_token('46a96fa056bca68ddb8835f70ad68974')

def team():
	teams = New_query.ss_get_results(sport='basketball', league='nba', ep='teams')
	team_season_stats = New_query.ss_get_results(sport='basketball', league='nba', ep='team_season_stats')
	# print teams[0]['teams'][0].keys()
	team_name_dict = {}
	team_slug_dict = {}

	for t in teams[0]['teams']: 
		team_slug = t['slug']
		team_name = t['name'] + " " + t['nickname']
		team_id = t['id']
		team_name_dict[team_id] = team_name
		team_slug_dict[team_id] = team_slug

	for tss in team_season_stats[0]['team_season_stats']: 
		team_id = tss['team_id']
		slug = team_slug_dict[team_id]
		name = team_name_dict[team_id]
		ppg = tss['average_points']
		apg = tss['average_assists']
		rpg = tss['average_rebounds']
		bpg = tss['average_blocks']
		spg = tss['average_steals']
		fga = tss['total_field_goals_att']
		fgm = tss['total_field_goals_made']
		tpg = tss['average_turnovers']
		threept_attempted = tss['total_three_points_att']
		threept_made = tss['total_three_points_made']
		fastbreak_points = tss['total_fast_break_pts']
		paint_points = tss['total_paint_pts']
		turnover_points = tss['total_points_off_turnovers']
		secondchance_points = tss['total_second_chance_pts']
		add_team(team_id, slug, name, ppg, apg, rpg, bpg, spg, fga, fgm, tpg, threept_attempted,
			threept_made, fastbreak_points, turnover_points, secondchance_points)

def add_team(team_id, team_slug, team_name, ppg, apg, rpg, bpg, spg, fga, fgm, tpg, threept_attempted, 
	threept_made, fastbreak_points, turnover_points, secondchance_points):
	team = Team.objects.create(team_id = team_id, team_slug = team_slug, team_name = team_name, ppg = ppg, apg = apg, rpg = rpg, bpg = bpg,
		spg = spg, fga = fga, fgm = fgm, tpg = tpg, threept_attempted = threept_attempted, threept_made = threept_made, 
		fastbreak_points = fastbreak_points, turnover_points = turnover_points, secondchance_points = secondchance_points)
	team.save()

team()