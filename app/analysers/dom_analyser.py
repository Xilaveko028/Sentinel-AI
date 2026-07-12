from bs4 import BeautifulSoup

class DOMAnalyser:
    """ The task of this class is to handle the following DOM interactions for sentinel AI:
        - parse the HTML content of a web page
        - extract specific elements from the DOM
        - analyze the structure and content of the DOM
    """
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")   

    def count_buttons(self):
        """ Count the number of button elements in the DOM """
        return len(self.soup.find_all("button"))
    
    def count_forms(self):
        """ Count the number of form elements in the DOM """
        return len(self.soup.find_all("form"))
    
    def count_inputs(self):
        """ Count the number of input elements in the DOM """
        return len(self.soup.find_all("input"))

    def count_links(self):
        """ Count the number of anchor (link) elements in the DOM """
        return len(self.soup.find_all("a"))
    
    def analyse(self):
        """ Analyse the DOM and return a summary of the counts of various elements """
        return {
            "buttons": self.count_buttons(),
            "forms": self.count_forms(),
            "inputs": self.count_inputs(),
            "links": self.count_links()
        }
 