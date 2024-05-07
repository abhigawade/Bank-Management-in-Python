class user:
    balance = 0
    def __init__(self,name,mobile,gmail,aadhar,password):
        self.name = name
        self.mobile = mobile
        self.gmail = gmail
        self.aadhar = aadhar
        self.password = password

    def __str__(s):
        return "Name:"+s.name+"\n"+"Mobile No:"+str(s.mobile)+"\n"+"Gmail:"+s.gmail+"\n"+"Aadhar No:"+str(s.aadhar)+"\n"+"Password:"+s.password

a=user('Jay','9876451256','jay@123','999988887777','jay123')

class bank:
    data = []
    def account(s):
        print('--Enter your data to create your account--')
        name = input('Enter your name : ')
        b=True
        while(b):
            mobile = input('Enter Your Mobile Number:')
            if(mobile.isdigit() and len(mobile) == 10):
                mobile = int(mobile)
                break
            else:
                print('Invalid Mobile Number\n Enter only numbers length should be 10')
                mobile = input('Enter Your Mobile Number:')
                b=False

        gmail = input('Enter your Mail ID: ')
        b=True
        while(b):
            aadhar = input('Enter Your Aadhar Number:')
            if(aadhar.isdigit() and len(aadhar) == 12):
                aadhar = int(aadhar)
                break
            else:
                print('Invalid Aadhar Number\n Enter only numbers')
                aadhar = input('Enter Your Aadhar Number:')
                b=False

        password = input('Enter your password :')
            
        s.data.append(user(name,mobile,gmail,aadhar,password))
            
        acn=0
        while(aadhar>0):
            rem = aadhar%10
            acn = acn*10+rem
            aadhar = aadhar//10
        print(f'Your Account successfully created, This is Your account no {acn}')
        print('------------------------------------------------------------------------------------------------')

    def login(s):

        print('--Enter your Email And Password to login--')
        gmail = input('Enter Your Email :')
        password = input('Enter Your Password:')
        for i in s.data:
            if gmail==i.gmail and password==i.password:
                return i
            
    def deposit(s):

        print('--Enter a ammount to deposit : ')
        amt = int(input('Enter a ammount to deposit: '))
        if(amt > 0):
            user.balance = user.balance + amt
        else:
            print('Please enter valid ammount')
        print(f'Your Account balance is {user.balance}')
        print('--------------------------------------------------------------------')
        
    def withdraw(s):
        print('--Enter a ammount to withdraw : ')
        amt = int(input('Enter a ammount to withdraw: '))
        if(amt <= user.balance and amt > 0):
            user.balance = user.balance - amt
        else:
            print('Insufficient Balance please check your Balance')
        print(f'Your Account balance is {user.balance}')
        print('---------------------------------------------------------------------')

    def viewbalance(s):
        print('-----------Welcome To Bank----------')
        print(f'Your balance is {user.balance}')
        print('---------------------------------------------------------------------')

    def transfer(s,user):
        amt = int(input('Enter a ammount to Transfer: '))
        if(amt > user.balance):
            print('Insufficient balance')
        elif(amt >=1 and amt <= user.balance):
            user.balance = user.balance - amt
##            a.balance = a.balance + amt
            print(f'Ammount Transfer Sucessfully Your Balance: {user.balance} \n Thanks for visiting')
        elif(amt < 1):
            print(f'You Cannot transfer this ammount')

              
    def mainmenu(s,u):
        k=True
        while(k):
            print('----------------------------------------------------------------------')
            print('--Enter 1 To Deposit Ammount--')
            print('--      2 To withdraw Ammount--')
            print('--      3 To view bank Balance--')
            print('--      4 To Account Details--')
            print('--      5 To Transfer Ammount')
            print('--      6 To Exit--')
            print('----------------------------------------------------------------------')

            q=int(input('Enter your choice: '))

            if(q==1):
                s.deposit()
            elif(q==2):
                 s.withdraw()
            elif(q==3):
                 s.viewbalance()
            elif(q==4):
                print(u)
                print('---------------------------------------------------------------------------')
            elif(q==5):
                s.transfer(a)
            elif(q==6):
                k=False
                
    def call(s):
        
       b=True
       while(b):
           
           print('-----------------------------WELCOME TO SATARA BANK-----------------------------')
           print('--Enter 1 to create your account--')
           print('--      2 to Login in Bank System--')
           print('--      3 to Exit from system--')
           print('---------------------------------------------------------------------------------')

           p=int(input('-Enter your choice : '))

           if(p==1):
               s.account()
           elif(p==2):
               u=s.login()
               if u is not None:
                   s.mainmenu(u)
               else:
                   print('--Invalid Data--')
           elif(p==3):
               print('-------------Visit Again---------------')
               b=False
           else:
               print('--Invalid Choice--')

b=bank()
b.call()



