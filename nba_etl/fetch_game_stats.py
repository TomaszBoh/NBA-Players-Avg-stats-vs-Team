import pandas as pd
import time
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv3

def fetch_games_for_season(season='2024-25'):
    print(f"Downloading games from season: {season}")
    try:
        gamefinder = leaguegamefinder.LeagueGameFinder(
            league_id_nullable='00',
            season_nullable=season,
            season_type_nullable='Regular Season'  # możesz zmienić na 'Playoffs'
        )
        games_df = gamefinder.get_data_frames()[0]
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

    if games_df.empty:
        print("No games.")
    else:
        print(f"Found {len(games_df)} rows.")
        print(games_df[['GAME_ID', 'TEAM_NAME', 'MATCHUP', 'GAME_DATE']].drop_duplicates())

    return games_df

def fetch_boxscores_for_games(game_ids):
    all_stats = []
    for gid in game_ids:
        print(f"Downloading game stats {gid}")
        try:
            boxscore = boxscoretraditionalv3.BoxScoreTraditionalV3(game_id=gid)
            player_stats = boxscore.player_stats.get_data_frame()
            all_stats.append(player_stats)
            time.sleep(3)  # To avoid block from api
            player_stats_df = pd.concat(all_stats, ignore_index=True)
            player_stats_df.to_csv(f'player_stats_2024-25.csv', index=False)
        except Exception as e:
            print(f"Eror durning downloading game {gid}: {e}")
            continue
    if all_stats:
        return print("Done")

if __name__ == "__main__":
    season_code = "2024-25"

    games_df = fetch_games_for_season(season=season_code)
    if games_df.empty:
        print("No games.")
        exit()

    # Unikalne ID meczów – tylko raz na mecz (nie 2x per drużyna)
    game_ids = games_df['GAME_ID'].drop_duplicates().tolist()
    print(game_ids)
    player_stats_df = fetch_boxscores_for_games(game_ids)

    # Zapisz wyniki
    games_df.to_csv(f'games_{season_code}.csv', index=False)
    # if not player_stats_df.empty:
    #     player_stats_df.to_csv(f'player_stats_{season_code}.csv', index=False)

    print("Files saved.")
