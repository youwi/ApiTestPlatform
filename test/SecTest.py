from sec import ProjectCode, unsigned_left_shitf

# print(ProjectCode.encode(12))

# print(ProjectCode.encode(124))

# print(ProjectCode.encode(196))

# print(ProjectCode.decode("qpat73thke64"))
# print(ProjectCode.decode("s2rcmic05vnl"))


#
# print(ProjectCode.fshr(17,-1985229065))
#
# print(ProjectCode.fshr(196,2))
#
# print(ProjectCode.fshr(196,3))
#
# print(ProjectCode.fshr(196,4))
#
# print(ProjectCode.fshl(196,1))
#
# print(ProjectCode.fshl(196,2))
#
# print(ProjectCode.fshl(196,3))
#
# print(ProjectCode.fshl(196,4))
#
#
# print(ProjectCode.decode("qpat73thke64"))
# print(ProjectCode.encode(196))
print(ProjectCode.decode("j2h6so6afltv"))

#
#
# print(ProjectCode.CHARSET_NUM)
# print(ProjectCode.CHARSET_CHAR)
#
#
# print(unsigned_left_shitf(ProjectCode.key, 32))

for i in range(1, 1000):
    print(ProjectCode.decode(ProjectCode.encode(i)))
