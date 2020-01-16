from benedict import benedict

dic = {'git':'sandy'}
#d = benedict(dict)
d = benedict()
d['h']= 'j'
d['f'] = 'l'
print(d.get_bool('h', default=False))

i = d.invert(flat=True)
print(i)