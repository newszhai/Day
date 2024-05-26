a=100
b=50
print(a,b,'要么出众，要么出局！！！')
print(ord('北'))
print(ord('京'))
print(chr(21271),chr(20140))

fp=open('note.txt', 'w')
print('北京欢迎你',file=fp)
fp.close()

print('北京欢迎你'+'2023')

# name=input('请输入您的姓名是：')
# print('我的姓名是：'+name)

num=input('请输入您的幸运数字')
print('您的幸运数字是：'+num)
num=int(num)
print('您的幸运数字这是：',num)
