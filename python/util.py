def get_color_arr(sum, size=2):
    ret = []
    rgb = ('#d9534f',
           '#5cb85c',
           '#428bca')

    # rgb = ('#A',
    #        '#B',
    #        '#C')

    lev = 0
    total = 1
    for i in range(1, sum + 1):
        ret.append(rgb[lev % 3])
        if i == total:
            lev += 1
            total += size ** lev
    return ret
