def hha(deg_seq):
    deg_seq = sorted(list(deg_seq), reverse = True)
    if sum(deg_seq)%2 or (len(deg_seq) == 1 and deg_seq[0] != 0):
        return False
    elif len(deg_seq)==0 or deg_seq == [0]:
        return True
    else:
        deg = deg_seq[0]
        new = deg_seq[1:]
        for x in range(deg):
            new[x] = new[x]-1
        return hha(new)


