class Mobile:
    def __init__(self, company, model, ram, storage):
        self.company = company
        self.model = model
        self.ram = ram
        self.storage = storage

    def display_company(self):
        print(f"This mobile is made by {self.company} company.")

    def display_model(self):
        print(f"its model is {self.model}.")

    def display_ram(self):
        print(f"its ram is {self.ram}.")

    def display_storage(self):
        print(f"And its storage is {self.storage}.")


mob1 = Mobile("Infinix", 123, "8 GB", "256 GB")
mob1.display_company()
mob1.display_model()
mob1.display_ram()
mob1.display_storage()