#Python Crash Course, Eric Matthes, Chapter 2,
#custom stripping names

first_name = "John"
middle_name = "Skittle"
last_name = "Longstockings"
nick_name = "\n\nSkippy\t"
title = "\tMr. \n"
extra_name = " Jr.\t\n"

regular_name = f" \t{title} \n\t{first_name} \t{middle_name}  \n\t\t\t {nick_name} \n\t\t {last_name.upper()} \n\t\t\t\t {extra_name.lower()}<--End."
print(regular_name)
print(regular_name.rstrip())
print(regular_name.lstrip())
print(regular_name.strip())

first_name = "  John"
middle_name = "Skittle \t"
last_name = "Longstockings"
nick_name = "\n\nSkippy\t"
title = "\tMr. \n"
extra_name = " Jr.\t\n"

regular_name = f"{title}{first_name}{middle_name}{nick_name}{last_name.upper()}{extra_name.lower()}<--End."
print(regular_name)
print(regular_name.rstrip())
print(regular_name.lstrip())
print(regular_name.strip())

first_name = "  John "
middle_name = "Skittle \t"
last_name = "Longstockings"
nick_name = "Skippy\t"
title = "\tMr. "
extra_name = " Jr.\t"

regular_name = f"{title}{first_name}{middle_name}{nick_name}{last_name.upper()}{extra_name.lower()}<--End."
print(regular_name)
print(regular_name.rstrip())
print(regular_name.lstrip())
print(regular_name.strip())