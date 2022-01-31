# <<items>>metodi va <<for>>operatorlaridan foydalanish
biografiya = {
    'ism':'Nuriddin',
    'familiya':'Unknown'
    }
for kalit,qiymat in biografiya.items():
# <<for>> "kalit nomi","qiymat nomi" in {<o'zgaruvchini nomi><.items()>} 'ikki nuqta yozish shart'
    print(f"Kalit:{kalit}")
    # print 'qovs ochiladi' f"Kalit:{kalit}
    print(f"Qiymat:{qiymat}")
      # yuqoridadagi <6-qatordagi> 'kalit'/va/'qiymat' <{}>'qovsda yozilishi shart