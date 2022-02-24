import os


def clearConsole():
    command = "clear"
    if os.name in ("nt", "cls"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


clearConsole()

auction_bids = []


def add_bid():
    name = input("Enter your name : ")
    bid = int(input("Enter your bid amount : "))
    bid_obj = {"name": name, "bid": bid}
    auction_bids.append(bid_obj)


def max_of_bids(auction_bids):
    max = auction_bids[0]
    for i in auction_bids:
        if i["bid"] > max["bid"]:
            max = i
    print(f"The winner of the bid is {max['name']}, valued at {max['bid']}")


add_bid()
while input("Are there any more people to bid?").lower() == "yes":
    add_bid()

max_of_bids(auction_bids)
