from tda import auth, client
#from tda.orders import EquityOrderBuilder, Duration, Session
import config
import datetime
import json


def requestOptionChain():       
 
    # Ticker Symbol
    print("\n")
    ticker = input("Enter Ticker: ")
    
    # Call or Put
    while True:
        contractType = input("Enter the Contract Type (C/P): ")          
        if contractType == 'C':
            break
        if contractType == 'P':
            break
        print("Incorrect Entry \n")


    # Strike Price
    strikePrice = input("Enter The Strike Price: ")
    
    # Expiration Date 
    while True:   
        contractExpirationDate = input("Enter The Expiration contract expiration Date (MM-DD-YY): ")
        if len(contractExpirationDate) == 8:
            break
        print("Incorrect Entry \n")  
        
    dateFormatted = contractExpirationDate.replace('-','')    
    
    mm = dateFormatted[0] + dateFormatted[1]
    dd = dateFormatted[2] + dateFormatted[3]
    yy = dateFormatted[4] + dateFormatted[5]
    
    m = int(mm)
    d = int(dd)
    y = int(yy) + 2000
    
    expDate = datetime.date(year = y, month = m, day = d) 
   
    optionChainPrint(ticker,contractType,strikePrice,expDate)    
    
#_____________________________________________________________________________________________________________________________________________________

# PRINT OPTION CHAIN FUNCTION 
   
def optionChainPrint(ticker,contractType,strikePrice,expDate):
    
    currentDate = datetime.date(year = 2021, month = 11, day = 30)
    
    # IF YOU WANT ONLY 1 CONTRACT
    currentDate = expDate
    
    if contractType == 'C' :

        response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.CALL, strike=strikePrice, from_date = currentDate, to_date = expDate)
        
        text = json.dumps(response.json())
        
        with open ('chainData.json','w') as f:
            chainData = json.loads(text)
            json.dump(chainData,f)
        
              
        #normalDistribution1(chainData)
        #print(json.dumps(response.json(), indent=4))  

    elif contractType == 'P':
        
        response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.PUT, strike=strikePrice, from_date = currentDate, to_date = expDate)

        print(json.dumps(response.json(), indent=4))
        
#______________________________________________________________________________________________________________________________________________________     
        
#def normalDistribution1(chainData):    
    


#def normalDistribution2():    
    
    
#______________________________________________________________________________________________________________________________________________________

try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path = config.chromedriver_path)as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

requestOptionChain()   