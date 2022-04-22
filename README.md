# Twitter Bot for Dublin Port Tides

## Setting Up
You will need a `credentials.py` file that looks something like:

```
access_token = '15CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCxy'
access_token_secret = 'gcJCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCRC'

api_key = "tuCCCCCCCCCCCCCCCyK"
api_key_secret = "IkCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC5rU1"
bearer_token = "AAAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCTGqPLEhhfIZiai"
```

## Maintenance
Every now and then go to:
  https://erddap.marine.ie/erddap/tabledap/IMI-TidePrediction.html

Download a `csv` with the latest predictions for "Dublin_Port" as far out as the interface will allow.
Then update `gethightides.py` to point to the downloaded file and rerun it.

![image](https://user-images.githubusercontent.com/58846/164282272-6012d3db-264e-47aa-bbfc-054e74adaa15.png)

