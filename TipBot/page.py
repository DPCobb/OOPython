class WelcomePage(object):
    # This is the Welcome page view, it displays the form and the users last total and tip%
    def __init__(self):
        '''
        Init function sets up the HTML modules for the view.
        '''
        # CSS location
        self.css = 'css/main.css'
        # Format the header section
        self.header = '''
<!DOCTYPE html>
<html>
    <head>
        <title>TipBot:Welcome</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
        <script src="js/main.js"></script>
    </head>
        '''
        # Open the body section
        self.body = '''
    <body>
        <h1><img src="img/logo.png" title="TipBot" alt="TipBot Logo"/></h1>
        '''
        # Create the Form
        self.form = '''
        <section>
            <h2>Let TipBot calculate your tip!</h2>
            <form name="form" onsubmit="return formValid(event)" method="GET">
                <label for="user">Name</label>
                <input type="text" id="user" name="user" placeholder="Enter your name"/>
                <label for="total">Enter your bill total</label>
                <input type="text" id="total" name="total" placeholder="Example: 40.00"/>
                <label for="tip">Enter the percent you wish to tip</label>
                <input type="text" id="tip" name="tip" placeholder = "Example: 10"/>
                <label for="guests">How many people will be splitting the bill</label>
                <input type="text" id="guests" name="guests" placeholder = "Example: 2"/>
                <input type="submit" value="submit"/>
            </form>
        '''
        # Close all sections and add the footer
        self.footer = '''
        </section>
    </body>
    <footer>

    </footer>
</html>
        '''

    def welcome_page(self, last):
        '''
        welcome_page function takes the HTML modules from __init__ and formats them into the view then returns the formatted view.
        '''
        # Combine the modules
        all = self.header + self.body + self.form + last + self.footer
        # Format the modules
        all = all.format(**locals())
        # Return the page
        return all


class ResultPage(object):
    # This is the Results Page view, it displays the data given by the user and the calculated results
    def __init__(self, user, total, tip, guests, calc_tip, guest_split, tip_options):
        '''
        The __init__ function sets up the HTML modules for the results page. The params needed are set to variables to be used inside
        the HTML.
        '''
        # Set params to variables
        self.user = user
        self.total = total
        self.tip_percent = tip
        self.guests = guests
        self.tip = calc_tip
        self.guest_split = guest_split
        self.tip_options = tip_options
        # Set the CSS location
        self.css = 'css/main.css'
        # Create the header module
        self.header = '''
<!DOCTYPE html>
<html>
    <head>
        <title>TipBot: Results</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
    </head>
        '''
        # Create the body module, displaying the user data in a table and the calculated results
        self.body = '''
    <body>
        <h1><img src="img/logo.png" title="TipBot" alt="TipBot Logo"/></h1>
        <section>
        <div class="user-data">
            <p>{self.user} you entered the following information:</p>
            <table>
                <tr>
                    <td>Bill Total:</td>
                    <td>{self.total}</td>
                </tr>
                <tr>
                    <td>Tip Percent:</td>
                    <td>{self.tip_percent}</td>
                </tr>
                <tr>
                    <td>Total Guests:</td>
                    <td>{self.guests}</td>
                </tr>
            </table>
            <h3>Your New Total</h3>
            <h4>{self.tip}</h4>
            <h3>Each Guests Pays About</h3>
            <h4>{self.guest_split}</h4>
            <h3>To add an additional 5% tip add ${self.tip_options}</h3>
            <a href="/" class="button">Calculate New Tip</a>
        </div>
        '''
        # Close open tags and add the footer
        self.footer = '''
        </section>
    </body>
    <footer>

    </footer>
</html>
                '''

    def results_page(self):
        '''
        results_page function combines the HTML modules into the view, formats, and returns the view
        '''
        # Combine the modules
        all = self.header + self.body + self.footer
        # Format the modules
        all = all.format(**locals())
        # Return the view
        return all
