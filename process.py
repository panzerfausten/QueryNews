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
def clean_word(_word):
    return _word.replace(".","").replace(",","").replace("?","").replace(" ","").replace("\n","")
def extract_features(_new):
    _very_violence = {"muerte": 1.00, "muerto" : 1.00, "fallecio" : 1.00, "fallecido" : 1.00}
    _mild_violence= {"accidente": 0.5, "volcadura" : 0.5, "arma blanca" :0.5}
    _low_violence  = {"bullying": 0.1, "acoso":0.1 }

    _newText = _new[2]

    _avg_violence = 0.0
    _total_matching_words = 0
    _matching_words = []

    for _line in _newText:
        for _word in _line.split(" "):
            _w = clean_word(_word)
            if _w in _very_violence:
                _total_matching_words += 1
                _avg_violence += _very_violence[_w]
                _matching_words.append(_w)

            if _w in _mild_violence:
                _total_matching_words += 1
                _avg_violence += _mild_violence[_w]
                _matching_words.append(_w)

            if _w in _low_violence:
                _total_matching_words += 1
                _avg_violence += _low_violence[_w]
                _matching_words.append(_w)


    if ( _total_matching_words != 0):
        _avg_violence = _avg_violence / _total_matching_words

    return [_new,_avg_violence,_matching_words]
####extracting features
_data = [ ]
for _new in _NEWS:
    _weight = extract_features(_new)[1]
    _data.append( [_weight,_weight])
    _new.append(_data)
    #print [_weight,_weight]
####classification
#X = [[0.1,0.1],[0.2,0.2],[0.3,0.3],[0.4,0.4],[0.5,0.5]]
#y =["a","b","c","d","e",]
X =  _data[:2]
y = ["No Violenta","Violenta"]
clf = svm.SVC()
clf.fit(X, y)  

result = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)

_CLASSIFIED_NEWS = _NEWS
_result = clf.predict(_data)
x = 0
for _classified_new in _CLASSIFIED_NEWS:
    print "Noticia: %s \nClasificacion: %s" % ( _classified_new[0].replace("\n",""), _result[x])
    print "\n"
    x +=1
