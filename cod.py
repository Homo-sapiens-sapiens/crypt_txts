import random

vars=["3141592653589793238462643383279", "2718281828459045235360287471352",
            "1618030988749894848204586834365", "7428401459137632060472614242303",
            "8694826929103247827490131959418", "9703982540812916946747644956425",
            "4385649798651850863985684205494", "5212134987593028384202934958020",
            "0306316438723054321209701381724", "6353174947336824749789713249547"]
alph="ЁqЙ1ЦQУ$КwЕ-НWГ>ШeЩ2ЗEХ%ЪrФ=ЫRВ<АtП3РTО?ЛyД[ЖYЭ^ЯuЧ4СUМ(ИiТ]ЬIБ*Юoё5йOц+уpк;еPн_гaш6щAз)хsъ'фSы вdа7пDр~оfл,дFж`эgя8чGсhм.иHтjь9бJюk/Kl0Lz\Zx!Xc}Cv@Vb{Bn#Nm:M"
ven=0
laph=0
ley=0
lin=0

def run(inp, ke, mode):
    outp = ces(inp, ke, mode)
    return outp

def ces(inn, key, mod):
    ven = len(vars[0])
    laph = len(alph)
    ley = len(key)
    lin = len(inn)
    out=""
    if mod:
        for i in range(lin): out+=alph[(alph.index(inn[i])-int(vars[ord(key[i%ley])%10][i%ven]))%laph]
    else:
        for i in range(lin): out+=alph[(alph.index(inn[i])+int(vars[ord(key[i%ley])%10][i%ven]))%laph]
    return out