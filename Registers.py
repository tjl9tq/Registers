#reads instructions from a textfile and splits them by lines
with open('instructions.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]

maxVal = 0; #initialize a maxValue as 0

dict ={} #initialize empty dictionary

#get the all the registers needed and save them into a dictionry and initialize their values to 0
for x in lines:
    split = x.split()
    dict[split[0]] = 0;

#split each line by ' '
for x in lines:
    split = x.split()
    assert (split[1] == 'inc' or split[1] == 'dec'), "Problem with instruction."
    assert (float(split[2]).is_integer()), "Problem with instruction."
    assert (split[3] == 'if'), "Problem with instruction."
    assert (split[5] == '>' or split[5] == '<' or split[5] == '>=' or split[5] == '<=' or split[5] == '=='or split[5] =='!='), "Problem with instruction."
    assert (float(split[6]).is_integer()), "Problem with instruction."
    if split[5] == '>':
        check = dict[split[4]] > int(split[6])
    if split[5] == '<':
        check = dict[split[4]] < int(split[6])
    if split[5] == '>=':
        check = dict[split[4]] >= int(split[6])
    if split[5] == '<=':
        check = dict[split[4]] <= int(split[6])
    if split[5] == '==':
        check = dict[split[4]] == int(split[6])
    if split[5] == '!=':
        check = dict[split[4]] != int(split[6])
    if check:
        if split[1] == 'inc':
            dict[split[0]] += int(split[2])
            if dict[split[0]] > maxVal:  # check if the new value is greater than the saved max value and update if it is
                maxVal = dict[split[0]]
        elif split[1] == 'dec':
            dict[split[0]] -= int(split[2])
            if dict[split[0]] > maxVal:  # update max value
                maxVal = dict[split[0]]

print(dict)

print('The largest value in any register is: ', max(dict.values()))
print('Highest value ever held is: ', maxVal)
