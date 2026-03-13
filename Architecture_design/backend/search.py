"""
File Name : seach.py

This file contains the main logic of the searches and the scoring logic.

"""

from data import details

def search_details(query=None, host_element=None, adjacent_element=None, exposure=None):
    """ 
    Search and rank details based on query text and contextual rules.

    Args:
        query (str, optional): Search string matched against title, tags, and description.
        host_element (str, optional): host element to match against detail rules.
        adjacent_element (str, optional): Adjacent element to match against detail rules.
        exposure (str, optional): Exposure context to match against detail rules.

    Returns:
        list[dict]: Top matching results sorted by relevance score.
    
    """
    # query = query.split().lower()
    query_words = []
    if query:
        query_words = query.lower().split() #.lower()
    
    results = []

    for detail in details:
        score = 0
        explanation = []

        # Text matching = checking query against "details"
        title = detail["title"].lower()
        # tag = details[category_tag].lower()
        description = detail["description"].lower()
        tags = [tag.lower() for tag in detail["tags"]] 

        # text matching
        for word in query_words:
            if word in title:
                score = score+ 3
                explanation.append(f"title matched '{word}'")
            if word in tags:
                score = score +2
                explanation.append(f"tag matched '{word}' ")
            if word in description:
                score = score +1
                explanation.append(f"description matched '{word}'")
        
        # context matching
        rule = detail["rule"]
        if host_element and host_element.lower() == rule["host_element"].lower():
            score = score +3
            explanation.append(f"host_element matched {host_element}")

        if adjacent_element and adjacent_element.lower() == rule["adjacent_element"].lower():
            score = score+ 2
            explanation.append(f"adjacent_element matched {adjacent_element}")

        if exposure and exposure.lower() == rule["exposure"].lower():
            score = score + 1
            explanation.append(f"exposure matched {exposure}")
        
        # scoring
        if score > 0:
            results.append({
                    "detail_id": detail["id"],
                    "title": detail["title"],
                    "score": score,
                    "explanation": ", ".join(explanation)
                })
        results.sort(key = lambda x:x['score'],reverse=True)
    return results[:5]
  
# results = search_details(query="window drip", host_element="Window")

# for r in results:
#     print(r)