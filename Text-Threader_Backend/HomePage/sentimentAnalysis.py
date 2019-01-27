import pickle


loaded_model_ara = pickle.load(open('../models-dump/sentiment_analysis_model_ara.sav', 'rb'))
loaded_model_tun = pickle.load(open('../models-dump/sentiment_analysis_model_tun.sav', 'rb'))
bow_model_ara = pickle.load(open('../models-dump/bow_model_ara.sav', 'rb'))
bow_model_tun = pickle.load(open('../models-dump/bow_model_tun.sav', 'rb'))


def predict_sentiment_ara(text):
    inst=[]
    inst.append(text)
    text_vect=bow_model_ara.transform(inst)
    prob=loaded_model_ara.predict_proba(text_vect)[0]
    x=prob[0]
    #print(x)
    if x <0.65 and x>0.45:
        return("NEU")
    else:
        return loaded_model_ara.predict(text_vect)[0]

def predict_sentiment_tun(text):
    inst=[]
    inst.append(text)
    text_vect=bow_model_tun.transform(inst)
    prob=loaded_model_tun.predict_proba(text_vect)[0]
    x=prob[0]
    #print(x)
    if x <0.65 and x>0.45:
        return("NEU")
    else:
        return loaded_model_tun.predict(text_vect)[0]
if __name__ == '__main__':
	print(predict_sentiment_tun("زبالة لابارك الله"))
