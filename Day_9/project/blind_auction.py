
# Old Solution 


# import art
# print(art.logo)

# # TODO-1: Ask the user for input
# # TODO-2: Save data into dictionary {name: price}
# # TODO-3: Whether if new bids need to be added
# # TODO-4: Compare bids in dictionary


# auction_data = {}

# def auction():
#     username = input("What is your name: ")
#     user_bid = int(input("What is your bid: $"))

#     auction_data[username] = user_bid
#     print(auction_data)

#     other_bid = input("Are there any other bidders? Type 'yes' or 'no'")
#     if other_bid == "yes":
#         print('\n' * 20)
#         auction()

# auction()


# max_value = max(auction_data.values())

# # Get the name of the highest bidder
# for name, bid in auction_data.items():
#     if bid == max_value:
#         winner = name
#         break

# print(f"The winner is {winner} with a bid of ${max_value}")




import  art
print(art.logo)

# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
def find_highest_bidders(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of${highest_bid}.")




bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' orr 'no'. \n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidders(bids)
    elif should_continue == "yes":
        print("\n" * 30)


# TODO-4: Compare bids in dictionary



