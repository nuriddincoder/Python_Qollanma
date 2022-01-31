# <<items,for,title>> metod va operatorlaridan foydalanish
biografiya = {
    'ism':'nuriddin',
    'familiya':'unknown',
    'noutbuk_nomi':'lenovo'
    }
for kalit,qiymat in biografiya.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat.title()}")