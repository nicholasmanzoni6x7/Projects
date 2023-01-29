from art import logo

print(logo)
bid_war = {}
bidding_ends = False

def highest_bidder(bidding_record):
	highest_bid = 0
	winner = ""
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of {highest_bid}!")

while not bidding_ends:
	name = input("What is your name? ")
	bid = int(input("What is your bid? $"))
	bid_war[name] = bid
	still_bidding = input("Are there any others bids? Type 'yes' or 'no'. ")
	if still_bidding == "no":
		bidding_ends = True
		highest_bidder(bid_war)