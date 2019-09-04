import os
import re
import json
import logging
import pandas as pd

# Load in file


class ParseGame(object):
    """ This class contains the code necessary to parse a game and write it to a database

	Attributes:
		filepath: A string indicating the path to the file
		dbcon: An object containing the database connection
		logger: A logger to keep track of events
	"""

    def __init__(self, filepath="", logpath="gameparser.log"):
        """ Inits empty class
		"""
        self.filepath = ""
        self.logpath = logpath
        self.logger = logging.basicConfig(
            filename=logpath,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
        )

    def import_game():
        """ Reads in the game JSON file, get basic game info such as match id, league and season
		"""
        self.logger.info("Starting to read in file")
        with open(self.filepath) as f:
            self.data = json.load(f)
        self.logger.info("Read in file " + self.filepath)

        self.logger.info("Gathering match id, league, season")
        self.match_id = re.findall("\d{6}", self.filepath)[0]
        self.league = re.findall("[A-Z]{3}\d", self.filepath)[0]
        self.season = re.findall("\d{4}-\d{4}", self.filepath)[
            0
        ]  # TODO: Fix this for single year seasons
        self.logger.info("Retrieved match id, league, season")
        self.logger.info(
            "Working on match "
            + self.match_id
            + " in league "
            + self.league
            + " in season "
            + self.season
        )

    def check_game_data():
        """ Sanitizes game data to see if there are any glaring errors
		"""
        raise NotImplementedError

    def extract_players():
        """ Extract player information, which is only the PlayerId and the name

		TODO: Maybe just roll this into a huge extract_players feature
		"""
        players = self.data["playerIdNameDictionary"]
        player_df = pd.Series(players).explode().reset_index()
        player_df.columns = ["PlayerId", "PlayerName"]
        self.player_data = player_df
        raise NotImplementedError

    def extract_referee():
        """ Extract referee data, which is only referee id, name and match id
		"""
        self.logger.info("Retrieving referee data " + self.match_id)
        referee_id = self.data["referee"]["officialId"]
        referee_name = self.data["referee"]["name"]
        referee_df = pd.DataFrame([self.match_id, referee_id, referee_name]).transpose()
        referee_df.columns = ["MatchId", "RefereeId", "RefereeName"]
        self.referee_data = referee_df
        self.logger.info("Retrieved referee data " + self.match_id)

    def extract_player_game():
        """ Extract info on player-games
		"""
        self.logger.info("Retrieving player-game info " + self.match_id)
        players_df = pd.DataFrame()
        for home_player in data["home"]["players"]:
            player_id = home_player["playerId"]
            shirt_num = home_player["shirtNo"]
            name = home_player["name"]
            player_pos = home_player["position"]
            height = home_player["height"]
            weight = home_player["weight"]
            age = home_player["age"]
            # first_eleven = home_player['isFirstEleven']  # TODO: Deal with subs
            man_of_match = home_player["isManOfTheMatch"]
            field = home_player["field"]
            player_row = pd.DataFrame(
                [
                    self.match_id,
                    player_id,
                    shirt_num,
                    name,
                    player_pos,
                    height,
                    weight,
                    age,
                    man_of_match,
                    field,
                ]
            ).transpose()
            player_row.columns = [
                "PlayerId",
                "ShirtNo",
                "Name",
                "Position",
                "Height",
                "Weight",
                "Age",
                "ManOfMatch",
                "Field",
            ]
            players_df = players_df.append(player_row)
        for away_player in data["away"]["players"]:
            player_id = away_player["playerId"]
            shirt_num = away_player["shirtNo"]
            name = away_player["name"]
            player_pos = away_player["position"]
            height = away_player["height"]
            weight = away_player["weight"]
            age = away_player["age"]
            # first_eleven = away_player['isFirstEleven']  # TODO: Deal with subs
            man_of_match = away_player["isManOfTheMatch"]
            field = away_player["field"]
            player_row = pd.DataFrame(
                [
                    self.match_id,
                    player_id,
                    shirt_num,
                    name,
                    player_pos,
                    height,
                    weight,
                    age,
                    man_of_match,
                    field,
                ]
            ).transpose()
            player_row.columns = [
                "PlayerId",
                "ShirtNo",
                "Name",
                "Position",
                "Height",
                "Weight",
                "Age",
                "ManOfMatch",
                "Field",
            ]
            players_df = players_df.append(player_row)
        self.player_game_data = players_df
        self.logger.info("Retrieved player-game info for " + self.match_id)

        def extract_game():
            """ Extract game info
			"""
            self.logger.info("Retrieving game info " + self.match_id)
            home_team_id = self.data["home"]["teamId"]
            home_team_name = self.data["home"]["name"]
            home_team_manager = self.data["home"]["managerName"]
            home_avg_age = self.data["home"]["averageAge"]

            away_team_id = self.data["away"]["teamId"]
            away_team_name = self.data["away"]["name"]
            away_team_manager = self.data["away"]["managerName"]
            away_avg_age = self.data["away"]["averageAge"]

            home_goals = int(self.data["score"].split(":")[0].strip())
            away_goals = int(self.data["score"].split(":")[1].strip())
            home_ht_goals = int(self.data["htScore"].split(":")[0].strip())
            away_ht_goals = int(self.data["htScore"].split(":")[1].strip())
            home_ft_goals = int(self.data["ftScore"].split(":")[0].strip())
            away_ft_goals = int(self.data["ftScore"].split(":")[1].strip())

            attendance = self.data["attendance"]
            venue_name = self.data["venueName"]
            weather_code = self.data["weatherCode"]
            start_time = self.data["startTime"]
            start_date = self.data["startDate"]

            game_info_df = pd.DataFrame(
                [
                    match_id,
                    league,
                    season,
                    venue_name,
                    attendance,
                    start_date,
                    start_time,
                    weather_code,
                    home_team_id,
                    home_team_name,
                    home_team_manager,
                    home_avg_age,
                    away_team_id,
                    away_team_name,
                    away_team_manager,
                    away_avg_age,
                    home_goals,
                    away_goals,
                    home_ht_goals,
                    away_ht_goals,
                    home_ft_goals,
                    away_ft_goals,
                ]
            ).transpose()
            game_info_df.columns = [
                "MatchId",
                "League",
                "Season",
                "VenueName",
                "Attendance",
                "StartDate",
                "StartTime",
                "WeatherCode",
                "HomeTeamId",
                "HomeTeamName",
                "HomeTeamManager",
                "HomeAvgAge",
                "AwayTeamId",
                "AwayTeamName",
                "AwayTeamManager",
                "AwayAvgAge",
                "HomeGoals",
                "AwayGoals",
                "HomeHTGoals",
                "AwayHTGoals",
                "HomeFTGoals",
                "AwayFTGoals",
            ]
            self.game_data = game_info_df
            self.logger.info("Retrieved game info " + self.match_id)
