from Games.Game import Game


class PullTab(Game):
    def __init__(self, id, db, price=-1):
        # Must be passed a price in order to guarantee proper calculations, as not all lowest prizes are the cost
        self.type = Game.PULL_TAB_STRING
        self.link = (
            db.getSingleUrl(self.type)
            + str(id)
        )
        super().__init__(id, db, price)
