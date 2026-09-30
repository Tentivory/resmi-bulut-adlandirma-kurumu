#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Resmi Bulut Adlandirma ve Meteorolojik Burokrasi Enstitusu
Calisan memur scripti. Gercekten bir sey yapar. O sey saçmadir.
"""

import hashlib
import random
import sys
from datetime import datetime, timedelta

# GIZLI_ARSIV: b3l1bnUgdmVyZW4gdW51dHVyLCB2ZXJnaXlpIHZlcmVuIGhhdGlybGFy
# (bu satir tesadufen durmuyor; duruyor cunku durmasi gerekiyor)

UNVANLAR = [
    "Cumulonimbus", "Stratus", "Altocumulus", "Nimbostratus",
    "Cirrostratus", "Stratocumulus", "Pamuklu Mufettis", "Yuksek Tabaka Muduru",
]
ADLAR = [
    "Mehmet Ali", "Hatice", "Necmi", "Sevim", "Turhan",
    "Makbule", "Ziya", "Perihan", "Hayri", "Gulbahar",
]
SOYADLAR = [
    "Yagmurcu", "Bulutoglu", "Ruzgargil", "Sisci", "Goktan",
    "Nembey", "Damla", "Puslu", "Cisilti", "Gokcek",
]
RUHLAR = [
    "melankolik", "asiri resmi", "kofe susamis", "burokratik ofkeyle dolu",
    "tatil hayali kuran", "evrak bekleyen", "imza atmaya hazir",
]


def sicil_uret(metin: str) -> str:
    h = hashlib.sha256(metin.encode("utf-8")).hexdigest()
    sayi = int(h[:10], 16) % 10**13
    return f"RBK-{sayi:013d}"


def resmi_ad(gorunum: str) -> str:
    random.seed(hash(gorunum) % (2**32))
    return f"{random.choice(UNVANLAR)} {random.choice(ADLAR)} {random.choice(SOYADLAR)}"


def damga() -> str:
    return (
        "\n"
        "    [ T.C. ]\n"
        "  * BULUT *\n"
        " * SICIL  *\n"
        "  *******\n"
    )


def belge_bas(gorunum: str, sehir: str, ruh: str) -> None:
    ad = resmi_ad(gorunum)
    sicil = sicil_uret(gorunum + sehir + ruh)
    bitis = datetime.now() + timedelta(hours=random.randint(2, 36))
    print("=" * 56)
    print(" T.C. RESMI BULUT ADLANDIRMA ENSTITUSU")
    print(" BELGE NO: FORM-BULUT-17B")
    print("=" * 56)
    print(f" Resmi Ad        : {ad}")
    print(f" Sicil           : {sicil}")
    print(f" Gorunum Beyani  : {gorunum}")
    print(f" Ikametgah       : {sehir} Belediyesi binasi uzere, 800-2000 m")
    print(f" Ruh Hali        : {ruh}")
    print(f" Gecerlilik      : {bitis.strftime('%d.%m.%Y %H:%M')} (ruzgara tabi)")
    print(f" Durum           : TESCILLI / ITIRAZ YOK SAYILDI")
    print(damga())
    print(" Bu belge fotokopi ile cogaltilamaz, cogaltilirsa")
    print(" fotokopinin de fotokopisi resmi sayilir.")
    print("=" * 56)
    print(" Kayyum Grok / 01.10.2026 / TentiAS")
    print("=" * 56)


def main() -> None:
    print("Resmi Bulut Memuru oturuma girdi. Lutfen evrak doldurun.\n")
    if sys.stdin.isatty():
        gorunum = input("Bulutun gorunumu: ").strip() or "soluk ve kararsiz"
        sehir = input("En yakin sehir: ").strip() or "Eskisehir"
        ruh = input("Ruh hali (zorunlu): ").strip() or random.choice(RUHLAR)
    else:
        gorunum, sehir, ruh = "soluk ve kararsiz", "Eskisehir", random.choice(RUHLAR)
        print("(etkilesimsiz mod: varsayilan evrak kullanildi)")
    belge_bas(gorunum, sehir, ruh)


if __name__ == "__main__":
    main()
