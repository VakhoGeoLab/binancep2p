import json
import requests
from pprint import pprint
from tabulate import tabulate
from prettytable import PrettyTable
import statistics
import telebot
import os

from flask import Flask
app = Flask(__name__)

@app.route("/execute", methods=["GET"])
def execute_code():
  # Replace with your bot token
  bot_token = "6922311688:AAFyqle7xAbVHBjtk_weoP06cMILNpoLfOY"

  # Replace with your Telegram group chat ID
  group_chat_id = "-1002014364460"

  # Create a Telegram bot instance
  bot = telebot.TeleBot(bot_token)


  url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

  sell_payload = json.dumps({
    "fiat": "GEL",
    "page": 1,
    "rows": 3,
    "transAmount": "5000",
    "tradeType": "SELL",
    "asset": "USDT",
    "countries": [],
    "proMerchantAds": False,
    "proMerchantAds": False,
    "shieldMerchantAds": False,
    "filterType": "all",
    "periods": [],
    "additionalKycVerifyFilter": 0,
    "publisherType": None,
    "payTypes": [],
    "classifies": [
      "mass",
      "profession",
      "fiat_trade"
    ]
  })


  buy_payload = json.dumps({
    "fiat": "GEL",
    "page": 1,
    "rows": 3,
    "transAmount": "5000",
    "tradeType": "buy",
    "asset": "USDT",
    "countries": [],
    "proMerchantAds": False,
    "proMerchantAds": False,
    "shieldMerchantAds": False,
    "filterType": "all",
    "periods": [],
    "additionalKycVerifyFilter": 0,
    "publisherType": None,
    "payTypes": [],
    "classifies": [
      "mass",
      "profession",
      "fiat_trade"
    ]
  })




  headers = {
    'sec-ch-ua-platform': '"macOS"',
    'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
    'lang': 'en',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'FVIDEO-ID': '3143bd8dec73a8c582bfe70122b0b0fd312d35b8',
    'BNC-UUID': '21b6fb5e-a74e-4c4e-8fdb-74bc62c28ed0',
    'X-PASSTHROUGH-TOKEN': '',
    'Content-Type': 'application/json',
    'FVIDEO-TOKEN': 'G80Egz97XstR3VuiRTQjaSA1RPe5nq6UTrITTlCrt97ygYjYLuDp6vniqKXuruxur63bPnnlerOrWc8pydAOZIsvF9h20B/wAVLk0v4Fp4RWbeRSKbKqx3PlpJQbqbLmpVDhrEx1uPOPEQ7itsej89CDhfZjOvEbLHReIiq8Ih+DeWb7oBYdm08iyY4toE/hE=0e',
    'X-TRACE-ID': 'f5ff4e5e-a798-4b42-9c71-c20285fe13bb',
    'c2ctype': 'c2c_web',
    'X-UI-REQUEST-TRACE': 'f5ff4e5e-a798-4b42-9c71-c20285fe13bb',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'clienttype': 'web',
    'BNC-Location': 'BINANCE',
    'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE2ODAsMTA1MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE2ODAsMTAyNSIsInN5c3RlbV92ZXJzaW9uIjoiTWFjIE9TIDEwLjE1LjciLCJicmFuZF9tb2RlbCI6InVua25vd24iLCJzeXN0ZW1fbGFuZyI6ImVuLVVTIiwidGltZXpvbmUiOiJHTVQrMDQ6MDAiLCJ0aW1lem9uZU9mZnNldCI6LTI0MCwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzAuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImxpc3RfcGx1Z2luIjoiUERGIFZpZXdlcixDaHJvbWUgUERGIFZpZXdlcixDaHJvbWl1bSBQREYgVmlld2VyLE1pY3Jvc29mdCBFZGdlIFBERiBWaWV3ZXIsV2ViS2l0IGJ1aWx0LWluIFBERiIsImNhbnZhc19jb2RlIjoiMmVlMWVmZjUiLCJ3ZWJnbF92ZW5kb3IiOiJHb29nbGUgSW5jLiAoSW50ZWwpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoSW50ZWwsIEFOR0xFIE1ldGFsIFJlbmRlcmVyOiBJbnRlbChSKSBJcmlzKFRNKSBQbHVzIEdyYXBoaWNzIDY1MCwgVW5zcGVjaWZpZWQgVmVyc2lvbikiLCJhdWRpbyI6IjEyNC4wNDM0NzY1NzgwODEwMyIsInBsYXRmb3JtIjoiTWFjSW50ZWwiLCJ3ZWJfdGltZXpvbmUiOiJBc2lhL1RiaWxpc2kiLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWMTMwLjAuMC4wIChNYWMgT1MpIiwiZmluZ2VycHJpbnQiOiI1ZTM3NWNkMjg1OTZhZTc3YmYzZDY5OGJjMjcwNWFiMCIsImRldmljZV9pZCI6IiIsInJlbGF0ZWRfZGV2aWNlX2lkcyI6IjE2NzUzMjYxNzA4MzI3RmZsU1pSSkZtODIyYXdQM2Y5LCJ9',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'host': 'p2p.binance.com'
  }

  # Create a list to store the extracted data
  table_data_sell = []
  table_data_buy = []

  response = requests.request("POST", url, headers=headers, data=sell_payload)
  # print(response.text)
  try:
    data = response.json()
  except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    data = {"data": []}


  # Extract desired fields from the JSON response
  count = 1
  for item in data["data"]:
      nick_name = item["advertiser"]["nickName"][:10]
      price = item["adv"]["price"]
      asset = item["adv"]["asset"]
      fiat_unit = item["adv"]["fiatUnit"]
      trade_method_name = item["adv"]["tradeMethods"][0]["tradeMethodName"]
      tradable_quantity = item["adv"]["tradableQuantity"]
      #print(count, item, "\n")

      # Add a row to the table data list for each item
      table_data_sell.append([count, nick_name, price, asset, fiat_unit, trade_method_name, tradable_quantity])
      count = count + 1

  # Format the table data as a string
  sell_table_str = tabulate(table_data_sell, headers=["<b>N</b>", "<b>Nickname</b>", "<b>Price</b>", "<b>Asset</b>", "<b>Fiat</b>", "<b>Bank</b>", "<b>Quantity</b>"], tablefmt="plain")


  response = requests.request("POST", url, headers=headers, data=buy_payload)
  print(response.text)
  try:
    data = response.json()
  except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    data = {"data": []}


  # Extract desired fields from the JSON response
  count = 1
  for item in data["data"]:
      nick_name = item["advertiser"]["nickName"][:10]
      price = item["adv"]["price"]
      asset = item["adv"]["asset"]
      fiat_unit = item["adv"]["fiatUnit"]
      trade_method_name = item["adv"]["tradeMethods"][0]["tradeMethodName"]
      tradable_quantity = item["adv"]["tradableQuantity"]
      #print(count, item, "\n")

      # Add a row to the table data list for each item
      table_data_buy.append([count, nick_name, price, asset, fiat_unit, trade_method_name, tradable_quantity])
      count = count + 1

  # Format the table data as a string
  buy_table_str = tabulate(table_data_buy, headers=["<b>N</b>", "<b>Nickname</b>", "<b>Price</b>", "<b>Asset</b>", "<b>Fiat</b>", "<b>Bank</b>", "<b>Quantity</b>"], tablefmt="plain")


  # SENDING THE MESSAGE

  # Differentiator Message
  text_message = "<b>BINANCE USDT-GEL P2P</b>"

  # Send a message
  bot.send_message(group_chat_id, text_message + "\n" + "<b>SELL</b>\n" + sell_table_str + "\n\n" + "<b>BUY</b>\n" + buy_table_str, parse_mode='HTML')
    # Place your code logic here
    # Remove or adjust any infinite loops or non-HTTP handling logic


  
  return "Code executed successfully!"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)







