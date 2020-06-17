#coding:utf-8
"""
综合项目:世行历史数据基本分类及其可视化
作者：王海玲
日期：2020/5/31

"""

import csv
import math
import pygal
import pygal_maps_world  #导入需要使用的库
word_maps = pygal_maps_world.maps.World()
    # worldmap_chart = pygal.maps.world.World()
    # worldmap_chart.title = 'Some countries'
    # worldmap_chart.add('F countries', ['fr', 'fi'])
    # worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                                   # 'mk', 'ml', 'mm', 'mn', 'mo',
                                   # 'mr', 'mt', 'mu', 'mv', 'mw',
                                   # 'mx', 'my', 'mz'])
    # worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
    # worldmap_chart.render()

def read_csv_as_nested_dict(filename, keyfield, separator, quote): #读取原始csv文件的数据，格式为嵌套字典
    """
    输入参数:
      filename:csv文件名
      keyfield:键名
      separator:分隔符
      quote:引用符

    输出:
      读取csv文件数据，返回嵌套字典格式，其中外层字典的键对应参数keyfiled，内层字典对应每行在各列所对应的具体值
    """
    result={}
    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row
    return result
    
pygal_countries = pygal.maps.world.COUNTRIES #读取pygal.maps.world中国家代码信息（为字典格式），
                                             #其中键为pygal中各国代码，值为对应的具体国名(建议将其显示在屏幕上了解具体格式和数据内容）
 
def reconcile_countries_by_name(plot_countries, gdp_countries): #返回在世行有GDP数据的绘图库国家代码字典，以及没有世行GDP数据的国家代码集合
    """
    
    输入参数:
    plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
    gdp_countries:世行各国数据，嵌套字典格式，其中外部字典的键为世行国家代码，值为该国在世行文件中的行数据（字典格式)
    
    输出：
    返回元组格式，包括一个字典和一个集合。其中字典内容为在世行有GDP数据的绘图库国家信息（键为绘图库各国家代码，值为对应的具体国名),
    集合内容为在世行无GDP数据的绘图库国家代码
    """
    set1 = set()
    dict1 = {}
    for i,j in gdp_countries.items():
        crusial = set(j.values())
        if len(crusial) == 5:
            set1.add(from_value_to_key(i))
        else:
            dict1[from_value_to_key(i)] = i
    for key,value in plot_countries.items():
        if key not in dict1:
            set1.add(key)
    tuple1 = (dict1,set1)
    return tuple1
    # 不要忘记返回结果
    
def from_value_to_key(value):
    for i,j in pygal_countries.items():
        if j == value:
            return i

def from_key_to_value(key):
    for i,j in pygal_countries.items():
        if i == key:
            return j 
            
           #通过自定义函数实现国家代码缩写与国名的自由转换

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    输入参数:
    gdpinfo: 
    plot_countries: 绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
    year: 具体年份值
    
    输出：
    输出包含一个字典和二个集合的元组数据。其中字典数据为绘图库各国家代码及对应的在某具体年份GDP产值（键为绘图库中各国家代码，值为在具体年份（由year参数确定）所对应的世行GDP数据值。为
    后续显示方便，GDP结果需转换为以10为基数的对数格式，如GDP原始值为2500，则应为log2500，ps:利用math.log()完成)
    2个集合一个为在世行GDP数据中完全没有记录的绘图库国家代码，另一个集合为只是没有某特定年（由year参数确定）世行GDP数据的绘图库国家代码
    """
    dict2 = {}
    set2 = set()
    for key,value in gdpinfo.items():
        if from_value_to_key(key) in plot_countries[0]:             #遍历判断"有数据的国家信息"的国名里的key，进入下一个判断
            if value[year] != "":                                   #若此年无数据，则放入第一个集合里
                aeee = float(value[year])
                dict2[from_value_to_key(key)] = math.log(aeee)
            else:
                set2.add(from_value_to_key(key))                     #若该年有数据，则放入字典里
    tuple2 = (dict2,set2,plot_countries[1])
    return tuple2          
    # # 不要忘记返回结果
    

def render_world_map(gdpinfo, plot_countries, year, map_file):
    #将具体某年世界各国的GDP数据(包括缺少GDP数据以及只是在该年缺少GDP数据的国家)以地图形式可视化
    """
    Inputs:
      
      gdpinfo:gdp信息字典
      plot_countires:绘图库国家代码数据，字典格式，其中键为绘图库国家代码，值为对应的具体国名
      year:具体年份数据，以字符串格式程序，如"1970"
      map_file:输出的图片文件名
    
    目标：将指定某年的世界各国GDP数据在世界地图上显示，并将结果输出为具体的的图片文件
    提示：本函数可视化需要利用pygal.maps.world.World()方法
    

    """
    dict3 = {}
    dict4 = {}
    list4 = list(gdpinfo[1])                      #将无序集合转换成为列表进行遍历，放入字典中并赋值"1"
    list5 = list(gdpinfo[2])
    for values in list4:
        dict3[values] = "1"
    for i in list5:
        if i != None:                             #删除第二个集合中的空值
            dict4[i] = "1"

    word_maps.title = '全球GDP分布图'                      #数据可视化输出
    word_maps.add('%s'%year,gdpinfo[0])
    word_maps.add('在绘图库中没有数据的国家',dict3)
    word_maps.add('该年在世行没有GDP数据的国家',dict4)
    word_maps.render_to_file(map_file)


    





# def test_render_world_map(year):  #测试函数
    # """
    # 对各功能函数进行测试
    # """
    # gdpinfo = {
        # "gdpfile": "isp_gdp.csv",
        # "separator": ",",
        # "quote": '"',
        # "min_year": 1960,
        # "max_year": 2015,
        # "country_name": "Country Name",
        # "country_code": "Country Code"
    # } #定义数据字典
  
   
    # pygal_countries = pygal.maps.world.COUNTRIES   # 获得绘图库pygal国家代码字典

    # # 测试时可以1970年为例，对函数继续测试，将运行结果与提供的svg进行对比，其它年份可将文件重新命名
    



pygal_countries = pygal.maps.world.COUNTRIES   # 获得绘图库pygal国家代码字典
#程序测试和运行
print("欢迎使用世行GDP数据可视化查询")
print("----------------------")
year=input("请输入需查询的具体年份:")
#test_render_world_map(year)
number1 = read_csv_as_nested_dict("isp_gdp.csv","Country Name",",",'"')      #运行函数
number2 = reconcile_countries_by_name(pygal_countries,number1)                 #运行第二个函数，并将结果存为变量number2
number3 = build_map_dict_by_name(number1,number2,year)                             #运行第三个函数，并将结果存为变量number3，便于引用
render_world_map(number3,pygal_countries,year,"isp_gdp_world_name_%s.svg"%year)   
