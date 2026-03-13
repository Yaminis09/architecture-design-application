# architecture-design-application

An application that allows users to find architectural construction details using text and context information.
Application contains small dataset within data.py containing architectural details and allows the user to search using
a text query host element adjacent element exposure condition
The backend calculate the relevance score based on the detail matches of the input query ad returns the top ranked results.
The application includes: FastAPI backend HTML, CSS, Javascript frontend In file memory based database
Techstack Backend: Python FastAPI Frontend: HTML Javascript Inline CSS
Project structure: Main folder:
Backend a. main.py b. Search.py c. Data.py
Frontend a. index.html Readme.md
**Instruction **
Clone repo
Navigate to backend folder
Create virtual environment Pip install fastapi unicorn
**How to run the app ** Unicorn main:app —reload Running UI: Open index.html after the backend is running.
Front end allows you to :
Enter search query
Option to make section
Shows result

Scoring : Relevance score The search system calculates a relevance score based on two factors:
Text Matching The query is matched against: • title • tags • description Each match contributes to the score.
Context Matching The request context is compared with the usage rules of each detail: • host_element • adjacent_element • exposure Matching fields increase the relevance score.
EXAMPLE: post request /docs
JSON req body: { "query": "window drip", "host_element": "Window", "adjacent_element": "External Wall", "exposure": "External" }
{ "results": [ { "detail_id": 2, "title": "Window Sill Detail with Drip", "score": 18, "explanation": "title matched 'window', tag matched 'window' , description matched 'window', title matched 'drip', tag matched 'drip' , description matched 'drip', host_element matched Window, adjacent_element matched External Wall, exposure matched External" }, { "detail_id": 1, "title": "External Wall – Slab Junction Waterproofing", "score": 1, "explanation": "exposure matched External" } ] }
