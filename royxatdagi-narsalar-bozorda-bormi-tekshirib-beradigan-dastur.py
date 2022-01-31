# <<Lug'at,for.if>>
  # foydalanib  bozorlik qilishda yordam beradigan dastur tuzildi
    # yani ro'yxatdagi narsalar bozorda bormi tekshirib beradigan dastur tuzildi
mahsulotlar = {
    'olma':'2 000',
    'o\'rik':'3 000',
    'nok':'2 000',
    'qovun':'8 000',
    'tarvuz':'8 000'
    }
bozorlik = ['olma', 'nok', 'go\'sht', 'baliq', 'qazi']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm ")

for kerakli in bozorlik:
    if kerakli not in mahsulotlar:
        print(f'Iltimos, do\'koningizga {kerakli.title()} ham olib keling')