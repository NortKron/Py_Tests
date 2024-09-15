from selenium.webdriver import Chrome

class Driver(Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # default time waiting for a locator
        self.implicitly_wait(5)
