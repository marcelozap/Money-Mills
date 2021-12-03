from os import EX_CANTCREAT
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
        contractexpDate = input("Enter The Expiration contract expiration Date (MM-DD-YY): ")
        if len(contractexpDate) == 8:
            break
        print("Incorrect Entry \n")  
    
    mm = contractexpDate[0] + contractexpDate[1]
    dd = contractexpDate[3] + contractexpDate[4]
    yy = contractexpDate[6] + contractexpDate[7]
    
    expDate = datetime.date(year = int(yy)+2000, month = int(mm), day = int(dd)) 

    #Calculate days reminainig for expiration date
    daysRemaining = expDate.day - datetime.datetime.now().day

    formatDate = str(expDate.year) + "-" + str(expDate.month) + "-" + str(expDate.day) + ":" + str(daysRemaining)
   
    optionChainPrint(ticker,contractType,strikePrice,expDate,formatDate)    

    #2021-12-23:20
#_____________________________________________________________________________________________________________________________________________________

class searchTools:
  def __init__(search, strike, date, file):
    search.file = file
    search.strike = strike
    search.date = date

# PRINT OPTION CHAIN FUNCTION 
   
def optionChainPrint(ticker,contractType,strikePrice,expDate,formatDate):

    #Set up Formats to insert into function
    strikePrice = float(strikePrice)
    strStrikePrice = str(strikePrice)





    # FOR SAMPLE RUN
    if contractType == 'C' :

        response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.CALL, strike=strikePrice, from_date = expDate, to_date = expDate)   
        
        text = json.dumps(response.json())
        chainData = json.loads(text)

        #SearchTools makes it easier to find information
        s = searchTools(strStrikePrice,formatDate,chainData)    

        print(getValue(s,'bid'))

    elif contractType == 'P':
        
        response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.PUT, strike=strikePrice, from_date = expDate, to_date = expDate)
        
        text = json.dumps(response.json())
        chainData = json.loads(text)   

        s = searchTools(strStrikePrice,formatDate,chainData)  

        print(getValue(s,'bid'))    
        
#______________________________________________________________________________________________________________________________________________________     


#def setVariableValues(chainData,strStrikePrice,formatDate):

        # SET ALL VARIABLES NEEDE DFOR EQUAITON HERE

def getValue(s,keyWord):
        return s.file['callExpDateMap'][s.date][s.strike][0][keyWord]     

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