s1 = {"$group":{"_id":"all", "sum":{"$sum":1}}}
db.corpusV2.aggregate(s1)