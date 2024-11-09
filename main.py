def send_email (message,recipient,sender = "university.help@gmail.com"):
    if  sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, ' на адрес ', recipient)
    elif     '@' not in recipient or '@' not in sender :
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    else:
        for i  in ('com','ru','net'):
         if i  in recipient :
             for j in ('com', 'ru', 'net'):
                 if j in sender:
                     print("Письмо успешно отправлено с адреса", sender, " на адрес", recipient)
             break
        else:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
send_email('Это сообщение для проверки связи', "university.help@gmail.com")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', 'urban.student@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.uk')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.', "university.help@gmail.com")