import matplotlib.pyplot as plt

# 使ったお金の種類と金額を入力させる。enterを押すまで種類を増やせる
categories = []
amounts = []

while True:
    category = input("使ったお金の種類を入力してください（追加後再Enterでグラフ作成開始します）: ")
    if category == "":
        break
    try:
        amount = float(input("金額を入力してください: "))
    except ValueError:
        print("無効な金額です。再度入力してください。")
        continue
    categories.append(category)
    amounts.append(amount)

# 種類ごとの金額を円グラフで表示
plt.figure(figsize=(8, 8))
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title("使ったお金の割合")
plt.show()