height = input('請輸入身高：')
weight = input('請輸入體重：')
height = float(height)
weight = float(weight)
bmi = weight / ((height / 100) * (height / 100))
# height = height / 100 換成公尺
if bmi < 18.5:
	print('體重過輕')
elif 18.5 <= bmi < 24:
	print('正常範圍')
elif 24 <= bmi < 27:
	print('過重')
elif 27 <= bmi < 30:
	print('輕度肥胖')
elif 30 <= bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')