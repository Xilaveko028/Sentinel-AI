import asyncio

from app.browser.browser_engine import BrowserEngine
from app.analysers.dom_analyser import DOMAnalyser
from app.observation.observer import ObservationEngine
from app.detectors.bug_detector import BugDetector

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

    """ To get the HTML content of the current web page"""
    html = await browser.get_html()

    analyser = DOMAnalyser(html)
    analysis = analyser.analyse()

    observation_engine = ObservationEngine(analysis)
    observations = observation_engine.generate()

    bug_detector = BugDetector(analysis)
    bugs = bug_detector.detect()

    print("\n========== PAGE INFORMATION ================")
    print(f"Page title is: {title}")
    print(f"Current URL: {current_url}")
    print("=============================================\n")

    print("========== HTML PREVIEW ====================")
    print(html[:500])          # Print only the first 500 characters
    print("=============================================\n")

    print("\n========== PAGE ANALYSIS ==========")

    for key, value in analysis.items():
        print(f"{key: <10}: {value}")

    print("===================================\n")


    print("\n========== BUG DETECTION ==========")
    if bugs:
        for bug in bugs:
            print(f"- {bug}")
    else:
        print("No potential usability or UI issues detected.")
    print("===================================\n")  
    """ To close the browser after being used"""
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())