nl = []
for i in range(1500,2701):
	i += 1
	if (i % 7 == 0) and (i % 5 == 0):
		nl.append(str(i))
print(','.join(nl))
