from tkinter import *
import requests
import json
import sqlite3

# api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=16678e0d-1685-4e32-8abc-af74a679610e")
#
# api = json.loads(api_request.content)
#
# print("------------------------")
# print("------------------------")
#
# # print(api["data"][0]coin[1])
# # print(api["data"][0]["quote"]["USD"]["price"])
# # print("{0:.4f}".format(api["data"][0]["quote"]["USD"]["price"]))
# #
# # print(api["data"]["symbol"]coin[1])
# # print(api["data"]["symbol"]["quote"]["USD"]["price"])
# # print("{0:.4f}".format(api["data"]["symbol"]["quote"]["USD"]["price"]))
# # NOTE: ("{0:.4f}".format) ARE USE TO PRINT THE DECIMAL UPTO 4-------------
#
# # ----------FETCHING THE DATA BY USING FOR LOOP-------------
# # for i in range(0, 6):
# #     print(api["data"][i]coin[1])
# #     print(api["data"][i]["quote"]["USD"]["price"])
# #     # --------------FOR LIMITED PLACE OF DECIMALS--------------
# #     print("{0:.4f}".format(api["data"][i]["quote"]["USD"]["price"]))
# #     print("-----------------------")
#
# # coins = ["BTC", "ETH"]
# #
# # for i in range(0, 6):
# #     for coin in coins:
# #         if api["data"][i]coin[1] == coin:
# #             print(api["data"][i]coin[1])
# #             print("{0:.4f}".format(api["data"][i]["quote"]["USD"]["price"]))
# #             print("-----------------")
#
# coins = [
#     {
#         "symbol": "BTC",
#         "amount_owned": 2,
#         "price_per_coin": 9500
#     },
#     {
#         "symbol": "ETH",
#         "amount_owned": 5,
#         "price_per_coin": 695
#     },
# ]
#
# # for i in range(0, 6):
# #     for coin in coins:
# #         if api["data"][i]coin[1] == coin[1]:
# #             print(api["data"][i]["name"] + "-" + api["data"][i]coin[1])
# #             print("Price - ${0:.4f}".format(api["data"][i]["quote"]["USD"]["price"]))
# #             print("-----------------------")
#
# # -------------FOR CALCULATING PROFIT AND LOSS------------
# total_pl = 0
#
# for i in range(0, 6):
#     for coin in coins:
#         if api["data"][i]coin[1] == coin[1]:
#             total_paid = coin[2] * coin[3]
#             current_value = coin[2] * api["data"][i]["quote"]["USD"]["price"]
#             pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
#             total_pl_coin = pl_percoin * coin[2]
#
#             total_pl = total_pl + total_pl_coin
#
#             print(api["data"][i]["name"] + "-" + api["data"][i]coin[1])
#             print("Price - ${0:.4f}".format(api["data"][i]["quote"]["USD"]["price"]))
#             print("Number of Coin:", coin[2])
#             print("Total Amount Paid:", "${0:.4f}".format(total_paid))
#             print("Current Value:", "${0:.4f}".format(current_value))
#             print("Profit/Loss Per coin", "${0:.4f}".format(pl_percoin))
#             print("Total P/L With Coin:", "${0:.4f}".format(total_pl_coin))
#             print("-----------------------")
#
# print("Total P/L For Portfolio:", "${0:.4f}".format(total_pl))


# --------------GUI (TKINTER)-----------------
from tkinter import *


pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')

con = sqlite3.connect('coin.db')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()

# cursorObj.execute("INSERT INTO coin VALUES(1, 'BTC', 2, 9595)")
# con.commit()
#
# cursorObj.execute("INSERT INTO coin VALUES(2, 'ETH', 5, 2095)")
# con.commit()
#
# cursorObj.execute("INSERT INTO coin VALUES(3, 'LTC', 75, 1313)")
# con.commit()
#
# cursorObj.execute("INSERT INTO coin VALUES(4, 'XMR', 10, 3250)")
# con.commit()
#
# cursorObj.execute("INSERT INTO coin VALUES(5, 'EOS', 95, 3250)")
# con.commit()

# def font_color(amount):
#     if amount >= 0:
#         return "green"
#     else:
#         return "red"

def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=500&convert=USD&CMC_PRO_API_KEY=16678e0d-1685-4e32-8abc-af74a679610e")

    api = json.loads(api_request.content)

    cursorObj.execute("SELECT * FROM coin")
    coins = cursorObj.fetchall()

    def font_color(amount):
        if amount >= 0:
            return "green"
        else:
            return "red"


    coins = [
        {
            "symbol": "BTC",
            "amount_owned": 2,
            "price_per_coin": 9500
        },
        {
            "symbol": "ETH",
            "amount_owned": 5,
            "price_per_coin": 695
        },
        {
            "symbol": "EOS",
            "amount_owned": 95,
            "price_per_coin": 2.05
        },
        {
            "symbol": "LTC",
            "amount_owned": 75,
            "price_per_coin": 25
        },
        {
            "symbol": "XMR",
            "amount_owned": 10,
            "price_per_coin": 40.05
        }
    ]

    total_pl = 0
    coin_row = 1
    total_current_value = 0
    total_amount_paid = 0

    for i in range(0, 500):
        for coin in coins:
            if api["data"][i]coin[1] == coin[1]:
                total_paid = coin[2] * coin[3]
                current_value = coin[2] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_pl_coin = pl_percoin * coin[2]

                total_pl += total_pl_coin
                total_current_value += current_value
                total_amount_paid += total_paid


                name = Label(pycrypto, text=api["data"][i]coin[1], bg="#F3F4F6", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrypto, text="${0:.4f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                no_coins = Label(pycrypto, text=coin[2], bg="#F3F4F6", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
                no_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text="${0:.4f}".format(total_paid), bg="#F3F4F6", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_val = Label(pycrypto, text="${0:.4f}".format(current_value), bg="#F3F4F6", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
                current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_coin = Label(pycrypto, text="${0:.4f}".format(pl_percoin), bg="#F3F4F6", fg=font_color(float("{0:.4f}".format(pl_percoin))), font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                totalpl = Label(pycrypto, text="${0:.4f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:.4f}".format(total_pl))), font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
                totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row += 1

    totalap = Label(pycrypto, text="${0:.4f}".format(total_amount_paid), bg="gray", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
    totalap.grid(row=coin_row, column=3, sticky=N + S + E + W)

    totalcv = Label(pycrypto, text="${0:.4f}".format(total_current_value), bg="gray", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
    totalcv.grid(row=coin_row, column=4, sticky=N + S + E + W)

    totalpl = Label(pycrypto, text="${0:.4f}".format(total_pl), bg="gray", fg="black", font="Lato 11", padx="5", pady="5", borderwidth=2, relief="groove")
    totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

    api = ""

    refresh = Button(pycrypto, text="Refresh", bg="aqua", fg="black", command=my_portfolio , font="Lato 12", padx="5", pady="5", borderwidth=2, relief="groove")
    refresh.grid(row=coin_row + 1, column=6, sticky=N + S + E + W)


def app_header():
    name = Label(pycrypto, text="Coin Name", bg="#142E54", fg="White", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=0, sticky=N+S+E+W)

    price = Label(pycrypto, text="Price", bg="#142E54", fg="White", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    price.grid(row=0, column=1, sticky=N+S+E+W)

    no_coins = Label(pycrypto, text="Coin Owned", bg="#142E54", fg="White", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    no_coins.grid(row=0, column=2, sticky=N+S+E+W)

    amount_paid = Label(pycrypto, text="Total Amount Paid", bg="#142E54", fg="White", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

    current_val = Label(pycrypto, text="Current Value", bg="#142E54", fg="White", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    current_val.grid(row=0, column=4, sticky=N+S+E+W)

    pl_coin = Label(pycrypto, text="P/L Per Coin", bg="#142E54", fg="White", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

    totalpl = Label(pycrypto, text="Total P/L With Coin", bg="#142E54", fg="White", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    totalpl.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()

print("Program Completed")

cursorObj.close()
con.close()