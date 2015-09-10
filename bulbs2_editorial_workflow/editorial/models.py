from enum import Enum


class State(Enum):
    """
    an enumeration for controlling content state
    """

    draft = 0
    waiting_for_editor = 1
    approved_for_publication = 3

    def __str__(self):
        """basically a pretty print for the value names
        """
        spaced = " ".join(self.name.split("_"))
        titled = spaced.title()
        return titled
