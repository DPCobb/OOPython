'''
Daniel Cobb
September 5, 2016
DWP
Simple Form
Pages Class for constructing pages
'''

class Pages(object):
    def __init__(self):
        # set the path to css file
        self.css = "css/main.css"
        # construct the head section for html
        self.head = """
<!DOCTYPE html>
<html>
    <head>
        <title>CloudVentory++</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com/css?family=Quicksand:400,700" rel="stylesheet">
    </head>
    <body>
        <header>
            <nav>
                <ul><img src="images/threeline.png" alt="Menu"/>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Store Front</a></li>
                    <li><a href="#">Settings</a></li>
                    <li><a href="#">Log Out</a></li>
                </ul>
            </nav>
            <h1>CloudVentory++</h1>
            <h2>Inventory management from anywhere.</h2>
        </header>
                """
        # construct the form for html
        self.form = """
        <form method="GET">
            <h2>Add a new Inventory Item:</h2>
            <label for="item">Enter Item Name</label><input type="text" name="item"/>
            <label for="price">Enter Item Price</label><input type="text" name="price"/>
            <label for="desc">Enter Item Description</label><input type="text" name="desc"/>
            <fieldset>
            <legend>Current Stock</legend>
            <input type="radio" name="stock" value="In Stock"> In Stock
            <input type="radio" name="stock" value="Not In Stock"> Not In Stock
            </fieldset>
            <label for="store">Select Availability</label>
            <div class="select-style">
                <select name="store">
                    <option value="Online">Online Only</option>
                    <option value="In Store">In Stores</option>
                    <option value="Online and In Store">Online and In Stores</option>
                </select>
            </div>
            <input type="hidden" name="confirm" value="false"/>
            <input type="submit" value="submit"/>
        </form>
                """
        # construct the footer for html
        self.footer = """
    </body>
</html>
                        """
    def confirm_input(self, item, price, desc, stock, store):
        '''
        This function is used to return the value of self.confirm.
        self.confirm is the formatted confirmation message shown on page two after form submission
        '''
        # set vars for items needed in the message
        self.item = item
        self.price = price
        self.desc = desc
        self.stock = stock
        self.store = store
        # format confirmation html
        self.confirm = """
        <section>
            <h2>Please confirm item:</h2>
            <table>
                <tr>
                    <td>Item</td>
                    <td>{self.item}
                </tr>
                <tr>
                    <td>Description</td>
                    <td>{self.desc}
                </tr>
                <tr>
                    <td>Price</td>
                    <td>{self.price}
                </tr>
                <tr>
                    <td>Current Stock</td>
                    <td>{self.stock}
                </tr>
                <tr>
                    <td>Store Availability</td>
                    <td>{self.store}
                </tr>
            </table>
            <a href="?confirm=True&item={self.item}" class="button">Confirm Addition</a>
            <a href="/" class="button">Cancel</a>
        </section>

                """
        #return self.confirm
        return self.confirm

    def message(self, item):
        '''
        This function formats the success message seen on page 3
        '''
        # set item var
        self.item = item
        # format message html
        self.message = """
        <section>
            <h2>Success!</h2>
            <p>You have added {self.item}</p>
            <a href="/" class="button">Add Another Item</a>
        </section>
                """
        # return self.message
        return self.message

    def print_form(self):
        '''
        PAGE 1
        This function is called when no GET data is present. It formats and displays page one using the head, form, and footer.
        '''
        # set all var to parts needed to construct page
        all = self.head + self.form + self.footer
        # format all parts to fill in needed locals
        all = all.format(**locals())
        # return all for display
        return all

    def print_confirm(self, item, price, desc, stock, store):
        '''
        PAGE 2
        This function is used to display page two. It is used when GET data is present BUT confirm is false. This page
        prompts the user to confirm the form submission on the previous page.
        '''
        # construct the needed parts for page 2
        all = self.head + self.confirm_input(item, price, desc, stock, store) + self.footer
        # format page two to fill in local vars
        all = all.format(**locals())
        # return page two for display
        return all

    def print_message(self, item):
        '''
        PAGE 3
        This function is used to display page three. It is used when GET data is present AND confirm is true. This page is
        basically a success message letting the user know that item X has been sucessfully added to the inventory.
        '''
        # construct page parts
        all = self.head + self.message(item) + self.footer
        # format parts of page
        all = all.format(**locals())
        # return page 3
        return all