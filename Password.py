password = 'a123456'
x = 3
while True :
	A = input ('請輸入密碼：')
	if A != password and x != 1 :
		x = x - 1
		print ('密碼錯誤，還有',x,'次機會')
	elif x == 1 :
		print ('登入失敗')
		break
	else :
		print ('登入成功')
		break