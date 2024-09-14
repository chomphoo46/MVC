import random

class Cow:
    def __init__(self, cow_id, breed, age_years, age_months):
        self.id = cow_id
        self.breed = breed
        self.age_years = age_years
        self.age_months = age_months
        self.is_bsod = False  # สถานะ BSOD
        self._is_sour_milk = False  # สถานะของนมเปรี้ยว

    def milk(self):
        """
        ฟังก์ชันที่เรียกเมื่อรีดนมจากวัว
        """
        if self.is_bsod:
            return f"วัว {self.id} (สีฟ้า) ไม่สามารถผลิตนมได้ เนื่องจากเป็น BSOD"
        
        return (self.milk_white_cow() if self.breed == "ขาว" 
                else self.milk_brown_cow() if self.breed == "น้ำตาล" 
                else "พันธุ์วัวไม่รู้จัก")

    def milk_white_cow(self):
        """
        ฟังก์ชันสำหรับการผลิตนมของวัวสีขาว
        """
        if self.is_sour_milk:
            return "ผลิตนมเปรี้ยว"
        
        if random.random() * 100 < 0.5 * self.total_age_months():
            self.is_bsod = True
            return "ผลิตนมถั่วเหลือง (วัวเป็น BSOD)"
        return "ผลิตนมจืด"

    def milk_brown_cow(self):
        """
        ฟังก์ชันสำหรับการผลิตนมของวัวสีน้ำตาล
        """
        if random.random() * 100 < 1 * self.age_years:
            self.is_bsod = True
            return "ผลิตนมอัลมอนด์ (วัวเป็น BSOD)"
        return "ผลิตนมช็อกโกแลต"

    def reset(self):
        """
        ฟังก์ชันสำหรับรีเซ็ตสถานะของวัว
        """
        self.is_bsod = False

    def total_age_months(self):
        """
        ฟังก์ชันสำหรับการคำนวณอายุรวมเป็นเดือน
        """
        return self.age_years * 12 + self.age_months

    @property
    def is_sour_milk(self):
        """
        ฟังก์ชันตรวจสอบว่าคุณได้เพิ่มมะนาวไปยังวัวสีขาว
        """
        return self._is_sour_milk

    @is_sour_milk.setter
    def is_sour_milk(self, value):
        self._is_sour_milk = value
