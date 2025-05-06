from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

def fetch_game_ids_by_date():
    print(f"Pobieranie GAME_ID meczów NBA z dnia...")

    # Pobierz wszystkie mecze (NBA regular season i playoffs)
    gamefinder = leaguegamefinder.LeagueGameFinder(league_id_nullable='00', season_nullable='2024-25')

    games_df = gamefinder.get_data_frames()[0]
    print(games_df)
    if games_df.empty:
        print("Brak meczów tego dnia.")
        return []

    # Wybierz unikalne GAME_ID
    game_ids = games_df['GAME_ID'].unique().tolist()

    print(f"Znaleziono {len(game_ids)} meczów:")
    print(game_ids)

    # (Opcjonalnie) Zapisz dane do pliku
    games_df.to_excel(f'games_2024-25.xlsx', index=False)
    print(f"Dane zapisano do pliku games_2024-25.xlsx")

    return game_ids

# Uruchom
fetch_game_ids_by_date()
