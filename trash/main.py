from core.base import Base


class GameLoop(Base):
    def initialize(self):
        print("Initializing window ...")

    def update(self):
        pass


GameLoop().run()
