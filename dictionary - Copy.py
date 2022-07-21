month_conversions = {
    "jan" : "january",
    "feb" : "february",
    "mar" : "march",
    "apr" : "april",
    "may" : "may",
    "jun" : "june",
    "jul" : "july"

}

print(month_conversions["jan"])
print(month_conversions.get("jan"))
print(month_conversions.get("luv"))
print(month_conversions.get("luv", "not a valid key"))
