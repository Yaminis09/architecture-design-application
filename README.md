# Architecture Design Application

An application that allows users to search and discover **architectural construction details** using a combination of **text queries and contextual information**.

The system contains a **small in-memory dataset** (`data.py`) of architectural details. Users can search for relevant construction details using keywords and contextual parameters such as:

- Host Element
- Adjacent Element
- Exposure Condition

The backend calculates a **relevance score** based on how well the query and context match the stored architectural details and returns the **top ranked results**.

---

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

---

# Project Structure
