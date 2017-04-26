from player.models import Player, Season_Stats, Game_Logs
from stattlepy import Stattleship


New_query = Stattleship()
Token = New_query.set_token('46a96fa056bca68ddb8835f70ad68974')

def get_team_slugs():
	team_slug_q = New_query.ss_get_results(sport='basketball',league='nba',ep='teams')[0]['teams']
	length = len(team_slug_q)
	teams = []
	for i in range(length):
		teams.append(team_slug_q[i]['slug'])
	return teams

def players():	
	team_slugs = get_team_slugs()
	for team in team_slugs:
		players = New_query.ss_get_results(sport='basketball', team_id=team, league='nba', ep='players')
		for n in players[0]['players']:
			if n['active']==True:							
				pid = n['id']
				name = n['name']	
				pos = n['position_abbreviation']
				tid = n['team_id']
				# print pid
				add_player(pid, name, pos, tid)

def add_player(player_id, player_name, pos, team):
	pl = Player.objects.create(player_id = player_id, player_name = player_name, position = pos, team_id = team);	
	pl.save()

def season_stats(): 
	team_slugs = get_team_slugs()
	for team in team_slugs:
		players = New_query.ss_get_results(sport='basketball', team_id=team, league='nba', ep='players')
		for p in players: 			
			season_stats = New_query.ss_get_results(sport='basketball',league='nba', ep='player_season_stats', team_id=team)
			for ss in season_stats[0]['player_season_stats']: 
				pid = ss['player_id']
				ppg = ss['average_points']
				apg = ss['average_assists']
				rpg = ss['average_rebounds']
				bpg = ss['average_blocks']
				spg = ss['average_steals']
				fga = ss['total_field_goals_att']
				fgm = ss['total_field_goals_made']
				tpg = ss['average_turnovers']
				threept_attempted = ss['total_three_points_att']
				threept_made = ss['total_three_points_made']
				add_season_stats(pid, ppg, apg, rpg, bpg, spg, fga, fgm, tpg, threept_attempted, threept_made)	
		
	

def add_season_stats(pid, ppg, apg, rpg, bpg, spg, fga, fgm, tpg, threept_attempted, threept_made):
	sstats = Season_Stats.objects.create(player_id = pid, ppg = ppg, apg = apg, rpg = rpg, bpg = bpg,
		spg = spg, fga = fga, fgm = fgm, tpg = tpg, threept_attempted = threept_attempted, threept_made = threept_made);	
	sstats.save()

def game_logs():
	team_slugs = get_team_slugs()
	for team in team_slugs:
		game_logs = New_query.ss_get_results(sport='basketball', team_id=team, league='nba', ep='game_logs')
		for n in game_logs[0]['game_logs']:
			game_log_id = n['id']
			player_id = n['player_id']
			team_id = n['team_id']
			opponent_id = n['opponent_id']
			pts = n['points']
			assists = n['assists']
			rebs = n['rebounds']
			blocks = n['blocks']
			steals = n['steals']
			fga = n['field_goals_attempted']
			fgm = n['field_goals_made']
			tpg = n['turnovers']
			threept_attempted = n['three_pointers_attempted']
			threept_made = n['three_pointers_made']
			home_team_score = n['home_team_score']
			away_team_score = n['away_team_score']
			team_score = n['team_score']
			team_outcome = n['team_outcome']
			add_game_log(game_log_id, player_id, team_id, opponent_id, pts, assists, rebs, blocks, steals,
				fga, fgm, tpg, threept_attempted, threept_made, home_team_score, away_team_score, team_score,
				team_outcome)

def add_game_log(game_log_id, player_id, team_id, opponent_id, pts, assists, rebs,
	blocks, steals, fga, fgm, tpg, threept_attempted, threept_made, home_team_score,
	away_team_score, team_score, team_outcome):
	gl = Season_Stats.objects.create(game_log_id = game_log_id, player_id = player_id, team_id = team_id, opponent_id = opponent_id, pts = pts, assists = assists, rebs = rebs,
	blocks = blocks, steals = steals, fga = fga, fgm = fgm, tpg = tpg, threept_attempted = threept_attempted, threept_made = threept_made, home_team_score = home_team_score,
	away_team_score = away_team_score, team_score = team_score, team_outcome = team_outcome)
	gl.save()

# LEave these commented out so we dont hit API again.
# players()
# season_stats()