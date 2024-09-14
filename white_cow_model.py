import random

class WhiteCow:
    def __init__(self, cow_id, age):
        self.id = cow_id
        self.breed = 'ขาว'
        self.age = age
        self.status = 'ปกติ'
        self.has_lemon = False
        self.milk_count = {"จืด": 0, "เปรี้ยว": 0, "ถั่วเหลือง": 0}

    def milk_cow(self):
        if self.status == 'BSOD':
            return "วัวอยู่ในสถานะ BSOD ไม่สามารถรีดนมได้", None

        if self.has_lemon:
            self.milk_count["เปรี้ยว"] += 1
            return "ผลิตนมเปรี้ยว (ไม่เกิดสถานะ BSOD)", self.milk_count

        age_years, age_months = divmod(self.age, 12)
        chance_of_soy_milk = 0.5 * age_months

        if random.random() * 100 < chance_of_soy_milk:
            self.status = 'BSOD'
            self.milk_count["ถั่วเหลือง"] += 1
            return "ผลิตนมถั่วเหลือง (ทิ้งไป) - วัวอยู่ในสถานะ BSOD", self.milk_count

        self.milk_count["จืด"] += 1
        return "ผลิตนมจืด", self.milk_count

    def add_lemon(self):
        self.has_lemon = True
        return "วัวได้กินมะนาวแล้ว"

    def reset_status(self):
        self.status = 'ปกติ'
        self.has_lemon = False
        return "วัวได้ถูกรีเซ็ตแล้ว"
