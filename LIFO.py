# 1. ADIM: İFADEYİ VE BOŞ YIĞINI (STACK) TANIMLIYORUZ ----
# Matematiksel karşılığı: 2 + (3 * 1) = 5
expression = ["2", "3", "1", "*", "+"]
stack = []

print(" Step-by-Step Stack Evaluation Started...\n")

#  2. ADIM: SAYILARI SIRAYLA YIĞINA EKLEYELİM ----
stack.append(int(expression[0])) # 2 eklendi
print("-> Pushed 2. Current Stack:", stack)

stack.append(int(expression[1])) # 3 eklendi
print("-> Pushed 3. Current Stack:", stack)

stack.append(int(expression[2])) # 1 eklendi
print("-> Pushed 1. Current Stack:", stack)


#  3. ADIM: İŞLEMLERİ YAPALIM (SON GİREN İLK ÇIKAR) ----
# [*] Çarpma işareti için son iki sayıyı (1 ve 3) çekip çarpıyoruz
num_b = stack.pop() 
num_a = stack.pop() 
stack.append(num_a * num_b)
print(f" [*] Operator: {num_a} * {num_b}. Current Stack:", stack)

# [+] Toplama işareti için kalan son iki sayıyı (3 ve 2) çekip topluyoruz
num_d = stack.pop() 
num_c = stack.pop() 
stack.append(num_c + num_d)
print(f" [+] Operator: {num_c} + {num_d}. Current Stack:", stack)


#  4. ADIM: SONUCU EKRANA YAZDIRMA ----
print("-" * 45)
print(" Evaluation Completed! Final Result:", stack.pop())