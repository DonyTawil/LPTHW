tabby_cat = "\tI'm tabbed in."
persian_cat =" I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print (tabby_cat,"%s,%s,%s,%s%s%s"%("\n",persian_cat,"\n", backslash_cat,"\n",fat_cat))

print (persian_cat)
print (backslash_cat)
print (fat_cat)

print ('%r %r'%("hello",'motto'))
print ("%s %s"%("hello",'motto'))
