import tkinter as tk
from cow_gui_view import CowGUI # Import GUI View หลัก

if __name__ == "__main__":

    # สร้างหน้าต่าง root ของ tkinter
    root = tk.Tk()
    
    # เริ่ม GUI
    app = CowGUI(root)
    
    # รัน loop ของ tkinter
    root.mainloop()
  