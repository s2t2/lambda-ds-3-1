
# my_lambdata/assignment.py

import pandas

# State abbreviation -> Full Name and visa versa.
# FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)

def add_state_names(my_df):
    """ Param my_df pandas dataframe with column name "abbrevs" """
    new_df = my_df.copy() # don't mutate existing df (just a pref, you could mutate and not return anything if you want)
    names_map = {
        "CA": "Cali",
        "CO": "Colo",
        "CT": "Conn",
        "DC": "Wash DC",
        "TX": "Texas"
    }
    #breakpoint()
    my_col = new_df["abbrevs"]
    other_col = my_col.map(names_map)
    new_df["state_name"] = other_col
    return new_df

if __name__ == "__main__":
    #print("hahahah")
    #input(".............")

    df = pandas.DataFrame({"abbrevs": ["CA", "CO", "CT", "DC", "TX"]})
    print(type(df))
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
