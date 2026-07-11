from playwright.async_api import async_playwright

class BrowserEngine:
    """ The task iof this class is to handle the following browser interactions for sentinel AI:
    - launch a browser
    - navigate around pages
    -capture screenshots
    -extract each page information
    """
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    """Starting a Playwright and launch a Chromium browser"""

    async def launch(self, headless=True):
        """
        Starts Playwright and launches a Chromium browser.
        """

        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=headless
        )

        self.page = await self.browser.new_page()

        print(" Browser launched successfully!!!")

    async def close(self):
        """To close the browser and stop playwright"""

        if self.browser:
            await self.browser.close()
        
        if self.playwright:
            await self.playwright.stop()
        
        print("The browser has been closed successfully!!!")

    