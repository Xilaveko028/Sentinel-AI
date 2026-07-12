# Sprint 01 -- Project Setup and Browser Engine

## Project

**Sentinel AI**

**Sprint Status:** :) Completed

---

# Sprint Goal

The goal of this sprint was to build the foundation of Sentinel AI.

Before implementing AI models or autonomous testing, I first needed to create a clean project structure, configure the development environment, and build a browser engine that can launch and manage a web browser.

This browser engine will become the component that future AI agents use to interact with websites.

---

# What I Built

During this sprint I completed the following tasks:

- Created the Sentinel AI GitHub repository
- Configured GitHub Codespaces as the development environment
- Organized the project into a modular folder structure
- Installed and configured Playwright
- Implemented the first version of the Browser Engine
- Successfully launched Chromium in headless mode
- Created the first integration test
- Learned the basic Git workflow for version control

---

# Project Structure

The project currently follows this structure.

```
Sentinel-AI/
│
├── app/
│   ├── browser/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── reports/
│   └── utils/
│
├── tests/
├── docs/
├── assets/
└── README.md
```

I chose this structure because I want the project to remain organized as new AI components are added.

---

# Browser Engine

The Browser Engine is the first working component of Sentinel AI.

Its responsibility is to manage browser operations using Playwright.

Currently, it can:

- Start Playwright
- Launch Chromium
- Create a browser page
- Close the browser safely

The methods implemented are:

- `launch()`
- `close()`

Keeping browser functionality inside a single class makes this project easier to maintain and extend.

---

# Testing

To verify that the Browser Engine works correctly, I created a simple integration test.

The test performs the following steps:

1. Create a BrowserEngine object.
2. Launch Chromium.
3. Verify that the browser starts successfully.
4. Lastly successfully close the browser.

The browser launched successfully inside GitHub Codespaces.

---

# Challenges I Faced when doing this sprint:

## 1. Python Import Errors

Initially, Python could not find the `app` package.

After investigating the problem, I learned that the project should be executed as a module instead of running the test file directly.

Correct command:

```bash
python -m tests.test_browser
```

---

## 2. Class Indentation

I received an error indicating that `BrowserEngine` did not contain the `launch()` method.

The problem was caused by incorrect indentation, which placed the methods outside the class definition.

Correcting the indentation resolved the issue.

---

## 3. Playwright Dependencies

Chromium initially failed to launch because some Linux libraries were missing inside GitHub Codespaces.

This was resolved by installing the required Playwright dependencies.

```bash
playwright install --with-deps chromium
```

---

## 4. Running a Headed Browser

I first attempted to launch Chromium using:

```python
headless=False
```

This produced an error because GitHub Codespaces does not provide a graphical desktop environment.

Changing the browser to run in headless mode solved the problem.

```python
headless=True
```

---

## 5. Closing Browser Resources

After launching the browser successfully, I received warnings when the application terminated.

I learned that browser resources should always be released after use.

To solve this, I implemented a `close()` method that properly shuts down Chromium and Playwright.

---

# What I Learned

This sprint helped me understand several important software engineering concepts.

I learned:

- How to organize a Python project
- Basic Git and GitHub workflow
- How GitHub Codespaces works
- How Playwright automates browsers
- Object-Oriented Programming using classes
- Asynchronous programming with `async` and `await`
- Why resource management is important
- How to debug problems step by step instead of guessing

One of the biggest lessons from this sprint was learning to identify **where** a problem occurs. Not every error is caused by Python code; some originate from the operating system, project configuration, or development environment.

---

# Sprint Outcome

At the end of this first Sprint [1], Sentinel AI is able to:

- Launch Chromium successfully
- Manage the browser lifecycle
- Run inside GitHub Codespaces
- Execute the first browser integration test

This provides the foundation for future browser automation and AI-driven testing.

---

# Next Sprint

The next sprint will focus on browser interaction.

The planned features include:

- Navigating to websites
- Reading page titles
- Taking screenshots
- Extracting page information
- Inspecting page elements

These features will allow Sentinel AI to begin understanding web pages before introducing AI-based reasoning and autonomous testing.