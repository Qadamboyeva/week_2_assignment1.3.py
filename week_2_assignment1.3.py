book_1_title=input("Title of the first book: ")
price_1_book=float(input("First book's price: "))
book_1_quantity=int(input("Quantity of the first book: "))

book_2_title=input("Title of the second book: ")
price_2_book=float(input("Second book's price: "))
book_2_quantity=int(input("Quantity of the second book: "))

book_3_title=input("Title of the third book: ")
price_3_book=float(input("Third book's price: "))
book_3_quantity=int(input("Quantity of the third book: "))

print("\n---Customer information---")
name=input("Name: ")
is_faculty_staff=input("Are you a faculty staff?(yes/no: ").lower() =="yes"
is_textbook_order=input("Is this a textbook order?(yes/no): ").lower()=="yes"
bulk_discount=input("Is this a bulk discount order? (yes/ no): ").lower()=="yes"
number_of_books= book_1_quantity + book_2_quantity + book_3_quantity

subtotal=(price_1_book*book_1_quantity)+(price_2_book*book_2_quantity)+(price_3_book*book_3_quantity)

faculty_discount_eligible = is_faculty_staff 
textbook_discount_eligible = is_textbook_order 
bulk_discount_eligible = bulk_discount
faculty_discount_amount = faculty_discount_eligible * subtotal * 0.2
textbook_discount_amount=textbook_discount_eligible*subtotal*.25
bulk_discount_amount=bulk_discount_eligible*subtotal*.08

is_faculty_staff = 0.20 * subtotal
is_textbook_order = 0.25 * subtotal 
bulk_discount = 0.08 * subtotal 
main_discount = is_faculty_staff * (is_textbook_order)
small_order_fee = (number_of_books < 3) * 10000
total_discount=(main_discount+bulk_discount)
subtotal_after_discount=("subtotal-total_discount")
tax = (is_textbook_order == False) * 0.05 * subtotal_after_discount
Shipping: 20000
print(f'  \nDISCOUNTS AND FEES')
print(f'\n{'='*40}')
print(f'faculty_discount_amount: {faculty_discount_amount}')
print(f'textbook_discount_amount: {textbook_discount_amount}')
print(f'bulk_discount_amount: {bulk_discount_amount}')
print(f'\nSubtotal before discount: {subtotal}')
print(f'Total discount: {total_discount}')
print(f'Subtotal after discount: {subtotal_after_discount}')
print(f'Tax: {tax}')
print(f'Small order fee: {small_order_fee}')
print(f'Shipping: 20000')
print(f'\nTotal amount due: {(subtotal_after_discount + tax + small_order_fee + 20000)}')
print(f'\n{"="*40}')
print("Thank you for your purchase!")

