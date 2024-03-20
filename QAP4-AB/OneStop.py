# Description: Program to enter and calculate customers policy claims.
# Author: Allison Boone
# Date: March 14, 2024 - March 20, 2024

# Define required libraries.
import FormatValues as FV
import datetime
import sys
import time

# Define program constants.
POLICY_NUM = 1944

BASIC_PREMIUM = 869.00
DIS_ADD_CAR = 0.25

COST_EX_LIA_COV = 130.00
COST_GL_COV = 86.00
COST_LOAN_CAR_COV = 58.00

HST_RATE = 0.15
MONTHLY_PROCESS_FEE = 39.99

CUR_DATE = datetime.datetime.now()

# Define program functions.
# Function to validate the province in a list.
def ValProv(Province):
    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "SK", "MB", "AB", "BC", "NT", "YT", "NV"]
    if Province in ProvLst:
        return True
    else:
        return False
    
# Function to calculate the monthly payment cost.   
def CalcMonthPayment(TotalCost, DownPayment = 0):
    if DownPayment:
        MonthlyDue = TotalCost - DownPayment
    else:
        MonthlyDue = TotalCost

    MonthlyPayment = (MonthlyDue + MONTHLY_PROCESS_FEE) / 8 
    return MonthlyPayment

# Function to calculate the extra costs.
def CalcExtraCosts(LiaCoverage, GlCoverage, LoanerCoverage):
    AddExtraCosts = 0
    if LiaCoverage == "Y":
        AddExtraCosts += COST_EX_LIA_COV * NumCarIns

    if GlCoverage == "Y":
        AddExtraCosts += COST_GL_COV * NumCarIns

    if LoanerCoverage == "Y":
        AddExtraCosts += COST_LOAN_CAR_COV * NumCarIns

    return AddExtraCosts

# Define Counters.
PolicyNumCtr = 1943
    
# Main program starts here.
AllowChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
AllowNum = set("1234567890")
while True:
    # Gather user inputs.
    while True: 
        CustFirstName = input("Enter the customers first name: ").title()
        if CustFirstName == "":
            print("Error - Customer first name cannot be blank.")
        else:
            break

    while True:
        CustLastName = input("Enter the customers last name: ")
        if CustLastName == "":
            print("Error - Customer last name cannot be blank.")
        else:
            break

    while True:
        StAdd = input("Enter the customers street address: ").title()
        if StAdd == "":
            print("Error - Street address cannot be blank.")
        else:
            break
    
    while True:
        City = input("Enter the customers city address: ").title()
        if City == "":
            print("Error - City cannot be blank.")
        else:
            break

    while True:
        Province = input("Enter the customers province (XX): ").upper()
        if Province == "":
            print("Error - Province cannot be blank.")
        elif ValProv(Province) == False:
            print("Error - Must be valid 2 character province.")
        else:
            break

    while True:
        PostalCode = input("Enter the customers postalcode (X9X9X9): ").upper()
        if PostalCode == "":
            print("Error - Postal code cannot be blank.")
        elif (len(PostalCode)) != 6:
            print("Error - Postal Code must be 6 characters.")
        else:
            break

    while True:
        PhNum = input ("Enter the customers phone number (9999999999): ")
        if PhNum == "":
            print("Error - Phone number cannot be blank.")
        elif (len(PhNum)) != 10:
            print("Error - Phone number must consist of 10 numbers.")
        elif set(PhNum).issubset(AllowNum) == False:
            print("Error - Phone number must be digits.")
        else:
            break

    while True:
        NumCarIns = input("Enter the number of cars being insured (99): ")
        NumCarIns = int(NumCarIns)
        if NumCarIns == "":
            print("Error - Number of cars insured cannot be blank.")
        else:
            break
    
    LiaCoverage = input("Enter if the customer wants liability coverage (Y/N): ").upper()
    if LiaCoverage == "Y":
        LiaCoverageMsg = "YES"
    else:
        LiaCoverage == "N"
        LiaCoverageMsg = "NO"

    GlCoverage = input("Enter if customer wants glass coverage (Y/N): ").upper()
    if GlCoverage == "Y":
        GlCoverageMsg = "YES"
    else:
        GlCoverage == "N"
        GlCoverageMsg = "NO"

    LoanerCoverage = input("Enter if the customer wants loaner car (Y/N): ").upper()
    if LoanerCoverage == "Y":
        LoanerCoverageMsg = "YES"
    else:
        LoanerCoverage == "N"
        LoanerCoverageMsg = "NO"
       
    PayOptLst = ["F", "M", "D"]
    while True:
        PaymentOpt = input("Enter in customer wants to pay Full, Monthly or Downpayment (F/M/D): ").upper()
        if PaymentOpt == "D":
            DownPayment = input("Enter the downpayment amount: ")
            DownPayment = int(DownPayment)
            PaymentOptMsg = "Down Payment"
            break
        elif PaymentOpt == "M":
             DownPayment = 0
             PaymentOptMsg = "Monthly Payment"
             break
        else: 
            PaymentOpt == "F"
            DownPayment = 0
            PaymentOptMsg = "Full Payment"
            break
                
    Claims = []
    while True:
        ClaimNum = input("Enter the claim number: ")
        ClaimDate = input("Enter the claim Date (YYYY-MM-DD): ")
        ClaimAmount = input("Enter the claim amount: ")
        ClaimAmount = int(ClaimAmount)

        Claims.append((ClaimNum, ClaimDate, ClaimAmount))

        PrevClaim = input("Would you like to process another previous insurance claim? (Y/N): ").upper()
        if  PrevClaim == "Y":
            continue
        else:
            PrevClaim == "N"
            break

    # Store the claim data into a file called Claims.dat
    for _ in range(5):  
        print('Saving claim data ...', end='\r')
        time.sleep(.3) 
        sys.stdout.write('\033[2K\r')  
        time.sleep(.3)

    f = open("Claims.dat", "a")
 
    f.write("{}, ".format(str(ClaimNum)))
    f.write("{}, ".format(str(ClaimDate))) 
    f.write("{}\n".format(str(ClaimAmount)))

    PolicyNumCtr += 1

    f.close()
 
    print()
    print("Claim data successfully saved ...", end='\r')
    time.sleep(1)  
    sys.stdout.write('\033[2K\r')  

    # Perform required calculations.
    InsurancePremium = BASIC_PREMIUM + ((NumCarIns - 1) * DIS_ADD_CAR)
    AddExtraCosts = CalcExtraCosts(LiaCoverage, GlCoverage, LoanerCoverage)

    TotalInPremium = InsurancePremium + AddExtraCosts
    HST = TotalInPremium * HST_RATE

    TotalCost = TotalInPremium + HST

    MonthlyPayment = CalcMonthPayment(TotalCost, DownPayment)

    InvoiceDate = CUR_DATE

    PaymentMonth = CUR_DATE.month + 1
    PaymentYear = CUR_DATE.year
    if PaymentMonth > 12:
        PaymentMonth = 1
        PaymentYear += 1

    PaymentDate = datetime.datetime(year = PaymentYear, month = PaymentMonth, day = 1)
    
    # Display results.
    print()
    print(f"       One Stop Insurance Company")
    print(f"             Claim Receipt")
    print(f"-------------------------------------------")
    print(f"Policy Number: {PolicyNumCtr:>4d}  Issue Date: {FV.FDateS(CUR_DATE):<12s}")
    print(f"-------------------------------------------")
    print()
    print(f"Customer Name and Address: ")
    print()
    print(f"      {CustFirstName + " " + CustLastName:<20s}")
    print(f"      {StAdd:<20s}")
    print(f"      {City:<15s} , {Province:<2s} {PostalCode:<6s}")
    print()
    print(f"Customer Phone Number: ")
    print()
    print(f"      {PhNum:<10s}")
    print()
    print(f"Number of Cars Insured:       {NumCarIns:>3d}")
    print()
    print(f"Liability Coverage:           {LiaCoverageMsg:>3s}")
    print(f"Glass Coverage:               {GlCoverageMsg:>3s}")
    print(f"Loaner Car Coverage:          {LoanerCoverageMsg:>3s}")
    print()
    print(f"Payment Method:   {PaymentOptMsg:>15s}")
    print()
    print(f"Insurance Premium:      {FV.FDollar2(InsurancePremium):>9s}")
    print(f"Extra charges:          {FV.FDollar2(AddExtraCosts):>9s}")
    print(f"HST:                    {FV.FDollar2(HST):>9s}")
    print(f"                        ---------")
    print(f"Total Cost:             {FV.FDollar2(TotalCost):>9s}")
    print()
    print(f"Down Payment Amount:    {FV.FDollar2(DownPayment):>9s}")
    print(f"Processing Fee:         {FV.FDollar2(MONTHLY_PROCESS_FEE):>9s}")
    print(f"                        ---------")
    print(f"Monthly Payment Due:    {FV.FDollar2(MonthlyPayment):>9s}")
    print()
    print(f"Previous Claims: ")
    print()
    print(f"Claim #    Claim Date    Claim Amount")
    print(f"-------------------------------------")
    print(f"{FV.FormatClaimData(Claims):>10s}")
    print(f"Policy Claim has been Saved.")
    print(f"-------------------------------------------")
    print(f"Next Payment Due Date: {FV.FDateS(PaymentDate):<10s}")
    print(f"-------------------------------------------")
    print()
    
    # Any housekieeping duties at the end of the program.
    f = open('Claims.dat', 'w')
    f.write("{}\n".format(str(Claims)))
    f.close()

    AnotherClaim = input("Would you like to process another insurance claim? (Y/N): ").upper()
    if  AnotherClaim == "Y":
        continue
    else:
        AnotherClaim == "N"
        print("Thanks for using One Stop Insurance Company!")
        break
                
    
        
