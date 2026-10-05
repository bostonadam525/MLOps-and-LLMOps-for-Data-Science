# DQDL Glue Rules for Data Quality Example

```
Rules = [
	# Order identity and uniqueness
	IsPrimaryKey "salesorderdetailid",
	Completeness "salesorderid" >= 0.99,
	ColumnValues "salesorderid" between 43658 and 75000,

	# Order lifecycle dates
	IsComplete "orderdate",
	IsComplete "duedate",
	IsComplete "shipdate",
	CustomSql "SELECT COUNT(*) FROM primary WHERE TO_DATE(orderdate, 'M/d/yyyy') > TO_DATE(duedate, 'M/d/yyyy')" = 0,
	CustomSql "SELECT COUNT(*) FROM primary WHERE TO_DATE(shipdate, 'M/d/yyyy') > TO_DATE(duedate, 'M/d/yyyy')" = 0,

	# Employee and customer linkage
	IsComplete "employeeid",
	ColumnValues "employeeid" between 273 and 291,
	IsComplete "customerid",
	ColumnValues "customerid" between 290 and 2000,

	# Financial integrity
	IsComplete "subtotal",
	ColumnValues "subtotal" > 0,
	IsComplete "taxamt",
	ColumnValues "taxamt" >= 0,
	IsComplete "freight",
	ColumnValues "freight" >= 0,
	IsComplete "totaldue",
	ColumnValues "totaldue" > 0,
	CustomSql "SELECT COUNT(*) FROM primary WHERE ABS(totaldue - (subtotal + taxamt + freight)) > 0.01" = 0,

	# Product and quantity validation
	IsComplete "productid",
	ColumnValues "productid" between 706 and 1000,
	IsComplete "orderqty",
	ColumnValues "orderqty" between 1 and 50,

	# Pricing and discount rules
	IsComplete "unitprice",
	ColumnValues "unitprice" > 0,
	IsComplete "unitpricediscount",
	ColumnValues "unitpricediscount" between 0 and 0.4,
	IsComplete "linetotal",
	ColumnValues "linetotal" > 0,
	CustomSql "SELECT COUNT(*) FROM primary WHERE ABS(linetotal - (orderqty * unitprice * (1 - unitpricediscount))) > 0.01" = 0
]


```
