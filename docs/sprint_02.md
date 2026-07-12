# Sprint 02 -- Browser Automation and Page Interaction

## Project

**Sentinel AI**

**Sprint Status:** :) Completed

## Sprint Goal

The goal of this sprint was to extend the Browser Engine so that Sentinel AI could do more than simply launch a browser. In Sprint 01, I built the basic browser infrastructure. During this sprint, I focused on teaching the application how to interact with websites by navigating to pages, extracting useful information, capturing screenshots and retrieving the HTML source.

These features are essential because an AI system cannot analyse a webpage until it can first access and understand its content.

## What I Built

During this sprint, I implemented the following features:

* Added website navigation using Playwright
* Retrieved webpage titles
* Retrieved the current URL after navigation
* Captured screenshots of webpages
* Extracted the HTML source code
* Expanded the Browser Engine with reusable methods
* Improved the browser integration test
* Successfully automated interactions with real websites

## Browser Engine Improvements

I extended the `BrowserEngine` class by adding several new methods that handle common browser tasks. The browser can now:

* Launch Chromium
* Visit any website
* Retrieve the page title
* Retrieve the current URL
* Capture screenshots
* Extract the HTML content of a webpage
* Close the browser safely

Keeping all browser-related functionality inside a single class makes the project much easier to maintain and allows future AI modules to reuse the same browser interface.

## Testing

To verify that everything worked correctly, I updated the browser integration test to execute a complete browser workflow.

The test performs the following steps:

1. Launch the browser.
2. Navigate to the Richfield Learning website.
3. Retrieve the page title.
4. Retrieve the current URL.
5. Capture a screenshot.
6. Extract the HTML source.
7. Display the collected information.
8. Close the browser.

The test completed successfully inside GitHub Codespaces and confirmed that each browser function worked as expected.

## Challenges I Faced

### Understanding Website Redirects

One of the first things I noticed was that visiting the Richfield Learning website did not keep the browser on the homepage. Instead, the website automatically redirected the browser to the login page.

This taught me that websites often perform redirects behind the scenes, so retrieving the current URL is more reliable than assuming the browser stays on the original address.

### Creating the Screenshot Directory

When I first tried to save screenshots, Playwright could not find the destination folder because it did not exist.

I created the required directory before running the application again:

```bash
mkdir -p assets/bug_screenshots
```

After creating the folder, screenshots were saved successfully.

### Working with HTML Content

After implementing HTML extraction, I realised that modern webpages generate extremely large HTML documents. Printing the entire document filled the terminal with thousands of lines, making it difficult to read.

To make debugging easier, I displayed only the first few hundred characters of the HTML output while confirming that the extraction worked correctly.

### Improving the Browser Engine

As I added more browser features, I realised how important it is to keep browser logic inside the `BrowserEngine` class rather than writing everything inside the test file.

This separation makes the code cleaner, easier to maintain, and much more reusable as the project grows.

### Becoming More Comfortable with Async Programming

This sprint gave me more practice with asynchronous programming in Python. Every browser interaction uses `await`, ensuring that each task finishes before the next one begins.

Although this was initially unfamiliar, it became much easier to understand after implementing several browser operations.

## What I Learned

This sprint helped me develop a stronger understanding of browser automation and software engineering.

Some of the key lessons I learned include:

* How Playwright interacts with websites
* How webpages automatically redirect users
* How to retrieve webpage metadata
* How to capture screenshots programmatically
* How to extract HTML source code
* How to design reusable classes
* How asynchronous programming works in real applications
* Why testing each feature individually makes debugging much easier

One lesson that stood out to me was the importance of building software incrementally. By implementing and testing one feature at a time, it became much easier to identify problems and understand how each component fits into the overall system.

## Sprint Outcome

By the end of Sprint 02, Sentinel AI was able to:

* Launch Chromium successfully
* Navigate to websites
* Retrieve webpage titles
* Detect redirected URLs
* Capture screenshots
* Extract HTML source code
* Complete an end-to-end browser automation workflow inside GitHub Codespaces

This sprint transformed Sentinel AI from a simple browser launcher into a browser automation tool capable of collecting information from real websites.

## Next Sprint

The next sprint will focus on analysing webpage content instead of simply collecting it.

The planned features include parsing HTML with BeautifulSoup, analysing the Document Object Model (DOM), counting webpage elements such as buttons and forms, and producing structured information that future AI components can use for bug detection and intelligent webpage analysis.
