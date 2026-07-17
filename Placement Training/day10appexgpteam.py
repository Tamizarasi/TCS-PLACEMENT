class APEXGPTEAM:
    engine = "Mercedes"

    def __init__(self, name):  # instance method
        self.name = name

    def status(self):
        print(f"{self.name} is on the Track")

    @classmethod
    def update_engine(cls, new_engine):
        cls.engine = new_engine
        print(f"Team changed engine to {cls.engine}")

    @staticmethod
    def checkWhether():
        print("Whether is Clear and Dry")


APEXGPTEAM.checkWhether()
sonny = APEXGPTEAM("Sonny Hayes")
sonny.update_engine("Ferrari")
sonny.status()
