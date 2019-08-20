# -*- coding: utf-8 -*-

import sys, codecs
from lxmls.sequences.label_dictionary import *
from lxmls.sequences.sequence import *
from lxmls.sequences.sequence_list import *



tmp =codecs.open("data_data.txt","r" , 'utf8')
file=tmp.readlines()
#print file

class SimpleSequence:

    def __init__(self):
        
        observe=unicode(['ا','ب','پ','ت','ث','ج','چ','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ک','گ','ل','م','ن','و','ه','ي','ي','\200c','آ','ک','_'])
        state  =[u'ا', u'ب', u'پ', u'ت',u'ث',u'ج',u'چ',u'ح',u'خ',u'د',u'ذ',u'ر',u'ز',u'س',u'ش',u'ص',u'ض',u'ط',u'ظ',u'ع',u'غ',u'ف',u'ق',u'ک',u'گ',u'ل',u'م',u'ن',u'و',u'ه',u'ي',u'ي','u\200c',u'آ',u'ک',u'_'] 
        
        s=''
        h_observe=[]
        h_state=[]

                    
        
        for i in range(0,len(observe)):
            for j in range(0,len(observe)):
                s=s.__add__(observe[i])
                s=s.__add__('@')
                s=s.__add__(observe[j])
                h_observe.append(s)
                s=''
        print u'h_observe=',h_observe
        for i in range(0,len(state)):
            for j in range(0,len(state)):
                s=s.__add__(state[i])
                s=s.__add__('@')
                s=s.__add__(state[j])
                h_state.append(s)
                s=''
   #     print 'state=',h_state
        self.x_dict = LabelDictionary(h_observe)
        
        
        self.y_dict = LabelDictionary(h_state)
        list3=[]
        list4=[]
        
        #print h_observe
        i=0
        j=0
        t=0
        list1=[] #is correct character
        list2=[] #is  incorrect character
        count=0
        s1=''
        s2=''
        
        for line in file :
            count=count+1
            i=i+1
            a=line.rstrip()
            a=a.split(' ')
           # print a
            if count==1:
                s1=s1.__add__(a[0])
                
                s2=s2.__add__(a[1])
            if len(a)==2 and count>1:
                s1=s1.__add__('@')
                s1=s1.__add__(a[0])
                s2=s2.__add__('@')
                s2=s2.__add__(a[1])
                ###print s1,s2
             #   print a[0],a[1]
                ##list1 is word corect
                ##list2 is word typed
                list1.append(s1)
                list2.append(s2)
                s1=''
                s2=''
                s1=s1.__add__(a[0])
                s2=s2.__add__(a[1])
                if a[0]=='_' and a[1]=='_':
                    t=t+1
                    # t is the number of words
                else:
                    continue
            elif len(a)==1:
                j=j+1
                continue
        t=t+1
        print 'Character_Number=',i   
        print 'Word_Number=',t
           
        co=0

        # Generate training sequences.
        train_sequences = SequenceList(self.x_dict, self.y_dict)
        
        test_sequences = SequenceList(self.x_dict, self.y_dict)
        
        
        #print list1[0]
        #Train set
        spl = 80*len(list1)/100
        train = list1[:int(spl)]
        test = list1[int(spl):]
        for i in range(0,len(train)):
            co=co+1
           
            list3.append(list1[i])
            list4.append(list2[i])
            #print 'co=',co,list4,list3
            #train_sequences.add_sequence(observation,state)
            train_sequences.add_sequence(list4,list3)
            list3=[]
            list4=[]
         #Test set
        for i in range(len(test)):
            co=co+1
            #test_sequences.add_sequence(observation,state)
            list3.append(list1[i])
            list4.append(list2[i])
           # print 'co1=',co,list4,list3
            #train_sequences.add_sequence(observation,state)
            test_sequences.add_sequence(list4,list3)
            list3=[]
            list4=[]
        # Generate test sequences.
            
        self.train = train_sequences
        self.test  = test_sequences
        

