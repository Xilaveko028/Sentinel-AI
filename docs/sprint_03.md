# Sprint 03 -- DOM Analysis and Webpage Understanding

## Project

**Sentinel AI**

**Sprint Status:** :) Completed

## Sprint Goal

The goal of this sprint was to give Sentinel AI the ability to understand the structure of a webpage instead of simply interacting with it.

In the previous sprint, the Browser Engine was responsible for visiting websites, capturing screenshots, and extracting HTML. During this sprint, I introduced DOM analysis so that Sentinel AI could inspect the contents of a webpage and gather useful information about its elements.

This marks an important milestone because the project is beginning to move from browser automation towards intelligent webpage analysis.

## What I Built

During this sprint, I completed the following tasks:

* Created a DOM Analysis module
* Parsed HTML using BeautifulSoup
* Counted buttons on a webpage
* Counted forms
* Counted input fields
* Counted hyperlinks
* Displayed a structured webpage analysis
* Integrated DOM analysis with the Browser Engine
* Extended the browser integration test

## DOM Analyser

To keep the project modular, I created a dedicated `DOMAnalyser` class.

Instead of placing HTML processing inside the Browser Engine, I separated browser automation from webpage analysis.

The Browser Engine is responsible for collecting webpage data, while the DOM Analyser is responsible for understanding that data.

This separation makes the project easier to maintain and follows good software engineering principles.

The DOM Analyser currently provides the following methods:

* `count_buttons()`
* `count_forms()`
* `count_inputs()`
* `count_links()`
* `analyse()`

This design will allow additional analysis methods to be added in future sprints without modifying the Browser Engine.

## Testing

I updated the integration test to verify both browser automation and DOM analysis.

The test now performs the following workflow:

1. Launch Chromium.
2. Visit the Richfield Learning website.
3. Retrieve the page title.
4. Retrieve the current URL.
5. Capture a screenshot.
6. Extract the HTML source.
7. Analyse the HTML using the DOM Analyser.
8. Display the webpage statistics.
9. Close the browser.

The output confirmed that the analyser correctly identified the main webpage elements.

Example output:

```text
========== PAGE ANALYSIS ==========

Buttons : 3
Forms   : 1
Inputs  : 4
Links   : 10

==================================
```

## Challenges I Faced

### Understanding the DOM

Before implementing the analyser, I needed to understand what the Document Object Model (DOM) actually represents.

I learned that every webpage is organised as a tree of HTML elements, allowing software to inspect and analyse different parts of the page programmatically.

Understanding this concept made it much easier to design the DOM Analyser.

### Separating Responsibilities

Initially, I considered placing the HTML analysis methods inside the Browser Engine.

After thinking about the project structure, I realised this would violate the principle of keeping each class responsible for a single task.

I decided to create a separate `DOMAnalyser` class instead.

This made the overall design cleaner and easier to extend.

### Working with BeautifulSoup

This was my first time using BeautifulSoup to analyse webpage content.

I learned how to search HTML elements using methods such as `find_all()` and how to count different types of elements on a webpage.

This significantly simplified HTML parsing compared to manually searching through raw HTML.

### Reading HTML

Initially, the extracted HTML looked overwhelming because modern webpages contain thousands of lines of code.

Instead of trying to understand the entire document at once, I focused on identifying specific HTML elements such as buttons, forms, inputs and links.

Breaking the problem into smaller tasks made the implementation much easier.

## Git Workflow

After completing and testing the new functionality, I followed the standard Git workflow.

First, I checked the project status:

```bash
git status
```

Then I staged all modified files:

```bash
git add .
```

After verifying that everything worked correctly, I created a commit describing the new feature:

```bash
git commit -m "feat(dom): implement webpage DOM analysis"
```

Finally, I pushed the completed sprint to GitHub:

```bash
git push origin main
```

Following this workflow after every sprint helps maintain a clear development history and makes it easier to track the evolution of the project.

## What I Learned

This sprint helped me better understand how webpages are structured and how software can analyse them.

Some of the most important lessons I learned were:

* How the Document Object Model (DOM) represents a webpage
* How BeautifulSoup parses HTML
* How to count HTML elements programmatically
* Why separating responsibilities improves software design
* How browser automation and webpage analysis work together
* How modular programming makes future development easier

This sprint also reinforced the importance of building reusable components instead of writing all functionality inside a single class.

## Sprint Outcome

By the end of Sprint 03, Sentinel AI was capable of:

* Visiting webpages
* Extracting HTML source code
* Parsing webpage content
* Counting important HTML elements
* Producing structured webpage statistics
* Separating browser automation from webpage analysis

This represents the first step towards giving Sentinel AI the ability to understand webpages rather than simply interacting with them.

## Next Sprint

The next sprint will focus on building an Observation Engine.

Instead of only counting webpage elements, Sentinel AI will begin making observations about webpage quality. The system will identify missing elements, detect potential usability issues, and generate structured observations that can later be used by AI models for automated bug detection and testing.
