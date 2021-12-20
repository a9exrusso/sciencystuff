from dataclasses import dataclass
import pandas as pd
from pandas.core.base import DataError
import requests
import chess.pgn
import chess

def get_data(username,timestamp):
    # Get the data from the API
    print("Getting data from API...")
    url = f"http://lichess.org/api/games/user/{username}?since={timestamp}"
    data = requests.get(url)
    if data.status_code != 200:
        raise Exception("The following response was returned: " + str(data.status_code))
    else:
        print("Successfully retrieved data")
        # Write data to file
        with open("data.pgn", "w") as f:
            f.write(data.text)


    
get_data("lonaya","1639554963")

# convert pgn file to dataframe
def pgn_to_df(pgn_file):
    totalkeyerrors = 0
    print("Converting pgn file to dataframe...")
    pgn = open(pgn_file)
    game = chess.pgn.read_game(pgn)

    #print(game)
    df = pd.DataFrame(columns=["Event","Site","Date","White","Black","Result","UTCDate","UTCTime","WhiteElo","BlackElo","WhiteRatingDiff","BlackRatingDiff","Variant","TimeControl","ECO","Termination","FEN","SetUp"])
    f = open("data.pgn", "r")
    game_list = []
    while True:
        game = chess.pgn.read_game(f)
        if game is None:
            break
        game_list.append(game)

    for game in game_list:
        try:
            df = df.append({"Event":game.headers["Event"],"Site":game.headers["Site"],"Date":game.headers["Date"],"White":game.headers["White"],"Black":game.headers["Black"],"Result":game.headers["Result"],"UTCDate":game.headers["UTCDate"],"UTCTime":game.headers["UTCTime"],"WhiteElo":game.headers["WhiteElo"],"BlackElo":game.headers["BlackElo"],"WhiteRatingDiff":game.headers["WhiteRatingDiff"],"BlackRatingDiff":game.headers["BlackRatingDiff"],"Variant":game.headers["Variant"],"TimeControl":game.headers["TimeControl"],"ECO":game.headers["ECO"],"Termination":game.headers["Termination"],"FEN":game.headers["FEN"],"SetUp":game.headers["SetUp"]},ignore_index=True)

        except KeyError:
            #print(KeyError)
            totalkeyerrors += 1
        except DataError:
            print("DataError")
        game = chess.pgn.read_game(pgn)
    #print("Total keyErrors: " + str(totalkeyerrors))
    return df
    

df1 = pgn_to_df("data.pgn")
print(df1)







