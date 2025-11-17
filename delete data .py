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
        
        if not found :
            print("Data not found ⛔")
            return None



def delete_data(data_bace : list) :
    '''حدف یک دیتا از دیتابیس با اعتبار سنجی کامل این تابع : 
    1. نام دیتا را دریافت می کند
    2. وجود آن را بررسی میکن
    3. رمز عبور را تایید می کند
    4. در صورت تایید, آن را حذف می کند'''


    print("\n\n------------------------ Delete Data --------------------- \n ")

    # دریافت نام دیتا
    data_name = input("Enter data name to delete :  ")
    data_password = input("Enter data password :  ")

    torget = check_data_name_password(data_bace, data_name, data_password)

    if torget :
        # اطمینان از حذف دیتا
        sure_delete_data = input("Are you sure to clear this data ? (y/n) ")
        if sure_delete_data == "y" :
            
            # عملیاتت حذف
            data_bace.remove(torget)
            print("data cleared ❎")

            # ذخیره در فایل
            with open("Data app Data Bace .json", "w", encoding="utf-8") as file :
                json.dump(data_bace, file, ensure_ascii=False, indent=4)
    

        elif sure_delete_data == "n" :
            print("Ok. data don't deleted ✅")
        



with open("Data app Data Bace .json", "r", encoding="utf-8") as file :
    data_bace = json.load(file)


delete_data(data_bace)