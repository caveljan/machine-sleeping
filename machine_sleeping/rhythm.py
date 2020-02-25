class CircamentRhythm:
    def __init__(
        self,
        state_name: str,
        state_quality: int,
        state_certainty: int,
    ):
        self.state_name = state_name
        self.state_quality = state_quality
        self.state_certainty = state_certainty

    def setState(
        self,
        state_name: str,
        state_quality: int,
        state_certainty: int,
    ):
        if (
            state_name == 'asleeping'
            or state_name == 'sleep'
            or state_name == 'awakening'
            or state_name == 'awake'
        ):
            self.state_name = state_name
            self.state_quality = state_quality
            self.state_certainty = state_certainty
