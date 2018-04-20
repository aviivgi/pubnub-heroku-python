from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import sys
from numpy import random
import random as rand
import pprint
import uuid
 
PUBKEY = "demo"
SUBKEY = "demo"
CHANNEL = "myHerokuDemo"

pnconfig = PNConfiguration()
pnconfig.subscribe_key = SUBKEY
pnconfig.publish_key = PUBKEY

def populateBidData():
	data = {}
	data["order_quantity"] = rand.randint(50, 1000)
	data["timestamp"] = int(time.time())
	return data;

def my_publish_callback(envelope, status):
  # Check whether request successfully completed or not
  if not status.is_error():
    # pass  # Message successfully published to specified channel.
    print("PUBLISHED...")

  else:
    pass  # Handle message publish error. Check 'category' property to find out possible issue
    # because of which request did fail.
    # Request can be resent using: [status retry];

if __name__ == "__main__":
  pubnub = PubNub(pnconfig)
  while True:
    data = populateBidData()
    pubnub.publish().channel(CHANNEL).message(data).async(my_publish_callback)
    time.sleep(0.25)