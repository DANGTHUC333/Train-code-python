import random
#1. Nhập vào một hội thoại giao tiếp ngắn gọn.
import math


def bai1():
      print("""Hello A\n
            Hi B
            nice to meet you
            nice to meet you too""")


#2. Tính diện tích hình chữ nhật, hình vuông, hình bình hành và hình thang cân.
def bai2():
      #dien tich hinh chư nhat
      print("Tính diện tích hình chữ nhật")
      a = int(input("Nhập a: "))
      b = int(input("Nhập b: "))
      s = a * b
      print("S HCN Là: ", s)

      #dien tich hình vuông
      print("Tính diện tích hình vuông")
      a = int(input("Nhập a: "))
      s = a * a
      print("S HV Là: ", s)

      #dien tich hình bình hành
      print("Tính diện tích hình bình hành")
      a = int(input("Nhập a: "))
      h = int(input("Nhập h: "))
      s = a * h
      print("S HBH Là: ", s)

      #dien tich hinh thang can
      print("Tính diện tích hình thang cân")
      a = int(input("Nhập vào đáy lớn: "))
      b = int(input("Nhập vào độ dài đáy nhỏ: "))
      h = int(input("Nhập vào chiều cao: "))
      s = ((a + b)*h)/2
      print("S HTC Là: ", s)

#3.    Tính chu vi và diện tích hình tròn, hình tam giác. Kiểm tra điều kiện của chúng.
def bai3():
      print("Tính chu vi hình  và diện tích hình tròn")
      r = int(input("Nhập bán khính: "))
      if r > 0:
            c = 2 * math.pi * r
            s = math.pi * r**2
            print("Chu vi hình tròn là: ", c)
            print("Diện tích hình tròn là: ", s)
      else:
            print("Không thể tính được")

      print("Tính chu vi và diện tích hình tam giác")
      a = int(input("Nhập a: "))
      b = int(input("Nhập b: "))
      c = int(input("Nhập c: "))
      if a > 0 and b > 0 and c > 0 and  (a + b > c) and (a + c > b) and (c + b > a):
            P = a + b +c
            print("Chu vi hình tam giác là: ", P)
            p = (a + b + c)/2
            s = math.sqrt((p-a) * (p -b) * (p-c))
            print("Diện tích hình tam giác là: ", s)
      else:
            print("Không thỏa mãn điều kiện")
# Nhập vào một số tự nhiên bất kỳ, kiểm tra số chẵn lẻ?
def bai4():
      a = int(input("Nhập số bất kì: "))
      if a % 2 == 0:
            print(a, " Là Số Chẵn ")
      else:
            print(a, "Là số lẻ")

#5.    Tìm số lớn nhất trong 3 số được nhập từ bàn phím
def bai5():
      # ham max_value de tim' so' lon' nhat'
      a = int(input("Nhập số bất kỳ 1: "))
      b = int(input("Nhập số bất kỳ 2: "))
      c = int(input("Nhập số bất kỳ 3: "))
      max_value = max(a,b,c)
      print("Số lon nhat trong 3 so la: ", max_value)

#6.    Tính chi phí sinh hoạt hàng tháng của bạn
def bai6():
      a = int(input("Nhap tien tro: "))
      b = int(input("Nhap tien an: "))
      c = int(input("Nhap tien di lai: "))
      s = a + b + c
      print("Tien sinh hoat cua ban la: ", s)

#7.    Nhập điểm các môn học kỳ này của 5 bạn và cho biết bạn nào có điểm cao và thấp nhất?
def bai7():
      S = []

      for i in range(5):
            n = input(f"Nhap ten{i + 1}: ")
            p = float(input(f"Nhap diem{n}: "))
            S.append((n, p))

      max_s = max(S, key=lambda x: x[1])
      min_s = min(S, key=lambda x: x[1])

      print(f"Bạn có điểm cao nhất là {max_s[0]} với điểm {max_s[1]}")
      print(f"Bạn có điểm thap nhất là {min_s[0]} với điểm {min_s[1]}")

#8.    Viết chương trình chuyển đôi qua lại giữ Km -> mm
def bai8():
      n = int(input("Nhap so can doi: "))
      c = input("Chọn đơn vị (km hoặc mm): ").strip().lower()
      if c ==  "km":
            result = n * 1000000
            print("km:", result)
      elif c == "mm":
            result = n / 1000000
            print("mm:", result)
      else:
            print("Nhap khong dung")

#9.    In ra bảng cửu chương theo phong cách của bạn?
def bai9():
      n = int(input("Nhap bang cuu chuong: "))
      for i in range(1, 11):
            a = n * i
            print(f"{n} x {i} = {a} ")

#10.    Nhập vào một số và kiểm tra xem có phải là số nguyên tố không?

def bai10():
      n = int(input("Nhập số bất kỳ: "))
      if n > 1:
            for i in range(2, int(n**0.5)+1):  # Kiểm tra từ 2 đến căn bậc hai của n
                  if n % i == 0:
                        print(f"{n} không phải số nguyên tố")
                        return
            print(f"{n} là số nguyên tố")
      else:
            print(f"{n} không phải số nguyên tố")

#11.    Tính giai thừa của n, với n nhập từ bàn phím.

def bai11():
      n = int(input("Nhập số bất kỳ: "))
      if n == 0 or n == 1:
            print(f"Kết quả là: 1") # trường hợp đặc biệt

      result = 1
      for i in range(2, n + 1):
            result = result * i
      print(f"Kết quả là: {result}")

#12.    Viết chương trình trò chơi đoán số vừa nhập, cho đoán tối đa 5 lần.
def bai12():
      print("Nhâp số từ 1-10, Có 5 lần đoán")
      n = random.randint(1,10)
      landoan = 0
      while landoan < 5:
            try:
                  doan = int(input(f"Lần đoán {landoan + 1}, Nhấp số: "))
                  if doan < 0 or doan > 10:
                        print("Nhập sai")
                        continue
                  if doan == n:
                        print(f"Đáp án {doan} là đúng")
                        return
                  elif doan < n:
                        print("Số bạn đoán nhỏ hơn đáp án.")
                  else:
                        print("Số bạn đoán lớn hơn đáp án.")

                  landoan = landoan + 1

            except ValueError:
                  print("Vui lòng nhập đúng")

      print(f"Bạn đã hết lượt, đáp án đúng là: {n}")

#13.    Nhập vào một danh sách và cho biết danh sách đó có bao nhiêu số lẻ và số chẵn?

def bai13():
      n = list(map(int, input("Nhập các số, cách nhau bởi khoảng trắng: ").split()))

      chan = sum(1 for x in n if x % 2 == 0) #tìm số chẵn
      le = len(n) - chan # số lẻ bằng số chẵn - lẻ

      print(f"Số chắn là: {chan}, Số lẻ là: {le}")

#14.     Tìm số nhỏ nhất trong danh sách
def bai14():
      n = list(map(int, input("Nhập các số, cách nhau bởi khoảng trắng: ").split()))
      M = min(n)
      print(f"Số nhỏ nhất trong danh sách là:{M}")

#15.    Tìm số lớn nhất trong danh sách
def bai15():
      n = list(map(int,input("Nhập các số, cách nhau bở khoảng trắng: ").split()))
      M = max(n)
      print(f"Số lớn nhất trong danh sách là:{M} ")




def Exit():
      exit()
while True:

      chon = int(input("Chọn chức năng: "))
      if chon == 0:
            Exit()
      if chon == 1:
            bai1()
      if chon == 2:
            bai2()
      if chon == 3:
            bai3()
      if chon == 4:
            bai4()
      if chon == 5:
            bai5()
      if chon == 6:
            bai6()
      if chon == 7:
            bai7()
      if chon == 8:
            bai8()
      if chon == 9:
            bai9()
      if chon == 10:
            bai10()
      if chon == 11:
            bai11()
      if chon == 12:
            bai12()
      if chon == 13:
            bai13()
      if chon == 14:
            bai14()
      if chon == 15:
            bai15()

      break