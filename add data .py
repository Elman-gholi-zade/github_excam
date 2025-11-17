import json
import secrets
import string


def add_data(data_bace : list, backup : list) :
    '''این تابع یک دیتا جدید از کاربر دریافت کرده,
    اعتبار سنجی میکند, سپس آن را در دیتابیس
    اضافه کرده و در فایل Json دخیره میکند
    و همچنین با خواست کاربر< برای رمز دیتای کاربر یک رمز تصادفی انتخاب و تعیین 
    میکند'''


    print("\n\n------------------------ Add Data --------------------- \n ")

    # دریافت ورودی ها
    data_name = input("Enter data name :  ")
    data_password = input("Enter your data password :  ")
    data = input("Enter your data : ")
     
    # تشخیص استفاده از رمز تصادفی برای دیتا کاربر
    if data_password == "random password" :
        allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
        pin = "".join(secrets.choice(allowed) for i in range(6))
        print(f"=============================\n| Set password :  {pin}    \n=============================\n \n")
        data_password = pin
        
    # جلوگیری از ورودی خالی
    if not data_name or not data_password or not data :
        print("Error : Fields cannot be empty ❌")

    else :
        # آمادی سازی برای ارسال به دیتابیس
        new_data = {data_name : {"data password" : data_password, "data" : data }}

        # افزودن و بازنویسی 
        data_bace.append(new_data)      # دیتابیس اصلی
        backup_data_bace.append(new_data)       # دیتابیس پشتیبان

        with open("Data app Data Bace .json", "w", encoding="utf-8") as file :
            json.dump(data_bace, file, ensure_ascii=False, indent=4)

        with open("Data app Data Bace - backup .json", "w", encoding="utf-8") as file :
            json.dump(data_bace, file, ensure_ascii=False, indent=4)

        print("append ✅")


with open("Data app Data Bace .json", "r", encoding="utf-8") as file :
    data_bace = json.load(file)
    
with open("Data app Data Bace - backup .json", "r", encoding="utf-8") as file :
    backup_data_bace = json.load(file)

add_data(data_bace, backup_data_bace)




# الان دارم گیت هاب رو تمرین میکنم
# پس بعدا این هارو پاک کن
