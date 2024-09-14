# View: แสดงข้อมูลวัว
class CowView:
    def display_cows(self, cows):
        """
        แสดงข้อมูลวัวทั้งหมด
        """
        for cow in cows:
            print(f"รหัสวัว: {cow.id}, พันธุ์: {cow.breed}, อายุ: {cow.age}")
