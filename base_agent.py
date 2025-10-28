class BaseAgent:

    """Base class for all agent types."""

    

    def run(self, *args, **kwargs):

        """Override this method in subclasses."""

        raise NotImplementedError("Subclasses must implement the run method")