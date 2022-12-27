import requests
import smtplib

def run():
        
        # Set the API endpoint and headers
    email_api_endpoint = "https://qfrucfvqrp17bzk-gifecpm.adb.us-ashburn-1.oraclecloudapps.com/ords/returns/email/email"
    headers = {"Content-Type": "application/json"}

        # Set the login credentials
    username = "gifecmailer@gmail.com"
    password = "eolpguhuktuzxwau"

        # Send a GET request to the API to retrieve the email information
    response = requests.get(email_api_endpoint, headers=headers)

        # Check if the request was successful
    if response.status_code == 200:
            # Parse the email information from the response

            

        first_item = response.json()
        email_info = first_item["items"][0]

            #print(email_info)

        from_address = email_info["from"]
        to_address = email_info["to"]
        subject = email_info["subject"]
        body = email_info["body"]
        alert_id = email_info["id"]

            # Construct the email message
        message = "Subject: {}\n\n{}".format(subject, body)

            # Connect to the server and send the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, message)
        server.quit()

            # Update the status of the alert table
            
            # Set the ID and status flag
        p_status = "S"
        
        update_api_endpoint = "https://qfrucfvqrp17bzk-gifecpm.adb.us-ashburn-1.oraclecloudapps.com/ords/returns/email/email"
        update_data = {"p_id": alert_id, "p_status": p_status}
            # Make the PUT request
        response = requests.put(update_api_endpoint, json=update_data, headers=headers)

            # Check the status code of the response
        if response.status_code == 200:
            print("Success")
        else:
            print("Error: {}".format(response.status_code))

def print_me():
    print( f'Hi this is me {__name__}')

