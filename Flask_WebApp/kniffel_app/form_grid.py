def form_grid(column, row):
	if 1 <= column <= 6 and 1 <= row <= 21:
		x_coordinates = [676, 804, 929, 1057, 1183, 1309, 1448]
		x = x_coordinates[column - 1]
		y_coordinates = [261, 341, 422, 503, 584, 664, 745, 829, 915, 1081, 1161, 1242, 1323, 1403, 1484, 1590, 1671, 1753, 1836, 1943, 2049, 2134]
		y = y_coordinates[row - 1]
		w = x_coordinates[column] - x_coordinates[column - 1]
		h = y_coordinates[row] - y_coordinates[row - 1]
		if row == 9:
			h = 85
		return x, y, w, h
	else:
		raise ValueError("Column or row does not exist")

if __name__ == '__main__':
	for column in range(1, 6 + 1):
		for row in range(1, 21 + 1):		
			print(form_grid(column, row))
