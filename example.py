import LoLpy
from info import API_KEY


def main():
    print "Let's get started!"
    lolpy = LoLpy.LoLpy(API_KEY)
    account = lolpy.get_summoner_by_name('Dyrus')['Dyrus'.lower()]
    league = lolpy.get_league_by_id(account['id'])
    ranked = lolpy.get_stats_ranked('Dyrus')
    print ranked


if __name__ == "__main__":
    main()
