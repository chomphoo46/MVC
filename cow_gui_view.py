import tkinter as tk
from tkinter import messagebox
from white_cow_view import WhiteCowGUI
from white_cow_model import WhiteCow
from brown_cow_model import BrownCow
from brown_cow_view import BrownCowGUI

class CowGUI:
    def __init__(self, root):
        self.root = root
        self.current_cow = None
        self.setup_main_window()

    def setup_main_window(self):
        self.root.title("ระบบตรวจสอบข้อมูลวัว")
        self.root.geometry("600x400")
        self.create_main_screen()

    def create_main_screen(self):
        tk.Label(self.root, text="กรุณาใส่รหัสวัว:", font=('Arial', 16)).pack(pady=20)
        self.entry = tk.Entry(self.root, font=('Arial', 14))
        self.entry.pack(pady=10)
        tk.Button(self.root, text="ตรวจสอบ", command=self.check_cow, font=('Arial', 14)).pack(pady=20)

    def check_cow(self):
        cow_id = self.entry.get().strip()
        if not self.is_valid_cow_id(cow_id):
            messagebox.showerror("ข้อผิดพลาด", "รหัสวัวต้องเป็นตัวเลข 8 หลัก และไม่ขึ้นต้นด้วยเลข 0")
            return

        cow = self.find_cow_by_id(cow_id)
        if cow:
            self.current_cow = cow
            self.clear_screen()
            self.open_cow_screen(cow)
        else:
            messagebox.showerror("ไม่พบข้อมูล", "ไม่พบข้อมูลวัวที่มีรหัสนี้")

    def is_valid_cow_id(self, cow_id):
        return cow_id.isdigit() and len(cow_id) == 8 and cow_id[0] != '0'

    def find_cow_by_id(self, cow_id):
        if cow_id.startswith('1'):
            return WhiteCow(cow_id, 5)
        elif cow_id.startswith('2'):
            return BrownCow(cow_id, 5)
        return None

    def open_cow_screen(self, cow):
        if cow.breed == 'ขาว':
            WhiteCowGUI(self.root, cow)
        else:
            BrownCowGUI(self.root, cow)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    CowGUI(root)
    root.mainloop()
