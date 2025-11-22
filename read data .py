import json


def check_data_name_password(data_bace, data_name, data_password) :
    '''پیدا کردن دیتا بر اساس نام + بررسی رز عبور
    اگر موفق باشد  : دیتا را بر می گرادند 
    اگر شکست بخورد : None بر می گرداند'''

    # جلوگیری از ورودی خالی
    if not data_name or not data_password :
        print("Error : Fields cannot be empty ❌")
        
    else :
        found = False

        # پیدا کردن نام
        for item in data_bace :
            if data_name in item :
                found = True
                print("Data found ✅")

                # بررسی برابری رمز دیتا
                if data_password == item[data_name]["data password"] :
                    
                    # برگرداندن دیتای پیدا شده
                    return item

                else :
                    print("password false ⛔")
                    return None
        




def see_data(data_bace : list) :
    '''این تابع نام دیتا را گرفته وبررسی میکند که در دیتابیس وجود دارد
    یا نه, اگر بود, رمزدیتتا را گرفته و بررسی ممیکند که رمز صحیح هست یانه.
    اگر اعتبار سنجی کامل بود, اطلاعات ر    if not found :
        print("Data not found ⛔")
        return Noneا نمایش میدهد'''

    print("\n\n------------------------ Read Data --------------------- \n ")
    
    data_name = input("Enter data name :  ")
    data_password = input("Enter data password :  ")

    target = check_data_name_password(data_bace, data_name, data_password)

    if target :
        for a in target :
            a = a
        
        # نمایش اطلاعات
        print("\n===============================================")
        print(f"\ndata name :  {a}")
        print(f"\ndata password :  {target[data_name]["data password"]}")
        print(f"\ndata :  {target[data_name]["data"]} \n")
        print("===============================================\n")
            


# این تیکه اضافه میباشد
with open("Data app Data Bace .json", "r", encoding="utf-8") as file :
    data_bace = json.load(file)



see_data(data_bace)








# الان دارم گیت هاب رو تمرین میکنم
# پس بعدا این هارو پاک کن
