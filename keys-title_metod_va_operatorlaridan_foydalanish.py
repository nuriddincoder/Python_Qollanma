# <<keys/va/title>> metod va operatorlaridan foydalanish
print('Do\'kondagi Mahsulotlar')
mahsulotlar = {
    'olma':'2 000',
    'o\'rik':'3 000',
    'nok':'2 000'
    }
for mahsulot in mahsulotlar.keys(): 
# eslatma
  # <<keys>>metodidan foydalansa ham foydalanmasa ham natija bir xil chiqadi 
    print(mahsulot.title())