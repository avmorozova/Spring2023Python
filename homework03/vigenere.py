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
            if plaintext[i] == ' ':
                ciphertext += ' '
            else:
                ciphertext += eng_A[(j[i] + k[i % len(keyword)]) % len(eng_A)]
        return ciphertext
    elif (a2 != -1):
        for i in range(len(keyword)):
            k.append(eng_a.find(keyword[i]))
        for i in range(len(plaintext)):
            j.append(eng_a.find(plaintext[i]))
            if plaintext[i] == ' ':
                ciphertext += ' '
            else:
                ciphertext += eng_a[(j[i] + k[i % len(keyword)]) % len(eng_a)]
        return ciphertext
    elif (a3 != -1):
        for i in range(len(keyword)):
            k.append(rus_A.find(keyword[i]))
        for i in range(len(plaintext)):
            j.append(rus_A.find(plaintext[i]))
            if plaintext[i] == ' ':
                ciphertext += ' '
            else:
                ciphertext += rus_A[(j[i] + k[i % len(keyword)]) % len(rus_A)]
        return ciphertext
    elif (a4 != -1):
        for i in range(len(keyword)):
            k.append(rus_a.find(keyword[i]))
        for i in range(len(plaintext)):
            j.append(rus_a.find(plaintext[i]))
            if plaintext[i] == ' ':
                ciphertext += ' '
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
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
