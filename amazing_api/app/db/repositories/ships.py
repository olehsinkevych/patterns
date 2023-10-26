from sqlalchemy.orm import Session

from app.models import models
from app.schemas.ship import IShip


class ShipRepository:
    def __init__(self, db_session: Session) ->None:
        self.db_session = db_session

    def create_ships(self, ships: IShip) -> IShip:
        return

