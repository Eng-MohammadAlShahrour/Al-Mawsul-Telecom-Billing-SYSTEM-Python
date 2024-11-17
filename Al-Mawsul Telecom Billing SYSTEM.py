# Function to calculate the cost of local SMS
# This function calculates the total cost of local SMS based on the number of messages
def calc_local_sms_cost(local_sms_count):
    # If the number of local SMS is 5 or less, each SMS costs 50 SYP
    if local_sms_count <= 5:
        return local_sms_count * 50
    else:
        # For the first 5 SMS, the cost is 50 SYP per SMS, after that it's 35 SYP per SMS
        return 5 * 50 + (local_sms_count - 5) * 35

# Function to calculate the cost of international SMS
# This function multiplies the number of international SMS by the fixed cost per SMS (100 SYP)
def calc_international_sms_cost(international_sms_count):
    return international_sms_count * 100

# Function to calculate the cost of local calls
# This function calculates the total cost of local calls based on the number of call minutes
def calc_local_call_cost(local_call_minutes):
    if local_call_minutes <= 5:
        # First 5 minutes cost 30 SYP per minute
        return local_call_minutes * 30
    elif local_call_minutes <= 10:
        # Next 5 minutes (6 to 10) are free
        return 5 * 30  # Charge only for the first 5 minutes
    else:
        # First 5 minutes cost 30 SYP per minute, after 10 minutes, it costs 25 SYP per minute
        return 5 * 30 + (local_call_minutes - 10) * 25

# Function to calculate the cost of international calls
# This function multiplies the number of international call minutes by the fixed cost per minute (200 SYP)
def calc_international_call_cost(international_call_minutes):
    return international_call_minutes * 200

# Function to calculate the total bill for the customer
# This function combines the cost of local and international SMS and calls to compute the total monthly bill
def calc_total_bill(local_sms_count, international_sms_count, local_call_minutes, international_call_minutes):
    # Calculate individual costs using the previous functions
    local_sms_cost = calc_local_sms_cost(local_sms_count)
    international_sms_cost = calc_international_sms_cost(international_sms_count)
    local_call_cost = calc_local_call_cost(local_call_minutes)
    international_call_cost = calc_international_call_cost(international_call_minutes)
    
    # Return the total bill by adding all the individual costs
    return local_sms_cost + international_sms_cost + local_call_cost + international_call_cost

# Function to input customer data
# This function asks the user to input the customer's details and stores them in a dictionary
def input_customer_data():
    customer_data = {}  # Initialize an empty dictionary to store customer information
    
    while True:  # Loop to allow multiple customer entries
        # Input for customer's name
        while True:
            name = input("Enter customer's name (e.g., MOHAMMAD): ")
            valid = True
            for char in name:
                if char in '0123456789':  # Check if the name contains any numbers
                    print("Error: Name cannot contain numbers. Please enter a valid name.")
                    valid = False
                    break
            if valid:
                print("Valid name. The Name Is:", name)
                break  # Proceed to next input if the name is valid

        # Input for customer's mobile number
        while True:
            mobile_number = input("Enter customer's mobile number (e.g., +963955200799): ")
            valid2 = True
            
            # Check if the mobile number starts with '+963' and has exactly 13 digits
            if not mobile_number.startswith('+963') or len(mobile_number) != 13:
                print("Error: Mobile number must start with '+963' and have 13 digits with +963 icludoded.")
                valid2 = False
            
            # Check if all characters after '+963' are digits
            if valid2:
                for char in mobile_number[5:]:
                    if char not in '0123456789':
                        print("Error: Mobile number must contain only digits after '+963'.")
                        valid2 = False
                        break
            
            if valid2:
                print("Valid mobile number The Number Is:", mobile_number)
                break  # Mobile number is valid, proceed to next input

        # Input for SMS and call details with error handling
        while True:
            try:
                local_sms_count = int(input("Enter number of local SMS: "))
                if local_sms_count < 0:  # Check for negative input
                    print("Error: The number of local SMS cannot be negative. Please enter a valid number.")
                    continue
                break  # Exit the loop if the input is valid
            except ValueError:  # Handle the case where input is not an integer
                print("Error: Please enter a valid integer for local SMS.")

        while True:
            try:
                international_sms_count = int(input("Enter number of international SMS: "))
                if international_sms_count < 0:  # Check for negative input
                    print("Error: The number of international SMS cannot be negative. Please enter a valid number.")
                    continue
                break  # Exit the loop if the input is valid
            except ValueError:  # Handle the case where input is not an integer
                print("Error: Please enter a valid integer for international SMS.")

        while True:
            try:
                local_call_minutes = int(input("Enter number of local call minutes: "))
                if local_call_minutes < 0:  # Check for negative input
                    print("Error: The number of local call minutes cannot be negative. Please enter a valid number.")
                    continue
                break  # Exit the loop if the input is valid
            except ValueError:  # Handle the case where input is not an integer
                print("Error: Please enter a valid integer for local call minutes.")

        while True:
            try:
                international_call_minutes = int(input("Enter number of international call minutes: "))
                if international_call_minutes < 0:  # Check for negative input
                    print("Error: The number of international call minutes cannot be negative. Please enter a valid number.")
                    continue
                break  # Exit the loop if the input is valid
            except ValueError:  # Handle the case where input is not an integer
                print("Error: Please enter a valid integer for international call minutes.")

        # Calculate the total bill for the current customer
        total_bill = calc_total_bill(local_sms_count, international_sms_count, local_call_minutes, international_call_minutes)
        
        # Store all the customer data in the dictionary using the mobile number as the key
        customer_data[mobile_number] = {
            "name": name,
            "local_sms_count": local_sms_count,
            "international_sms_count": international_sms_count,
            "local_call_minutes": local_call_minutes,
            "international_call_minutes": international_call_minutes,
            "total_bill": total_bill  # Store the total bill calculated earlier
        }
        
        # Ask the user if they want to continue adding more customers
        cont = input("Do you want to continue? (Y/N): ")
        if cont == 'N':  # If the user inputs 'N', break the loop and stop input
            break
    
    return customer_data  # Return the collected customer data

# This function can be used to calculate the total bill (you can modify it according to your needs)
def calc_total_bill(local_sms_count, international_sms_count, local_call_minutes, international_call_minutes):
    # Total bill calculation
    local_sms_cost = calc_local_sms_cost(local_sms_count)
    international_sms_cost = calc_international_sms_cost(international_sms_count)
    local_call_cost = calc_local_call_cost(local_call_minutes)
    international_call_cost = calc_international_call_cost(international_call_minutes)

    return local_sms_cost + international_sms_cost + local_call_cost + international_call_cost  # Return the calculated total bill

# Function to print all bills
# This function prints the total bill for each customer stored in the dictionary
def print_bills(customer_data):
    for mobile_number in customer_data:  # Iterate over each customer in the dictionary
        # Print customer details including name, mobile number, and total bill
        print(f"\nCustomer: {customer_data[mobile_number]['name']}")
        print(f"Mobile Number: {mobile_number}")
        print(f"Total Bill: {customer_data[mobile_number]['total_bill']} SYP")

# Function to get the bill by mobile number
# This function retrieves the total bill for a specific customer by their mobile number
def get_bill_by_mobile(customer_data, mobile_number):
    # Check if the mobile number exists in the customer data
    if mobile_number in customer_data:
        # Return the total bill for the specified mobile number
        return customer_data[mobile_number]["total_bill"]
    else:
        return None  # Return None if the mobile number is not found

# Function to get the mobile number with the highest bill
# This function finds the customer with the highest bill and returns their mobile number
def get_mobile_with_highest_bill(customer_data):
    highest_bill_mobile = None  # Initialize a variable to store the mobile number with the highest bill
    highest_bill = 0  # Initialize the highest bill amount to zero
    for mobile_number in customer_data:  # Iterate over each customer in the dictionary
        # If the current customer's bill is higher than the recorded highest, update the highest
        if customer_data[mobile_number]["total_bill"] > highest_bill:
            highest_bill = customer_data[mobile_number]["total_bill"]
            highest_bill_mobile = mobile_number  # Store the mobile number of the customer with the highest bill
    return highest_bill_mobile  # Return the mobile number with the highest bill

# Function to get the customer name with the highest bill
# This function returns the name of the customer with the highest bill
def get_customer_with_highest_bill(customer_data):
    highest_bill_mobile = get_mobile_with_highest_bill(customer_data)  # Use the previous function to get the mobile number
    return customer_data[highest_bill_mobile]["name"]  # Return the name of the customer with the highest bill

# Function to get the top 3 customers by bill amount (without using lambda)
# This function returns the top 3 customers based on their bill amounts in descending order
def get_top_3_customers(customer_data):
    # Create a list of (name, total_bill) tuples for each customer
    customer_list = []
    for mobile_number in customer_data:
        # Append each customer's name and total bill to the list
        customer_list.append((customer_data[mobile_number]['name'], customer_data[mobile_number]['total_bill']))
    
    # Sort the list manually in descending order based on the bill amounts
    for i in range(len(customer_list)):
        for j in range(i + 1, len(customer_list)):
            # Compare the bill amounts to sort in descending order
            if customer_list[i][1] < customer_list[j][1]:  # Compare the bill amounts
                customer_list[i], customer_list[j] = customer_list[j], customer_list[i]  # Swap if needed
    
    return customer_list[:3]  # Return the top 3 customers by bill amount

# Function to write customer data to a file
# This function writes all the customer data from the dictionary to a specified file
def write_to_file(customer_data, filename):
    with open(filename, "w") as file:  # Open the file in write mode
        for mobile in customer_data:  # Iterate over each customer in the dictionary
            # Write customer details to the file
            file.write(f"Customer: {customer_data[mobile]['name']}, Mobile: {mobile}, Total Bill: {customer_data[mobile]['total_bill']} SYP\n")

print("Welcome to Al-Mawsul Telecommunication Company!")  # Welcome message to the user
customer_data = input_customer_data()  # Collect customer data
print_bills(customer_data)  # Print all customer bills


while True:
    mobile = input("Enter the mobile number to check the bill:(e.g., +963955200799):")
    valid2 = True
    # Check if the mobile number starts with '+963' and has exactly 13 digits
    if not mobile.startswith('+963') or len(mobile) != 13:
        print("Error: Mobile number must start with '+963' and have 13 digits with (+) included of 13 digit.")
        valid2 = False
            
    # Check if all characters after '+963' are digits
    if valid2:
        for char in mobile[5:]:
            if char not in '0123456789':
                print("Error: Mobile number must contain only digits after '+963'.")
                valid2 = False
                break 
    if valid2:
        print("Valid mobile number:", mobile)
        break 
bill = get_bill_by_mobile(customer_data, mobile)  # Retrieve bill for the specified mobile number
if bill:
    print(f"Bill for mobile {mobile}: {bill} SYP")  # Display the bill if found
else:
    print("Mobile number not found.")  # Message if the mobile number is not found

# Get the customer with the highest bill and print their name
highest_bill_customer = get_customer_with_highest_bill(customer_data)
print(f"\nCustomer with the highest bill: {highest_bill_customer}")

# Get the top 3 customers by bill and print their names and bill amounts
top_3_customers = get_top_3_customers(customer_data)
print("\nTop 3 customers by bill:")
for customer in top_3_customers:
    print(f"{customer[0]}: {customer[1]} SYP")

# Write the customer data to a file called "customer_bills.txt"
filename = "customer_bills.txt"
write_to_file(customer_data, filename)  # Write customer data to the specified file
print(f"\nCustomer data written to {filename}")  # Confirmation message

print("\nThank you for choosing Al-Mawsul Telecommunication Company! We are always here to serve you.")
