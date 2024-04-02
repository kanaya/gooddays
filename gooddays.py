# gooddays.py

import datetime
import parsedatetime as pdt
import locale

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

start = "April 8, 2024"
end = "April 26, 2024"
slots = ["1限目", "2限目", "3限目", "4限目", "5限目"]

cal = pdt.Calendar()
start_date, _ = cal.parseDT(start)
end_date, _ = cal.parseDT(end)

def date_range(start, end):
	current = start
	while current <= end:
		if current.weekday() < 5:
			yield current
		current += datetime.timedelta(days=1)

for d in date_range(start_date, end_date):
	dd = d.strftime("%m/%d (%a)")
	for s in slots:
		print("{} {}".format(dd, s))



