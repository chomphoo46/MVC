import random

class Cow:
    def __init__(self, cow_id, breed, age):
        self.id = cow_id
        self.breed = breed
        self.age = age
        self.is_bsod = False  # สถานะ BSOD ของวัว

    def milk(self):
        """รีดนมจากวัว"""
        if self.is_bsod:
            return f"วัว {self.id} (สีฟ้า) ไม่สามารถผลิตนมได้ เนื่องจากเป็น BSOD"
        return self.milk_white_cow() if self.breed == "ขาว" else self.milk_brown_cow() if self.breed == "น้ำตาล" else "พันธุ์วัวไม่รู้จัก"

    def milk_white_cow(self):
        """ผลิตนมจากวัวสีขาว"""
        if self.is_sour_milk:
            return "ผลิตนมเปรี้ยว"
        
        if random.random() * 100 < 0.5 * self.age_months():
            self.is_bsod = True
            return "ผลิตนมถั่วเหลือง (วัวเป็น BSOD)"
        return "ผลิตนมจืด"

    def milk_brown_cow(self):
        """ผลิตนมจากวัวสีน้ำตาล"""
        if random.random() * 100 < 1 * self.age_years():
            self.is_bsod = True
            return "ผลิตนมอัลมอนด์ (วัวเป็น BSOD)"
        return "ผลิตนมช็อกโกแลต"

    def reset(self):
        """รีเซ็ตสถานะของวัว"""
        self.is_bsod = False

    def age_years(self):
        """คำนวณอายุเป็นปี"""
        return int(self.age)

    def age_months(self):
        """คำนวณอายุเป็นเดือน"""
        years, months = divmod(self.age, 1)
        return int(years * 12 + months)

    @property
    def is_sour_milk(self):
        """ตรวจสอบว่ามีมะนาวหรือไม่"""
        return getattr(self, '_is_sour_milk', False)

    @is_sour_milk.setter
    def is_sour_milk(self, value):
        self._is_sour_milk = value
