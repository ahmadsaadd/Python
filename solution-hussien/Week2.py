# Q1
# بيانات 10 طلاب (كل طالب: name, surname, midterm, final, oral)
students = {
    1: {'name': 'Ali',    'surname': 'Khan',   'midterm': 78, 'final': 85, 'oral': 80},
    2: {'name': 'Sara',   'surname': 'Ahmed',  'midterm': 65, 'final': 70, 'oral': 75},
    3: {'name': 'Omar',   'surname': 'Youssef','midterm': 90, 'final': 92, 'oral': 88},
    4: {'name': 'Layla',  'surname': 'Hussein','midterm': 58, 'final': 62, 'oral': 60},
    5: {'name': 'Noor',   'surname': 'Ali',    'midterm': 72, 'final': 75, 'oral': 80},
    6: {'name': 'Khalid', 'surname': 'Omar',   'midterm': 88, 'final': 86, 'oral': 90},
    7: {'name': 'Huda',   'surname': 'Saleh',  'midterm': 45, 'final': 50, 'oral': 55},
    8: {'name': 'Yara',   'surname': 'Sami',   'midterm': 77, 'final': 73, 'oral': 70},
    9: {'name': 'Zaid',   'surname': 'Nasser', 'midterm': 69, 'final': 68, 'oral': 72},
    10:{'name': 'Fatima', 'surname': 'Karim',  'midterm': 84, 'final': 80, 'oral': 86},
}

weights = {'midterm': 0.3, 'final': 0.5, 'oral': 0.2}

# 1) حساب GPA لكل طالب وإضافته في القاموس
for sid, info in students.items():
    gpa = (info['midterm'] * weights['midterm'] +
           info['final']   * weights['final'] +
           info['oral']    * weights['oral'])
    info['GPA'] = round(gpa, 2)   # تقريب خانتين عشريتين

# 2) إيجاد الطالب صاحب أعلى GPA وطباعته
highest_id = max(students, key=lambda k: students[k]['GPA'])
highest = students[highest_id]
print("أعلى GPA:", highest['name'], highest['surname'], "->", highest['GPA'])

# 3) فصل الاسم واللقب في tuple وإضافة كل tuple إلى قائمة
name_surname_tuples = [(info['name'], info['surname']) for info in students.values()]
print("قائمة tuples (name, surname):", name_surname_tuples)

# 4) ترتيب الأسماء أبجدياً (حسب الاسم الأول)
sorted_first_names = sorted([t[0] for t in name_surname_tuples])
print("الأسماء مرتبة أبجدياً (حسب الاسم الأول):", sorted_first_names)

# (اختياري) لو تريد ترتيب tuples حسب اللقب:
sorted_by_surname = sorted(name_surname_tuples, key=lambda t: t[1])
print("tuples مرتبة حسب اللقب:", sorted_by_surname)

# 5) مجموعة (set) للطلاب الذين GPA < 70
low_gpa_set = { (info['name'], info['surname']) 
                for info in students.values() 
                if info['GPA'] < 70 }
print("طلاب GPA < 70 (set):", low_gpa_set)

# --- للطباعة التفصيلية لكل طالب (اختياري) ---
print("\nقائمة الطلاب مع GPAs:")
for sid, info in students.items():
    print(sid, info['name'], info['surname'], "GPA =", info['GPA'])

    
    
    
    
    
# Q2


import json
import os

# ملف تخزين البيانات
FILE_NAME = "movies.json"

# تحميل البيانات من الملف إذا كان موجود
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        movies = json.load(f)
else:
    movies = {}


# 1) إضافة فيلم جديد
def add_movie():
    name = input("اسم الفيلم: ")
    director = input("المخرج: ")
    year = input("سنة الإصدار: ")
    genre = input("النوع: ")
    
    movies[name] = {
        "director": director,
        "year": year,
        "genre": genre
    }
    print("✅ تم إضافة الفيلم بنجاح!")

# 2) تعديل بيانات فيلم
def edit_movie():
    name = input("أدخل اسم الفيلم المراد تعديله: ")
    if name in movies:
        print("اختر ما تريد تعديله: director / year / genre")
        field = input("الحقل: ")
        if field in movies[name]:
            new_value = input(f"أدخل القيمة الجديدة لـ {field}: ")
            movies[name][field] = new_value
            print("✅ تم تعديل الفيلم!")
        else:
            print("❌ الحقل غير صحيح.")
    else:
        print("❌ الفيلم غير موجود.")

# 3) حذف فيلم
def delete_movie():
    name = input("أدخل اسم الفيلم المراد حذفه: ")
    if name in movies:
        del movies[name]
        print("✅ تم الحذف!")
    else:
        print("❌ الفيلم غير موجود.")

# 4) عرض الأفلام
def view_movies():
    print("1) عرض كل الأفلام")
    print("2) عرض حسب النوع")
    print("3) عرض حسب سنة الإصدار")
    choice = input("اختر: ")
    
    if choice == "1":
        for name, info in movies.items():
            print(f"{name} - {info['director']} - {info['year']} - {info['genre']}")
    elif choice == "2":
        genre = input("أدخل النوع: ")
        for name, info in movies.items():
            if info['genre'].lower() == genre.lower():
                print(f"{name} - {info['director']} - {info['year']} - {info['genre']}")
    elif choice == "3":
        year = input("أدخل سنة الإصدار: ")
        for name, info in movies.items():
            if info['year'] == year:
                print(f"{name} - {info['director']} - {info['year']} - {info['genre']}")

# حفظ البيانات في الملف
def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)

# القائمة الرئيسية
while True:
    print("1) إضافة فيلم")
    print("2) تعديل فيلم")
    print("3) حذف فيلم")
    print("4) عرض الأفلام")
    print("5) خروج")
    choice = input("اختر: ")
    
    if choice == "1":
        add_movie()
    elif choice == "2":
        edit_movie()
    elif choice == "3":
        delete_movie()
    elif choice == "4":
        view_movies()
    elif choice == "5":
        save_data()
        print("📁 تم حفظ البيانات، إلى اللقاء!")
        break
    else:
        print("❌ اختيار غير صحيح.")
    
    
    
# Q3

# Customer Management System with Functions

customers = {}
next_id = 1

def add_customer():
    global next_id
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    customers[next_id] = {
        "name": name,
        "surname": surname,
        "email": email,
        "phone": phone
    }
    print(f"Customer added with ID: {next_id}")
    next_id += 1

def update_customer():
    cid = int(input("Enter customer ID to update: "))
    if cid in customers:
        print("Current info:", customers[cid])
        customers[cid]["name"] = input("Enter new name: ")
        customers[cid]["surname"] = input("Enter new surname: ")
        customers[cid]["email"] = input("Enter new email: ")
        customers[cid]["phone"] = input("Enter new phone: ")
        print("Customer updated!")
    else:
        print("Customer not found.")

def delete_customer():
    cid = int(input("Enter customer ID to delete: "))
    if cid in customers:
        del customers[cid]
        print("Customer deleted!")
    else:
        print("Customer not found.")

def list_customers():
    if not customers:
        print("No customers available.")
    else:
        for cid, info in customers.items():
            print(f"ID: {cid}, Name: {info['name']} {info['surname']}, "
                  f"Email: {info['email']}, Phone: {info['phone']}")

def menu():
    print("\n--- Customer Management System ---")
    print("1. Add new customer")
    print("2. Update customer information")
    print("3. Delete customer")
    print("4. List all customers")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        update_customer()
    elif choice == "3":
        delete_customer()
    elif choice == "4":
        list_customers()
    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
