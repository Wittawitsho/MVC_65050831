import tkinter as tk  #โมดูลสร้าง GUI
from view import CowApp 
from controller import CowController


def main():
    root = tk.Tk()  #สร้างหน้าต่างหลักของ
    controller = CowController()  #จัดการข้อมูลวัว
    app = CowApp(root, controller)  #ส่วนติดต่อผู้ใช้
    root.mainloop()

if __name__ == "__main__":
    main()
