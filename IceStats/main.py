'''
Daniel Cobb
DPW - Dynamic Site
9/18/2016
'''
import webapp2
from data import Player, PlayerData
from page import PageTemplate, ContentPage, ErrorPage, WelcomePage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        '''
        This function contains all the logic for displaying pages and passes needed data to classes
        '''
        # Set p to an instance of PlayerData to be used for retrieving data for display
        p = PlayerData()
        # Main conditional: If there is GET data...
        if self.request.GET:
            # Set player equal to GET data (id)
            player = self.request.GET['id']
            '''
            Set data to player_data and pass player, player_data checks which name is passed to it and then returns the
            value of the appropriate getter for that name which holds the player stats
            '''
            data = p.player_data(player)
            # IF p.player_data returns false than there was no match in the data for player, so an error is displayed
            if data is False:
                # set data to player list, which returns an array from data of the players names and last name for url
                data = p.player_list
                # pass data to ErrorPage
                page = ErrorPage(data)
                # Display ErrorPage
                self.response.write(page.page_out())
            # If the data successfully returns
            else:
                # Pass data to the content page for formatting and display
                page = ContentPage(data)
                # Display Content page
                self.response.write(page.page_out())
        # Main Conditional: If there is NOT GET data...
        else:
            # set data to player list, which returns an array from data of the players names and last name for url
            data = p.player_list
            # Send data to WelcomePage
            page = WelcomePage(data)
            # Display WelcomePage
            self.response.write(page.page_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
