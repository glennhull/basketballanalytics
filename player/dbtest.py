from stattlepy import Stattleship

New_query = Stattleship()

def get_team_slugs():
	team_slug_q = New_query.ss_get_results(sport='basketball',league='nba',ep='teams')[0]['teams']
	length = len(team_slug_q)
	teams = []
	for i in range(length):
		teams.append(team_slug_q[i]['slug'])
	return teams

def players():	
	Token = New_query.set_token('46a96fa056bca68ddb8835f70ad68974')
	# player_id = "nba-%s" % player_name
	team_slugs = get_team_slugs()
	for team in team_slugs:
		players = New_query.ss_get_results(sport='basketball', team_id=team, league='nba', ep='players')
		for n in players[0]['players']:
			if n['active']==True:							
				pid = ['id']
				name = ['name']	
				pos = ['position_abbreviation']
				tid = ['team_id']
				add_player(pid, name, pos, tid)

def add_player(player_id, player_name, pos, team):
	print "adding player"
	pl = Player.objects.create(player_id = player_id, player_name = player_name, position = pos, team_id = tid);	
	pl.save()
	
players()