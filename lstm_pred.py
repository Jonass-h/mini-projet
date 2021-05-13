import random


# max tracked person
num_person = 2
# stor person id's and their poses
# TODO : 7aja kima ttl
ctx = { }
# store keys
keys = []

def update_keys(

):
    return [k for k,v in ctx.items()]

def update_ctx(
    new_id,
    new_pose
):
    if new_id in ctx:
        if(len(ctx[new_id]) >= 4):
                        # make predection !
            ret = ctx[new_id]
            ctx[new_id].pop(0)  ## 
            ctx[new_id].append(new_pose)
            return True, ret
        ctx[new_id].append(new_pose)

    else :
        if len(ctx) == num_person:
            keys = update_keys()
            random.shuffle(keys) # TODO : za3ma sa7 :/
            key = keys.pop(0)
            ctx.pop(key)
        
        ctx[new_id] = [new_pose]
    return False, None
