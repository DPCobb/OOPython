'''

Daniel Cobb
September 5, 2016
Design Patterns for Web Programming
Simple Form

'''

# Project Summary :
# Create a form for inventory additions and confirmations.
# Page 1 : Display form to add items using GET
# Page 2 : Reprint user submitted data for confirmation
# Page 3 : Confirm addition of inventory item
# Use 5 inputs, at least one text, radio, and select

import webapp2

# Import Pages class from pages.py
from pages import Pages

# Set variables and build out the page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        '''
        This function uses if statements to decide which page to show.
        First it checks for any GET data, if there is GET data it checks another condition, the value of confirm.
        If confirm is true than a success message is displayed, if it is false then the confirm item page is shown.
        If no GET data is present then the form is displayed
        '''
        # if there is GET data the script will show one of two pages
        if self.request.GET:
            # if confirm is set to True the page shows a simple confirmation of submission with link to home page
            if self.request.GET['confirm'] == "True":
                # set item var which is used to format success message
                item = self.request.GET['item']
                # set p to an instance of Pages
                p = Pages()
                # display the success message
                self.response.write(p.print_message(item))
            # if confirm is set to false (from hidden form field) then a review of what data was submitted is shown and user is prompted to confirm
            else:
                # setting vars used to structure confirmation page, vars are from form input
                item = self.request.GET['item']
                price = self.request.GET['price']
                desc = self.request.GET['desc']
                stock = self.request.GET['stock']
                store = self.request.GET['store']
                # set p to an instance of Pages
                p = Pages()
                # display confirmation page and pass needed vars for formatting
                self.response.write(p.print_confirm(item, price, desc, stock, store))
        # if there is no get data the page will show the form
        else:
            # set p to instance of Pages
            p = Pages()
            # display the form
            self.response.write(p.print_form())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
