import os
import json 

filename= 'PROGRESS_FILE.json'

def read_file():
    if os.path.exists(filename):
        try:
            with open(filename, 'r')as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}   
    else:
        data = {}        
    
    if "users" not in data:
        data['users'] = []
    return data
               
def save_file(data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent= 4)
        
def reg():
    fn = input("First Name: ")
    sn= input("Last Name: ")
    dob= input("D.O.B: ")
    st= input("State of origin: ")
    lc= input("L.G.A: ")
    wa= input("WhatsApp num: ")
    em= input("Email: ")
    ad= input("House address: ")
    uni= input("School: ")
    co= input("Course: ")
    
    existing_data = read_file()
    users = existing_data.get('users', [])
    
    new_user= {
        "First Name: ": fn,
        "Last Name: ": sn,
        "D.O.B: ": dob,
        "State Of Origin: ": st,
        "L.G.A: ": lc,
        "WhatsApp Num: ": wa,
        "Email: ": em,
        "House Address: ": ad,
        "School: ": uni,
        "Course: ": co
    }
    
    users.append(new_user)
    existing_data['users'] = users
    save_file(existing_data)
    print("Registration successful.....")
    
def main():
    print('='* 20)
    print('aci registration'.upper())
    print('='*20)
    
    while True:
        print("\n1.Register")
        print("2.Exit..")
        print("3.Access Backend")
        
        cho = input("select: ")
        
        if cho == "1":
            reg()
        elif cho == "2":
            print("Exiting..........")  
            break 
        elif cho == "3":
            try:
                pas = input("Password: ")
                if pas == "1234":
                    data = read_file()
                    users = data.get("users", [])
                    if users:
                        print(f"Registered users: {len(users)}")
                        print('='* 20)
                        for i, users in enumerate(users, 1):
                            print(f'\nUser: {i}')
                            for key, value in users.items():
                                print(f"{key}: {value}")
                    else:
                        print("No registration yet...")
                else:
                    print(f"Incorrect password contact developers")     
            except Exception as e:
                print(f"Error:  {e} invalid request!!!!")
if __name__=="__main__":
    main()            
