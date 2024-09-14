import random

class BrownCow:
    def __init__(self, cow_id, age):
        """
        สร้างอ็อบเจ็กต์ของวัวสีน้ำตาล

        :param cow_id: รหัสของวัว
        :param age: อายุของวัว (หน่วยเป็นเดือน)
        """
        self.id = cow_id
        self.breed = 'น้ำตาล'
        self.age = age
        self.status = 'ปกติ'
        self.milk_count = {
            "ช็อกโกแลต": 0,
            "อัลมอนด์": 0,
        }

    def milk_cow(self):
        """
        รีดนมวัวและตรวจสอบสถานะของวัว

        :return: ข้อความผลลัพธ์และข้อมูลการผลิตนม
        """
        if self.status == 'BSOD':
            return "วัวอยู่ในสถานะ BSOD ไม่สามารถรีดนมได้", None

        # คำนวณโอกาสในการผลิตนมอัลมอนด์
        age_years = self.age // 12
        chance_of_almond_milk = 1 * age_years
        
        # ตัดสินใจว่าผลิตนมอัลมอนด์หรือไม่
        if random.random() * 100 < chance_of_almond_milk:
            self.status = 'BSOD'
            self.milk_count["อัลมอนด์"] += 1
            return "ผลิตนมอัลมอนด์ (ทิ้งไป) - วัวอยู่ในสถานะ BSOD", self.milk_count
        else:
            self.milk_count["ช็อกโกแลต"] += 1
            return "ผลิตนมช็อกโกแลต", self.milk_count

    def reset_status(self):
        """
        รีเซ็ตสถานะของวัว

        :return: ข้อความผลลัพธ์
        """
        self.status = 'ปกติ'
        return "วัวได้ถูกรีเซ็ตแล้ว"
