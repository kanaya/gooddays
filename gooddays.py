# gooddays.py
# 開始日から終了日までスロット付きで印字します．「調整さん」にコピペする文字列として便利です．
# 土日祝日は候補日から外します．

import datetime
import parsedatetime as pdt
import jpholiday
import locale

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

# 開始日（ここを書き換えて下さい）
start = "April 8, 2024"

# 終了日（ここを書き換えて下さい）
end = "April 30, 2024"

# 各候補日のスロット（ここを書き換えて下さい）
slots = ["1限目", "2限目", "3限目", "4限目", "5限目"]

cal = pdt.Calendar()
start_date, _ = cal.parseDT(start)
end_date, _ = cal.parseDT(end)

def date_range(start, end):
	current = start
	while current <= end:
		if current.weekday() < 5 and not jpholiday.is_holiday(current):
			yield current
		current += datetime.timedelta(days=1)

for d in date_range(start_date, end_date):
	dd = d.strftime("%m/%d (%a)")
	for s in slots:
		print("{} {}".format(dd, s))
