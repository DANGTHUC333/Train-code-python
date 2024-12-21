from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ql_vemaybay"
)
window = Tk()
window.geometry("800x500")
window.title("Giao diện")
window.configure(background="light blue")
mycursor = mydb.cursor()

def dat_ve():
    def add():
        idve = entry_id_ve.get()
        idchuyenbay = inp_chuyen_bay.get()
        idkhach = entry_customer_id.get()
        soghetrong = entry_soghe.get()
        giave = entry_price.get()
        ngaymua = entry_date.get()

        if not idve or not idchuyenbay or not idkhach or not soghetrong or not giave or not ngaymua:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        # Kiểm tra số ghế đã tồn tại trong chuyến bay hay chưa
        sql_check_seat = "SELECT COUNT(*) FROM tickets WHERE idchuyenbay = %s AND soghetrong = %s"
        val_check_seat = (idchuyenbay, soghetrong)
        mycursor.execute(sql_check_seat, val_check_seat)
        result = mycursor.fetchone()
        if result and result[0] > 0:
            messagebox.showerror("Lỗi", "Số ghế đã tồn tại trong chuyến bay này!")
            return

        # Kiểm tra số ghế còn lại trong chuyến bay
        sql_check_remaining_seats = "SELECT soghe FROM flights WHERE id = %s"
        val_check_remaining_seats = (idchuyenbay,)
        mycursor.execute(sql_check_remaining_seats, val_check_remaining_seats)
        remaining_seats = mycursor.fetchone()

        if not remaining_seats or int(soghetrong) > remaining_seats[0]:
            messagebox.showerror("Lỗi", "Đã hết ghế trong chuyến bay!")
            return

        # Kiểm tra mã vé đã tồn tại chưa
        sql_check_ticket_id = "SELECT COUNT(*) FROM tickets WHERE id = %s"
        val_check_ticket_id = (idve,)
        mycursor.execute(sql_check_ticket_id, val_check_ticket_id)
        ticket_exists = mycursor.fetchone()

        if ticket_exists and ticket_exists[0] > 0:
            messagebox.showerror("Lỗi", "Mã vé đã tồn tại!")
            return

        # Thêm vé vào cơ sở dữ liệu
        sql_insert_ticket = "INSERT INTO tickets (id, idchuyenbay, idkhach, soghetrong, giave, ngaymua) VALUES (%s, %s, %s, %s, %s, %s)"
        val_insert_ticket = (idve, idchuyenbay, idkhach, soghetrong, giave, ngaymua)
        mycursor.execute(sql_insert_ticket, val_insert_ticket)
        mydb.commit()

        messagebox.showinfo("Thành Công", "Thêm vé thành công!")
        listbox.insert(END,
                       f"Mã vé: {idve} - Mã chuyến bay: {idchuyenbay} - Mã khách hàng: {idkhach} - Số ghế: {soghetrong} - Giá vé: {giave} - Ngày mua: {ngaymua}")

    from tkinter import messagebox

    def edit():
        id_ve = entry_id_ve.get()
        idchuyenbay = inp_chuyen_bay.get()
        idkhach = entry_customer_id.get()
        soghetrong = entry_soghe.get()
        giave = entry_price.get()
        ngaymua = entry_date.get()

        if not id_ve or not idchuyenbay or not idkhach or not soghetrong or not giave or not ngaymua:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        # Kiểm tra xem vé có tồn tại không
        sql_check_ticket = "SELECT * FROM tickets WHERE id=%s"
        mycursor.execute(sql_check_ticket, (id_ve,))
        if not mycursor.fetchone():
            messagebox.showerror("Lỗi", "Mã vé chưa tồn tại.")
            return

        # Thực hiện câu lệnh UPDATE để cập nhật thông tin vé
        sql_update_ticket = "UPDATE tickets SET idchuyenbay=%s, idkhach=%s, soghetrong=%s, giave=%s, ngaymua=%s WHERE id=%s"
        val = (idchuyenbay, idkhach, soghetrong, giave, ngaymua, id_ve)
        mycursor.execute(sql_update_ticket, val)
        mydb.commit()
        messagebox.showinfo("Thành Công", "Cập nhật vé thành công!")

    def delete():
        id_ve = entry_id_ve.get()

        if not id_ve:
            messagebox.showerror("Lỗi", "Vui lòng nhập mã vé.")
            return

        # Kiểm tra xem vé có tồn tại trong cơ sở dữ liệu không
        sql_check_ticket = "SELECT COUNT(*) FROM tickets WHERE id=%s"
        mycursor.execute(sql_check_ticket, (id_ve,))
        result = mycursor.fetchone()

        if not result or result[0] == 0:
            messagebox.showerror("Lỗi", "Mã vé không tồn tại!")
            return

        # Nếu vé tồn tại, tiến hành xóa
        sql_delete_ticket = "DELETE FROM tickets WHERE id=%s"
        mycursor.execute(sql_delete_ticket, (id_ve,))
        mydb.commit()
        messagebox.showinfo("Thành Công", "Xóa vé thành công!")

    def search():
        id_ve = entry_id_ve.get()

        if not id_ve:
            messagebox.showerror("Lỗi", "Vui lòng nhập mã vé.")
            return

        # Thực hiện câu truy vấn SQL để tìm vé theo mã vé
        sql_search_ticket = "SELECT * FROM tickets WHERE id=%s"
        mycursor.execute(sql_search_ticket, (str(id_ve),))
        danh_sach_ve = mycursor.fetchall()

        listbox.delete(0, END)  # Xóa danh sách hiện tại trong Listbox

        if danh_sach_ve:
            for ve in danh_sach_ve:
                info = (
                    f"Mã vé: {ve[0]} - Mã chuyến bay: {ve[1]} - Mã khách hàng: {ve[2]} - Số ghế trống: {ve[3]} - Giá vé: {ve[4]} - Ngày Mua: {ve[5]}")
                listbox.insert(END, info)
                listbox.insert(END, "")
        else:
            messagebox.showinfo("Không Tìm Thấy", "Không tìm thấy vé.")

    def show():
        mycursor.execute("SELECT * FROM tickets")
        danh_sach_ve = mycursor.fetchall()
        listbox.delete(0, END)
        if danh_sach_ve:
            for ve in danh_sach_ve:
                info = (
                    f"Mã vé: {ve[0]} - Mã chuyến bay: {ve[1]} - Mã khách hàng: {ve[2]} - Số ghế: {ve[3]} - Giá vé: {ve[4]} - Ngày Mua: {ve[5]}")
                listbox.insert(END, info)
                listbox.insert(END, "")  # Thêm một dòng trống sau mỗi thông tin vé
        else:
            messagebox.showinfo("Thông báo", "Không có dữ liệu vé nào trong cơ sở dữ liệu.")

    def clear_fields():
        entry_id_ve.delete(0, END)
        inp_chuyen_bay.set('')  # Xóa giá trị đã chọn trong Combobox
        entry_customer_id.delete(0, END)
        entry_soghe.delete(0, END)
        entry_price.delete(0, END)

    def layidchuyenbay():
        sql = f"SELECT id FROM flights"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        sx = [row[0] for row in result]
        return sx

    def lay_gia_ve(idchuyenbay):
        sql = "SELECT giave FROM flights WHERE id = %s"
        mycursor.execute(sql, (idchuyenbay,))
        result = mycursor.fetchone()
        return result[0] if result else None


    def on_chuyen_bay_select(event):
        selected_id = inp_chuyen_bay.get()
        giave = lay_gia_ve(selected_id)
        if giave is not None:
            entry_price.delete(0, END)
            entry_price.insert(0, str(giave))

    def tinh_tong_ve_thang(thang, nam):
        # Kiểm tra xem tháng và năm có được chọn không
        if not thang or not nam:
            messagebox.showerror("Lỗi", "Vui lòng chọn tháng và năm.")
            return

        # Thực hiện câu truy vấn SQL để tính tổng số vé bán được theo tháng và năm
        sql_tinh_tong_ve_thang = """
        SELECT COUNT(*) AS tong_so_ve
        FROM tickets
        WHERE MONTH(ngaymua) = %s AND YEAR(ngaymua) = %s
        """
        mycursor.execute(sql_tinh_tong_ve_thang, (thang, nam))
        ket_qua = mycursor.fetchone()

        # Hiển thị kết quả trong một thông báo
        if ket_qua and ket_qua[0] > 0:
            messagebox.showinfo("Kết Quả", f"Tổng số vé bán được trong tháng {thang}/{nam}: {ket_qua[0]} vé")
        else:
            messagebox.showinfo("Kết Quả", f"Không có vé bán được trong tháng {thang}/{nam}.")

    window = Tk()
    window.geometry("800x300")
    window.title("Quản Lý Đặt Vé")
    window.configure(background="light blue")

    label_id_ve = Label(window, text="Mã Vé:")
    label_id_ve.place(x=20, y=10, width=100, height=20)

    entry_id_ve = Entry(window)
    entry_id_ve.place(x=140, y=10, width=220, height=20)

    label_id_chuyen_bay = Label(window, text="Mã chuyến bay :")
    label_id_chuyen_bay.place(x=20, y=40, width=100, height=20)

    inp_chuyen_bay = ttk.Combobox(window)
    inp_chuyen_bay.place(x=140, y=40, width=220, height=20)
    inp_chuyen_bay['values'] = layidchuyenbay()
    inp_chuyen_bay.bind("<<ComboboxSelected>>", on_chuyen_bay_select)

    label_customer_id = Label(window, text="Mã khách hàng:")
    label_customer_id.place(x=20, y=70, width=100, height=20)

    entry_customer_id = Entry(window)
    entry_customer_id.place(x=140, y=70, width=220, height=20)

    label_soghe = Label(window, text="Số ghế:")
    label_soghe.place(x=20, y=100, width=100, height=20)

    entry_soghe = Entry(window)
    entry_soghe.place(x=140, y=100, width=220, height=20)

    label_price = Label(window, text="Giá vé:")
    label_price.place(x=20, y=130, width=100, height=20)

    entry_price = Entry(window)
    entry_price.place(x=140, y=130, width=220, height=20)

    label_date = Label(window, text="Năm/tháng/ngày: ")
    label_date.place(x=20, y=160, width=100, height=20)

    entry_date = Entry(window)
    entry_date.place(x=140, y=160, width=220, height=20)

    button_add = Button(window, text="Thêm", command=add)
    button_add.place(x=20, y=200, width=100, height=30)

    button_edit = Button(window, text="Sửa", command=edit)
    button_edit.place(x=140, y=200, width=100, height=30)

    button_delete = Button(window, text="Xóa", command=delete)
    button_delete.place(x=260, y=200, width=100, height=30)

    button_search = Button(window, text="Tìm Kiếm", command=search)
    button_search.place(x=20, y=240, width=100, height=30)

    button_clear = Button(window, text="Xóa Trường", command=clear_fields)
    button_clear.place(x=140, y=240, width=100, height=30)

    button_danh_sach = Button(window, text="Danh Sách", command=show)
    button_danh_sach.place(x=260, y=240, width=100, height=30)

    listbox = Listbox(window)
    listbox.place(x=380, y=10, width=400, height=260)

    # Thêm các widget chọn tháng và năm
    label_thang = Label(window, text="Chọn Tháng:")
    label_thang.place(x=20, y=280, width=100, height=20)

    combo_thang = ttk.Combobox(window, values=[str(i) for i in range(1, 13)])
    combo_thang.place(x=140, y=280, width=100, height=20)

    label_nam = Label(window, text="Chọn Năm:")
    label_nam.place(x=260, y=280, width=100, height=20)

    combo_nam = ttk.Combobox(window, values=[str(i) for i in range(2020, 2031)])
    combo_nam.place(x=380, y=280, width=100, height=20)

    # Thêm nút tính tổng số vé theo tháng
    button_tinh_tong_ve_thang = Button(window, text="Tổng Vé Tháng",
                                       command=lambda: tinh_tong_ve_thang(combo_thang.get(), combo_nam.get()))
    button_tinh_tong_ve_thang.place(x=500, y=280, width=100, height=30)

    window.mainloop()


# Hình ảnh demo
hinh_demo = PhotoImage(file="img.png")
label_logo = Label(window, image=hinh_demo)
label_logo.image = hinh_demo
label_logo.place(x=0, y=70, width=800, height=400)
lb1 = Label()
lb1.place(x=0, y=0, width=800, height=20)
lb1["bg"] = "white"

# Tạo các nút và cấu hình kích thước
button_chuyen_bay = Button(window, text="Chuyến bay", width=5, height=1)
button_hang = Button(window, text="Hãng", width=5, height=1)
button_khach_hang = Button(window, text="Khách hàng", width=5, height=1)
button_dat_ve = Button(window, text="Đặt vé", width=5, height=1, command=dat_ve)
button_doanh_thu = Button(window, text="Doanh thu", width=5, height=1)
button_help = Button(window, text="Help", width=5, height=1)


# Đặt các nút trên lưới (grid) và sử dụng sticky để kéo dài theo chiều ngang
button_chuyen_bay.grid(row=0, column=0, padx=5, pady=30, sticky="ew")
button_chuyen_bay.config(bg="Light Blue")
button_hang.grid(row=0, column=1, padx=5, pady=30, sticky="ew")
button_hang.config(bg="Light Blue")
button_khach_hang.grid(row=0, column=2, padx=5, pady=30, sticky="ew")
button_khach_hang.config(bg="Light Blue")
button_dat_ve.grid(row=0, column=3, padx=5, pady=30, sticky="ew")
button_dat_ve.config(bg="Light Blue")
button_doanh_thu.grid(row=0, column=4, padx=5, pady=30, sticky="ew")
button_doanh_thu.config(bg="Light Blue")
button_help.grid(row=0, column=5, padx=5, pady=30, sticky="ew")
button_help.config(bg="Light Blue")
# Cấu hình các cột để chúng có thể co giãn khi thay đổi kích thước cửa sổ
for i in range(5):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
