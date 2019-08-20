import codecs
import lxmls.sequences.hmm as hmmc
import simple_sequence as sq
simple=sq.SimpleSequence()
hmm = hmmc.HMM(simple.x_dict, simple.y_dict)
hmm.train_supervised(simple.train,smoothing=0.0000001)

'''
print "Initial Probabilities:"    , hmm.initial_probs
print "Transition Probabilities:" , hmm.transition_probs
print "Final Probabilities:"      , hmm.final_probs
print "Emission Probabilities"    , hmm.emission_probs


initial_scores, transition_scores, final_scores, emission_scores = hmm.compute_scores(simple.train.seq_list[0])
print 'initial_scores='    , initial_scores
print 'transition_scores'  , transition_scores
print 'final_scores'       , final_scores
print 'emission_scores'    ,emission_scores

import numpy as np
#from lxmls.sequences.log_domain import *
a = np.random.rand(10)
print np.log(sum(np.exp(a)))
log_likelihood, forward = hmm.decoder.run_forward(initial_scores, transition_scores,final_scores, emission_scores)
print 'Log-Likelihood =', log_likelihood
state_posteriors, _, _ = hmm.compute_posteriors(initial_scores,transition_scores,final_scores,emission_scores)
print state_posteriors[0]
print len(state_posteriors)
y_pred = hmm.posterior_decode(simple.test.seq_list[0])
print len(simple.test.seq_list)
print "Prediction test 0:", y_pred
print "Truth test 0:", simple.train.seq_list[0]

log_likelihood, backward = hmm.decoder.run_backward(initial_scores, transition_scores, final_scores, emission_scores)
#print 'Log-Likelihood =', log_likelihood
'''

Err=[]
a=float(len(simple.test.seq_list))  
print 'Number Of Characters For Test :',int(a)
output = ''
#h=0
#q=0
#count=0
for e in range(0,len(simple.test.seq_list)):
    
    y_pred, score = hmm.viterbi_decode(simple.test.seq_list[e])
    #print y_pred
#print "Viterbi decoding Prediction test 0 with smoothing:", y_pred, score


    #h=h+1
    #x=str(simple.test.seq_list[e])
    y=str(y_pred)  
    #count =count +1
    #x1=x.rstrip().split(' ')
    
    y1=y.rstrip().split(' ')
    
    #for u in range(0,len(x1)):
        
       # tmp1=x1[u].split('/')
       # tmp1=str(tmp1[1]).rstrip().split('@')
    tmp2=y1[0].split('/')
    tmp2=str(tmp2[1]).rstrip().split('@')
    if tmp2[0] == '_':
        output = output + ' '
    else:
        output = output + tmp2[0]
fp = open('output.txt', 'w' , 'utf8')
fp.write(output)
fp.close()
       # if tmp1[1]==tmp2[1]:
         #   q=q+1
        #print x1[u].split('/'),y1[u].split('/')
        #print 'q=',q
    
    #print 'count=',count
    #print y
#print x[0],x[6]

 
#print 'Mean_Err_Correcting typos10 without a dictionary=',1-(float(q)/count)
#print Err
