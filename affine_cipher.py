def affine_cipher(message, k1, k2):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if message == '':
        return 'Так не получится. Введите что-нибудь)'
    if len(alphabet) % k1 == 0:
        return 'Так нельзя.'
    else:
        message = message.lower()
        new_message = ''
        index = 0
        for i in range(0, len(message)):
            for j in range(0, len(alphabet)):
                if message[i] not in alphabet:
                    new_message += message[i]
                    break
                if message[i] == alphabet[j]:
                    index = (k1 * j + k2) % len(alphabet)
                    new_message += alphabet[index]
                    break
        return new_message
print(affine_cipher('мэнн', 4, 7))

def affine_cipher_decode(message, k1, k2):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if len(alphabet) % k1 == 0:
        return 'Так нельзя.'
    if message == '':
        return 'Так не получится. Введите что-нибудь)'
    else:
        message = message.lower()
        new_message = ''
        index = 0
        for i in range(len(alphabet)):
            if (k1 * i) % len(alphabet) == 1:
                k1 = i
        for i in range(0, len(message)):
            for j in range(0, len(alphabet)):
                if message[i] not in alphabet:
                    new_message += message[i]
                    break
                if message[i] == alphabet[j]:
                    index = ((j - k2) * k1) % len(alphabet)
                    new_message += alphabet[index]
                    break
        return new_message
#print(affine_cipher_decode('', 7, 7))