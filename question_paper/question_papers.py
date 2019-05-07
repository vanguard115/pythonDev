import states
import random
# print(states.capitalOf('Texas'))

states_list = states.capitals
state_keys = list(states_list.keys())
state_capitals = list(states_list.values())


print('# DEBUG: ',states.capitals.keys(),len(states.capitals.keys()))

for x in range(2):
        fileHandel = open("question_paper_for_%s" %(x+1),'w')
        fileHandel.write("Question Paper number %s \n\n\n"%(x+1))
        count = 1
        already_in = []
        while count <= 50:
            state_keys = list(states_list.keys())
            state_capitals = list(states_list.values())
            selected_key = random.choice(state_keys)
            if selected_key in already_in:
                continue
            else:
                already_in.append(selected_key)

            capital = states_list[selected_key]
            st = {selected_key:capital}

            fileHandel.write("\n\n{}. The captital of {} ? \n".format(count,selected_key))

            state_keys.remove(selected_key)
            state_capitals.remove(capital)

            options = random.sample(state_capitals,3)
            options.append(states.capitals.get(selected_key))
            chars = ['A','B','C','D']
            for y in range(4):
                select = random.choice(options)
                options.remove(select)
                fileHandel.write("\n     {}. {}".format('ABCD'[y],select))
            count +=1
        fileHandel.close()
