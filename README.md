LoLpy
=====

Python library for accessing League of Legends' API

## Getting Started:

1. Import LoLpy.py into your python script.
2. Initialize a new LoLpy object using LoLpy(API_KEY) where API_KEY is your applications key.
3. Use LoLpy's methods to easily get information for your python applicatoin.

## Methods:

### getchampions()
Returns a python dictionary with all the League of Legends champions and their attributes.
```python
lolpy = LoLpy(API_KEY)
champions = lolpy.getchampions()
```

### get_summoner_by_name(summonerName)
Returns a python dictionary with information about the summoner
```python
lolpy = LoLpy(API_KEY)
game = lolpy.get_summoner_by_name('Trick2g')
```

### get_game(summonerName)
Returns a python dictionary with information about the game a summoner is currently in and their recent games
```python
lolpy = LoLpy(API_KEY)
game = lolpy.get_game('Trick2g')
```

### get_league(summonerName)
Returns a python dictionary with information about the summoner's league
```python
lolpy = LoLpy(API_KEY)
game = lolpy.get_league('Trick2g')
```

### get_stats_summary(summonerName)
Returns a python dictionary with information about the summoner's stats
```python
lolpy = LoLpy(API_KEY)
game = lolpy.get_stats_summary('Trick2g')
```

## Reducing API Calls:
* Each method that takes a summoner name also has a method that takes a summonerID which can be found in the return of get_summoner_by_name(). This removes one request for every method.
* To call these append "\_by\_id" to any method with the parameter summonerName other than get_summoner_by_name().
* Example:
```python
game = lolpy.get_game_by_id(summonerID)
```

## Notes:
* To change region from NA, it can be changed in the contructor with the call LoLpy(API_KEY,region='EUW')
* Some methods cannot be called with certain regions, be sure to check the API if you have issues with regions other than NA
