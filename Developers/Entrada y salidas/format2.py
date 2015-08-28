__author__ = 'brapastor'
tabla = {'sjoerd':4127, 'jack':4098,'Dcab':7678}
#
# for nombre, telefono in tabla.items():
#     print('{0,10} ==> {1:10d}'.format(nombre,telefono))

print('jack: {0[jack]:d}; Sjoerd: {0[sjoerd]:d}; Dcab {0[Dcab]:d}'.format(tabla))


