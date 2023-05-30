import os
from art import logo

print(logo)

bids = {}
bidders = True

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for user in bidding_record:
    if bidding_record[user] > highest_bid:
      highest_bid = bidding_record[user]
      winner = user
  print(f"The highest bidder is {winner} with ${highest_bid}")

while bidders:
  name = input("What is your name?: ")
  price = int(input("What is your bid price?: $"))
  
  bids[name] = price
  
  other_bidders = input("Are there any other users who want to bid? 'Yes' or 'No'\n").lower()
  if other_bidders == "yes":
    os.system('cls')
  else:
    os.system('cls')
    bidders = False
    highest_bidder(bids)