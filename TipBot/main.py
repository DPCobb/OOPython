'''
Daniel Cobb
September 12, 2016
DPW - Reusable Library
'''

import webapp2
# Import views from page.py
from page import WelcomePage, ResultPage
# Import TipMachine ( calculates the tips and bill splits) and LastTip ( acts as a history class for previous tip %) from lib.py
from lib import TipMachine, LastTip

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # If the user has submitted data then...
        if self.request.GET:
            # Sets t to an instance of the TipMachine
            t = TipMachine()
            # Retrieve the total and set value user setter
            t.total = self.request.GET['total']
            # Retrieve the tip and set value user setter
            t.tip = self.request.GET['tip']
            # Retrieve the number of guests and set value user setter
            t.guests = self.request.GET['guests']
            # Retrieve the user name and set value user setter
            t.user = self.request.GET['user']
            # Calculate the tip
            tip = t.calc_tip()
            # Calculate the approximate bill split
            guest_split = t.split_bill()
            # Calculate the cost of and additional 5% of tip
            tip_options = t.tip_options()
            h = LastTip()
            h.last = "Your last calculated tip was " + t.tip + '% on a $' + t.total + ' bill.'
            # Send the results to the view for display
            p = ResultPage(t.user, t.total, t.tip, t.guests, tip, guest_split, tip_options)
            # Display the results
            self.response.write(p.results_page())
        # If the user has not submitted data then...
        else:
            # Set p to a new instance of the WelcomePage view
            p = WelcomePage()
            # Set h to an instance of LastTip, which displays the users last total and tip %
            h = LastTip()
            # Write the welcome page to the view
            self.response.write(p.welcome_page(h.last))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
