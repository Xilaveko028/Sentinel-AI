import asyncio

from app.browser.browser_engine import BrowserEngine

async def main():
    browser = BrowserEngine()

    await browser.launch(headless=True)

    await browser.visit("https://chatgpt.com")
    title = await browser.get_title()
    print(f"Page title is: {title}")

    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())