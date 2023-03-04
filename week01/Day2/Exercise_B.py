users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}
print("Starting:")
# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print("1: " + users["Jonathan"] ["twitter"])
# 2. Get Erik's hometown
print("2: " + users ["Erik"] ["home_town"])
# 3. Get the list of Erik's lottery numbers
print("3a: " + str(users ["Erik"] ["lottery_numbers"]))
print(f'3b: {users ["Erik"] ["lottery_numbers"]}')
# 4. Get the species of Avril's pet Monty
print("4: " + users ["Avril"] ["pets"] [0] ["species"])
# 5. Get the smallest of Erik's lottery numbers
users ["Erik"] ["lottery_numbers"].sort()
# sorted(users ["Erik"] ["lottery_numbers"])[0]
# min(users ["Erik"] ["lottery_numbers"])
print(f'5: {(users ["Erik"] ["lottery_numbers"] [0])}')
# 6. Return an list of Avril's lottery numbers that are even
even_lottery = []
for number in (users ["Avril"] ["lottery_numbers"]):
  if number % 2 == 0:
    even_lottery.append(number)
print(f'6: {even_lottery}')

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
print(f'7a: {users ["Erik"] ["lottery_numbers"]}')
users ["Erik"] ["lottery_numbers"].append(7)
print(f'7b: {users ["Erik"] ["lottery_numbers"]}')

# 8. Change Erik's hometown to Edinburgh
print(f'8a: {users ["Erik"] ["home_town"]}')
users ["Erik"] ["home_town"] = "Edinburgh"
print(f'8b: {users ["Erik"] ["home_town"]}')

# 9. Add a pet dog to Erik called "fluffy"
print(f'9a: {users ["Erik"] ["pets"]}')
users["Erik"] ["pets"].append({"name": "fluffy", "species": "dog"})
print(f'9b: {users ["Erik"] ["pets"]}')

# 10. Add another person to the users dictionary
users["Claire"] = { 
        "twitter": "no_ta",
        "lottery_numbers": [4, 7, 33, 38, 15, 25],
        "home_town": "Edinburgh",
    "pets": [
      {"name": "elsa", "species": "cat"},
      {"name": "eddi", "species": "dog"}
    ]
    }
print(f'10:  {users["Claire"]}')