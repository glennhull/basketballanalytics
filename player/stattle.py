from stattlepy import Stattleship

New_query = Stattleship()
Token = New_query.set_token('46a96fa056bca68ddb8835f70ad68974')
Output = New_query.ss_get_results(sport='basketball',league='nba',ep='player_season_stats',player_id='nba-stephen-curry')

print Output