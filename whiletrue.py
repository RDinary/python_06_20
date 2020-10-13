"""
תרגיל:
כתבו פונקציה שתפקידה לקלוט מספר מהמשתמש ולוודא שהמספר בתחום בין 0 ל- 10000.V


V על הפונקציה לבקש קלט עד שהמשתמש יזין קלט נכון.
V על הפונקציה להחזיר את המספר בתור Integer.
תוודאו שהפונקציה לא תקרוס בשום שלב.
"""

#this is a git test
def get_num():
    num = 5
    while not (num <= 10000 and num >= 0):
        try:
            num = int(input("write a number 0-10000: "))
        except ValueError:
            print("this is not legal integer!")
        except:
            print("something went wrong")
    return num


get_num()

'''
תרגיל:
כעת נממש את פונקציות Lower/Upper הקיימות ב- Python:
כתבו פונקציה המקבלת שני פרמטרים: מחרוזת ומספר.

אם המספר הוא 1 עליכם להחזיר מחרוזת באותיות קטנות, אם המספר הוא 2 עליכם להחזיר את המחרוזת באותיות גדולות.  
בכל מקרה עליכם להדפיס את מספר המופעים של אותיות קטנות, אותיות גדולות, מספרים ואחר(סימנים וכו').

בצעו בדיקת קלט לפונקציה: לוודא שהמספר הוא 1 / 2 וגם שהמחרוזת היא אכן מחרוזת.

השתמשו בתכונות של טבלת ASCII

'''

a_ord = ord('a')  # number
z_ord = ord('z')  # number

A_ord = ord('A')  # number
Z_ord = ord('Z')  # number
ord_0 = ord('0')

delta = a_ord - A_ord  # number


def Lower(somestring):
    letters_list = []
    for s in somestring:  # s -> str with len ==1
        if A_ord <= ord(s) <= Z_ord:  # if s is capital letter
            letters_list.append(chr(ord(s) + delta))  # ord(s) + delta -> num, chr() ->str
        else:
            letters_list.append(s)
    lowerstring = "".join(letters_list)
    return lowerstring


def Upper(somestring):
    pass


def selector_function(some_string, some_number):
    if some_number == 1:
        print(Lower(some_string))
    elif some_number == 2:
        print(Upper(some_string))


selector_function("Have A wonderful day", 1)
