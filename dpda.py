#!/usr/bin/env python2.7

import sys
import os

cmdrules = sys.argv[1]
cmdinput = sys.argv[2]

rules = open(cmdrules)

title = rules.readline()
title = title.strip()

print title

inputa = rules.readline()
alpha = [x.strip() for x in inputa.split(',')] # parsing the input alphabet and putting into array

inputs = rules.readline()
stackalph = [y.strip() for y in inputs.split(',')] # parsing the stack inputs and putting into array

s = rules.readline()
states = [z.strip() for z in s.split(',')] # parsing the states and putting into array

first = rules.readline()
first = first.strip() # getting the first initial start state into a variable

l = rules.readline()
last = [w.strip() for w in l.split(',')]    # parsing the accepted states and putting into array

transition = []
stack = []
#trapstates = []

rulecount = 1
for line in rules:          # printing the rules and appending them to a list
        print "Rule #" + str(rulecount) + " : " + line,
        line = line.replace('|', ",")
        transition.append([str(u.strip()) for u in line.split(',')])
        rulecount += 1


print '\n'
input = open(cmdinput)



for inputlines in input.readlines():    # loop through the strings in the input file
    stack = []      # reset the stack
    ifrulefound = 0
    i = 0
    step = 0
    ruleno = 0
    currentst = first
    inputlines = inputlines.strip()
    print 'String: ' + inputlines
#    for inputc in inputlines:
    while i < len(inputlines): # loop through the characters in the each input string
        if inputlines[i] not in alpha:      #check for incorrect input
            print "an input character was not in the specified input alphabet provided"
            ifrulefound = 1;
            break
        else:
            ruleno = 0
            foundrule = 0
            stacklength = len(stack)
            for transc in transition:       # loop through the rules
                ruleno = ruleno + 1

                if currentst == transc[0] and inputlines[i] == transc[1]:   #checking to find state and input value
                    if transc[2] == '~':        #check to see if you need to add to the stack or do nothing
                        prestate = currentst
                        currentst = transc[3]
                        step += 1
                        foundrule += 1
                        if transc[2] == '~' and transc[4] != '~':
                            if len(stack) == 0:
                                print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), '~', '|', str(currentst),
                            else:    
                                print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), stack[-1:], '|', str(currentst),
                            stack.append(transc[4])
                            print stack[::-1]
                        elif transc[2] == '~' and transc[4] == '~':
                            if len(stack) == 0:
                                print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), '~', '|', str(currentst),
                            else:    
                                print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), stack[-1:], '|', str(currentst),                           
                            if len(stack) == 0:
                                print '~'
                            else:
                                print stack[::-1]
                        i += 1
                        break
                    if stacklength != 0 and transc[2] == stack[-1]:     # check to see if you need to do all 4 operations(replace, pop, push, or nothing)
                        prestate = currentst
                        currentst = transc[3]
                        step += 1
                        foundrule += 1
                        if len(stack) == 0:
                            print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), '~', '|', str(currentst),
                        else:    
                            print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), stack[-1:], '|', str(currentst),                         
                        if transc[2] == '~' and transc[4] != '~':
                            stack.append(transc[4])
                        elif transc[2] == '~' and transc[4] == '~':
                            pass
                        elif transc[2] != '~' and transc[4] == '~':
                            stack.pop()
                        elif transc[2] != '~' and transc[4] != '~':
                            stack.pop()
                            stack.append(transc[4])
                        if len(stack) == 0:
                            print '~'
                        else:
                            print stack[::-1]
                        i += 1
                        break
                if currentst == transc[0] and transc[1] == '~':     # check to see there is a default transition with input being ~
                    prestate = currentst
                    currentst = transc[3]
                    step += 1
                    foundrule += 1
                    if len(stack) == 0:
                        print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), '~', '|', str(currentst),
                    else:    
                        print 'Step', step, '#', 'Rule', ruleno, ':', str(prestate), str(inputlines[i]), stack[-1:], '|', str(currentst),
                    stack.append(transc[4])
                    print stack[::-1]
                    break
            if foundrule == 0:      #if a runthrough didn't find a rule then it will break and reject
                ifrulefound = 1
                break
    if currentst not in last or ifrulefound == 1:       # Reject and Accept Testing
        print 'Rejected'
    elif currentst in last:
        print 'Accepted'
    print '\n'



input.close()
rules.close()
        
           
          
