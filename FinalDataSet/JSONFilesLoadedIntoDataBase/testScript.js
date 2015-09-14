query = 
	{$group:
  		{"_id":"all", "average":
  		  {$avg: "$noteFrequency"
  		  }
  		}
	}
db.corpusV2.aggregate(query)

query = 
{ $group: 
  { "_id": "all",
    "sum" :{ $sum : 1},
    "avg": { $avg: "$noteFrequency"},
    "min": {$min: "$noteFrequency"},
    "max": {$max: "$noteFrequency"},
  }
}
db.corpusV2.aggregate(query)
 
 
query = 
{$group: {"_id":"$noteFrequency", "sum":{"$sum":1}}}

query =
{$group: {"_id":"$title", "val":{"$sum":1}}}
db.corpusV2.aggregate(query)

db.corpusV2.findOne()

query = 
{$group:{"_id":"$noteFrequency", 'Number of times this occurs':{"$sum":1}}}

db.corpusV2.aggregate(query)


