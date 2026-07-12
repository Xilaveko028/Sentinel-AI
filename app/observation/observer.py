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
            observation.append("Forms detected!!")

        if self.analysis["inputs"] > 0:
            observation.append(f"Inputs detected: {self.analysis['inputs']}")
        
        if self.analysis["links"] > 0:
            observation.append(f"Links detected: {self.analysis['links']}")
        
        if self.analysis["buttons"] > 0:
            observation.append(f"Buttons detected: {self.analysis['buttons']}")

        return observation