from sklearn import svm
###########Read
with open("noticias/noticias.txt","r") as _file:
    _NEWS = []
    _tempbody = ""
    _tempheader = ""
    _temptime = ""
    _templines = []
    for _line in _file:
        if "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%" in _line:
            _tempheader = _templines[0]
            _temptime = _templines[1]
            _tempbody = _templines[2:]
            
            _NEWS.append([_tempheader,_temptime,_tempbody])
            
            _templines = []

            
        else:
            _templines.append(_line)

####extracting features
for _new in _NEWS:
    print _new[2][3]

def extract_features(_new):
    _very_violence = {"muerte": 1.00, "muerto" : 1.00, "fallecio" : 1.00, "fallecido" : 1.00}
    _mild_violence= {"accidente": 0.5, "volcadura" : 0.5, "arma blanca" :0.5}
    _low_violence  = {"bullying": 0.1, "acoso":0.1 }

    for _item in _very_violence.items():
        pass
####classification
X = [ [0,0],[1,1]]
y =["violenta","no violenta"]
clf = svm.SVC()
clf.fit(X, y)  

result = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)

p = clf.predict([[0., 0.]])
#print p
