# MVC_65050831
model.py -> เก็บข้อมูลของวัวแต่ละ และฟังก์ชันที่เกี่ยวกับวัวแต่ละตัว 
controller.py -> ตัวควบคุมหลักของระบบที่เชื่อมโยงโมเดลกับการกระทำในส่วนผู้ใช้ 
view.py -> เป็นส่วนที่จัดการ UI
main.py -> ตัวที่รันแอปพลิเคชัน

การทำงานร่วมกัน
model.py เก็บข้อมูลของวัวและจัดการการกระทำที่เกี่ยวข้อง controller.py คอยรับการร้องขอจาก ผู้ใช้(view.py) และจัดการกับข้อมูลในโมเดล จากนั้นบันทึกการเปลี่ยนแปลงกลับไปยังไฟล์ JSON 
