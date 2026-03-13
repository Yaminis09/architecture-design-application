"""
File Name : data.py

This file stores the architectural detail dataset in memory.

Each detail includes:
- descriptive information (title, tags, description)
- usage rules (host_element, adjacent_element, exposure)

The search system will use this dataset to perform
text matching and context matching.
"""

details = [

    {
        "id": 1,
        "title": "External Wall – Slab Junction Waterproofing",
        "category": "Wall",
        "tags": ["wall", "slab", "waterproofing", "external"],
        "description": "Waterproof membrane continuity at external wall and slab junction",

        "rule": {
            "host_element": "External Wall",
            "adjacent_element": "Slab",
            "exposure": "External"
        }
    },

    {
        "id": 2,
        "title": "Window Sill Detail with Drip",
        "category": "Window",
        "tags": ["window", "sill", "drip", "external"],
        "description": "External window sill detail with drip groove",

        "rule": {
            "host_element": "Window",
            "adjacent_element": "External Wall",
            "exposure": "External"
        }
    },

    {
        "id": 3,
        "title": "Internal Wall – Floor Junction",
        "category": "Wall",
        "tags": ["wall", "floor", "internal"],
        "description": "Junction detail between internal wall and finished floor",

        "rule": {
            "host_element": "Internal Wall",
            "adjacent_element": "Floor",
            "exposure": "Internal"
        }
    }

]

# for d in details:
#     print(d["title"])