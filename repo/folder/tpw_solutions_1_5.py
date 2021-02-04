# Exercise 1: Mailing Address
# Format from https://www.canadapost.ca/web/en/kb/details.page?article=addressing_mail_accu&cattype=kb&cat=addressing&subcat=accuracy

full_name = 'JOHN JONES'
additional_information = 'MARKETING DEPT'
unit = '10'
civic_number = '123'
street = '1/2 MAIN ST NW'
city = 'MONTREAL'
province = 'QC'
postal_code = 'H32 2YZ'
print('{} \n{} \n{}-{} {} \n{} {} {}'.format(full_name, additional_information, unit, civic_number, street, city, province, postal_code))

# Exercise 2: Hello

name = input('What is your name?')
print('Hello {}!'.format(name))

# Exercise 3: Area of a Room

length = float(input('Length: '))
width = float(input('Width: '))
area = length * width
unit = 'meters'
print('The area of the room is {} square {}!'.format(area, unit))

# Exercise 4: Area of a Field

length = float(input('Length: '))
width = float(input('Width: '))
acres = length * width / 43_560.0
print('The area of the field is {} acres!'.format(acres))
  
# Exercise 5: Bottle Deposits

small = int(input('Number of bottles that hold 1L or less: '))
large = int(input('Number of bottles that hold more than 1L: '))
small_refund = small * 0.10
large_refund = large * 0.25
total_refund = small_refund + large_refund 
print('Your total refund is ${}!'.format(total_refund))
