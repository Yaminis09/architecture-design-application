# Architecture Design Application
---


---

# Project Structure

- Backend Folder
- - main.py
  - search.py
  - data.py
- Frontend Folder
- - index.html
    
# How to set up
1. Clone repo
2. Create virtual enviroment
python -m venv venv
source venv/bin/activate (mac)
venv\Scripts\activate(win)
Install : pip install fastapi uvicorn
4. cd backend folder
5. run : uvicorn main:app --reload
6. In frontend folder open index.html
(if using vscode, install extension to run html file

# Example
Req:
{
 "query": "window drip",
 "host_element": "Window",
 "adjacent_element": "External Wall",
 "exposure": "External"
}

Result:
{
  "results": [
    {
      "detail_id": 2,
      "title": "Window Sill Detail with Drip",
      "score": 18,
      "explanation": "title matched 'window', tag matched 'window' , description matched 'window', title matched 'drip', tag matched 'drip' , description matched 'drip', host_element matched Window, adjacent_element matched External Wall, exposure matched External"
    },
    {
      "detail_id": 1,
      "title": "External Wall – Slab Junction Waterproofing",
      "score": 1,
      "explanation": "exposure matched External"
    }
  ]
}

# Relevance Score
Search and Ranking Logic
The search system calculates a relevance score using two main components.
1 Text Matching
The query is matched against the following fields of each architectural detail:
Title
Tags
Description
Each match contributes to the relevance score.
Example matches:
Title contains keyword
Tag contains keyword
Description contains keyword
2 Context Matching
The request context is compared with the usage rules of each architectural detail.
Context fields include:
host_element
adjacent_element
exposure
If a field matches the stored rule, the relevance score increases.


# Tech Stack

### Backend
- Python
- FastAPI

### Frontend
- HTML
- JavaScript
- Inline CSS

### Database
- In-memory dataset (Python file)

# Questions:
1. If this system needed to support 100,000+ details, what changes would you make?
   a. Instead of in script memory, I will use large scale database, preferbly postgreSQL
   b. complete sentence query search
2. What improvements would you make to the search or ranking logic in a production
system?
 a. Making logic of searches little detailed, like including fuzzy searches
 b. One probaky can make use of NLP to make searches better
 c. Can add synomyic understanding in the seaches. for example window sill means window edge.
3. What additional data or signals could help improve recommendation quality?
   a. one can add more metadata to make reccomenation better
   b. historical frequent selected detailing can be added to make recc quality better.
   c. When used metadata, signals, we can run ML models to make better predictions and reccomendation
4. If this API became a shared service used by multiple applications, what changes
would you make to its architecture?
 a. add authentication and api key management to enhance security
 b. use docker or cloud services to deploy the application
5. What would you change if this system needed to support AI-based
recommendations in the future?



