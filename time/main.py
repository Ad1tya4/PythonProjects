import datetime, math

datw = datetime.datetime.today()
when_i_see_her = datetime.datetime(2023,9,10, hour=9, minute=50)

result = when_i_see_her-datw

hours = (result.total_seconds()/60/60)-(result.days*24)
hou = math.floor(hours)
min = hours - math.floor(hours)
minutes = math.floor(min*60)
seconds = min*60 - minutes
sec = math.floor(seconds*60)
print(f"days:{result.days}\nhours:{hou}\nminutes:{minutes}\nseconds:{sec}")

result.min