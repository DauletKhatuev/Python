from logs_writer import collection

def top5_popular():
    pipeline = [
        {"$group": {
            "_id": {"type": "$search_type", "params": "$params"},
            "count": {"$sum": 1},
            "last": {"$max": "$timestamp"}   # ВАЖНО: в логах должен быть ключ "timestamp"
        }},
        {"$sort": {"count": -1, "last": -1}},
        {"$limit": 5}
    ]
    return list(collection.aggregate(pipeline))