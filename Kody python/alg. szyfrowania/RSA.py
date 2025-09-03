from random import choice
def nwd(a,b):
    if(a > b):
        n = b
        liczba = a
    else:
        n = a
        liczba = b
            
    for i in range(n,0,-1):
        if liczba % i == 0 and n%i==0:
            return i

def odwr_mod(a,c):
    for b in range(c-1):
        if a*b%c == 1:
            return b

def gen_klucze_RSA():
    # zasadnicza część funkcji RSA  
    pierwsze = [11, 13, 17, 19, 23, 29, 31] #gotowa lista liczb
    p = 0
    q = 0

    while p == q:
        p, q = choice(pierwsze), choice(pierwsze) # funkcja cho
        phi, n = (p - 1) * (q - 1), p * q #obliczenie n i war
        e = 3 # dobieramy możliwie małą wartość dla e
        d = odwr_mod(e, phi) # obliczamy wartość d
        
        while nwd(e, phi) != 1:
            e += 2
            d = odwr_mod(e, phi)

    
    return (e, n), (d, n) #zwracamy klucze


def szyfrowanie_RSA(tekst: str,
                    klucz_publiczny: tuple):
    e, n = klucz_publiczny
    szyfr = [(ord(t) ** e) % n for t in tekst]
    return szyfr


def odszyfrowanie_RSA(szyfrogram: list,
                      klucz_prywatny: tuple):
    d, n = klucz_prywatny
    jawny = [chr((kod ** d) % n) for kod in szyfrogram]
    return "".join(jawny)

klucz_publ, klucz_priv = gen_klucze_RSA()
szyfrogram = szyfrowanie_RSA("Jestescie najlepsi",
                             klucz_publ)
print(szyfrogram)
print(odszyfrowanie_RSA(szyfrogram ,klucz_priv))
