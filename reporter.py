import pandas
import os
from datetime import datetime


csv_filepath = os.path.join(os.path.dirname(__file__),"Data", "sales-201710.csv")
info = pandas.read_csv(csv_filepath)

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

def get_date_of_sales_report(info):
    first_row = info.iloc[0].to_dict() # Takes first row of data and converts it into a dictionary
    time = first_row["date"] #Finds the date
    real_time = datetime.strptime(time, "%Y-%m-%d") # Converts the date into datetime object
    year = real_time.year #Finds the year and then returns it
    month = real_time.month
    parsed_string = f"Sales Report for: {month}-{year}"
    return parsed_string

def find_total(info):
     total = info["sales price"].sum() #Sums the "sales price" column
     return total


def top_selling_products(info):
    highs = info.sort_values('sales price', ascending=False) #Sorts the column based off on ascending values
    print("TOP SELLING PRODUCTS:")
    print(highs.head(3)) #Selects top 3 items on list

if __name__ == "__main__":

    sales_date = get_date_of_sales_report(info)
    
    total = find_total(info)

    grand_total = to_usd(total)

    print(sales_date)
    print("TOTAL:", grand_total)

    top_selling_products(info)

