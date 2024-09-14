import tkinter as tk #ใช้สร้าง GUI
from tkinter import messagebox #ใช้แสดง pop up

#สร้างคลาส CowApp สำหรับจัดการ interface ผู้ใช้
class CowApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.all_milk_count = 0  #เพิ่มตัวแปรสำหรับนมทั้งหมด

        #ตั้งค่าหน้าจอ
        self.root.geometry("800x600")
        self.root.title("Cow Milk System")

        #ฟอนต์
        self.large_font = ("Arial", 16)
        self.medium_font = ("Arial", 14)

        self.create_main_screen()
    
    def create_main_screen(self):
        self.clear_screen()

        
        self.label = tk.Label(self.root, text="Enter Cow ID:", font=self.large_font)
        self.label.pack(pady=100)
        
        self.entry = tk.Entry(self.root, font=self.large_font, width=20)
        self.entry.pack(pady=5)
        
        #ปุ่ม Submit, Reset, Reset Milk Count และ Reset BSOD
        self.submit_button = tk.Button(self.root, text="Submit", font=self.medium_font, command=self.check_cow)
        self.submit_button.pack(side=tk.LEFT, padx=50, pady=20)
        
        self.reset_button = tk.Button(self.root, text="Reset", font=self.medium_font, command=self.reset_all)
        self.reset_button.pack(side=tk.LEFT, padx=50, pady=20)
        
        self.reset_milked_count_button = tk.Button(self.root, text="Reset Milk Count", font=self.medium_font, command=self.reset_milked_count)
        self.reset_milked_count_button.pack(side=tk.LEFT, padx=50, pady=20)
        
        self.reset_bsod_button = tk.Button(self.root, text="Reset BSOD", font=self.medium_font, command=self.reset_bsod)
        self.reset_bsod_button.pack(side=tk.LEFT, padx=10)
    
    #หน้าจอวัวที่เลือก
    def create_cow_info_screen(self, cow):
        self.clear_screen()

        #แสดงข้อมูลของวัวที่เลือก
        self.info_label = tk.Label(self.root, text=f"Cow ID: {cow.id}\nColor: {cow.color}\nAge: {cow.age_years} years and {cow.age_months} months\nจำนวนนม: {cow.milked_count}", font=self.large_font)
        self.info_label.pack(pady=10)
        
        #แสดงจำนวนนมทั้งหมด
        self.all_milk_count_label = tk.Label(self.root, text=f"จำนวนนมทั้งหมด: {self.all_milk_count}", font=self.large_font)
        self.all_milk_count_label.pack(pady=10)
        
        #ถ้าวัวสีขาวแสดงปุ่มรีดนมและปุ่มเพิ่มมะนาว
        if cow.color == 'white':
            self.milk_button = tk.Button(self.root, text="รีดนม", font=self.medium_font, command=self.milk_cow)
            self.milk_button.pack(side=tk.LEFT, padx=100)
            
            self.lime_button = tk.Button(self.root, text="กินมะนาว", font=self.medium_font, command=self.go_to_lime_cow_info_screen)
            self.lime_button.pack(side=tk.LEFT, padx=100)
        #ถ้าวัวสีน้ำตาลแสดงแค่ปุ่มรีดนม
        elif cow.color == 'brown':
            self.milk_button = tk.Button(self.root, text="รีดนม", font=self.medium_font, command=self.milk_cow)
            self.milk_button.pack(side=tk.LEFT, padx=100)

        #ปุ่ม Back กลับหน้าหลัก
        self.back_button = tk.Button(self.root, text="Back", font=self.medium_font, command=self.create_main_screen)
        self.back_button.pack(side=tk.LEFT, padx=100)
    
    #หน้าจอสำหรับวัวที่เพิ่มมะนาว
    def create_lime_cow_screen(self, cow):
        self.clear_screen()

        #แสดงข้อมูลวัวที่กินมะนาว
        self.info_label = tk.Label(self.root, text=f"Cow ID: {cow.id}\nColor: {cow.color}\nAge: {cow.age_years} years and {cow.age_months} months\nจำนวนนม: {cow.milked_count}\n\nวัวกินมะนาว", font=self.large_font)
        self.info_label.pack(pady=10)
        
        #แสดงจำนวนนมทั้งหมด
        self.all_milk_count_label = tk.Label(self.root, text=f"จำนวนนมทั้งหมด: {self.all_milk_count}", font=self.large_font)
        self.all_milk_count_label.pack(pady=10)
        
        #ปุ่มรีดนม
        self.milk_button = tk.Button(self.root, text="รีดนม", font=self.medium_font, command=self.milk_cow_from_lime_screen)
        self.milk_button.pack(side=tk.LEFT, padx=100)
        
        #ปุ่ม Back
        self.back_button = tk.Button(self.root, text="Back", font=self.medium_font, command=self.create_main_screen)
        self.back_button.pack(side=tk.LEFT, padx=100)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def check_cow(self):
        cow_id = self.entry.get()
        cow = self.controller.get_cow_by_id(cow_id)
        if cow:
            self.controller.current_cow = cow
            self.create_cow_info_screen(cow)
        else:
            messagebox.showerror("Error", "ไม่พบ ID")

    #ฟังก์ชันรีดนมวัว
    def milk_cow(self):
        if self.controller.current_cow and not self.controller.current_cow.BSOD:  #ถ้าวัวไม่เสีย
            result = self.controller.milk_cow()  #เรียกฟังก์ชันรีดนมจาก controller
            self.all_milk_count += 1  # เพิ่มจำนวนนมทั้งหมด
            self.create_cow_info_screen(self.controller.current_cow)  #อัปเดตหน้าจอแสดงข้อมูลวัว
            messagebox.showinfo("Info", result)  #แสดงผลการรีดนม
        elif self.controller.current_cow.BSOD:  #ถ้าวัวเสีย
            messagebox.showinfo("Info", "วัวผลิตน้ำนมไม่ได้แล้ว")  #แสดงข้อความว่าวัวเสีย

    #ฟังก์ชันรีดนมวัวในหน้าจอที่ใส่มะนาว
    def milk_cow_from_lime_screen(self):
        if self.controller.current_cow and not self.controller.current_cow.BSOD:
            result = self.controller.milk_cow()  
            self.all_milk_count += 1 
            self.create_lime_cow_screen(self.controller.current_cow) 
            messagebox.showinfo("Info", result) 
        elif self.controller.current_cow.BSOD:  
            messagebox.showinfo("Info", "วัวผลิตน้ำนมไม่ได้แล้ว")

    # ฟังก์ชันเปลี่ยนหน้าจอไปยังหน้าข้อมูลวัวที่กินมะนาว
    def go_to_lime_cow_info_screen(self):
        if self.controller.current_cow:
            self.controller.current_cow.color = 'whiteUp'
            self.create_lime_cow_screen(self.controller.current_cow)  #แสดงหน้าจอที่เพิ่มมะนาว

    # ฟังก์ชันรีเซ็ตข้อมูลทั้งหมด
    def reset_all(self):
        self.controller.reset_cow()  #รีเซ็ตข้อมูลวัวจาก controller
        self.controller.reset_milked_count()  #รีเซ็ตจำนวนรีดนม
        self.controller.reset_bsod()  #รีเซ็ตสถานะ BSOD
        self.all_milk_count = 0  #รีเซ็ตจำนวนนมทั้ังหมด
        messagebox.showinfo("Info", "รีเซ็ตข้อมูลเรียบร้อย")  #แจ้งผู้ใช้ว่าข้อมูลถูกรีเซ็ตแล้ว
        self.create_main_screen()  #กลับไปยังหน้าหลัก

    # ฟังก์ชันรีเซ็ตจำนวนการรีดนม
    def reset_milked_count(self):
        self.controller.reset_milked_count()  #รีเซ็ตจำนวนรีดนม
        for cow in self.controller.cows:  #วนลูปเพื่อตรวจสอบวัวที่เป็นพันธุ์ whiteUp
            if cow.color == 'whiteUp':
                cow.color = 'white'  #เปลี่ยนกลับเป็น white
        self.all_milk_count = 0  #รีเซ็ตจำนวนนมทั้งหมด
        messagebox.showinfo("Info", "จำนวนนมถูกรีเซ็ตแล้ว")  #แจ้งผู้ใช้ว่าจำนวนนมถูกรีเซ็ตแล้ว
        self.create_main_screen()  #กลับไปยังหน้าหลัก

    # ฟังก์ชันรีเซ็ตสถานะ BSOD
    def reset_bsod(self):
        self.controller.reset_bsod()  # เรียกฟังก์ชันรีเซ็ตBSOD จาก controller
        messagebox.showinfo("Info", "รีเซ็ตวัวที่เสียแล้ว")  #แจ้งผู้ใช้ว่ารีเซ็ตวัวที่เสียแล้ว
        self.create_main_screen()  #กลับไปยังหน้าหลัก
