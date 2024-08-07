N = int(input().strip())

unique_countries = set()
for i in range(N):
    country = str(input().strip())
    unique_countries.add(country)

unique_count = len(unique_countries)
print(unique_count)
