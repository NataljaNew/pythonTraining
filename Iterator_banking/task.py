def annual_return(start, percent, years):
    for _ in range(years):
        result = start*(100+percent)/100
        yield result
        start = result

for value in annual_return(120000, 10, 3):
    print(round(value))