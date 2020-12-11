import json

rate = {
    "usd": {
        "value": 1,
        "notation": 'us dollars'
    },
    "gbp": {
        "value": 0.75,
        "notation": 'pound sterling'
    },
    "inr": {
        "value": 73.66,
        "notation": 'Rupees'
    },
    "eur": {
        "value": 0.85,
        "notation": 'euros'
    },
    "aud": {
        "value": 1.33,
        "notation": 'Australian Pound'
    },
    "jpy": {
        "value": 112.63,
        "notation": 'yen'
    },
    "swi": {
        "value": 0.88,
        "notation": 'Swiss Franc'
    },
    "nzd": {
        "value": 1.41,
        "notation": 'New Zealand Dollars'
    },
    "zar": {
        "value": 13.77,
        "notation": 'Rand'
    },
    "sgd": {
        "value": 1.34,
        "notation": 'Singapore Dollar'
    },
    "bdt": {
        "value": 84.79,
        "notation": 'Bangladeshi Taka'
    },
    "brl": {
        "value": 5.17,
        "notation": 'Brazilian Real'
    },
    "hkd": {
        "value": 7.75,
        "notation": 'Hong Kong Dollar'
    },
    "irr": {
        "value": 42000.00,
        "notation": 'Iranian Rial'
    },
    "xau": {
        "value": 0.00544,
        "notation": 'Gold'
    },
    "xag": {
        "value": 0.0417,
        "notation": 'silver'
    },
    "sek": {
        "value": 8.12,
        "notation": 'krona'
    }
}
AQuery = {
    'CV': '',
    'from': '',
    'to': ''
}
result = ''
print("Welcome to the currency conversion platform ")
userInput = input("Enter the query : ").lower()
splittedInput = userInput.split(" ")
AQuery['CV'] = float(splittedInput[0])
AQuery['from'] = str(splittedInput[1])
AQuery['to'] = str(splittedInput[3])
if(AQuery['from'] in rate.keys() and AQuery['to'] in rate.keys()):
    if AQuery['to'] == 'usd':
        result = AQuery['CV'] / rate[AQuery['from']]['value']
    else:
        result = (AQuery['CV'] / rate[AQuery['from']] ['value'])*rate[AQuery['to']] ['value']

    print(rate[AQuery ['to']] ['notation'] + "%.5f " % result )

else:
    print("Please enter the correct format, example: 400 usd to inr")
