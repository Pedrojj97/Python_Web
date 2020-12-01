import numpy as np
import os
def class_p(data):
    """
    :param data:(num_samples.num_features+1)
    :return:class_p_dict: dict,probility of each class
    """
    class_p_dict={}
    for i in range(np.shape(data)[0]):
        print(data[i,-1])
        if data[i,-1] in class_p_dict.keys():
            class_p_dict[data[i,-1]]+=1
        else:
            class_p_dict[data[i,-1]]=1
    for key in class_p_dict.keys():
        class_p_dict[key]=class_p_dict[key]/np.shape(data)[0]
    return class_p_dict
def calss_conditional_probability(cls,data,input):
    new_data=cut_data(data,cls)
    print(new_data)
    clss_con_p=P_x(new_data,input)
    return  clss_con_p

def P_x(data,input):
    p_xi=1
    for index,x_i in enumerate(input):
        num=0
        for j in range(np.shape(data)[0]):
            if data[j,index]==x_i:
                num+=1
        p_xi*=(num/np.shape(data)[0])
    return p_xi
def cut_data(data,label):
    tem=[]
    for i in range(np.shape(data)[0]):
        if data[i,-1]==label:
            tem.append(data[i,:])
    return np.array(tem)
def predict(input,data):
    class_pro_dict=class_p(data)
    num_class=len(class_pro_dict)
    pri_list=[]
    for i in range(num_class):
        clss_con_p=calss_conditional_probability(i,data,input)
        print(clss_con_p)
        print(class_pro_dict[i])
        pri_list.append(clss_con_p*class_pro_dict[i]/P_x(data,input))
    print(pri_list)
    return np.argmax(pri_list)
if __name__=='__main__':
    data=[[1,2,3,1,0],[1,2,3,2,1],[1,2,3,3,0]]
    input=[1,2,3,2]
    data=np.array(data)
    print(np.shape(data))
    input=np.array(input)
    print(predict(input,data))


