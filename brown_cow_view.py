import tkinter as tk
from tkinter import messagebox

class BrownCowGUI:
    def __init__(self, root, cow):
        self.root = root
        self.cow = cow
        self.setup_screen()

    def setup_screen(self):
        self.root.title("วัวสีน้ำตาล")
        self.create_cow_screen()

    def create_cow_screen(self):
        tk.Label(self.root, text=f"รหัสวัว: {self.cow.id}\nพันธุ์: {self.cow.breed}\nอายุ: {self.cow.age} ปี", font=('Arial', 16)).pack(pady=20)
        self.add_buttons()

    def add_buttons(self):
        tk.Button(self.root, text="รีดนม", command=self.milk_cow, font=('Arial', 14)).pack(pady=10)
        tk.Button(self.root, text="รีเซ็ต", command=self.reset_status, font=('Arial', 14)).pack(pady=10)
        tk.Button(self.root, text="ดูรายงาน", command=self.show_report, font=('Arial', 14)).pack(pady=10)
        tk.Button(self.root, text="กลับไปหน้าหลัก", command=self.back_to_main, font=('Arial', 14)).pack(pady=10)

    def milk_cow(self):
        result, _ = self.cow.milk_cow()
        messagebox.showinfo("ผลลัพธ์การรีดนม", result)
        if self.cow.status == 'BSOD':
            messagebox.showwarning("สถานะ BSOD", "วัวอยู่ในสถานะ BSOD (ผลิตนมไม่ได้) - ต้องรีเซ็ต")
        self.show_report()

    def reset_status(self):
        messagebox.showinfo("สถานะรีเซ็ต", self.cow.reset_status())

    def show_report(self):
        milk_count = self.cow.milk_count
        report = (f"รายงานการผลิตนม:\n"
                  f"นมช็อกโกแลต: {milk_count['ช็อกโกแลต']} ขวด\n"
                  f"นมอัลมอนด์: {milk_count['อัลมอนด์']} ขวด\n"
                  f"รวม: {sum(milk_count.values())} ขวด\n")
        messagebox.showinfo("รายงานการผลิตนม", report)
        if self.cow.status == 'BSOD':
            tk.Button(self.root, text="รีเซ็ตวัวทั้งหมด", command=self.reset_all_cows, font=('Arial', 14)).pack(pady=10)

    def reset_all_cows(self):
        self.cow.reset_status()
        messagebox.showinfo("สถานะรีเซ็ต", "วัวทั้งหมดได้ถูกรีเซ็ตแล้ว")

    def back_to_main(self):
        self.clear_screen()
        from main import CowGUI
        CowGUI(self.root)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
