def simple_change_encode(message, alphabet, alphabet_key):
    if len(alphabet) != len(alphabet_key):
        return 'Разные длины алфавитов, попробуйте снова.'
    if message == '':
        return 'Так не получится. Введите что-нибудь)'
    else:
        new_message=''
        message_list=list(message)
        alp = list(alphabet)
        alp_key = list(alphabet_key)
        for i in range(0, len(message_list)):
            for j in range(0, 33):
                if message_list[i] == alp[j]:
                    new_message += alp_key[j]
                if message_list[i] not in alp:
                    new_message += message_list[i]
                    break
        return new_message

#print(simple_change_encode('криптография', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'йцукенгшщзхъфывапролджэячсмитьбюё'))

def simple_change_decode(message, alphabet, alphabet_key):
    if len(alphabet) != len(alphabet_key):
        return 'Разные длины алфавитов, попробуйте снова.'
    if message == '':
        return 'Так не получится. Введите что-нибудь)'
    else:
        new_message=''
        message_list = list(message)
        alp = list(alphabet)
        alp_key = list(alphabet_key)
        for i in range(0, len(message_list)):
            for j in range(0, 33):
                if message[i] == alp_key[j]:
                    new_message += alp[j]
                if message_list[i] not in alp:
                    new_message += message_list[i]
                    break
        return new_message



