height = input('請輸入身高：')
weight = input('請輸入體重：')
height = int(height) / 100
weight = int(weight) 
bmi = weight / height / height
if bmi < 18.5:
    print('你的BMI', bmi, '屬於過輕')
elif 18.5 <= bmi < 24:
    print('你的BMI', bmi, '屬於正常範圍')
elif 24 <= bmi < 27:
    print('你的BMI', bmi, '屬於過重')
elif 27 <= bmi < 30:
    print('你的BMI', bmi, '屬於輕度肥胖')
elif 30 <= bmi < 35:
    print('你的BMI', bmi, '屬於中度肥胖')
else:
    print('你的BMI', bmi, '屬於重度肥胖')