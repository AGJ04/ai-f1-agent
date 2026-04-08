import fastf1
import pandas as pd

fastf1.Cache.enable_cache('data/raw')

def load_race_data(year, gp):
    session = fastf1.get_session(year, gp, 'R')
    session.load()

    laps = session.laps
    results = session.results

    return laps, results