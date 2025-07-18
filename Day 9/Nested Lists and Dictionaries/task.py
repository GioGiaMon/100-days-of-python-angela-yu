capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# nested List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dij"],
    "Germany": ["Stuttgart", "Berlin"],
}
# PAUSE 1 print Lille
print(f"Travel log France, {travel_log["France"][1]}")
#
# Nesting Lists inside other Lists
nested_list = ["A", "B", ["C", "D"]]
#
# PAUSE 2 - print out letter D
print(f"{nested_list[2][1]}")
#
# Nesting a Dictionary inside a Dictionary
travel_log_v2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
# PAUSE 3 - Figure out how to print out "Stuttgart" from the previous list
print(f"{travel_log_v2["Germany"]["cities_visited"][2]}")