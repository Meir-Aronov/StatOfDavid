
def print_texts_with_category():
    # מבקש מהמשתמש להזין את הקטגוריה
    category = input("What is the category: ")

    # מבקש מהמשתמש להזין טקסטים, עד שהמשתמש יפסיק להזין
    texts = []
    while True:
        user_input = input("Enter a text (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        texts.append(user_input)

    # מדפיס את הטקסטים עם הקטגוריה בפורמט המבוקש
    for text in texts:
        print(f'{{ "text": "{text}", "category": "{category}" }},')

# קריאה לפונקציה
print_texts_with_category()

