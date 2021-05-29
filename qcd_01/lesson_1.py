# name = input("请输入姓名:")
# age = input( "请输入年龄:")
# gender = input("请输入性别:")
#
# print("""
#          **********************
#          姓名:{0}
#          年龄:{1}
#          性别:{2}
#          **********************
#       """.format(name,age,gender))
str1 = "python hello aaa 123123aabb"
#1.请取出并打印字符串中的"python"
# 2.请分别判断"o a"   "he"  "ab"是否是该字符串的成员？
# 3.替换"python"为"lemon"
# 4.找到"aaa"的起始位置

#print(str1[:6:])


#str1 = str1.replace ("python","lemon")
#print(str1)


# print(str1.index("o a") )
# print(str1.find('o a'))
# print(str1.index("he"))
# print(str1.find("he"))
# print(str1.index("ab") )
# print(str1.find("ab"))

#print(str1.index("aaa"))
#print(str1.find("aaa"))


print("o a"in str1 )
print("he" in str1)
print("ab" in str1)