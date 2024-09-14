from cow_model import Cow
import json

class CowController:
    def __init__(self):
        """
        สร้างอ็อบเจ็กต์ของ CowController และโหลดข้อมูลวัวจากไฟล์
        """
        self.cows = []
        self.load_cows()

    def load_cows(self):
        """
        โหลดข้อมูลวัวจากไฟล์ JSON และสร้างอ็อบเจ็กต์ Cow
        """
        with open('cow_data.json', 'r', encoding='utf-8') as file:
            cow_data = json.load(file)
            for cow in cow_data:
                new_cow = Cow(cow['id'], cow['breed'], cow['age'])
                self.cows.append(new_cow)

    def find_cow_by_id(self, cow_id):
        """
        ค้นหาวัวจากรหัสวัว

        :param cow_id: รหัสวัวที่ต้องการค้นหา
        :return: อ็อบเจ็กต์ Cow หากพบ, มิฉะนั้นคืนค่า None
        """
        for cow in self.cows:
            if cow.id == cow_id:
                return cow
        return None

    def reset_cow(self, cow_id):
        """
        รีเซ็ตสถานะของวัวตามรหัสวัว

        :param cow_id: รหัสวัวที่ต้องการรีเซ็ต
        """
        cow = self.find_cow_by_id(cow_id)
        if cow:
            cow.reset()
