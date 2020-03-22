#######################################################################
# Computer Project #5
# 
# Algorithm
#
#   Main function is called. Open_file function is called an returns a 
#   filepointer. This file is then interated through and spliced to 
#   seperate pertinent information. If product name is same as the name 
#   preceding it its ROI is calculated and stored as well as its sales amount
#   per ad. The largest ROI and Sale amount is displayed per product.
#
########################################################################

def open_file():
    '''prompt for file name, open file, return file pointer'''
    
    # Continuously prompt until correct file inputted
    
    while True:
    
        try:
    
            filename = input("Input a file name: ")
            
            fp = open(filename)
            
            return fp
            
        except FileNotFoundError: 
            
            print("Unable to open file. Please try again.")
    
    
def revenue(num_sales, sale_price):
    '''revenue = sales * price'''
    
    # calculates revenue
    
    rev = int(num_sales) * float(sale_price)
    
    return rev

def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    '''costs of goods sold = advertising total + production total'''
    
    # calculates cost of goods
    
    c_of_sold = (int(num_ads) * float(ad_price)) + (int(num_sales) * float(production_cost))
    
    return c_of_sold

def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    '''ROI = (Revenue - Cost of goods sold)/Cost of goods sold'''
    
    # calls revenue function
    
    rev = revenue(num_sales,sale_price)
    
    # calls cost_of_goods_sold function

    cost_goods_sold = cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost)
    
    # calculates ROI using the return value of the above two functions
    
    ROI = ((rev - cost_goods_sold) / cost_goods_sold)
    
    return ROI

def main():
    
    # open the file
    
    file = open_file()
    
    # Some print lines to match formatting in Mimir tests
    
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print() 
    
    # read the file
    
    # initialize counters and strings
     
    ROI_counter = 0
    
    sales_count = 0
    
    ad_name_roi = ''
    
    ad_name_sales = ''
    
    name_list = [" "]
    
    # iterate through file splicing at important data points
    
    for line in file:
        
        name = line[:27]
        
        ad = line[27:54]
        
        num_ads = line[54:62]
        
        ad_price = line[62:70]
        
        num_sales = line[70:78]
        
        sale_price = line[78:86]
        
        production_cost = line[86:94]
        
        # if name list is blank - list entry is name. Only used in first entry
        
        if name_list[0] == " ":
            
            name_list[0] = name
            
        # if name of current lines matches. Execute suite
        
        if name == name_list[0]:
            
            # calls ROI function
            
            local_roi = calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost)
           
            # captures max ROI
            
            if local_roi > ROI_counter:
                
               ROI_counter = local_roi
               
               ad_name_roi = ad
               
            # captures max sales
               
            if int(sales_count) < int(num_sales):
                
                sales_count = num_sales
                
                ad_name_sales = ad
        
        # If new product - prints
        
        else:
            
            # round and convert ROI
    
            string_roi = (str(round(ROI_counter,2)) + "%")
    
            print(name_list[0])
            print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
            print("  {:27s}{:>11s}".format(str(ad_name_sales),str(sales_count)))
            print()
            
            print("  {:27s}{:>11s}".format("Best ROI","percent"))
            print("  {:27s}{:>11s}".format(str(ad_name_roi),string_roi))
            print()
            
            # IMPORTANT: Records data for the current line after printing
            
            name_list[0] = name
            
            ROI_counter = 0
            
            sales_count = 0
            
            local_roi = calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost)
                
            if local_roi > ROI_counter:
                
               ROI_counter = local_roi
               
               ad_name_roi = ad
               
            if int(sales_count) < int(num_sales):
                
                sales_count = num_sales
                
                ad_name_sales = ad
                
    # Block of code responsible for printing the last product in the list
                
    string_roi = (str(round(ROI_counter,2)) + "%")            
                
    print(name_list[0])
    print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
    print("  {:27s}{:>11s}".format(str(ad_name_sales),str(sales_count)))
    print()
    
    print("  {:27s}{:>11s}".format("Best ROI","percent"))
    print("  {:27s}{:>11s}".format(str(ad_name_roi),string_roi))
    print()
                

if __name__ == "__main__":
    
    main()