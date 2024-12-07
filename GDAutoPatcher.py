import urllib.request
def download_file_from_google_drive(file_id, destination):
    base_url = "https://drive.google.com/uc?export=download"
    session_url = f"{base_url}&id={file_id}"

    try:
        with urllib.request.urlopen(session_url) as response:
            content = response.read().decode('utf-8')

            if 'confirm' in content:
                confirm_token = "t" 
                download_url = f"https://drive.usercontent.google.com/download?id={file_id}&confirm={confirm_token}"
                print(f"Download URL: {download_url}")
            else:
                print("Confirmation token not found, using initial URL.")
                download_url = session_url

            
            with urllib.request.urlopen(download_url) as file_response, open(destination, 'wb') as out_file:
                out_file.write(file_response.read())

        print(f"File successfully downloaded to {destination}")
    except Exception as e:
        print(f"An error occurred: {e}")


print("GDAutoPatcher use 'help' for list of commands")
user_input = input("User: ")

if user_input == "help":
    print("List of commands: 1.9, 2.0, 2.11, 2.204, 2.206 downloads their respective versions. Adding 'Geode' AFTER a version number will download geode with it as long as it's not a version before 2.204 Windows/Linux only. The same with adding '4GB' BEFORE a version number as long as it's not a version after 2.204 Windows/Linux only. Using 'ALL' will result in all unmodded versions being downloaded Windows/Linux only. PS: These are CaSe-SeNsItIve")
    print("Using 'Mac' AFTER a version number will download the MacOS version of the specified version")
    input("You'll have to restart the script. Press Enter...")

# Unmodded
if user_input == "1.9":
    file_id = "1y1O9WxcXU0aSHo9yggYm8EHN0Igvg9-I"  
    destination_path = "1.9.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.0":
    file_id = "1ZY749tBKNbvcdPZT3QynX5HvxFMetBGO"  
    destination_path = "2.0.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.11":
    file_id = "1HYp696x0QB1U38HYpeB1l9qLEOOmMyI8"  
    destination_path = "2.11.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.204":
    file_id = "1d-4YYA5CXw-FF3BFksHRGNsis7YujeUL"  
    destination_path = "2.204.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.206":
    file_id = "18XWf9PaG9IJT8FbpOLQaKw4M6gigHysD"  
    destination_path = "2.206.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.207":
    file_id = "1BHcansV-0otffNu3NLSPpre3ReRshs65"  
    destination_path = "2.207.zip"
    download_file_from_google_drive(file_id, destination_path)

# Geode
if user_input == "2.204Geode":
    file_id = "1IgqttHt-xz7Xda_8OdvMnY6uxho9gD6v"  
    destination_path = "2.204 Geode.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.206Geode":
    file_id = "1vj2V9BiaKQtf1TtbKnZ8dmAXsO6Gj1aZ"  
    destination_path = "2.206 Geode.zip"
    download_file_from_google_drive(file_id, destination_path)


# 4GB Patch
if user_input == "4GB1.9":
    file_id = "1R7VhR4Y8FrTorTpTJm8rJx-m8wy0NwkE"  
    destination_path = "4GB 1.9.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "4GB2.0":
    file_id = "1saO1D5pp6s9V0Iw7zkPlP7L9aw8uryrp"  
    destination_path = "4GB 2.0.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "4GB2.11":
    file_id = "1y0j3_rPWcuVxHJWw9ROcmgPTi8YxtHlY"  
    destination_path = "4GB 2.11.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "4GB2.204":
    file_id = "1ZarpTnCG-wbrDWVOEgk3lCR6aJC4puyV"  
    destination_path = "4GB 2.204.zip"
    download_file_from_google_drive(file_id, destination_path)

# 2.204 w/4GB Patch and Geode
if user_input == "4GB2.204Geode":
    file_id = "1snhxxPHsFdAmJP8hc49v-eiGUSYf9FpG"  
    destination_path = "4GB 2.204 Geode.zip"
    download_file_from_google_drive(file_id, destination_path)


# All
if user_input == "ALL":
    file_id = "1tEp1WMeq70_nugGVWuAvJQw9P1_k3K9S"  
    destination_path = "ALL.zip"
    download_file_from_google_drive(file_id, destination_path)


# MacOS
# 0% chance these work lmao
if user_input == "1.9Mac":
    file_id = "1bvCxb9HlXdCNPlJsLro1Yk92IBVtIpPI"  
    destination_path = "1.9 Mac.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.0Mac":
    file_id = "1MIK6qv5aXLUKANXsTFk4vAuODNKuGt0w"  
    destination_path = "2.0 Mac.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.11Mac":
    file_id = "1RpkTmDQW8V-H7zE-HJc9QOfArWT5Q26j"  
    destination_path = "2.11 Mac.zip"
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.206Mac":
    file_id = "104RcQpWnXHqR_MV5Om5HgJmLbH27K0UB"  
    destination_path = "2.206 Mac.zip"
    download_file_from_google_drive(file_id, destination_path)


# Misc
if user_input == "2.204Mac":
    print("Error: 2.204 Doesn't exist on MacOS")
    input("You'll have to restart the script. Press Enter...")


if user_input == "2.1":
    file_id = "1HYp696x0QB1U38HYpeB1l9qLEOOmMyI8"  
    destination_path = "2.11.zip"
    print("Downloading '2.11'")
    download_file_from_google_drive(file_id, destination_path)


if user_input == "2.1Mac":
    file_id = "1RpkTmDQW8V-H7zE-HJc9QOfArWT5Q26j"  
    destination_path = "2.11 Mac.zip"
    print("Downloading '2.11'")
    download_file_from_google_drive(file_id, destination_path)