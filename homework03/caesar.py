import typing as tp

eng_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_a = 'abcdefghigklmnopqrstuvwxyz'
rus_A = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus_a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

    ciphertext = ''
    eng_A_caesar = ''
    eng_a_caesar = ''
    rus_A_caesar = ''
    rus_a_caesar = ''

    for i in range(len(eng_A)):
        eng_A_caesar += eng_A[(i + shift) % len(eng_A)]
    for i in range(len(eng_a)):
        eng_a_caesar += eng_a[(i + shift) % len(eng_a)]
    for i in range(len(rus_A)):
        rus_A_caesar += rus_A[(i + shift) % len(rus_A)]
    for i in range(len(rus_a)):
        rus_a_caesar += rus_a[(i + shift) % len(rus_a)]

    encrypt_eng_A = str.maketrans(eng_A, eng_A_caesar)
    encrypt_eng_a = str.maketrans(eng_a, eng_a_caesar)
    encrypt_rus_A = str.maketrans(rus_A, rus_A_caesar)
    encrypt_rus_a = str.maketrans(rus_a, rus_a_caesar)

    ciphertext = plaintext.translate(encrypt_eng_A).translate(encrypt_eng_a).translate(encrypt_rus_A).translate(encrypt_rus_a)

    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:

    plaintext = ''
    eng_A_caesar = ''
    eng_a_caesar = ''
    rus_A_caesar = ''
    rus_a_caesar = ''

    for i in range(len(eng_A)):
        j = i - shift
        if j < 0:
            eng_A_caesar += eng_A[j + len(eng_A)]
        else:
            eng_A_caesar += eng_A[j]

    for i in range(len(eng_a)):
        j = i - shift
        if j < 0:
            eng_a_caesar += eng_a[j + len(eng_a)]
        else:
            eng_a_caesar += eng_a[j]

    for i in range(len(rus_A)):
        j = i - shift
        if j < 0:
            rus_A_caesar += rus_A[j + len(rus_A)]
        else:
            rus_A_caesar += rus_A[j]

    for i in range(len(rus_a)):
        j = i - shift
        if j < 0:
            rus_a_caesar += rus_a[j + len(rus_a)]
        else:
            rus_a_caesar += rus_a[j]

    decrypt_eng_A = str.maketrans(eng_A, eng_A_caesar)
    decrypt_eng_a = str.maketrans(eng_a, eng_a_caesar)
    decrypt_rus_A = str.maketrans(rus_A, rus_A_caesar)
    decrypt_rus_a = str.maketrans(rus_a, rus_a_caesar)

    plaintext = ciphertext.translate(decrypt_eng_A).translate(decrypt_eng_a).translate(decrypt_rus_A).translate(decrypt_rus_a)

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
