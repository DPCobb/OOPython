class LastTip(object):
    # This class holds information for the last total and tip % calculated
    def __init__(self):
        '''
        __init__ sets the last calculated tip message in user history, if none exists a default message is shwon
        '''
        self.__last_tip_calc = 'You have not calculated any tips yet!'

    @property
    def last(self):
        '''
        getter for __last_tip_calc, returns the current value of __last_tip_calc for display
        '''
        return self.__last_tip_calc

    @last.setter
    def last(self, tip):
        '''
        Setter for __last_tip_calc sets value the value of tip param
        '''
        self.__last_tip_calc = tip

class TipMachine(object):
    # This is the tip machine, it handles the calculations and sets values based on the user input
    def __init__(self):
        '''
        __init__ sets the initial variables to zero and hides them using access modifiers
        All interaction with these variables is handled with getters and setters
        '''
        self.__user = "None"
        self.__total = 0
        self.__tip_percent = 0
        self.__guests = 0

    @property
    def user(self):
        '''
        getter for __user returns current value of __user
        '''
        return self.__user

    @user.setter
    def user(self, u):
        '''
        setter for __user sets __user to param
        '''
        self.__user = u

    @property
    def total(self):
        '''
        getter for __total returns current value of __total
        '''
        return self.__total

    @total.setter
    def total(self, t):
        '''
        setter for __total sets __total to param
        '''
        self.__total = t

    @property
    def tip(self):
        '''
        getter for __tip_percent returns current value of __tip_percent
        '''
        return self.__tip_percent

    @tip.setter
    def tip(self, t):
        '''
        setter for __tip_percent sets __tip_percent to param
        '''
        self.__tip_percent = t

    @property
    def guests(self):
        '''
        getter for __guests returns current value of __guests
        '''
        return self.__guests

    @guests.setter
    def guests(self, g):
        '''
        setter for __guests sets __guests to param
        '''
        self.__guests = g

    def calc_tip(self):
        '''
        This function calculates the new total with the tip include and returns a formatted version of that number
        '''
        # Calculate how much to add onto the bill with: total * (tip / 100)
        tip = float(self.total) * (float(self.tip) / 100)
        # Add the tip amount to the total with: total + tip
        total = float(self.total) + float(tip)
        # Return a formatted total to 2 decimal places
        return "%.2f" % round(total, 2)

    def split_bill(self):
        '''
        This calculates about how much each party will pay towards the bill
        '''
        # Set the total to the returned value of calc_tip()
        total = self.calc_tip()
        # Determine each guests share by: total / guests
        each_pay = float(total) / float(self.guests)
        # Return a formatted total to 2 decimal places
        return "%.2f" % round(each_pay, 2)

    def tip_options(self):
        '''
        Calculate the additional cost of a 5% greater tip
        '''
        # Determine the cost by: total * (5.00 / 100)
        total = float(self.total) * (float(5.00) / 100)
        # Format the total to 2 decimal places
        total = "%.2f" % round(total, 2)
        # Return a string version of total
        return str(total)
