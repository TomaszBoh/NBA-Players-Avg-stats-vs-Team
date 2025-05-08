import pandas as pd
from datetime import datetime, timedelta
from nba_api.stats.static import players, teams
from nba_api.live.nba.endpoints import scoreboard
import time

import pandas as pd
from nba_api.stats.static import players, teams

def fetch_active_players():
    print("Pobieranie listy aktywnych zawodników NBA...")
    player_list = players.get_active_players()
    df = pd.DataFrame(player_list)
    df = df.sort_values(by="full_name")
    df.to_csv("players.csv", index=False)
    print(f"Zapisano {len(df)} zawodników do players.csv")

def fetch_nba_teams():
    print("Pobieranie listy drużyn NBA...")
    team_list = teams.get_teams()
    print(team_list)
    df = pd.DataFrame(team_list)
    # df = df[df['is_nba_team']]  # tylko oficjalne zespoły NBA
    df = df.sort_values(by="full_name")
    df.to_csv("teams.csv", index=False)
    print(f"Zapisano {len(df)} drużyn do teams.csv")

if __name__ == "__main__":
    fetch_active_players()
    fetch_nba_teams()
