#รับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้และคำนวณหาผลรวมและค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป็นเท่าใด และแสดงผลทางหน้าจอ
#ขอ4ฟังก์ชั่น ดังนั้นทำให้ได้ 4 feature

#=====================================
#Program Average 5 Number
#=====================================
#Enter number 1 : <input>
#Enter number 2 : <input>
#Enter number 3 : <input>
#Enter number 4 : <input>
#Enter number 5 : <input>
#=====================================
#Sum of 5 number is : <input>
#Average of 5 number is : <input> 

def get_user_numbers():
    numbers = []
    for i in range(5):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def display_result(sum_result, average_result):
    print(f"Sum of 5 number is : {sum_result}")
    print(f"Average of 5 number is : {average_result:.4f}")

print("=================================")
print("==== Program Average 5 Number ===")
print("=================================")
user_numbers = get_user_numbers()
print("=================================")
sum_result = calculate_sum(user_numbers)
average_result = calculate_average(user_numbers)
display_result(sum_result, average_result)
print("=================================")