import pandas as pd
import time
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv3

def fetch_boxscores_for_games(game_ids):
    all_stats = []
    print(f"Pobieranie statystyk dla meczu {game_ids}")

    boxscore = boxscoretraditionalv3.BoxScoreTraditionalV3(game_id='0022401167')
    player_stats = boxscore.player_stats.get_data_frame()
    print(player_stats.shape)
    df = player_stats
    df.to_csv('stats.csv')
    all_stats.append(player_stats)

    time.sleep(3)  # Limitowanie zapytań – nie usuwaj

    data = pd.DataFrame(all_stats, index=False)
    data.to_excel("Stats.xlsx")

    return print('text')

if __name__ == "__main__":
    game_ids = ['0022401167','0022401168','0022401169']
    fetch_boxscores_for_games('0022401167')