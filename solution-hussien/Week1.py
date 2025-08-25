# Task 1
# print number from 1 to 10
# for i in range(1,11):
#     print(i)


# Task 2

# أخذ مدخل من المستخدم
# num = int(input("Enter Number :"))

#طباعة الأرقام الزوجية من 0 حتى num باستخدام for
# for i in range(0, num + 1):
#     if i % 2 == 0:
#         print(i)

# أخذ مدخل من المستخدم
# num = int(input("Enter Numbe :"))

# طباعة الأرقام الزوجية من 0 حتى num باستخدام while
# i = 0
# while i <= num:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# Task 3

# أخذ مدخل من المستخدم
# start = int(input("Enter Numbe Start :"))
# end = int(input("Enter Numbe End :"))

# for i in range(start, end + 1):
#     print(i)
    
# Task 4

# num = int(input("Enter Numbe End :"))
# if num % 2 == 0 :
#     print("Even")
# else :
#     print("Odd")
    

# Task 5

# أخذ رقم من المستخدم
# num = int(input("Enter Number positive : "))

# التحقق من أن الرقم موجب
# if num < 0:
#     print("الرجاء إدخال رقم موجب فقط.")
# else:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i  
#     print("factorial", factorial)

# Task 6

# أخذ الرقم من المستخدم
# num = int(input("Enter Number : "))

# التحقق إذا كان أوليًا
# if num <= 1:
#     print("Not Primiry")
# else:
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("Primiry")
#     else:
#         print("Not Primiry ")


# Task 7

# أخذ الحد الأعلى من المستخدم
# limit = int(input("أدخل الحد الأعلى لمتتالية فيبوناتشي: "))

# بدء المتتالية من 0 و 1
# fib_sequence = []
# a, b = 0, 1

# while a <= limit:
#     fib_sequence.append(a)
#     a, b = b, a + b

# طباعة النتيجة
# print("متتالية فيبوناتشي حتى", limit, "هي:")
# print(fib_sequence)


# Task 8

# أخذ الكلمة من المستخدم
# word = input("أدخل كلمة: ")

# عكس الكلمة باستخدام تقطيع السلاسل [::-1]
# reversed_word = word[::-1]

# طباعة النتيجة
# print("عكس الكلمة هو:", reversed_word)


# Task 9 

# أخذ الكلمة من المستخدم
# word = input("أدخل كلمة: ")

# is_palindrome = True  # نفترض أنها متناظرة

# فحص كل حرف من البداية والنهاية
# for i in range(len(word) // 2):
    # if word[i] != word[-(i + 1)]:
        # is_palindrome = False
        # break

# طباعة النتيجة
# if is_palindrome:
    # print("Palindrome")
# else:
    # print("Not Palindrome")


# Task 10

# while True:

#     # أخذ المدخلات من المستخدم
#     weight = float(input("Enter Your weight with KG "))
#     height = float(input("Enter length with M"))
#     age = int(input("أدخل عمرك: "))

#     # حساب مؤشر كتلة الجسم
#     bmi = weight / (height ** 2)

#     # تحديد الحالة بناءً على BMI والعمر
#     if bmi < 25:
#         print("الحالة: ناقص الوزن.")
#     elif 25 <= bmi < 30:
#         print("الحالة: طبيعي.")
#     elif 30 <= bmi <= 40:
#         print("الحالة: زائد الوزن.")
#     if bmi > 40 or age > 40:
#         print("الحالة: تعاني من زيادة الوزن بسبب ارتفاع BMI أو العمر.")

# Task 11

# أخذ الأرقام من المستخدم كسلسلة نصية مفصولة بفواصل
# input_str = input("أدخل مجموعة من الأرقام مفصولة بفواصل: ")

# # تحويل السلسلة إلى قائمة من الأعداد الصحيحة
# numbers = [int(x.strip()) for x in input_str.split(",")]

# # التحقق من أن هناك على الأقل 3 أرقام
# if len(numbers) < 3:
#     print("يجب إدخال 3 أرقام على الأقل.")
# else:
#     # ترتيب الأرقام تنازليًا
#     numbers.sort(reverse=True)

#     # أخذ أكبر ثلاثة أرقام
#     top_three = numbers[:3]

#     # طباعة النتيجة
#     print("أكبر ثلاثة أرقام هي:", top_three)

# Task 12

# عدد الدروس
# num_courses = 4

# for lesson_num in range(1, num_courses + 1):
    
#     midterm = float(input("It enters the middle of winter : "))
#     final = float(input("It enters the end of winter : "))

#     # حساب متوسط نهاية العام
#     average = 0.4 * midterm + 0.6 * final

#     # تحديد حالة النجاح أو الرسوب
#     if average < 50:
#         result = "راسب"
#     else:
#         result = "ناجح"

#     # طباعة النتيجة
#     print(f"Average Lesson{lesson_num} = {average:.2f} --> {result}")


# Problem 1

# قراءة عددين من المستخدم
# a = int(input())
# b = int(input())

# # طباعة النتائج
# print(a + b)   
# print(a - b)   
# print(a * b)   


# problem 2

# n = int(input())

# # قراءة قائمة النتائج وتحويلها إلى أعداد صحيحة
# scores = list(map(int, input("Enter number : ").split()))

# # إزالة التكرار للحصول على قيم فريدة
# unique_scores = list(set(scores))

# # ترتيب القيم تنازليًا
# unique_scores.sort(reverse=True)

# # طباعة ثاني أعلى نتيجة (المركز الثاني)
# print(unique_scores[1])

# problem 3

# n = int(input())

# for i in range(1, n + 1):
#     print(i, end="")


# problem 4

# عدد الطلاب
# n = int(input())

# القاموس لتخزين الدرجات
# student_marks = {}

# # قراءة بيانات الطلاب
# for _ in range(n):
#     data = input("Enter Info Student : ").split()
#     name = data[0]
#     scores = list(map(float, data[1:]))
#     student_marks[name] = scores

# # اسم الطالب المطلوب حساب معدله
# query_name = input("Enter Name Student : ")

# # حساب المتوسط
# marks = student_marks[query_name]
# average = sum(marks) / len(marks)

# # طباعة النتيجة بدقة عشريتين
# print(f"{average:.2f}")


def calculator(a ,b):
    num1 = float(input("أدخل الرقم الأول: "))
    op = input("أدخل العملية (+ - * /): ")
    num2 = float(input("أدخل الرقم الثاني: "))

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print("عملية غير صحيحة")

calculator()
