from fastapi import FastAPI
from pydantic import BaseModel
from search import search_details

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestSearchDeatails(BaseModel):
    """
    Pydantic class to check if the input query is up to the needed standards

    Args: Inbuilt BaseModel
    
    """
    query: str | None = None
    host_element: str | None = None
    adjacent_element: str | None = None
    exposure: str | None = None

@app.post('/search')


def search_api(request:RequestSearchDeatails):
    """
    FastAPI endpoint to search and retrieve ranked details.

    Args:
        request (RequestSearchDetails): Request body containing query validated by pydantic class

    Returns:
        dict: A dictionary with a "results" key containing the top 5 matched details.
    """
    results = search_details(
        query=request.query,
        host_element=request.host_element,
        adjacent_element=request.adjacent_element,
        exposure=request.exposure
    )

    return {"results": results}
