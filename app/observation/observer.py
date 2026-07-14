class ObservationEngine:
    """ The task of this class is to handle the following observation interactions for sentinel AI:
    - observe the DOM structure of a web page
    - analyze the DOM structure of a web page
    - capture screenshots
    """
    
    def __init__(self, analysis: dict):
        self.analysis = analysis
    
    def generate(self):
        observation = []

        if self.analysis["forms"] > 0:
            observation.append("This web page contains a form!!")

        if self.analysis["inputs"] > 0:
            observation.append(f"This web page contains {self.analysis['inputs']} input fields.")

        if self.analysis["forms"] > 0 and self.analysis["inputs"] > 0:
            observation.append("The page appears to accept a user input through one or more forms.")

        if self.analysis["links"] > 0:
            observation.append(f"This web page contains {self.analysis['links']} links.")

        if self.analysis["buttons"] > 0:
            observation.append(f"This web page contains {self.analysis['buttons']} buttons.")

        if self.analysis["buttons"] == 0:
            observation.append("No buttons were detected.")

        if self.analysis["buttons"] > 0 and self.analysis["links"] > 5:
            observation.append(
                "The page provides multiple navigation and interaction options."
            )
        if self.analysis["forms"] == 0 and self.analysis["inputs"] == 0:
            observation.append(
                "The page appears to be informational rather than intended for data entry."
            )
        return observation