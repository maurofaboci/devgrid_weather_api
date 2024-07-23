from enum import Enum

class EStatus(str, Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    FINISHED = 'FINISHED'
    ERROR = 'ERROR'   