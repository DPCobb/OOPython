# This is the basic Page Template
class PageTemplate(object):
    def __init__(self):
        '''
        __init__ sets up the basic layout for the page.
        '''
        # Set Title
        self.title = "IceStats: Welcome"
        # Set CSS file location
        self.css = "css/main.css"
        # Construct the head area
        self.head = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com/css?family=Bevan" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Baloo+Tamma" rel="stylesheet">

    </head>
        '''
        # Add the opening body Tag
        self.body = '''
    <body>
        '''
        # Set the header, nav, and opening main tags
        self.main = '''
        <header>
            <h1><img src="../img/logo.png" class="logo" title="IceStats"/></h1>
            <nav>

            </nav>
        </header>
        <main>


        '''
        # Set the footer and close all open tags
        self.footer = '''
        </main>
    </body>
    <footer>
    </footer>
</html>
        '''

    def page_out(self):
        '''
        page_out builds, formats, and returns the page for display
        '''
        all = self.head + self.body + self.main + self.footer
        all = all.format(**locals())
        return all


# This is the formatting for the main welcome page, which inherits from PageTemplate
class WelcomePage(PageTemplate):
    def __init__(self, list):
        '''
        __init__ sets up the needed elements for the welcome page. It also calls __init__ for PageTemplate. It takes
         param list for use in creating the buttons and player cards
        '''
        super(WelcomePage, self).__init__()
        # Set list to list param
        self.list = list
        # Set up empty buttons var
        self.buttons = ''
        # Loop through list and for each item create the player cards and buttons
        for name in self.list:
            self.buttons += '<span class="button-wrap" id="' + name[1] + '"><a href="/?id=' + name[1] + '" class="button">' + name[0] + '</a></span>'
        # Set up content which displays the player cards
        self.content = '''
            <section class="container">
                <h2>NHL All Time Point Leaders</h2>
                {self.buttons}
            </section>
                '''
        # Change self.main to include the nav version of the buttons
        self.main = '''
                <header>
                    <h1><img src="../img/logo.png" class="logo" title="IceStats"/></h1>
                    <nav>
                        {self.buttons}
                    </nav>
                </header>
                <main>

                '''
    # Overwrites PageTemplate
    def page_out(self):
        '''
        This function changes the page_out to include self.content. It builds, formats, and returns the page for display
        '''
        all = self.head + self.body + self.main + self.content + self.footer
        all = all.format(**locals())
        return all

# This is the formatting for the player stats page
class ContentPage(PageTemplate):
    def __init__(self, player):
        '''
        __init__ calls PageTemplate and sets the formatting for the player stats page. It takes player as a param, which is data
         passed for the current player and assigns the data to variables for formatting and display
        '''
        super(ContentPage, self).__init__()
        # Set the data to needed variables
        self.title = player.name
        self.name = player.name
        self.position = player.position
        self.assists = player.assists
        self.goals = player.goals
        self.games_played = player.games_played
        self.points = player.points
        self.goals_per_game = player.goals_per_game
        self.points_per_game = player.points_per_game
        self.assists_per_game = player.assists_per_game
        # Build the strucure for the image tag
        self.image = '<img src="' + player.img + '" />'
        # Build content to display player info
        self.content = '''
        <section class="player-info">
            {self.image}
            <div class="right">
                <h2>{self.name}</h2>
                <h3>{self.position}</h3>
                <table>
                    <tr>
                        <td>Games Played:</td>
                        <td>{self.games_played}</td>
                    </tr>
                    <tr>
                        <td>Total Goals:</td>
                        <td>{self.goals}</td>
                    </tr>
                    <tr>
                        <td>Total Assists:</td>
                        <td>{self.assists}</td>
                    </tr>
                    <tr>
                        <td>Total Points:</td>
                        <td>{self.points}</td>
                    </tr>
                    <tr>
                        <td>Average Goals Per Game:</td>
                        <td>{self.goals_per_game}</td>
                    </tr>
                    <tr>
                        <td>Average Assists Per Game:</td>
                        <td>{self.assists_per_game}</td>
                    </tr>
                    <tr>
                        <td>Average Points Per Game:</td>
                        <td>{self.points_per_game}</td>
                    </tr>
                </table>
                <a href="/" id="button-back">Home</a>
            </div>
        </section>
        '''
    # Overwrites PageTemplate
    def page_out(self):
        '''
        Adds self.content to page_out. Builds, formats, and returns page for display
        '''
        all = self.head + self.body + self.main + self.content + self.footer
        all = all.format(**locals())
        return all


# This is the formatting for the 'Error Page'
class ErrorPage(PageTemplate):
    def __init__(self, list):
        '''
        Set variables, call PageTemplate and build the error page. Takes list param for use in building links and player cards
        '''
        super(ErrorPage, self).__init__()
        # Set up vars
        self.title = "Error"
        self.list = list
        self.buttons = ''
        # loop through list and build buttons/player cards
        for name in self.list:
            self.buttons += '<span class="button-wrap" id="' + name[1] + '"><a href="/?id=' + name[
                1] + '" class="button">' + name[0] + '</a></span>'
        # Change self.main to include nav buttons
        self.main = '''
                        <header>
                            <h1><img src="../img/logo.png" class="logo" title="IceStats"/></h1>
                            <nav>
                                {self.buttons}
                            </nav>
                        </header>
                        <main>

                        '''
        # Build content, displays player cards
        self.content = '''
        <section class="container">
            <h2>Uh oh, it seems like something went wrong, let's try again.</h2>
            {self.buttons}
        </section>
        '''
    # Overwrites PageTemplate
    def page_out(self):
        '''
        Add self.content to page_out build, format, and return page for display
        '''
        all = self.head + self.body + self.main + self.content + self.footer
        all = all.format(**locals())
        return all

