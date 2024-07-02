from tkinter import *
from PIL import ImageTk, Image

lst_antique = ['AN ANTIQUE RAJASTHANI GANGA JAMUNA HUKKAH', 'A HAND CARVED CAMPHOR CHEST',
               'AN EXCEPTIONALLY LARGE ANGLO-INDIAN ROSEWOOD WARDROBE',
               'A PAIR OF COLOURED ALABASTER EWERS ON PEDESTALS', 'SHIVA STATUE',
               'A LARGE CHINESE DISPLAY CABINET WITH MOTHER OF PEARL INLAY',
               "AN ANTIQUE SILVER ROSE WATER SPRINKLER SET"]
p_antique = [415000, 250000, 600000, 900000, 2000000, 700000, 1100000]
lst_property = ['SM Dyechem', 'Avinash Bhosale/Abeeys Realcon LLP', 'Ghanshyambhai Dholakia', ' JK Papers', 'Chandru',
                'Ravi and Neel Raheja']
p_property = [1036000000, 1038000000, 1850000000, 2530000000, 4270000000]
loc_property = ['Satellite Sesen', ' Malabar Hill.Mumbai', 'Satellite Sesen.Malabar Hill.Mumbai',
                'Panhar Bungalow.Worli', 'Prithviraj Road.Delhi', 'Raheja Artesia.Worli.Mumbai']
lst_cd = ['Air Conditioners-8', 'iPhone 13 Pro-31', 'Marshall speaker-12', 'Adidas shoes-340', 'Electric bicycle-9',
          'Men jackets-80']
p_cd = [120000, 90000, 190000, 180000, 53800, 75000]
lst_no = ['LC 200-0001', 'RJ 45 CG 1', 'KL 01 CK 1', 'GJ 01 WA 007', 'RJ 14 CP 0001', 'KL 01 CB 0001']
p_no = [1700000, 1600000, 3100000, 3400000, 1030000, 1800000]
name = []
pno = []
address = []
email = []
d_property = ['''A speciality chemicals manufacturer that has strong 
connections to the packaged foods industry, SM Dyechem was founded 
in 1982 by SM Shetty and has recently purchased a 51st and 52nd floor 
duplex, registered for ownership back in May 2021.''', '''Another investment in the high-end Malabar Hill property
 came from well-known industrialist Bhosale, who cleared a similar duplex 
 sale to SM Dyechem by paying a slight premium for locating their
  purchase on the 53rd and 54th floor.''', '''One of Surat's most prominent diamond merchants, 
  Dholakia purchased the massive six-storey 19,886 square-feet property 
  through his company, Harkrishna Exports Pvt. Ltd. The merchant's elder
   brother, Savji Dholakia, stated that the bungalow was meant as a 
   long-term residence for their large joint family.''', '''This December-2021 deal saw JK Paper's director, 
   Amar Singh Mehta, purchase the 11,193 square-feet bungalow from Bhai 
   Manjit Singh and Vikramjit Singh, both of whom have familial ties to 
   the pharmaceutical giant, Ranbaxy Laboratories''', '''Another instance of a sale within Raheja's coveted 
   Artesia project, this immense 66,800 square feet purchase is one of
    the largest single real estate deals to have substantiated in Mumbai.
     The three promoters and their wives own three duplexes across the
      41st and 45th floors, and have also attained a massive 42 car 
      parking slots as a result.''']
d_cd = ['''1)Imported from Japan
2)Company-Hitachi
3)Star rating-5
4)Capacity-1.5 tonne''', '''1)Imported from Canada
2)256 gb
3)All colors are there in lot''', '''1)Imported from US
2)80 watt''', '''1)Size- US 4 to US 11
2)Imported from Germany
3)Type -Sports and sneakers''', '''1)Size-22”
2)Imported from Italy
3)Type-Mountain bike''', '''1)Size- M-XXL
2)Imported from London''']
d_no = ['''1.)    LC 200-0001 :- 
In 2012, Jagjit Singh Chahal, owner of Chahal tyres in
 Chandigarh won a registration number CH-01AN-0001 for
  a whopping Rs 17 lakh for his Toyota Land Cruiser LC200 
  worth an estimated Rs 1 crore, the highest ever amount 
  for a new series number in the history of Chandigarh. 
  The auction for the new series was conducted by the Registration
   and Licensing Authority (RLA).''', '''2.) RJ 45 CG 1 :-
    Rahul Taneja is an owner of a wedding management company 
    called Live Creations who at an early age worked in a
     Dhaba for a few bucks and came into the headlines in
      2018 when he purchased Rs 16 lakh number plate
       RJ45 CG 001 for his brand new Rs 1.5 crore car.''', '''3.)    KL 01 CK 1 :
        K S Balagopal, a resident of Kowdiar, Thiruvananthapuram 
        is a proprietor of Devi Pharma, a leading pharmaceuticals
         distribution company had paid a fortune to get a fancy
          registration number for his blue Porsche 718 Boxster
           worth Rs 1 crore. In 2019, Balagopal won the 
           registration number ‘KL-01-CK-1’, for his brand-new 
           Miami Blue sports car by paying Rs 30 lakh in the auction
            held at the regional transport office (RTO)''', '''4.)   GJ 01 WA 007 :-
             In 2020, Ahmedabad-based transporter, Ashik Patel bought a 
             new SUV for Rs 39.5 lakh but you will be surprised to know 
             that he paid extra Rs 34 lakh for its number plate only. Yes,
              you read that right Ashik was granted vehicle registration 
              number GJ01WA007 for his Toyota Fortuner, and for his love
               for James Bond''', '''5.) RJ 14 CP 0001 :-
                Rahul Taneja owns a BMW 5-Series which he bought in 2011.
                 Rahul feels that number 1 is lucky for him. He paid
                  a huge sum of Rs. 10.3 lakhs to get the registration
                   number RJ 14 CP 0001 for his vehicle. He sold his 
                   5-series later on but retained the number which was
                    inherited by his 7-series later on. ''', '''6.)  KL 01 CB 0001 :-
                     Land Cruiser is owned by K.S. Balagopal from Thiruvananthapuram.
                      He spent Rs 18 lakhs for buying the registration number
                       KL 01 CB 0001. He bought this number for his car back in
                        2017 and has a lot more luxury cars in his garage with 
                        VIP number plates as well!''']
d_antique = ['''1.)   AN ANTIQUE RAJASTHANI GANGA JAMUNA HUKKAH:-
  A bell shaped partial gilt hukkah, the gilt body with stylised
   petal flutes resting on a twisted cord design. The chillum has
    pierced acanthus leaves and bird motifs and a similarly 
    pierced lid.This lot is over one hundred years old or
     National Art Treasure, cannot be exported out of India as
      per Antiques and Art Treasures Act, 1972.
Gross Weight : 2.966 kgs
Size : 21.5 x 7 x 7 in not including smoking pipe
''', '''2.)  A HAND CARVED CAMPHOR CHEST:-
 A rectangular, camphorwood chest. The lot depicts detailed carvings 
 featuring distinct oriental motifs that include figurative
  and floral designs on five sides. Secured with a decorative
   brass pad-lock. The unit rests on four feet.

This lot is over one hundred years old or National Art Treasure,
 cannot be exported out of India as per Antiques and Art Treasures Act, 1972.
Size : 23 x 41 x 20.5 in
Medium : Camphorwood''', '''3.)  AN EXCEPTIONALLY LARGE ANGLO-INDIAN ROSEWOOD WARDROBE:- 
 Featuring four large exquisitely pierced front doors, enclosing
  three separate compartments. The wardrobe has a finely pierced, 
  detachable pediment top. The whole unit rests on well-proportioned
   animal claw feet.

Property from the Estate of Muncherji N Cama.

This lot is over one hundred years old or National Art Treasure,
 cannot be exported out of India as per Antiques and Art Treasures Act, 1972.) 
 Size : 94 x 98 x 22 in
Medium : Rosewood''', '''4.) A PAIR OF COLOURED ALABASTER EWERS ON PEDESTALS:- 
The presented lot showcases a pair of elegantly crafted alabaster ewers 
with a carved spout and stylized handles in scroll-design. The mid-sections
 and the base of the ewers are made of coloured alabaster which renders a 
 contrast to the design of the unit. The pedestals are made entirely of 
 coloured alabaster and have a circular stepped base.This lot is a set of 2.

This lot is over one hundred years old or National Art Treasure,
 cannot be exported out of India as per Antiques and Art Treasures Act, 1972.
Size : 87 x 13 x 12 in
Medium : Alabaster''', '''5.)    SHIVA STATUE:-
 This lot is a National Art Treasure - Non Exportable Item.
This lot is a registered antique with the Government of India, under the 
Antiquities and Art Treasures Act -1972, under Antiquities and Art Treasures
 Rule 1973, under section 16 of the above act, with the Archaeological Survey of India (ASI).
Provenance : From an important private collection based in Mumbai.
Originally sold by Natesans Antiqarts, Mumbai. Chera Dynasty, Kerala, 14 x 8 x 7.5 in, Bronze''', '''6.) A LARGE CHINESE DISPLAY CABINET WITH MOTHER OF PEARL INLAY:-
 The impressive display cabinet features exquisite carving, further 
 accentuated by the depicted Pagodas throughout the upper section. 
 The large central display unit is flanked by multiple smaller units on either side.
This lot is over one hundred years old or National Art Treasure, cannot be exported 
out of India as per Antiques and Art Treasures Act, 1972.
(Size : 115 x 67 x 20 in
Medium : Hardwood''', '''7.) AN ANTIQUE SILVER ROSE WATER SPRINKLER SET:-
 An unusual antique rose water sprinkler set from Rajasthan with two 
 imperial lions on a footed tray. This rare sprinkler set of royal silver
  is distinguished by the 2 original boxes that slot into the central
   receptacle. They are adorned with pierced shikar scenes against a foiled 
   background. This set with it's regal lions constitutes a rare variation
This lot is over one hundred years old or National Art Treasure, cannot be exported
out of India as per Antiques and Art Treasures Act, 1972.
Gross Weight : 2.171 kgs
Size : 9 x 13.5 x 11 in
''']


def bid1():
    print('''                   Welcome To BIDIT
          This is a Python based Biding Platform''')
    print('''                        
                      DISCLAMER
    Under no circumstances shall Bidder have any kind of claim 
    against BIDIT, Broker of record, or anyone else, if the 
    Bidder fails to reach the site then the company is not 
    responsible. Bidder(s) are encouraged to use the “Maximum
     Bid” feature on the bidding platform and lock in their 
     maximum bid amount if they are concerned about technology
    failure during the auction. The SELLER and/or Auction 
    Company reserves the right to (pause) the online auction 
    bidding in the event of any internal or external technology
    failure, to preserve the integrity of the auction event and
    maintain a fair and impartial bidding environment.''')
    e = input(("View terms and conditions  (T/F)"))
    if e.upper() == 'T':
        print('''1.)By submitting a proposal, each bidder shall be deemed
    to acknowledge that they have carefully read the entire invitation for bid,
    including all forms, schedules and annexure hereto and have fully informed 
    themselves as to all existing conditions and limitations.

    2.)The material for sale is categorized and the details are 
    given in the screen displayed at site.Material Description is indicative only.
    
    a.Bidders may inspect the material for sale, at least 1 day before start of Auction process, 
    in their own interest, and be informed about the same..
    
    b. By participating in Auction, the Bidder confirms to have fully informed themselves 
    regarding the physical condition of the material on offer. No complaint would be entertained 
    in respect of the same at any later stage

    3.)BIDIT reserves the right to withdraw at any time, any material in full or part, 
    without assigning any reason thereof. At the time of delivery if any material 
    found useful, can be withheld without assigning any reason thereof.

    4.)Successful bidders will be required to submit full amount of Security Deposit 
    to BIDIT, as indicated against each Lot, before the date of commencement of Tender. 
    
    i. Invoicing will start only after receipt of full security amount. 
    
    ii. The same shall be refunded within 4 weeks of successful completion of contract.
     No interest will be payable by BIDIT to the tenderer on the amount of the Security Deposit \n''')  # TERMS AND CONDITIONS


obj = bid1()
# def bid3():
print("Please select a category to list:")
print("1. Antique pieces")
print("2. Properties")
print("3. Custom Confiscated goods")
print("4. Fancy Car Registration No.")
category = int(input("Select Any One:\n"))
print("Thankyou")
print("Please select an item to bid for:")
if category == 1:
    for i in range(7):
        print(i + 1, '. ', lst_antique[i])
        print("Starting Price:", p_antique[i])
        print("The binding should be 5% above previous bid price")
elif category == 2:
    for i in range(5):
        print(i + 1, '. ', lst_property[i])
        print("Starting Price:", p_property[i])
        print("Location: ", loc_property[i])
        print("The binding should be 0.5% above previous bid price")
if category == 3:
    for i in range(6):
        print(i + 1, '. ', lst_cd[i])
        print("Starting Price:", p_cd[i])
        print("The binding should be 5% above previous bid price")
if category == 4:
    for i in range(6):
        print(i + 1, '. ', lst_no[i])
        print("Starting Price:", p_no[i])
        print("The binding should be 2% above previous bid price")
item = int(input("Item no.:"))
print("Details of Items")
if category == 1:
    print(d_antique[item - 1])
if category == 2:
    print(d_property[item - 1])
if category == 3:
    print(d_cd[item - 1])
if category == 4:
    print(d_no[item - 1])

# obj = bid1()
# obj=bid3()

# def bid2():
lst_namevalue = []
lst_phonevalue = []
lst_emailvalue = []
lst_gendervalue = []
lst_emergencyvalue = []
lst_paymentmodevalue = []

root = Tk()
root.title("BIDit")

image_0 = Image.open('Screenshot (63) - Copy.png')
bck_end = ImageTk.PhotoImage(image_0)
lbl = Label(root, image=bck_end)
lbl.place(x=0, y=0)

lbl2 = Label(root, text='Welcome to BIDit Auction', bg='black', fg="white", font=("comicsansms", 40, "bold"))
lbl2.pack(side=TOP, fill="x")


def getvals():
    for i in range(1):
        lst_namevalue.append(namevalue.get())
        lst_phonevalue.append(phonevalue.get())
        lst_emailvalue.append(emailvalue.get())
        lst_gendervalue.append(gendervalue.get())
        lst_emergencyvalue.append(emergencyvalue.get())
        lst_paymentmodevalue.append(paymentmodevalue.get())

    print(
        f"Name of Person:{namevalue.get()} \n Phone No.: {phonevalue.get()} \n Email: {emailvalue.get()} \n Gender: {gendervalue.get()} \n Emergency Contact: {emergencyvalue.get()} \n Payment Mode: {paymentmodevalue.get()}")
    if auctionservicevalue.get() == 1:
        print("Terms and Conditions Accepted")
    else:
        print("Terms and Conditions NOT Accepted")

    with open("records1.txt", "a") as hi:
        hi.write(
            f"Name of person: {namevalue.get()}, PhoneNo. : {phonevalue.get()}, Email: {emailvalue.get()}, Gender: {gendervalue.get()}, Emergency No. : {emergencyvalue.get()}, Payment Mode: {paymentmodevalue.get()}, {auctionservicevalue.get()}\n")


def tnc():
    print(
        "1. By submitting a proposal, each bidder shall be deemed to acknowledge that they have carefully read the entire invitation for bid, including all forms, schedules and annexure hereto and have fully informed themselves as to all existing conditions and limitations. \n 2. The material for sale is categorized and the details are given in the screen displayed at site.Material Description is indicative only. \n a.Bidders may inspect the material for sale, at least 1 day before start of Auction process, in their own interest, and be informed about the same.. \n b. By participating in Auction, the Bidder confirms to have fully informed themselves regarding the physical condition of the material on offer. No complaint would be entertained in respect of the same at any later stage \n 3. BIDIT reserves the right to withdraw at any time, any material in full or part, without assigning any reason thereof. At the time of delivery if any material found useful, can be withheld without assigning any reason thereof. \n 4. Successful bidders will be required to submit full amount of Security Deposit to BIDIT, as indicated against each Lot, before the date of commencement of Tender.  \n i. Invoicing will start only after receipt of full security amount.  \n ii. The same shall be refunded within 4 weeks of successful completion of contract. No interest will be payable by BIDIT to the tenderer on the amount of the Security Deposit \n 5. EMD must be remitted by RTGS / crossed Demand Draft, drawn in favour of BIDIT pvt. Limited, on any Indian scheduled Bank, payable at New Delhi. NO OTHER MODE OF PAYMENT WILL BE ACCEPTED.  \n i. The EMD of the unsuccessful bidders shall be refunded within 4-weeks after the award of the contract to the successful bidder(s). \n 6. This invitation to bid is not an offer and is issued with no commitment.BIDIT reserves the right to withdraw the invitation to bid and change or vary any part thereof at any stage. BIDIT also reserves the right to disqualify any bidder, should it be so necessary at any stage. \n 7. No oral conversations or agreements with any employee of BIDIT shall affect or modify any terms of this invitation for bid. \n 8. Timing and sequence of events resulting from this invitation to bid shall be determined by BIDIT")


root.geometry("1080x720")
root.maxsize(1980, 810)
root.minsize(300, 100)

f1 = Frame(root, bg="gray15", borderwidth=6, relief=SUNKEN)
f1.pack(side=RIGHT, padx=50)

Label(f1, text="Login Details        ", background='gray15', fg="lightgrey", font="comicsansms 25 bold", pady=15).grid(
    row=0, column=3)

name = Label(f1, text="Name", fg="lightgrey", background='gray15', font="comicsansms 13 bold", padx=10, pady=12)
phone = Label(f1, text="Phone", fg="lightgrey", background='gray15', font="comicsansms 13 bold", padx=10, pady=12)
email = Label(f1, text="Email", fg="lightgrey", background='gray15', font="comicsansms 13 bold", padx=10, pady=12)
gender = Label(f1, text="Gender", fg="lightgrey", background='gray15', font="comicsansms 13 bold", padx=10, pady=12)
emergency = Label(f1, text="Emergency Contact", fg="lightgrey", background='gray15', font="comicsansms 13 bold",
                  padx=10, pady=12)
paymentmode = Label(f1, text="Payment Mode", fg="lightgrey", background='gray15', font="comicsansms 13 bold", padx=10,
                    pady=12)

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
email.grid(row=3, column=2)
gender.grid(row=4, column=2)
emergency.grid(row=5, column=2)
paymentmode.grid(row=6, column=2)

namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
auctionservicevalue = IntVar()

nameentry = Entry(f1, textvariable=namevalue)
phoneentry = Entry(f1, textvariable=phonevalue)
emailentry = Entry(f1, textvariable=emailvalue)
genderentry = Entry(f1, textvariable=gendervalue)
emergencyentry = Entry(f1, textvariable=emergencyvalue)
paymentmodeentry = Entry(f1, textvariable=paymentmodevalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
emergencyentry.grid(row=5, column=3)
paymentmodeentry.grid(row=6, column=3)

auctionservice = Checkbutton(f1, text="I agree to the Terms and Conditions", variable=auctionservicevalue, fg="white",
                             background='gray15')
auctionservice.grid(row=7, column=3)

Button(f1, text="T&C", command=tnc, fg="lightgrey", background='gray15').grid(row=8, column=3)

Button(f1, text="Submit to BIDit", command=getvals, fg="white", background='grey', font="10").grid(row=9,
                                                                                                         column=2)

root.mainloop()
print(
    "Everyone please get ready with the sum \n ->  Everyone will get chance one by one \n ->  If you want to skip Enter 'skip' \n->   if everyone skips the bid last Bider will win the Biding")
print("Now, Starting the Biding.....")
if category == 1:
    price = p_antique[item - 1]
    margin = 5
if category == 2:
    price = (p_property[item - 1])
    margin = 0.5
if category == 3:
    price = (p_cd[item - 1])
    margin = 5
if category == 4:
    price = (p_no[item - 1])
    margin = 2
bidprice = price
maxname = ''
while len(lst_namevalue) > 0:
    #
    print("Now Biding at", price)
    i = 0
    length=len(lst_namevalue)
    # for i in range (len(lst_namevalue)):
    while len(lst_namevalue) > 0:
        print("Now Biding at : ", price)
       #f
        print(lst_namevalue[i], end=' ')
        #print(i,end=' ')
        bidprice = input("bids :")
        if bidprice == 'skip':

            lst_namevalue.pop(i)
            lst_phonevalue.pop(i)
            lst_emailvalue.pop(i)
            lst_gendervalue.pop(i)
            lst_emergencyvalue.pop(i)
            lst_paymentmodevalue.pop(i)
            i -=1
            if i<0:
                i=0



        elif int(bidprice) <= price * (100 + margin) / 100:
            print("Please enter greater price")
          #  i += 1
        else:
            price = int(bidprice)
            name = lst_namevalue[i]
            ph = lst_phonevalue[i]
            em = lst_emailvalue[i]
            g = lst_gendervalue[i]
            ev = lst_emergencyvalue[i]
            lp = lst_paymentmodevalue[i]
            i += 1
        if i % length == 0:
            i = 0
print("SOLD TO ", name, "for an amount of ", price)
print("DETAILS")
print("Phone Number:", ph)
print("Email ID:", em)
print("Gender:", g)
print("Payment mode:", lp)
print("1.) Security Deposit will be refunded for all other participants")
print("2.) ", name, "should make payment within a week")
print("Thankyou for participanting in the auction")