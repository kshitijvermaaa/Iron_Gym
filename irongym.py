#!/usr/bin/env python
# coding: utf-8

# In[265]:


import time


# In[266]:


super_users_dict = {'admin':'admin'}
members_credentials_dict = {12345:'mem'}
members_info_dict = {}
bmi_regimes = {1: ['Chest','Biceps','Rest','Back','Triceps','Rest','Rest'], 2: ['Chest','Biceps','Cardio/Abs','Back','Triceps','Legs','Rest'],3:['Biceps','Abs/Cardio','Back','Triceps','Legs','Cardio'],4:['Chest','Biceps','Cardio','Back','Triceps','Cardio','Cardio']}


# In[267]:


class Iron_Gym:
    def __init__(self):
        print("_________________________________________")
        print("\n\tWelcome to Iron Gym")
        print("_________________________________________")
        time.sleep(1)
        print("\n")
        self.login_menu()
    def login_menu(self):
        login = False
        print("1. Login as a Super User. \n2. Login as a Member. \n3. Exit")
        login_menu_input = int(input())
        
        
        if login_menu_input == 1:
            self.id = input("Enter your ID: ")
            self.password = input("Enter your password: ")
            for credentials in super_users_dict:
                if self.id == credentials and self.password == super_users_dict[credentials]:
                    time.sleep(1)
                    print("Access Granted")
                    login = True
                    time.sleep(2)
                    super_users()
            else:
                if login is False:
                    print("We cant find the given credentials. Please Check!!")
                    time.sleep(2)
                    self.login_menu()
        
        
        elif login_menu_input == 2:
            self.contact_number = int(input("Enter your Contact Number: "))
            self.passwd = input("Enter your Password: ")
            for credentials in members_credentials_dict:
                if self.contact_number == credentials and self.passwd == members_credentials_dict[credentials]:
                    time.sleep(1)
                    print("Access Granted")
                    login = True
                    members()
            else:
                if login is False:
                    print("We cant find the given credentials. Please Check!!")
                    time.sleep(2)
                    self.login_menu()
        
        
        elif login_menu_input == 3:
            exit()
        
        else:
            print("Check your input please!!")


    
class super_users:
    def __init__(self):
        print("1. Create Member. \n2. View Members. \n3. Delete Member. \n4. Update Member's Membership. \n5. Create Regimen. \n6. View Regimen. \n7. Delete Regimen. \n8. Update Regimen. \n9. Sign Out.")
        sup_input = int(input())
        if sup_input == 1:
            self.add_members()
        if sup_input == 2:
            self.view_members()
        if sup_input == 3:
            self.delete_member()
        if sup_input == 4:
            self.update_membership()
        if sup_input == 5:
            self.create_bmi_regime()
        if sup_input == 6:
            self.view_regime()
        if sup_input == 7:
            self.delete_regimen()
        if sup_input == 8:
            self.update_regimen()
        if sup_input == 9:
            print("Signing Out, Please Wait")
            time.sleep(3)
            z = Iron_Gym.login_menu(self)
    def add_members(self):
        self.name = input("Enter the full name of the new member: ")
        self.age= int(input("Enter the age of the new member: "))
        self.gender = input("Enter the gender of the new member: ")
        self.mobile_number = int(input("Enter the mobile number of the new member: "))
        self.password = input("Enter any password you want: ")
        self.email = input("Enter the email id of the new member: ")
        self.bmi = int(input("Enter the BMI of the new member: "))
        self.membership = int(input("Enter the Membership details of the new member(in months): "))
        new_user_info_list = [self.name,self.age,self.gender,self.email,self.mobile_number,self.bmi,self.membership]
        members_info_dict[self.mobile_number] = new_user_info_list
        members_credentials_dict[self.mobile_number] = self.password
        print("New Member {} added successfully".format(self.name))
        time.sleep(3)
        self.__init__()
    def view_members(self):
        flag = 0
        view_mem_input = int(input("Enter the Mobile Number of the Member: "))
        for values in members_info_dict:
            print(members_info_dict[view_mem_input])
            flag = 1
            time.sleep(2)
            self.__init__()
        else:
            if flag == 0:
                print("No such members found.")
                time.sleep(2)
                self.__init__()
        time.sleep(3)
        self.__init__()
    def delete_member(self):
        
        a = int(input("Enter the Mobile Number of Customer you want to Delete: "))
        if a in members_credentials_dict:
            members_info_dict.pop(a)
            print("Please wait....")
            time.sleep(2)
            members_credentials_dict.pop(a)
            print("Successfully Removed the user from Iron Gym.")
            time.sleep(2)
            self.__init__()
        else:
            print("No such users found!!")
            time.sleep(3)
            self.__init__()
    def update_membership(self):
        b = int(input("Enter the Mobile Number of member whose membership you want to change: "))
        if b in members_info_dict:
            c = int(input("Enter the new membership(in months): "))
            members_info_dict[b][6] = c
            time.sleep(2)
            print("Successfully changed the membership for {}".format(b))
            time.sleep(2)
            self.__init__()
        
        else:
            print("No such Users Found! ")
            time.sleep(3)
            self.__init__()
    def create_bmi_regime(self):
        print("1. BMI Less than 18. \n2. BMI Less than 25. \n3. BMI Less than 30. \n4. BMI Greater than 30.")
        bmi_inp = int(input("Enter the number for which you want to create a BMI Regimen "))
        self.monday = input("Enter the workout for Monday: ")
        self.tuesday = input("Enter the workout for Tuesday: ")
        self.wednesday = input("Enter the workout for Wednesday: ")
        self.thursday = input("Enter the workout for Thursday: ")
        self.friday = input("Enter the workout for Friday: ")
        self.saturday = input("Enter the workout for Saturday: ")
        self.sunday = input("Enter the workout for Sunday: ")
        bmi_list_todict = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]
        bmi_regimes[bmi_inp] = bmi_list_todict
        time.sleep(2)
        print("Workout Regimen added for the selected range {}".format(bmi_inp))
        time.sleep(2)
        self.__init__()
    
    def view_regime(self):
        print("1. BMI Less than 18. \n2. BMI Less than 25. \n3. BMI Less than 30. \n4. BMI Greater than 30. \n5. View all BMI Regimes")
        input_1 = int(input())
        if input_1 == 1:
            try:
                if bmi_regimes[input_1]:
                    print("MONDAY: {}".format(bmi_regimes[input_1][0]))
                    print("TUESDAY: {}".format(bmi_regimes[input_1][1]))
                    print("WEDNESDAY: {}".format(bmi_regimes[input_1][2]))
                    print("THURSDAY: {}".format(bmi_regimes[input_1][3]))
                    print("FRIDAY: {}".format(bmi_regimes[input_1][4]))
                    print("SATURDAY: {}".format(bmi_regimes[input_1][5]))
                    print("SUNDAY: {}".format(bmi_regimes[input_1][6]))
                    time.sleep(2)
                    self.__init__()
            except:
                print("No such BMI Regimen Found")
        elif input_1 == 2:
            try:
                if bmi_regimes[input_1]:
                    print("MONDAY: {}".format(bmi_regimes[input_1][0]))
                    print("TUESDAY: {}".format(bmi_regimes[input_1][1]))
                    print("WEDNESDAY: {}".format(bmi_regimes[input_1][2]))
                    print("THURSDAY: {}".format(bmi_regimes[input_1][3]))
                    print("FRIDAY: {}".format(bmi_regimes[input_1][4]))
                    print("SATURDAY: {}".format(bmi_regimes[input_1][5]))
                    print("SUNDAY: {}".format(bmi_regimes[input_1][6]))
                    time.sleep(2)
                    self.__init__()
            except:
                print("No such BMI Regimen Found")
        elif input_1 == 3:
            try:
                if bmi_regimes[input_1]:
                    print("MONDAY: {}".format(bmi_regimes[input_1][0]))
                    print("TUESDAY: {}".format(bmi_regimes[input_1][1]))
                    print("WEDNESDAY: {}".format(bmi_regimes[input_1][2]))
                    print("THURSDAY: {}".format(bmi_regimes[input_1][3]))
                    print("FRIDAY: {}".format(bmi_regimes[input_1][4]))
                    print("SATURDAY: {}".format(bmi_regimes[input_1][5]))
                    print("SUNDAY: {}".format(bmi_regimes[input_1][6]))
                    time.sleep(2)
                    self.__init__()
            except:
                print("No such BMI Regimen Found")
        elif input_1 == 4:
            try:
                if bmi_regimes[input_1]:
                    print("MONDAY: {}".format(bmi_regimes[input_1][0]))
                    print("TUESDAY: {}".format(bmi_regimes[input_1][1]))
                    print("WEDNESDAY: {}".format(bmi_regimes[input_1][2]))
                    print("THURSDAY: {}".format(bmi_regimes[input_1][3]))
                    print("FRIDAY: {}".format(bmi_regimes[input_1][4]))
                    print("SATURDAY: {}".format(bmi_regimes[input_1][5]))
                    print("SUNDAY: {}".format(bmi_regimes[input_1][6]))
                    time.sleep(2)
                    self.__init__()
            except:
                print("No such BMI Regimen Found")
                
        elif input_1 == 5:
            for values in bmi_regimes:
                print(bmi_regimes[values])
            time.sleep(2)
            self.__init__()
            
            
            
            
        else:
            print("That BMI is not defined")
            time.sleep(2)
            self.__init__()
    def delete_regimen(self):
        print("Which BMI Regimen you want to delete")
        print("1. BMI Less than 18. \n2. BMI Less than 25. \n3. BMI Less than 30. \n4. BMI Greater than 30.")
        del_inp = int(input())
        if del_inp in bmi_regimes:
            bmi_regimes.pop(del_inp)
            print("BMI Regimen Successfully Deleted")
            time.sleep(2)
            self.__init__()
        else:
            print("Cant find that BMI Regimen")
            time.sleep(2)
            self.__init__()
    def update_regimen(self):
        print("Which BMI Regime you want to update")
        print("1. BMI Less than 18. \n2. BMI Less than 25. \n3. BMI Less than 30. \n4. BMI Greater than 30.")
        input_update = int(input())
        if input_update == 1:
            bmi_regimes.pop(input_update)
            self.monday = input("Enter the workout for Monday: ")
            self.tuesday = input("Enter the workout for Tuesday: ")
            self.wednesday = input("Enter the workout for Wednesday: ")
            self.thursday = input("Enter the workout for Thursday: ")
            self.friday = input("Enter the workout for Friday: ")
            self.saturday = input("Enter the workout for Saturday: ")
            self.sunday = input("Enter the workout for Sunday: ")
            bmi_list_todict = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]
            bmi_regimes[input_update] = bmi_list_todict
            time.sleep(2)
            print("Workout Regimen Updated")
            time.sleep(2)
            self.__init__()
        elif input_update == 2:
            bmi_regimes.pop(input_update)
            self.monday = input("Enter the workout for Monday: ")
            self.tuesday = input("Enter the workout for Tuesday: ")
            self.wednesday = input("Enter the workout for Wednesday: ")
            self.thursday = input("Enter the workout for Thursday: ")
            self.friday = input("Enter the workout for Friday: ")
            self.saturday = input("Enter the workout for Saturday: ")
            self.sunday = input("Enter the workout for Sunday: ")
            bmi_list_todict = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]
            bmi_regimes[input_update] = bmi_list_todict
            time.sleep(2)
            print("Workout Regimen Updated")
            time.sleep(2)
            self.__init__()
        elif input_update == 3:
            bmi_regimes.pop(input_update)
            self.monday = input("Enter the workout for Monday: ")
            self.tuesday = input("Enter the workout for Tuesday: ")
            self.wednesday = input("Enter the workout for Wednesday: ")
            self.thursday = input("Enter the workout for Thursday: ")
            self.friday = input("Enter the workout for Friday: ")
            self.saturday = input("Enter the workout for Saturday: ")
            self.sunday = input("Enter the workout for Sunday: ")
            bmi_list_todict = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]
            bmi_regimes[input_update] = bmi_list_todict
            time.sleep(2)
            print("Workout Regimen Updated")
            time.sleep(2)
            self.__init__()
        elif input_update == 4:
            bmi_regimes.pop(input_update)
            self.monday = input("Enter the workout for Monday: ")
            self.tuesday = input("Enter the workout for Tuesday: ")
            self.wednesday = input("Enter the workout for Wednesday: ")
            self.thursday = input("Enter the workout for Thursday: ")
            self.friday = input("Enter the workout for Friday: ")
            self.saturday = input("Enter the workout for Saturday: ")
            self.sunday = input("Enter the workout for Sunday: ")
            bmi_list_todict = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]
            bmi_regimes[input_update] = bmi_list_todict
            time.sleep(2)
            print("Workout Regimen Updated")
            time.sleep(2)
            self.__init__()
        else:
            print("OOPS There was an error!!")
        


class members:
    def __init__(self):
        print("Welcome to Iron Gym")
        time.sleep(2)
        print("1. View your Regime. \n2. View Profile. \n3. Signout")
        mem_input = int(input())
        if mem_input == 1:
            self.view_regime()
        if mem_input == 2:
            self.view_details()
        if mem_input == 3:
            print("Signing Out, Please Wait")
            time.sleep(3)
            z = Iron_Gym.login_menu(self)
            
    def view_details(self):
        status = False
        print("For Security Reasons Please Provide Your Phone Number Again!")
        ph_num = int(input())
        for values in members_info_dict:
            if ph_num == values:
                print(members_info_dict[ph_num])
                status = True
                time.sleep(2)
                self.__init__()
        else:
            if status == False:
                print("Please check the Phone Number Provided")
                time.sleep(2)
                self.__init__()
    def view_regime(self):
        status = False
        print("For Security Reasons Please Provide Your Phone Number Again!")
        ph_num = int(input())
        for values in members_info_dict:
            if ph_num == values:
                a = members_info_dict[ph_num][5]
                if a in range(0,19):
                    status = True
                    print("THE BELOW GIVEN LIST STARTS FROM MONDAY AND ENDS ON SUNDAY")
                    print(bmi_regimes[1])
                    time.sleep(2)
                    self.__init__()
                elif a in range(19,26):
                    status = True
                    print("THE BELOW GIVEN LIST STARTS FROM MONDAY AND ENDS ON SUNDAY")
                    print(bmi_regimes[2])
                    time.sleep(2)
                    self.__init__()
                elif a in range(26,30):
                    status = True
                    print("THE BELOW GIVEN LIST STARTS FROM MONDAY AND ENDS ON SUNDAY")
                    print(bmi_regimes[3])
                    time.sleep(2)
                    self.__init__()
                elif a in range (30,100):
                    status = True
                    print("THE BELOW GIVEN LIST STARTS FROM MONDAY AND ENDS ON SUNDAY")
                    print(bmi_regimes[4])
                    time.sleep(2)
                    self.__init__()
                else:
                    print("Sorry, Error Occured!!")
                    
        else:
            if status == False:
                print("Please check the Phone Number Provided")
                time.sleep(2)
                self.__init__() 

        


# In[268]:


a = Iron_Gym()


# In[ ]:




