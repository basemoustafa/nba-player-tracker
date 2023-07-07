# nba-player-tracker

This Python script allows you to receive NBA player stats via SMS. After providing the name of an NBA player and your phone number, the script fetches the player's current season stats and sends them to your phone number using Twilio.

## Features

- Fetches the current season stats of an NBA player
- Sends player stats as an SMS to a specified phone number
- Easy setup and usage with prompts for player name and phone number

## Setup

1. Clone the repository:

         git clone <repository-url>

2. Install the required dependencies:

        pip install twilio


3. Obtain Twilio credentials:

    - Sign up for a free Twilio account at [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio).
    - Retrieve your Account SID and Auth Token from the Twilio dashboard.
    - Replace the placeholder values in the `keys.py` file with your actual Account SID and Auth Token.

## Usage

1. Run the script:

        python3 player_stats_texter.py


2. Follow the prompts:

    - Enter the name of the NBA player for whom you want to receive stats.
    - Enter your phone number (in the format: <country code><phone number>, e.g., +12025551234).

3. Receive player stats via SMS:

    - The script fetches the player's current season stats from the NBA API.
    - The stats are sent to your phone number using the Twilio API.

