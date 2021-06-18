

def parse(link):
    field, value = "", ""
    equal_sign = False
    questionmark = False
    for char in link:
        if questionmark == False:
            if char == '?':
                questionmark = True
            continue
        if char == '&':
            print(f'{field} = {value}')
            field, value = "", ""
            equal_sign = False
        elif char == '=':
            equal_sign = True
        elif equal_sign == False:
            field += char
        elif equal_sign == True:
            value += char

def main():
    links = ["https://www.google.pl/search?q=xd&source=lmns&bih=722&biw=1536&hl=pl&sa=X&ved=2ahUKEwiCzMqAyv7wAhVK6CoKHTzVBUAQ_AUoAHoECAEQAA", "https://www.google.pl/search?q=xd&hl=pl&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjrxuL_yf7wAhUutYsKHd2NBxcQ_AUoAXoECAEQAw&cshid=1622830310160996&biw=1536&bih=722&dpr=1.25" ]
    
    for link in links:
        parse(link)
        print()

main()