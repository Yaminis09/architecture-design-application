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
   -  Instead of in script memory, I will use large scale database, preferbly postgreSQL
   -  Use of better search algo preferbly hashing or indexing.
   -  
2. What improvements would you make to the search or ranking logic in a production
system?
   -  Better search logic like fuzzy search, typo considering. so that misspelled words can also give us expected results.
   -  Better ranking rules to improve ranking logic. rightnow the rules are simple, adding score if certain words matches. we can include, bonus score if all words match or adding weights if a certain words matches with the dataset more than once.
   - One probaky can make use of NLP to make searches better

3. What additional data or signals could help improve recommendation quality?
   -  one can add more metadata to make reccomenation better
   -  We can add functionality to make recc better by user behaviour, or project they are working on.
   -  We can use ML based recc if we make a space for each user. Lets say they are working on bedroom, there project is bedroom, their parameter is ancient rome like structure, then using the ML model we can reccommend structural designs can can go well with bedroom and acient rome.
   -  historical frequent selected detailing can be added to make recc quality better.
     
 4. If this API became a shared service used by multiple applications, what changes
would you make to its architecture?
   -  add authentication and api key management to enhance security
   -   use docker or cloud services to deploy the application
   -   Look out for edge cases like application failure, one needs cloudwatch(logs) to understand the failure and api workload.
5. What would you change if this system needed to support AI-based
recommendations in the future?
   - The best place of change will be in searching. instead of word to word search, the searches in AI based model are semantic based.
   - Vector based searches, this might also reduce our run time.
   



