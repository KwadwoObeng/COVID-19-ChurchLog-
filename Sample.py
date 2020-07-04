"""
This program allows a user to book a church appointment
"""
class Church:
    """Initializing church attributes"""

    def __init__(self,max_capacity= 100,total_services=5):
        """default values"""
        self.max_capacity = max_capacity
        self.total_services = total_services
        self.current_capacity = 0

        self.name = ''

        self.service_two_capacity = 0
        self.service_three_capacity = 0
        self.service_four_capacity = 0
        self.service_five_capacity = 0



    def service_n(self, number):
        """Service Alternatives """


        if  number == 1:
            if  self.current_capacity < 100:
                success ="Congratulations we look forward to seeing you at 7:30am"
                print(success)



            else:
                print('Sorry service '+str(number)+" is fully booked")
                prompt = input('Please type the service number you would like to attend:')
                number = int(prompt)


        if number == 2:
            if self.service_two_capacity < 100:
                print("Congratulations we look forward to seeing you at 9:00am")



            else:
                print("Sorry service "+str(number)+" is fully booked")
                prompt = input("Please type the service number you would like to attend:  ")
                number = int(prompt)

        if number == 3:
            if self.service_three_capacity < 100:
                print("Congratulations we look forward to seeing you at 10:30am")



            else:
                print("Sorry service " + str(number) + " is fully booked")
                prompt = input("Please type the service number you would like to attend:  ")
                number = int(prompt)

        if  number == 4:
            if self.service_four_capacity < 100:
                print("Congratulations we look forward to seeing you at 12pm")

            else:
                print("Sorry service " + str(number) + " is fully booked")
                prompt = input("Please type the service number you would like to attend:  ")
                number = int(prompt)

        if  number == 5:
            if self.service_five_capacity < 100:
                print("Congratulations we look forward to seeing you at 1:30pm")



            else:
                print("Sorry all services are fully booked")





    def cap_inrease(self,number):
        """Increases service capacity for every booking """
        if number == 1:
            self.current_capacity += 1
        elif number == 2:
            self.service_two_capacity += 1
        elif number == 3:
            self.service_three_capacity += 1
        elif number == 4:
            self.service_four_capacity += 1
        elif number == 5:
            self.service_five_capacity += 1

    def user_input(self):
        """Allows user to select a service to attend"""


        welcome = "Welcome to the church booking platform"
        print(welcome)
        alt = Church()
        while True:
            t_name = input('Please type your name: ')

            number = input("Please type the service number you would like to attend:  ")
            number = int(number)
            self.name = t_name



            alt.service_n(number)
            alt.cap_inrease(number)







#make other methods that allow churches access user  data.


#Church administrator
    def church_admin(self):
        """ Church admnistrators can access user data here"""









me = Church()
me.user_input()



