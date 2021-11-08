from tda import auth, client
#from tda.orders import EquityOrderBuilder, Duration, Session
import config
import datetime
import json


# authenticate


try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path = config.chromedriver_path)as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)



# get price history for a symbol
#r = c.get_price_history('TSLA',
#        period_type=client.Client.PriceHistory.PeriodType.YEAR,
#        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#        frequency=client.Client.PriceHistory.Frequency.DAILY)

#assert r.ok, r.raise_for_status()

#print(json.dumps(r.json(), indent=4))




ticker = input("Enter Ticker: ")

print("\n")

contractType = input("Enter Contract Type (C/P): ")

print("\n")

strikePrice = input("Enter The Strike Price: ")

#print("\n")

#GOOG_012122P620: GOOG Jan 21 2022 620 Put

#expiration = input("Enter the Contract expiration date (MM-DD-YY): ")


#to_date = expiration[0] +expiration_date[1] +expiration_date[3] +expiration_date[4] +expiration_date[6] +expiration_date[7]

#correctInput = ticker+ '_' + dateFormat + contractType + strikePrice

#print(correctInput)

print("\n")

#response = c.get_option_chain(ticker,contract_type = contractType, strike = strikePrice, to_date = dateFormat)

#response = c.get_option_chain(ticker)

if contractType == 'C' :

   response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.CALL, strike=strikePrice)

print(json.dumps(response.json(), indent=4))

#if contractType == 'P' :

#response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.PUT, strike=strikePrice)
    
#print(json.dumps(response.json(), indent=4))

#if contractType == 'ALL':

    #response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.ALL, strike=strikePrice)
    
#print(json.dumps(response.json(), indent=4))