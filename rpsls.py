#coding:gbk
'''
程序说明:第 一个小项目：Rock-paper-scissors-lizard-Spock
作者:王海玲
日期：2020/4//11
'''
import random
#reprint("请输入任意一个选择（石头/剪刀/布/蜥蜴/史波克）:")
number=random.randint(0,4)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name): # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
	if name==("石头"):
		return 0 # 不要忘记返回结果
	elif name==("史波克"):
		return 1
	elif name==("纸"):
		return 2
	elif name==("蜥蜴"):
		return 3
	elif name==("剪刀"):
		return 4
	else:
		return 5
		 # 使用if/elif/else语句将各游戏对象对应到不同的整数
   
	
def number_to_name(number):    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
	#                           #将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	if number==0:    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
		b="石头"
	elif number==1:
		b="史波克"
	elif number==2:
		b="纸"
	elif number==3:
		b="蜥蜴"
	elif number==4:
		b="剪刀"
	return b# 不要忘记返回结果
		
def rpsls(player_choice):#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	if name_to_number(player_choice)==5:
		print("Error:No Correct Name!")
	else:
		player_number=name_to_number(player_choice)
		comp_number=random.randint(0,5)
		value1=str(number_to_name(comp_number))
		print("计算机的选择是：") # 在屏幕上显示计算机选择的随机对象
		print(value1)
		c=int(player_number)-int(comp_number)
		if c==1 or c==2 or c==-3 or c==-4:
			print("您赢了！")
		elif c==-1 or c==-2 or c==3 or c==4:
			print("计算机赢了！")
		else:# c==0
			print("您和计算机出的一样呢！") # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
		return 0# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

print("欢迎使用RPSLS游戏")
print("----------------")# 输出"-------- "进行分割
print("请输入您的选择:")    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
choice_name=input()
rpsls(choice_name)
