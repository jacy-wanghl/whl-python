#coding:gbk
'''
����˵��:�� һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
����:������
���ڣ�2020/4//11
'''
import random
#reprint("����������һ��ѡ��ʯͷ/����/��/����/ʷ���ˣ�:")
number=random.randint(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name): # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
	if name==("ʯͷ"):
		return 0 # ��Ҫ���Ƿ��ؽ��
	elif name==("ʷ����"):
		return 1
	elif name==("ֽ"):
		return 2
	elif name==("����"):
		return 3
	elif name==("����"):
		return 4
	else:
		return 5
		 # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
   
	
def number_to_name(number):    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
	#                           #������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	if number==0:    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
		b="ʯͷ"
	elif number==1:
		b="ʷ����"
	elif number==2:
		b="ֽ"
	elif number==3:
		b="����"
	elif number==4:
		b="����"
	return b# ��Ҫ���Ƿ��ؽ��
		
def rpsls(player_choice):#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	if name_to_number(player_choice)==5:
		print("Error:No Correct Name!")
	else:
		player_number=name_to_number(player_choice)
		comp_number=random.randint(0,5)
		value1=str(number_to_name(comp_number))
		print("�������ѡ���ǣ�") # ����Ļ����ʾ�����ѡ����������
		print(value1)
		c=int(player_number)-int(comp_number)
		if c==1 or c==2 or c==-3 or c==-4:
			print("��Ӯ�ˣ�")
		elif c==-1 or c==-2 or c==3 or c==4:
			print("�����Ӯ�ˣ�")
		else:# c==0
			print("���ͼ��������һ���أ�") # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
		return 0# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")# ���"-------- "���зָ�
print("����������ѡ��:")    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
choice_name=input()
rpsls(choice_name)
