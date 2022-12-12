def affine_rec_cipher(message, a1, a2, b1, b2):
    if message == '':
        return 'Введите что-нибудь.'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    new_message = ''
    array_a = [a1, a2]
    array_b = [b1, b2]
    for i in range(2, len(message)):
        array_a.append((array_a[i - 1] * array_a[i - 2]) % len(alphabet))
        array_b.append((array_b[i - 1] + array_b[i - 2]) % len(alphabet))
    #print(array_a)
    #print(array_b)

    for i in range(0, len(message)):
        for j in range(0, len(alphabet)):
            if message[i] not in alphabet:
                new_message += message[i]
                break
            if message[i] == alphabet[j]:
                #print(j, count)
                index = (array_a[i] * j + array_b[i]) % len(alphabet)
                new_message += alphabet[index]

    return new_message
print(affine_rec_cipher('cryptograhy', 3, 5, 10, 4))

def affine_rec_cipher_decode(message, a1, a2, b1, b2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ''
    array_a = [a1, a2]
    array_b = [b1, b2]

    for i in range(2, len(message)):
        array_a.append((array_a[i - 1] * array_a[i - 2]) % len(alphabet))
        array_b.append((array_b[i - 1] + array_b[i - 2]) % len(alphabet))
    print(array_a)
    print(array_b)

    for i in range(0, len(message)):
        for j in range(0, len(alphabet)):
            if message[i] not in alphabet:
                new_message += message[i]
                break
            if message[i] == alphabet[j]:
                t = None
                for mod_to_num in range(len(alphabet)):
                    if (array_a[i] * mod_to_num) % len(alphabet) == 1:
                        t = mod_to_num
                if t:
                    index = ((j - array_b[i]) * t) % len(alphabet)
                    new_message += alphabet[index]
                else:
                    return 'Не удалось посчитать модуль'

    return new_message
print(affine_rec_cipher_decode('qlkzjqgngbs', 3, 5, 10, 4))

#криптоанализ методом перебора всех ключей
def generator():
    for a in range(1, 26):
        for g in range(1, 26):
            for i in range(1, 26):
                for n in range(1, 26):
                    yield a, g, i, n

text_input = 'Rosemary Fell was not exactly beautiful. She was young, brilliant, extremely modern, well dressed and amazingly well read in the newest of the new books. Rosemary had been married two years, and her husband was very fond of her. They were rich, really rich, not just comfortably well-off, so if Rosemary wanted to shop, she would go to Paris as you and I would go to Bond Street. One winter afternoon she went into a small shop to look at a little box which the shopman had been keeping for her. He had shown it to nobody as yet so that she might be the first to see it.'
message = affine_rec_cipher(text_input, 1, 1, 20, 4)
for my_list in generator():
    text = affine_rec_cipher_decode(message, my_list[0], my_list[1], my_list[2], my_list[3])
    with open('res.txt', 'a', encoding='utf-8') as file:
        file.write(f'{" ".join(map(str, my_list))} - {text}\n')


#print(affine_rec_cipher_decode('qlkzjqgngtns', 3, 5, 10, 4))