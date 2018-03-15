import datetime

from Common.utils.DataMaker import DataMaker

t = datetime.datetime.now()

t.isoformat()
print(t.isoformat())
print(t.isoweekday())

print(t.timestamp())
TPL_TIME_ISO = "%Y-%m-%dT%H:%M:%S%z"
print((datetime.date.today() + datetime.timedelta(days=0)).strftime(TPL_TIME_ISO))
print((datetime.datetime.now()).strftime(TPL_TIME_ISO))

# print(DataMaker.number())
print(t.utcnow())

from datetime import datetime, tzinfo, timedelta


class simple_utc(tzinfo):
    def tzname(self, **kwargs):
        return "UTC"

    def utcoffset(self, dt):
        return timedelta(0)


print(datetime.utcnow().replace(tzinfo=simple_utc()).isoformat())
# '2014-05-16T22:51:53.015001+00:00'

print(DataMaker.number(1, 2))

print(DataMaker.email())

for i in range(1, 100):
    print(DataMaker.telephone())


for i in range(1, 100):
    print(DataMaker.chinese_name())
