eng_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_a = 'abcdefghigklmnopqrstuvwxyz'
rus_A = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus_a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    k = []
    ciphertext = ""
    for i in range(len(keyword)):
        if (eng_A.find(keyword[i]) != -1):
            k.append(eng_A.find(keyword[i]))
        elif (eng_a.find(keyword[i]) != -1):
            k.append(eng_a.find(keyword[i]))
        elif (rus_A.find(keyword[i]) != -1):
            k.append(rus_A.find(keyword[i]))
        elif (rus_a.find(keyword[i]) != -1):
            k.append(rus_a.find(keyword[i]))

    for i in range(len(plaintext)):
        if (eng_A.find(plaintext[i]) != -1):
            ciphertext += eng_A[(eng_A.find(plaintext[i]) + k[i % len(keyword)]) % len(eng_A)]
        elif (eng_a.find(plaintext[i]) != -1):
            ciphertext += eng_a[(eng_a.find(plaintext[i]) + k[i % len(keyword)]) % len(eng_a)]
        elif (rus_A.find(plaintext[i]) != -1):
            ciphertext += rus_A[(rus_A.find(plaintext[i]) + k[i % len(keyword)]) % len(rus_A)]
        elif (rus_a.find(plaintext[i]) != -1):
            ciphertext += rus_a[(rus_a.find(plaintext[i]) + k[i % len(keyword)]) % len(rus_a)]
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    k = []
    plaintext = ""
    for i in range(len(keyword)):
        if (eng_A.find(keyword[i]) != -1):
            k.append(eng_A.find(keyword[i]))
        elif (eng_a.find(keyword[i]) != -1):
            k.append(eng_a.find(keyword[i]))
        elif (rus_A.find(keyword[i]) != -1):
            k.append(rus_A.find(keyword[i]))
        elif (rus_a.find(keyword[i]) != -1):
            k.append(rus_a.find(keyword[i]))

    for i in range(len(ciphertext)):
        if (eng_A.find(ciphertext[i]) != -1):
            if (eng_A.find(ciphertext[i]) - k[i % len(keyword)]) < 0:
                plaintext += eng_A[(eng_A.find(ciphertext[i]) - k[i % len(keyword)] + len(eng_A)) % len(eng_A)]
            else:
                plaintext += eng_A[(eng_A.find(ciphertext[i]) - k[i % len(keyword)]) % len(eng_A)]

        elif (eng_a.find(ciphertext[i]) != -1):
            if (eng_a.find(ciphertext[i]) - k[i % len(keyword)]) < 0:
                plaintext += eng_a[(eng_a.find(ciphertext[i]) - k[i % len(keyword)] + len(eng_a)) % len(eng_a)]
            else:
                plaintext += eng_a[(eng_a.find(ciphertext[i]) - k[i % len(keyword)]) % len(eng_a)]

        elif (rus_A.find(ciphertext[i]) != -1):
            if (rus_A.find(ciphertext[i]) - k[i % len(keyword)]) < 0:
                plaintext += rus_A[(rus_A.find(ciphertext[i]) - k[i % len(keyword)] + len(rus_A)) % len(rus_A)]
            else:
                plaintext += rus_A[(rus_A.find(ciphertext[i]) - k[i % len(keyword)]) % len(rus_A)]

        elif (rus_a.find(ciphertext[i]) != -1):
            if (rus_a.find(ciphertext[i]) - k[i % len(keyword)]) < 0:
                plaintext += rus_a[(rus_a.find(ciphertext[i]) - k[i % len(keyword)] + len(rus_a)) % len(rus_a)]
            else:
                plaintext += rus_a[(rus_a.find(ciphertext[i]) - k[i % len(keyword)]) % len(rus_a)]
        else:
            plaintext += ciphertext[i]
    return plaintext
