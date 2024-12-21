import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import date

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345a.",
        database="quan_ly_ve_may_bay"
    )

def them_hang():
    ten_hang = entry_hang.get()
    if ten_hang:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO hang (ten_hang) VALUES (%s)", (ten_hang,))
        db.commit()
        db.close()
        messagebox.showinfo("Thành công", "Đã thêm hãng hàng không")
        entry_hang.delete(0, tk.END)
        update_hang_combobox()
    else:
        messagebox.showwarning("Cảnh báo", "Tên hãng không được để trống")

def them_chuyen_bay():
    ten_chuyen_bay = entry_chuyen_bay.get()
    hang_id = hang_combobox.current() + 1
    if ten_chuyen_bay and hang_id:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO chuyen_bay (ten_chuyen_bay, hang_id) VALUES (%s, %s)", (ten_chuyen_bay, hang_id))
        db.commit()
        db.close()
        messagebox.showinfo("Thành công", "Đã thêm chuyến bay")
        entry_chuyen_bay.delete(0, tk.END)
        update_chuyen_bay_combobox()
    else:
        messagebox.showwarning("Cảnh báo", "Tên chuyến bay và hãng không được để trống")

def them_khach():
    ten_khach = entry_khach.get()
    cmnd = entry_cmnd.get()
    if ten_khach and cmnd:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO khach (ten_khach, cmnd) VALUES (%s, %s)", (ten_khach, cmnd))
        db.commit()
        db.close()
        messagebox.showinfo("Thành công", "Đã thêm khách hàng")
        entry_khach.delete(0, tk.END)
        entry_cmnd.delete(0, tk.END)
        update_khach_combobox()
    else:
        messagebox.showwarning("Cảnh báo", "Tên khách và CMND không được để trống")

def dat_ve():
    khach_id = khach_combobox.current() + 1
    chuyen_bay_id = chuyen_bay_combobox.current() + 1
    ngay_dat = entry_ngay_dat.get()
    if khach_id and chuyen_bay_id and ngay_dat:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO dat_ve (khach_id, chuyen_bay_id, ngay_dat) VALUES (%s, %s, %s)", (khach_id, chuyen_bay_id, ngay_dat))
        db.commit()
        db.close()
        messagebox.showinfo("Thành công", "Đã đặt vé")
        entry_ngay_dat.delete(0, tk.END)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin")

def them_doanh_thu():
    thang = entry_thang.get()
    nam = entry_nam.get()
    tong_doanh_thu = entry_tong_doanh_thu.get()
    if thang and nam and tong_doanh_thu:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO doanh_thu (thang, nam, tong_doanh_thu) VALUES (%s, %s, %s)", (thang, nam, tong_doanh_thu))
        db.commit()
        db.close()
        messagebox.showinfo("Thành công", "Đã thêm doanh thu")
        entry_thang.delete(0, tk.END)
        entry_nam.delete(0, tk.END)
        entry_tong_doanh_thu.delete(0, tk.END)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin")

def lay_danh_sach_hang():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hang")
    result = cursor.fetchall()
    db.close()
    return result

def lay_danh_sach_khach():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM khach")
    result = cursor.fetchall()
    db.close()
    return result

def lay_danh_sach_chuyen_bay():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM chuyen_bay")
    result = cursor.fetchall()
    db.close()
    return result

def update_hang_combobox():
    hang_combobox['values'] = [hang[1] for hang in lay_danh_sach_hang()]

def update_khach_combobox():
    khach_combobox['values'] = [khach[1] for khach in lay_danh_sach_khach()]

def update_chuyen_bay_combobox():
    chuyen_bay_combobox['values'] = [chuyen_bay[1] for chuyen_bay in lay_danh_sach_chuyen_bay()]

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý vé máy bay")

# Tab control
tab_control = ttk.Notebook(root)

tab_hang = ttk.Frame(tab_control)
tab_chuyen_bay = ttk.Frame(tab_control)
tab_khach = ttk.Frame(tab_control)
tab_dat_ve = ttk.Frame(tab_control)
tab_doanh_thu = ttk.Frame(tab_control)

tab_control.add(tab_hang, text='Quản lý hãng')
tab_control.add(tab_chuyen_bay, text='Quản lý chuyến bay')
tab_control.add(tab_khach, text='Quản lý khách hàng')
tab_control.add(tab_dat_ve, text='Quản lý đặt vé')
tab_control.add(tab_doanh_thu, text='Quản lý doanh thu')

tab_control.pack(expand=1, fill='both')

# Quản lý hãng
frame_hang = tk.Frame(tab_hang)
frame_hang.pack(padx=10, pady=10)

tk.Label(frame_hang, text="Tên hãng hàng không:").grid(row=0, column=0, pady=5)
entry_hang = tk.Entry(frame_hang)
entry_hang.grid(row=0, column=1, pady=5)
tk.Button(frame_hang, text="Thêm hãng", command=them_hang).grid(row=1, column=1, pady=10)

# Quản lý chuyến bay
frame_chuyen_bay = tk.Frame(tab_chuyen_bay)
frame_chuyen_bay.pack(padx=10, pady=10)

tk.Label(frame_chuyen_bay, text="Tên chuyến bay:").grid(row=0, column=0, pady=5)
entry_chuyen_bay = tk.Entry(frame_chuyen_bay)
entry_chuyen_bay.grid(row=0, column=1, pady=5)

tk.Label(frame_chuyen_bay, text="Hãng:").grid(row=1, column=0, pady=5)
hang_combobox = ttk.Combobox(frame_chuyen_bay)
hang_combobox.grid(row=1, column=1, pady=5)
update_hang_combobox()

tk.Button(frame_chuyen_bay, text="Thêm chuyến bay", command=them_chuyen_bay).grid(row=2, columnspan=2, pady=10)

# Quản lý khách hàng
frame_khach = tk.Frame(tab_khach)
frame_khach.pack(padx=10, pady=10)

tk.Label(frame_khach, text="Tên khách hàng:").grid(row=0, column=0, pady=5)
entry_khach = tk.Entry(frame_khach)
entry_khach.grid(row=0, column=1, pady=5)

tk.Label(frame_khach, text="CMND:").grid(row=1, column=0, pady=5)
entry_cmnd = tk.Entry(frame_khach)
entry_cmnd.grid(row=1, column=1, pady=5)

tk.Button(frame_khach, text="Thêm khách hàng", command=them_khach).grid(row=2, columnspan=2, pady=10)

# Quản lý đặt vé
frame_dat_ve = tk.Frame(tab_dat_ve)
frame_dat_ve.pack(padx=10, pady=10)

tk.Label(frame_dat_ve, text="Khách hàng:").grid(row=0, column=0, pady=5)
khach_combobox = ttk.Combobox(frame_dat_ve)
khach_combobox.grid(row=0, column=1, pady=5)
update_khach_combobox()

tk.Label(frame_dat_ve, text="Chuyến bay:").grid(row=1, column=0, pady=5)
chuyen_bay_combobox = ttk.Combobox(frame_dat_ve)
chuyen_bay_combobox.grid(row=1, column=1, pady=5)
update_chuyen_bay_combobox()

tk.Label(frame_dat_ve, text="Ngày đặt (YYYY-MM-DD):").grid(row=2, column=0, pady=5)
entry_ngay_dat = tk.Entry(frame_dat_ve)
entry_ngay_dat.grid(row=2, column=1, pady=5)

tk.Button(frame_dat_ve, text="Đặt vé", command=dat_ve).grid(row=3, columnspan=2, pady=10)

# Quản lý doanh thu
frame_doanh_thu = tk.Frame(tab_doanh_thu)
frame_doanh_thu.pack(padx=10, pady=10)

tk.Label(frame_doanh_thu, text="Tháng:").grid(row=0, column=0, pady=5)
entry_thang = tk.Entry(frame_doanh_thu)
entry_thang.grid(row=0, column=1, pady=5)

tk.Label(frame_doanh_thu, text="Năm:").grid(row=1, column=0, pady=5)
entry_nam = tk.Entry(frame_doanh_thu)
entry_nam.grid(row=1, column=1, pady=5)

tk.Label(frame_doanh_thu, text="Tổng doanh thu:").grid(row=2, column=0, pady=5)
entry_tong_doanh_thu = tk.Entry(frame_doanh_thu)
entry_tong_doanh_thu.grid(row=2, column=1, pady=5)

tk.Button(frame_doanh_thu, text="Thêm doanh thu", command=them_doanh_thu).grid(row=3, columnspan=2, pady=10)

# Chạy ứng dụng
root.mainloop()
