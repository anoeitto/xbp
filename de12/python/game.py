print("大切な試合の最後のPKの場面だ!")
name=input("プレイヤー名を入れてね")
print(name,"さんはラストのキッカー！")
point=0

for i in range(1,6):
 print(i,"回目")
 print("1.右　2.真ん中　3.左")
 select=int(input("コースを数字で選んでね"))

import random
a = random.randint(1,3)
print("キーパーが選んだのは",a)
if select==a:
   print("止められた...")
else:
  print("ナイスシュート")
  point=point+1

if point>=4:
  print(name,"さんの結果は",point,"点で勝利！")
elif point<=3:
 print(name,"さんの結果は",point,"点で敗北")