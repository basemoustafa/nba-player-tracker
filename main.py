from twilio.rest import Client
import keys
import requests
from datetime import datetime

client = Client(keys.account_sid, keys.auth_token)

def fetch_player_stats(player_name):
    base_url = "https://www.balldontlie.io/api/v1/"

    # Fetch player details
    player_search_url = base_url + "players?search={}".format(player_name)
    response = requests.get(player_search_url)
    data = response.json()

    # Check if player was found
    if data['meta']['total_count'] == 0:
        print("Player not found.")
        return None
    
    player_id = data['data'][0]['id']

     # Get current season
    current_year = datetime.now().year 
    season = "{}".format(current_year - 1)

    # Fetch player stats for the current season
    player_season_stats_url = base_url + "season_averages?season={}&player_ids[]={}".format(season, player_id)
    response = requests.get(player_season_stats_url)
    data = response.json()

    # Check if player season stats are available
    if len(data['data']) == 0:
        print("No season stats available for the player.")
        return None

    # Extract the relevant season stats from the response
    season_stats = data['data'][0]
    player_season_stats = {
        'Points per Game': season_stats['pts'],
        'Assists per Game': season_stats['ast'],
        'Rebounds per Game': season_stats['reb'],
        # Add more stats as per your preference
    }

    return player_season_stats

def send_sms(to_number, body):
    client.messages.create(to=to_number, from_=keys.twilio_number, body=body)
    # print(body)

player_name = input("Enter the player's name: ")
phone_number = input("Enter your phone number: ")
phone_number = phone_number
# Fetch player stats
player_stats = fetch_player_stats(player_name)

# Check if player stats are available
if player_stats is None:
    print("Player stats not available.")
else:
    # Send the player stats to the phone number
    stats_string = "\nPlayer: {}\n\n==========================\n\nSeason Averages:\n\n".format(player_name)
    for stat, value in player_stats.items():
        stats_string += "{}: {}\n".format(stat, value)

    # Add code to send the message to the phone number using your preferred method (e.g., SMS API, email, etc.)
    send_sms(phone_number, stats_string)
    print("Player stats sent to {} successfully.".format(phone_number))