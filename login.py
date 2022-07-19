import sys
import json

##this program is written by Aryan Jaswaal
## on date 19 July 2022

user = str(sys.argv[1])
passwd = str(sys.argv[2])
main_data = ""
if user  == "aryan" and passwd == "aryan":
    main_data = {
        "status":"ok",
        "login":"yes"
        }
    main_data= json.dumps(main_data)
    print(main_data)
else:
    main_data ={
        "status":"no",
        "login":"no",
        }
    main_data = json.dumps(main_data)
    print(main_data)
