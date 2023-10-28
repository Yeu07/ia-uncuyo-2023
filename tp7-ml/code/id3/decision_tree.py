import pandas as pd
import math
import os

class Node:
    def __init__(self,parent = None,value = None,children = None,label=None, classification = None):
        self.parent = parent
        self.value = value
        self.children = children
        self.label = label
        self.classification = classification
    
    def add_child(self,node):
        if self.children != None:
            self.children.append(node)

    def add_label(self,label):
        self.label = label

    def is_leaf(self):
        return self.children == None
    
    def get_value_node(self,value):
        n = len(self.children)
        for i in range(n):
            if self.children[i].label == value:
                return self.children[i]
        return None
    

def decision_tree(examples,classifier):
    attributes = list(examples.columns.values)
    attributes.remove(classifier)

    return learn_decision_tree(examples,attributes,examples,None,classifier)

def plurality_value(data_frame,parent,classifier):
    return Node(parent,None,None,None, data_frame[classifier].value_counts().idxmax())

def same_classification(examples,classifier):
    return len(examples.groupby(["play"])) == 1
   
def bestAttribute(data_frame,classifier,attributes):
    best_save = -1
    best = ""

    for attribute in attributes:
        gain = importance(data_frame,attribute,classifier)
        if gain > best_save:
            best_save = gain
            best = attribute
        return best
    
def importance(data_frame,attribute,classifier):
    value = data_frame.groupby([attribute,classifier]).size().reset_index(name='counts')
    positive = value.loc[value["play"]=="yes","counts"].sum()
    negative = value.loc[value["play"]=="no","counts"].sum()
    entropyy = entropy((positive/(positive+negative)))
    result = remainder(value,classifier,attribute,positive,negative)
    return entropyy-result

def entropy(value):
    if (value == 0 or value == 1):
        return 0
    else:
        return -(value*math.log(value,2)+(1-value)*math.log((1-value),2))
    
def remainder(values,classifier,attribute,positive,negative):
    size = len(values)
    rem = 0
    val_list = list(values[attribute].unique())

    for val in val_list:
        pk = values.loc[(values["play"]=="yes") & (values[attribute]==val),"counts"].sum()
        nk = values.loc[(values["play"]=="no") & (values[attribute]==val),"counts"].sum()
        rem += ((pk+nk)/(positive+negative))*entropy((pk/(pk+nk)))

    return rem

def predict(tree,data_frame,classifier):
    size = len(data_frame)
    df = data_frame.loc[:,data_frame.columns != classifier]
    columns_size = df.columns.size
    data_frame["prediction"] = ""

    for index in df.index:
        previous_node = None
        current_node = tree
        while current_node != None and not(current_node.is_leaf()):
            attr = current_node.value
            val = df.loc[index,attr]
            previous_node = current_node
            current_node = current_node.get_value_node(val)
        if current_node != None:
            prediction = current_node.classification
        else:
            return False
        data_frame.loc[index,"prediction"] = prediction
    return True

def print_tree(tree):
    levels=[]
    printTreeRec(tree,0,levels)
    for i in range(0,len(levels)):
        for j in range(0,len(levels[i])):
            print(levels[i][j],"_", end=" ")
        print()

def printTreeRec(tree,level,levels):
    levels.append([])
    if tree.parent==None:
        print("PARENT")
        print(tree.value)
        print("")
    if tree.children==None:
        return       
    for i in range(0,len(tree.children)):
        if (tree.children[i].isLeaf()):
            label="|lab="+str(tree.children[i].label)
            classification="{{"+str(tree.children[i].classification)+ "}}"
            node = label + classification
        else:
            label="|lab: "+str(tree.children[i].label)
            value=("["+str(tree.children[i].value) + "]")
            node = label + value
        printTreeRec(tree.children[i],level+1,levels)
        levels[level].append(node)
    
        


def learn_decision_tree(examples,attributes,parent_examples,parent,classifier):
    if examples.empty:
        return plurality_value(parent_examples,examples,classifier)
    elif same_classification(examples,classifier):
        return plurality_value(examples,parent,classifier)
    elif len(attributes)==0:
        return plurality_value(examples,parent,classifier)
    
    attribute = bestAttribute(examples,classifier,attributes)

    tree = Node(parent,attribute,children=[])

    values = list(examples[attribute].unique())

    for value in values:
        exs = examples.loc[examples[attribute]==value]
        attributes.remove(attribute)
        subtree = learn_decision_tree(exs,attributes,examples,tree,classifier)
        attributes.append(attribute)
        subtree.add_label(value)
        tree.add_child(subtree)

    return tree