# my_lambdata/assignment_w_inherit.py

import pandas

class MyFrame(pandas.DataFrame):

    def inspect_data(self):
        print(self.head())

    def add_state_names(self):
        """
        State abbreviation -> Full Name and visa versa.
        FL -> Florida, etc.
        """
        names_map = {
            "CA": "Cali",
            "CO": "Colo",
            "CT": "Conn",
            "DC": "Wash DC",
            "TX": "Texas"
        }
        #breakpoint()
        my_col = self["abbrevs"]
        other_col = my_col.map(names_map)
        self["state_name"] = other_col

if __name__ == "__main__":

    #df = pandas.DataFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})

    my_frame = MyFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})
    print(my_frame.head())
    my_frame.inspect_data()
    my_frame.add_state_names()
    my_frame.inspect_data()
