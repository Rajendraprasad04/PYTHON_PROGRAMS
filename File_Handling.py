'''fo=open('data.txt','w')
s=['raj ','prasad',' hello']
fo.writelines(s)
fo.close()
print(fo)'''

'''fo=open('data.txt','a')
fo.write('my name is k rajendra prasad')
fo.close()





with open('hai.txt','w') as fo:
    fo.write('Hi k Rajendra prasad')
    print(fo.closed)
print(fo.closed)

with open('jsondata1.txt','w') as fo:
    import json
    po={'name':'k Rajendra prasad','age':23,'mobile':(987,654),'male':True,'female':False,'GF':None}
    print(po)
    jo=json.dumps(po)
    print(jo)
    fo.write(jo)
    
with open('jsondata3.txt','w') as fo:
    import json
    po={'name':'k Rajendra prasad','age':23,'mobile':(987,654),'male':True,'female':False,'GF':None}
    print(po)
    json.dump(po,fo)
    
with open('rajendra.txt','r') as fo:
    import json
    jd=fo.read()
    print(jd)
    pd=json.dumps(jd)
    print(pd)
'''

'''
with open('binarydata1.pkl','wb') as f:
    import pickle
    po={'name':'k rajendra','age':22}
    print(po)
    bo=pickle.dumps(po)
    print(bo)
    f.write(bo)'''

'''
with open('binarydata2.pkl','wb') as f:
    po={'name':'rajendra','age':22}
    import pickle
    print(po)
    bo=pickle.dump(po,f)
    print(bo)'''


with open('binarydata1.pkl','rb') as f:
    import pickle
    bo=f.read()
    print(bo)
    po=pickle.loads(bo)
    print(po)
    































































    
       
