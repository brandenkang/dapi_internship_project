#The JSON file I shared with you contains the transaction history of a bank account. 
#The project is to take this history and categorize it into different categories like food, hotel, transportation, etc.
import json

# read file
with open('TransactionHistory.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)

food, foodTotal = [],0
hotel, hotelTotal = [],0 
petrol, petrolTotal = [],0 
taxi, taxiTotal = [],0
visa, visaTotal = [],0 
etisalat, etisalatTotal = [],0
cstore, cstoreTotal = [],0
inwardCreditTransfer, inwardTotal = [],0 
outwardDebitTransfer, outwardTotal = [],0
accountTransfer, accountTransferTotal = [],0
miscFeesandCharges, feesOrChargesTotal = [],0 
tax, taxTotal = [],0
miscPayments, miscTotal = [],0 #Pink Pepper Photo, Abu Dhabi Global Market, Google XGSuite, Digital Ocean

#current object in transactions list 
for count, description in enumerate(obj['transactions']):
    curr = obj['transactions'][count] 
    if "Zomato" in curr['description'] or "SHAKESHACK" in curr['description'] or "CAFE" in curr['description']: 
        food.append(curr)
        foodTotal += int(curr["amount"])
    elif "HOTEL" in curr['description']:
        hotel.append(curr)
        hotelTotal += int(curr["amount"])
    elif "MARAT-HASSA-4855" in curr['description']: 
        petrol.append(curr) 
        petrolTotal += int(curr["amount"])
    elif "TAXI" in curr['description']: 
        taxi.append(curr)
        taxiTotal += int(curr["amount"])
    elif "EMBASSY" in curr['description']: 
        visa.append(curr)
        visaTotal += int(curr["amount"])
    elif "Etisalat" in curr['description']: 
        etisalat.append(curr) 
        etisalatTotal += int(curr["amount"])
    elif "CSTORE" in curr['description']: 
        cstore.append(curr) 
        cstoreTotal += int(curr["amount"])
    elif "Inward" in curr['description']: 
        inwardCreditTransfer.append(curr)
        inwardTotal += int(curr["amount"])
    elif "Outward" in curr['description']: 
        outwardDebitTransfer.append(curr)
        outwardTotal += int(curr["amount"])
    elif "Account Transfer Charges" in curr['description']: 
        accountTransfer.append(curr)
        accountTransferTotal += int(curr["amount"])
    elif "Fees or Charges" in curr['description']: 
        miscFeesandCharges.append(curr)
        feesOrChargesTotal += float(curr["amount"])
    elif "Tax" in curr['description']: 
        tax.append(curr)
        taxTotal += int(curr["amount"])
    else: 
        miscPayments.append(curr)
        miscTotal += int(curr["amount"])

def main():

    print("Here's the categorized list of transactions for Job ID: 130d3a70-13a9-47ce-b28b-489a01831209.\n")
    while True: 
        print(" Food | Hotel | Petrol | Taxi \n Visa | Etisalat | Convenience | Credit Transfer \n Debit Transfer | Tax | Misc. Fees | Misc. Charges")
        val = input("Please select a category to view relevant transactions.")

        if val == "Food" or val == "food": 
            print("Here's the summary of transactions regarding food:")
            for i in food: 
                print (i)
            print("Total spent:")
            print(foodTotal) 

        elif val == "Hotel" or val == "hotel": 
            print("Here's the summary of transactions regarding hotels:")
            for i in hotel: 
                print (i)
            print("Total spent:")
            print(hotelTotal) 

        elif val == "Petrol" or val == "petrol": 
            print("Here's the summary of transactions regarding petrol:")
            for i in petrol: 
                print (i)
            print("Total spent:")
            print(petrolTotal) 

        elif val == "Taxi" or val == "taxi": 
            print("Here's the summary of transactions regarding taxis:")
            for i in taxi: 
                print (i)
            print("Total spent:")
            print(taxiTotal) 

        elif val == "Visa" or val == "visa": 
            print("Here's the summary of transactions regarding visa:")
            for i in visa: 
                print (i)
            print("Total spent:")
            print(visaTotal) 

        elif val == "Etisalat" or val == "etisalat": 
            print("Here's the summary of transactions regarding etisalat:")
            for i in etisalat: 
                print (i)
            print("Total spent:")
            print(etisalatTotal) 

        elif val == "Convenience" or val == "convenience": 
            print("Here's the summary of transactions regarding convenience stores:")
            for i in cstore: 
                print (i)
            print("Total spent:")
            print(cstoreTotal) 

        elif val == "Credit Transfer" or val == "credit transfer" or val == "Credit transfer": 
            print("Here's the summary of transactions regarding inward credit transfers:")
            for i in inwardCreditTransfer: 
                print (i)
            print("Total received:")
            print(inwardTotal) 

        elif val == "Debit Transfer" or val == "Debit transfer" or val == "debit transfer": 
            print("Here's the summary of transactions regarding outward debit transfers:")
            for i in outwardDebitTransfer: 
                print (i)
            print("Total sent:")
            print(outwardTotal) 

        elif val == "Tax" or val == "tax": 
            print("Here's the summary of transactions regarding taxes:")
            for i in tax: 
                print (i)
            print("Total spent:")
            print(taxTotal) 

        elif val == "Misc. Fees" or val == "misc. fees": 
            print("Here's the summary of transactions regarding account miscellaneous fees and charges:")
            for i in miscFeesandCharges: 
                print (i)
            print("Total spent:")
            print(feesOrChargesTotal) 

        elif val == "Misc. Charges" or val == "misc. charges": 
            print("Here's the summary of transactions regarding miscellaneous payments:")
            for i in miscPayments: 
                print (i)
            print("Total spent:")
            print(miscTotal) 

main()
