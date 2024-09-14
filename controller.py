import json  
from model import load_cows  

#สร้างclass CowController เพื่อจัดการวัวและข้อมูลต่างๆ
class CowController:
    def __init__(self):
        self.cows = load_cows('cows.json')  #โหลดข้อมูลวัวจากไฟล์ cows.json และเก็บไว้ในตัวแปร cows
        self.current_cow = None  #เก็บวัวที่ถูกเลือกในปัจจุบัน
    
    #ฟังก์ชันเพื่อหาวัวตาม Cow ID
    def get_cow_by_id(self, cow_id):
        for cow in self.cows:  #วนลูปเพื่อตรวจสอบวัวแต่ละตัว
            if cow.id == cow_id:  
                return cow  
        return None 

    #ฟังก์ชันรีดนมวัว
    def milk_cow(self):
        if self.current_cow:  #ตรวจสอบว่ามีวัวถูกเลือกหรือไม่
            result = self.current_cow.milk()  #เรียกใช้ฟังก์ชัน milk ของวัวที่ถูกเลือก
            self.current_cow.check_BSOD()  # ตรวจสอบว่าวัวอยู่สถานะ BSOD ไหม
            self.save_cows()  #บันทึกสถานะปัจจุบันของวัวทั้งหมดลงไฟล์
            return result  #คืนค่าผลการรีดนม
        return "ไม่มีวัวถูกเลือก"  #คืนข้อความถ้าไม่มีวัวถูกเลือก
    
    #ฟังก์ชันวัวกินมะนาว
    def apply_lime(self):
        if self.current_cow:  
            result = self.current_cow.apply_lime()  
            self.current_cow.check_BSOD()  
            self.save_cows()  
            return result 
        return "ไม่มีวัวถูกเลือก"
    
    #ฟังก์ชันรีเซ็ตสถานะวัวที่ถูกเลือก
    def reset_cow(self):
        if self.current_cow: 
            self.current_cow.reset()  #เรียกใช้ฟังก์ชัน reset ของวัวที่ถูกเลือก
            self.save_cows()  
            return "วัวถูกรีเซ็ตแล้ว"  
        return "ไม่มีวัวถูกเลือก"  
    
    #ฟังก์ชันรีเซ็ตจำนวนการรีดนมของวัวทุกตัว
    def reset_milked_count(self):
        for cow in self.cows:  #วนลูปเพื่อรีเซ็ตการรีดนมของวัวทุกตัว
            cow.milked_count = 0 
        self.save_cows()  #บันทึกสถานะปัจจุบันของวัวทั้งหมดลงไฟล์

    #ฟังก์ชันรีเซ็ตสถานะ BSOD ของวัวทั้งหมด
    def reset_bsod(self):
        for cow in self.cows: 
            if cow.BSOD:  
                cow.reset()  
        self.save_cows() 

    # ฟังก์ชันบันทึกสถานะวัวทั้งหมดลงไฟล์ JSON
    def save_cows(self):
        with open('cows.json', 'w') as file:  
            json.dump([cow.__dict__ for cow in self.cows], file, indent=4)
