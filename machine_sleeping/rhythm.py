class CircamentRhythm:
    def __init__(
        self,
        state: str,
        certainty: int,
    ):
        self.state = state
        self.certainty = certainty

    def setState(
        self,
        state: str,
        certainty: int,
    ):
        if (
            state == 'sleep'
            or state == 'awake'
            or state == 'falling'
            or state == 'awakening'
        ):
            self.state = state
            self.certainty = certainty
