import random
import json

class Cow:
    def __init__(self, id, breed, age):
        """
        สร้างข้อมูลวัว
        :param id: รหัสวัว
        :param breed: พันธุ์วัว (ขาว/น้ำตาล)
        :param age: อายุของวัว (ปีและเดือน)
        """
        self.id = id
        self.breed = breed
        self.age = age

class CowModel:
    def __init__(self):
        """
        จัดการข้อมูลทั้งหมดของวัว
        """
        self.cows = []
        self.generate_cows()  # สร้างข้อมูลวัว

    def generate_cows(self, num_cows=10):
        """
        สร้างข้อมูลวัวและเก็บใน self.cows
        :param num_cows: จำนวนวัวที่ต้องการสร้าง
        """
        self.cows = [Cow(self.generate_cow_id(), 
                         random.choice(['ขาว', 'น้ำตาล']), 
                         self.generate_age()) 
                     for _ in range(num_cows)]

    def generate_cow_id(self):
        """
        สร้างรหัสวัวเป็นเลข 8 หลัก (ไม่เริ่มต้นด้วย 0)
        :return: รหัสวัว
        """
        return str(random.randint(1, 9)) + ''.join(str(random.randint(0, 9)) for _ in range(7))

    def generate_age(self):
        """
        สร้างอายุของวัว (ปีและเดือน)
        :return: อายุวัวในรูปแบบ "X ปี Y เดือน"
        """
        years = random.randint(0, 10)
        months = random.randint(0, 11)
        return f"{years} ปี {months} เดือน"

    def save_to_file(self, filename="cow_data.json"):
        """
        บันทึกข้อมูลวัวลงไฟล์ JSON
        :param filename: ชื่อไฟล์ JSON
        """
        data = [{'id': cow.id, 'breed': cow.breed, 'age': cow.age} for cow in self.cows]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
