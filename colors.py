import random

def select_color(_used):
    colors = ['aliceblue', 'aqua', 'aquamarine', 'azure', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'cornflowerblue', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dodgerblue', 'firebrick', 'forestgreen', 'fuchsia', 'gainsboro', 'gold', 'goldenrod', 'green', 'greenyellow', 'honeydew', 'indianred', 'indigo', 'lavender', 'lavenderblush', 'lawngreen', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'moccasin', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'peachpuff', 'peru', 'pink', 'plum', 'purple', 'red', 'rosybrown', 'royalblue', 'seagreen', 'sienna', 'skyblue', 'slateblue', 'springgreen', 'steelblue', 'thistle', 'tomato', 'turquoise', 'violet', 'yellowgreen'
    ]


    index = random.randint(0, len(colors) - 1)

    while colors[index] in _used:
        index = random.randint(0, len(colors))

    return (colors[index])
