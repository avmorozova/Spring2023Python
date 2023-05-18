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
    a1 = eng_A.find(plaintext[0])
    a2 = eng_a.find(plaintext[0])
    a3 = rus_A.find(plaintext[0])
    a4 = rus_a.find(plaintext[0])
    ciphertext = ""
    k = []
    j = []
    if (a1 != -1):
        for i in range(len(keyword)):
            k.append(eng_A.find(keyword[i]))
        for i in range(len(plaintext)):
            j.append(eng_A.find(plaintext[i]))
            if plaintext[i].isalpha():
                ciphertext += eng_A[(j[i] + k[i % len(keyword)]) % len(eng_A)]
            else:
                ciphertext += plaintext[i]
        return ciphertext
    elif (a2 != -1):
        for i in range(len(keyword)):
            k.append(eng_a.find(keyword[i]))
        for i in range(len(plaintext)):
            j.append(eng_a.find(plaintext[i]))
            if plaintext[i].isalpha():
                ciphertext += eng_a[(j[i] + k[i % len(keyword)]) % len(eng_a)]
            else:
                ciphertext += plaintext[i]
        return ciphertext
    elif (a3 != -1):
        for i in range(len(keyword)):
            k.append(rus_A.find(keyword[i]))
        for i in range(len(plaintext)):
            j.append(rus_A.find(plaintext[i]))
            if plaintext[i] == ' ':
                ciphertext += plaintext[i]
            else:
                ciphertext += rus_A[(j[i] + k[i % len(keyword)]) % len(rus_A)]
        return ciphertext
    elif (a4 != -1):
        for i in range(len(keyword)):
            k.append(rus_a.find(keyword[i]))
        for i in range(len(plaintext)):
            j.append(rus_a.find(plaintext[i]))
            if plaintext[i] == ' ':
                ciphertext += plaintext[i]
            else:
                ciphertext += rus_a[(j[i] + k[i % len(keyword)]) % len(rus_a)]
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
    a1 = eng_A.find(ciphertext[0])
    a2 = eng_a.find(ciphertext[0])
    a3 = rus_A.find(ciphertext[0])
    a4 = rus_a.find(ciphertext[0])
    plaintext = ""
    k = []
    j = []
    if (a1 != -1) :
        for i in range(len(keyword)):
            k.append(eng_A.find(keyword[i]))
        for i in range(len(ciphertext)):
            j.append(eng_A.find(ciphertext[i]))
            if ciphertext[i].isalpha():
                if (j[i] - k[i % len(keyword)]) < 0:
                    plaintext += eng_A[j[i] - k[i % len(keyword)] + len(eng_A)]
                else:
                    plaintext += eng_A[(j[i] - k[i % len(keyword)]) % 26]
            else:
                plaintext += ciphertext[i]
        return plaintext

    elif (a2 != -1):
        for i in range(len(keyword)):
            k.append(eng_a.find(keyword[i]))
        for i in range(len(ciphertext)):
            j.append(eng_a.find(ciphertext[i]))
            if ciphertext[i].isalpha():
                if (j[i] - k[i % len(keyword)]) < 0:
                    plaintext += eng_a[j[i] - k[i % len(keyword)] + len(eng_a)]
                else:
                    plaintext += eng_a[(j[i] - k[i % len(keyword)]) % 26]
            else:
                plaintext += ciphertext[i]

        return plaintext


    elif (a3 != -1):
        for i in range(len(keyword)):
            k.append(rus_A.find(keyword[i]))
        for i in range(len(ciphertext)):
            j.append(rus_A.find(ciphertext[i]))
            if ciphertext[i] == ' ':
                plaintext += ciphertext[i]
            elif (j[i] - k[i % len(keyword)]) < 0:
                plaintext += rus_A[j[i] - k[i % len(keyword)] + len(rus_A)]
            else:
                plaintext += rus_A[j[i] - k[i % len(keyword)]]
        return plaintext

    elif (a4 != -1):
        for i in range(len(keyword)):
            k.append(rus_a.find(keyword[i]))
        for i in range(len(ciphertext)):
            j.append(rus_a.find(ciphertext[i]))
            if ciphertext[i] == ' ':
                plaintext += ciphertext[i]
            elif (j[i] - k[i % len(keyword)]) < 0:
                plaintext += rus_a[j[i] - k[i % len(keyword)] + len(rus_a)]
            else:
                plaintext += rus_a[j[i] - k[i % len(keyword)]]
        return plaintext
