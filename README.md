LoLpy
=====

Python library for accessing League of Legends' API

###Getting Started:

1. Import lol.py into your python script.
2. Initialize a new LoLpy object using LoLpy(API_KEY) where API_KEY is your applications key.
3. Use LoLpy's methods to easily get information for your python applicatoin.

###Methods:

###getchampions()

Returns a python dictionary with all the League of Legends champions and their attributes.
```python
lolpy = LoLpy(API_KEY)
champions = lolpy.getchampions()
```