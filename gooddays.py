# gooddays.py
# 開始日から終了日までスロット付きで印字します．「調整さん」にコピペする文字列として便利です．
# 土日祝日は候補日から外します．

import argparse
import datetime
import parsedatetime as pdt
import jpholiday
import locale

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=str, help="Start", default="today")
parser.add_argument("-e", "--end", type=str, help="End", default="tomorrow")
parser.add_argument("-l", "--slots", type=str, help="Slots", default="1,2,3,4,5")
parser.add_argument("-x", "--suffix", type=str, help="Suffix", default="時限目")
parser.add_argument("-f", "--format", type=str, help="Format", default="{} {}{}")
parser.add_argument("-n", "--noholiday", action='store_true', help="No Holiday")
args = parser.parse_args()

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

start = args.start
end = args.end
slots = args.slots
suffix = args.suffix
format_str = args.format
noholiday = bool(args.noholiday)

# 各候補日のスロット
slot_list = slots.split(",")

cal = pdt.Calendar()
start_date, _ = cal.parseDT(start)
end_date, _ = cal.parseDT(end)

def date_range(start, end):
	current = start
	if noholiday:
		while current <= end:
			yield current
			current += datetime.timedelta(days=1)
	else:
		while current <= end:
			if current.weekday() < 5 and not jpholiday.is_holiday(current):
				yield current
			current += datetime.timedelta(days=1)

for d in date_range(start_date, end_date):
	dd = d.strftime("%m/%d (%a)")
	for s in slot_list:
		print(format_str.format(dd, s, suffix))
