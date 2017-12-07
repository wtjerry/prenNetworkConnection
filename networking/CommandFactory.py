from networking.StartCommand import StartCommand
from networking.PositionCommand import PositionCommand


class CommandFactory(object):

    def __init__(self):
        self.__id_to_command_mapping = {
            1: self._create_start_command,
            2: self._create_position_command
        }

    def _create_start_command(self, parameter):
        return StartCommand()

    def _create_position_command(self, parameter):
        x, y = parameter.split(',')
        return PositionCommand(int(x), int(y))

    def create(self,command_id, parameter):
        class_type = self.__id_to_command_mapping.get(command_id)
        return class_type(parameter)