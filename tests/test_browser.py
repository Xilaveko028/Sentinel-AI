import asyncio

from app.browser.browser_engine import BrowserEngine

async def main():
    browser = BrowserEngine()

    await browser.launch(headless=True)

    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())