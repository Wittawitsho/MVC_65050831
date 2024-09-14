import json #ใช้สำหรับการทำงานกับไฟล์ JSON
import random

#สร้าง class Cow ที่มีข้อมูลของวัวแต่ละตัว
class Cow:
    # ตัวแปรที่ใช้เก็บข้อมูลของวัวแต่ละตัว
    def __init__(self, id, color, age_years, age_months, milked_count=0, BSOD=False):
        self.id = id
        self.color = color #พันธุ์วัว
        self.age_years = age_years
        self.age_months = age_months
        self.milked_count = milked_count
        self.BSOD = BSOD
    
    #ฟังก์ชันที่ใช้รีดนมวัว
    def milk(self):
        if self.BSOD: #ถ้าวัวอยู่ในสถานะ BSOD
            return 'วัวผลิดน้ำนมไม่ได้'
        
        #กำหนดประเภทของนมตามสีของวัว
        if self.color == 'white':
            milk_type = 'นมจืด'
        elif self.color == 'brown':
            milk_type = 'นมช็อกโกแลต'
        elif self.color == 'whiteLime':
            milk_type = 'นมเปรี้ยว'
        else:
            return 'ไม่มีพันธุ์นี้'
        
         #เช็คว่าวัวอยู่ในสถานะ BSOD ก่อนเพิ่มจำนวนครั้งที่รีดนม
        self.check_BSOD()
        
        if not self.BSOD: #ถ้าวัวไม่อยู่ในสถานะ BSOD
            self.milked_count += 1  #เพิ่มจำนวนครั้งที่รีดนม
            return f"Produced {milk_type}" #ส่งข้อความผลลัพธ์ของการรีดนมวัวกลับไปยังฟังก์ชันที่เรียกใช้เพื่อบอกว่าการรีดนมนั้นสำเร็จ
        else:
            return 'วัวผลิตน้ำนมไม่ได้แล้ว'
    
    #ฟังก์ชันที่ใช้เพิ่มมะนาวให้กับวัวสีขาว
    def apply_lime(self):
        if self.color == 'white': #เฉพาะวัวสีขาวเท่านั้นที่สามารถเพิ่มมะนาวได้
            if not self.BSOD:
                self.milked_count += 1 
                return 'นมเปรี้ยว'
            else:
                return 'วัวผลิตน้ำนมไม่ได้แล้ว'
        return 'นมจืด'
    
     #ฟังก์ชันที่ใช้ตรวจสอบว่าวัวจะเข้าสถานะ BSOD หรือไม่
    def check_BSOD(self):
        if self.color == 'white':
            chance_of_BSOD = 0.005 * self.age_months 
        elif self.color == 'brown':
            chance_of_BSOD = 0.01 * self.age_years 
        else:
            chance_of_BSOD = 0
        #สุ่มค่าถ้าค่าน้อยกว่าโอกาสที่กำหนด วัวจะเข้าสถานะ BSOD
        if random.random() < chance_of_BSOD:
            self.BSOD = True
    #ฟังก์ชันสำหรับรีเซ็ตสถานะ BSOD ของวัว 
    def reset(self):
        self.BSOD = False

# ฟังก์ชันสำหรับโหลดข้อมูลวัวจากไฟล์ JSON
def load_cows(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return [Cow(**cow) for cow in data]
