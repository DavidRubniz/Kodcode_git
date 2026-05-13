#1
def check_active_users(users):
    active_users = []
    for user in users:
        if user[1] >= 18 and user[2]:
            active_users.append(user[0])
    return active_users

users_dict = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]
print(check_active_users(users_dict))


#2
def check_email(user_email):
    if not user_email:
        print("Invalid user")
        return False
    return True

def check_quantity(quantity, stock):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return False
    return True

def make_price(quantity, product_price):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price


def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not check_email(user_email):
        return
    if not check_quantity(quantity, stock):
        return
    price = make_price(quantity, product_price)
    stock -= quantity
    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status


#3
def validation(name, grade):
    if not name or len(name) < 2:
        print("Error: invalid name")
        return False
    if grade < 0 or grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True

def calculate_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)
    return average, top_count, failing_count

def print_report(names, grades, average, top_count, failing_count):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

def save_to_file(names, grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

def manage_students(names, grades, new_name, new_grade):
    if not validation(new_name, new_grade):
        return None
    grades.append(new_grade)
    average, top_count, failing_count = calculate_stats(grades)
    print_report(names, grades, average, top_count, failing_count)
    save_to_file(names, grades)
    return names, grades


#4
def name_validation(name):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")

def email_validation(email):
    if "@" not in email:
        raise ValueError("Invalid email")

def create_users(name, email, permission):
    email_validation(email)
    name_validation(name)
    return name, email, permission, "2024-01-01", True


#5
def get_status(score):
    status = "excellent" if score >= 90 else "good" if score >= 70 else "average" if score >= 55 else "unknown"
    return status

def is_valid_age(age):
    if isinstance(age, int) and 0 < age < 120:
        return True
    return False

def get_greeting(hour):
    greeting = ('Good morning' if 5 <= hour < 12
                else "Good afternoon" if 12 < hour < 17
                else "Good evening" if 17 < hour < 21
                else "Good night")
    return greeting


#6
def validate_student(name, grades):
    if not name:
        print(f"Error: missing name")
        return False
    if not grades:
        print(f"Error: {name} has no grades")
        return False
    return True

def calculate_student_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    status = "pass" if average >= 56 else "fail"
    highest = max(grades)
    lowest = min(grades)
    return average, status, highest, lowest

def _print_report(result_names, result_averages, result_statuses, result_lows, result_highs):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()
    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")

def process_grades(names, all_grades):
    result_names, result_averages, result_statuses, result_highs, result_lows = [], [], [], [] ,[]
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]
        #validation
        if not validate_student(name, grades):
            continue
        #calculate
        average, status, highest, lowest = calculate_student_stats(grades)
        result_names.append(name)
        result_averages.append(round(average, 1))
        result_statuses.append(status)
        result_highs.append(highest)
        result_lows.append(lowest)
    #print report
    _print_report(result_names, result_averages, result_statuses, result_lows, result_highs)
    return result_names, result_averages, result_statuses


#7
TAX_PERCENT = 0.17
def process_cart(prices, quantities, user_type):
  total = 0
  for index in range(len(prices)):
    price = prices[index]
    quantity = quantities[index]
    total = total + price * quantity
  # add tax
  total = total+ total * TAX_PERCENT
  if user_type == 'premium':
    total = total * 0.9
  elif user_type == 'vip':
    total = total * 0.8
  if total > 500:
    shipping = 0
  elif total > 200:
    shipping = 25
  else:
    shipping = 50
  total = total + shipping
  return total




