# create empty dictionary
contacts = {}
# use while loop conditions.
while True:
    # create choices of contact book.
    print('/n Welcome to Contacts book /n')
    print('1.create contact')
    print('2.view  contact')
    print('3. update contact')
    print('4. delete contact')
    print('5. count contact')
    print('6.search contact')
    print('7. Exit')
    
    choice = input('Enter your choice = ')
    
    if choice == '1':
        name = input('Enter your name:')
        # use  membership (in )operation 
        if name in contacts:
            print('f contact name {name} already exist')
        else:
            age = input('Enter your age:')
            email = input ('Enter your email:')
            cellno = input('Enter your number:')
            #add values like age, email, cellno to key(contacts) in empty dictionary of contacts 
            contacts[name] = {'age':int (age),'email':email,'cellno':cellno}
            print('f contact name {name} has been created.')
    
    elif choice == '2':
        name = input('Enter contact name to view:')
        
        if name in contacts:
            #pass the name variable in contacts dictionary
            contact = contacts[name]
            print(f'Name :{name},Age :{age},Cellno: {cellno}')
        else:
            print('contact name not found') 
    
    elif choice == '3':
        name = input('Enter name to update your contact:') 
        if name in contacts:
            age = input('Enter your updated age:')
            email = input ('Enter your updated email:')
            cellno = input('Enter your updated number:')
            contacts[name] = {'age':int (age),'email':email,'cellno':cellno}
        else:
            print('contact name not found') 
            
    elif choice == '4':
        name = input('Enter  contact name to delete:')
        if name in contacts:
            del contacts[name]
            print(f'contact name{name} has been delete')
        else:
            print('contact not found')  
            
    elif choice =='5':
        print(f'total contacts in contact book :{len(contacts)}') 
        
    elif choice == '6':
        search_name = input('Enter contact name to search:')
        found = False
        # use for loop for iterrating values like age ,email,cellno in contacts dictionary.
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Founnd-Name{name}, Age:{age},Email:{email},Cellno:{cellno}')
                found = True
        if not found:
            print('No contact found with that name')
            
    elif choice == '7':
        print('Closing the program')
        break
    
    else:
        print('Invalid input')
        
    
        
            
            
        
        
        

         
              
             
            
          
            
                
            
            
            
            
        
        
        
               
            
            
              
            
        
        
            
            
            
            
                    
        
    
    
    
        


