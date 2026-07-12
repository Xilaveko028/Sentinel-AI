import asyncio

from app.browser.browser_engine import BrowserEngine

async def main():
    """ To launch a browser """
    browser = BrowserEngine()
    await browser.launch(headless=True)

    """ To visit the URL and get title"""
    await browser.visit("https://learning.richfield.ac.za")
    title = await browser.get_title()

    """To extract the current URL """
    current_url = await browser.get_current_url()

    """ To capture a screenshot"""
    await browser.take_screenshot("Richfield_login.png")

    print("\n========== PAGE INFORMATION ================")
    print(f"Page title is: {title}")
    print(f"Current URL: {current_url}")
    print("=============================================\n")

    """ To close the browser after being used"""
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())