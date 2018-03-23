from controlling.Dummies.Dummy import Dummy
from controlling.Dummies.DummyBalanceEngine import DummyBalanceEngine
from controlling.Dummies.DummyPosition import DummyPosition
from controlling.Dummies.DummyTargetDetection import DummyTargetDetection
from controlling.Dummies.DummyLoadPositionComparer import DummyLoadPositionComparer
from controlling.Dummies.DummyMagnet import DummyMagnet
from controlling.Dummies.DummyMovementEngine import DummyMovementEngine
from controlling.Dummies.DummyTelescopeEngine import DummyTelescopeEngine


class Binding:
    use_real_balancer = False
    use_real_goal_detection = False
    use_real_load_position_comparer = False
    use_real_magnet = False
    use_real_movement = False
    use_real_position_calculator = False
    use_real_position_output = False
    use_real_telescope = False
    use_real_x_position = False
    use_real_start_signal = False
    use_real_position = False

    def __init__(self, goalfound_function):
        # TODO replace Dummy(), it raises an error when initialized
        self.movement_engine = Dummy() if self.use_real_movement else DummyMovementEngine()
        self.target_detection = Dummy() if self.use_real_goal_detection else DummyTargetDetection(goalfound_function)
        self.magnet = self.get_real_magnet() if self.use_real_magnet else DummyMagnet()
        self.telescope_engine = Dummy() if self.use_real_telescope else DummyTelescopeEngine()
        self.position = self._get_real_position() if self.use_real_position \
            else DummyPosition(self.movement_engine, self.telescope_engine)
        self.balancer = Dummy() if self.use_real_balancer else DummyBalanceEngine(self.position)
        self.load_position_comparer = Dummy() if self.use_real_load_position_comparer \
            else DummyLoadPositionComparer(self.position)

    def _get_real_position(self):
        from position.Position import Position
        return Position(self.movement_engine, self.telescope_engine)


    def get_real_magnet(self):
        from magnet.Magnet import Magnet
        return Magnet()