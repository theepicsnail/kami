#r red
#k black
#b blue
#y yellow
#w white
#o orange
#n brown

levels = [
# Page 1, level1
(1,["rrrrrrrrrr",    "rrrrrrrrrr",    "rrrrrrrrrr",    "rrrrrrrrrr",    "rrrrrrrrrr",    "rrrrrrrrrr",    "rrrrrrrrrr",    "rrrrrrrrrr",
    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk"])
, # level 2
(1,["bbbbbbbbbb",    "bbbbbbbbbb",    "bbbbbbbbbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",
    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbbbbbbbbb",    "bbbbbbbbbb",    "bbbbbbbbbb"])
, # level 3
(2,["bbbbbbbbbb",    "bbbbbbbbbb",    "bbbbbbbbbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbkkkkkkbb",    "bbkkkkkkbb",
    "bbkkkkkkbb",    "bbkkkkkkbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbrrrrrrbb",    "bbbbbbbbbb",    "bbbbbbbbbb",    "bbbbbbbbbb"])
, # level 4
(3,["bbbbbbbbbb",    "bbbbbbbbbb",    "kkkkkkkkkk",    "kbbbbbbbbk",    "kbrrrrrrbk",    "kbrkkkkrbk",    "kbrkrrkrbk",    "kbrkrrkrbk",
    "kbrkrrkrbk",    "kbrkrrkrbk",    "kbrkkkkrbk",    "kbrrrrrrbk",    "kbbbbbbbbk",    "kkkkkkkkkk",    "bbbbbbbbbb",    "bbbbbbbbbb"])
, # level 5
(5,["bbbrrbrrbb",    "bbrrbbbrrb",    "brrnnkbbrr",    "rrbbkkkbbr",    "rbbkkbkkbb",    "rbkkbrbkkb",    "rbbkkbkkbb",    "rrbbkkkbbr",
    "brrbbkbbrr",    "bbrrbbbrrb",    "bbbrrbrrbb",    "kbbbrrrbbb",    "kkbbbrbbbk",    "bkkbbbbbkk",    "bbkkbbbkkb",    "bbbkkbkkbb"])
, # level 6
(3,["rrbbbkkkbb",    "rrbbbkkkbb",    "rrbbbkkkbb",    "rrbbbkkkkk",    "rbbbbkrrkk",    "rkkrrkrrkk",    "rkkrrkrrkk",    "rkkrrkkkkk",
    "rbbrrkkkkk",    "kkbrrkrrbb",    "kkbrrkrrbb",    "kkbrrkrrbb",    "krrbbkbbrr",    "krrbbkbbrr",    "krrbbkbbrr",    "kkkkkkbbrr"])
, # level 7
(4,["bbbbbbbbbb",    "bbbbbbbbbb",    "bbbbbbbbbb",    "bbbrrrrrrr",    "bbbrrrrrrr",    "bbbrrkkkkk",    "bbbrrkkkkk",    "bbbrrkkbbb",
    "bbbrrkkbbb",    "bbbrrkkbbb",    "bbbrrkkbbb",    "kkbkkrrbrr",    "kkbkkrrbrr",    "kkkbbbbrrr",    "kkkkkrrrrr",    "kkkkkrrrrr"])
, # level 8
(4,["bbbbbbbbbb",    "rrrrrrrrrr",    "kkkkkkkkkk",    "kkkkkkkkkk",    "rrrrrrrrrr",    "bbbbbbbbbb",    "bkkbkkbkkb",    "bkkbkkbkkb",
    "bbbbbbbbbb",    "rrrrrrrrrr",    "rrrrrrrrrr",    "bbbbbbbbbb",    "bbbbbbbbbb",    "bbbbbbbbbb",    "kkkkkkkkkk",    "kkkkkkkkkk"])
, # level 9
(4,["kkkkkkkkkk",    "kbbkbbbbbk",    "kbbkbkkkbk",    "kkkkbkrkbk",    "kkkkbkkkbk",    "kkkkbbbbbk",    "kkkkkkkkkk",    "kkkkkkkkkk",
    "krrrrrrrrk",    "krkkkkkkrk",    "krkrrrrkrk",    "krkrbbrkrk",    "krkrrrrkrk",    "krkkkkkkrk",    "krrrrrrrrk",    "kkkkkkkkkk"])
, # Page 2, level 10
(3,["rrrrrrrrrr",    "rrrrrrrrrr",    "rrrrrrkrrr",    "rrrrrrkrrr",    "rrrrrrkrrr",    "yyyyyykyyy",    "yyyyyykyyy",    "wwwwwwkwww",
    "wwwwwwkwww",    "wwwwwwkwww",    "rrrrrrkrrr",    "rrrrkkkkkr",    "rrrrrkkkrr",    "rrrrrrkrrr",    "rrrrrrrrrr",    "rrrrrrrrrr"])
, # level 11
(3,["kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkrrrrrrkk",    "kkrrrrrrkk",    "kkrrrrrrkk",    "wwyyyyyyww",    "kkyyyyyykk",
    "kkyyyyyykk",    "wwyyyyyyww",    "kkrrrrrrkk",    "kkrrrrrrkk",    "kkrrrrrrkk",    "kkkkkkkkkk",    "kkkkkkkkkk",    "kkkkkkkkkk"])
, # level 12
(4,["rryyykkkww",    "rryyykkkww",    "rryyykkkwk",    "rryyykkkkk",    "ryyyykrrkk",    "rwwrrkrrkk",    "rwwrrkrrkk",    "rwwrrkkkkk",
    "ryyrrkkkkk",    "kkyrrkrryy",    "kkyrrkrryy",    "kkyrrwrryy",    "krryykyyrr",    "krryykyyrr",    "krryykyyrr",    "kkkkkkyyrr"])
,
(3,["kkkkkkkkkk",    "kkkkkkykyk",    "kkkkkkkykk",    "kkkkkkykyk",    "rkkkkkkkkk",    "krkkkkkkkk",    "kkrkkkkkkk",    "kkkrkkkkkk",
    "kkkkrkkkkk",    "kkkkkrkkkk",    "kkkkkkrkkk",    "kkkkkkkrkk",    "kkkkkkkkrk",    "kkkkkkkkkr",    "kkkkkkkkkk",    "kkkkkkkkkk"])
,
(3,["kkkkkkkkkk",    "kkkkkkykyk",    "kkkkkkkykk",    "kkkkkkykyk",    "rkkkkkkkkk",    "krkkkkkkkk",    "kkrkkkkkkk",    "kkkwkkkkkk",
    "kkkkrkkkkk",    "kkkkkrkkkk",    "kkkkkkrkkk",    "kkkkkkkrkk",    "kkkkkkkkrk",    "kkkkkkkkkr",    "kkkkkkkkkk",    "kkkkkkkkkk"])
,
(4,["kkkkkkkkkk",    "kkkkkkykyk",    "kkkkkkkykk",    "kkkkkkykyk",    "rkkkkkkkkk",    "krkkkkkkkk",    "kkrkkkkkkk",    "rkkwkkkkkk",
    "krkkrkkkkk",    "kkwkkrkkkk",    "kkkrkkrkkk",    "kkkkrkkrkk",    "wwkkkrkkrk",    "wwkkkkrkkr",    "kkrrkkkrkk",    "kkrrkkkkkk"])
,
(4,["kkkkkkkkkk",    "kkykykkkkk",    "kkkykkkkkr",    "kkykykkkrk",    "kkkkkkkrkk",    "kkkkkkrkkk",    "kkkkkrkkkk",    "rkkkwkkykk",
    "kwkrkkykyk",    "kkrkkkkykk",    "kkkrkkykyk",    "kkkkwkkykk",    "kkkkkrkkkk",    "kkkkkkrkkk",    "kkkkkkkrkk",    "kkkkkkkkrk"])
,
(7,["yyyyyykykk",    "yrrwkkwrrk",    "yrrwkkwrry",    "ywwykkywwk",    "yrrryykkky",    "rrkykkykkk",    "kkkykkykkk",    "kkkwrrwkkk",
    "kkkwrrwkkk",    "kkkykkykkk",    "rrkykkykkk",    "yrrryykkky",    "ywwykkywwk",    "yrrwkkwrry",    "yrrwkkwrrk",    "yyyyyykykk"])
,
(7,["yyyyyykykw",    "yrrwkkwrrk",    "yrrwkkwrry",    "ywwykkywwk",    "yrrryykkky",    "rrkykkykkk",    "kkkykkykkk",    "kkkwrrwkkk",
    "kkkwrrwkkk",    "kkkykkykkk",    "rrkykkykkk",    "yrrryykkky",    "ywwykkywwk",    "yrrwkkwrry",    "yrrwkkwrrk",    "yyyyyykykw"])
, # Page 3, level 19
(3,["kkkkkkkrrr",    "krrrrrrrrr",    "krkkkkkrrr",    "krrccckkrr",    "kkkkkckkkk",    "kooocckkkk",    "kockkkkkkk",    "koooooocck",
    "kkkkkkkkck",    "kkkkccccck",    "kkkkckkkkk",    "rrkkccccck",    "rrrkkkkkrk",    "rrrrrrrkrk",    "rrrkkkrrrk",    "rrkkkkkkkk"])
,
(3,["kkkkkkkrrk",    "krrrrrrrkk",    "krkkkkkrrk",    "krrccckkrr",    "kkkkkckkkk",    "kooocckkkk",    "kockkkkkkk",    "koooooocck",
    "kkkkkkkkck",    "kkkkccccck",    "kkkkckkkkk",    "rrkkccccck",    "krrkkkkkrk",    "kkrrrrrkrk",    "krrkkkrrrk",    "rrkkkkkkkk"])
,
(4,["kkkkkkkrrk",    "krccrrrrkk",    "kokkkkkrrk",    "kooccckkrr",    "kkkkkckkkk",    "kooocckkkk",    "kokkkkkkkk",    "koooooocck",
    "kkkkkkkkck",    "kkkkccccck",    "kkkkckkkkk",    "rrkkccccck",    "krrkkkkkok",    "kkrrrcckok",    "krrkkkrrrk",    "rrkkkkkkkk"])
,
(4,["krrrkkkook",    "kkorooookk",    "kkorkkkook",    "cccccckkoo",    "ckorkckcck",    "ckorrccckk",    "ckoorkkcck",    "ckcorrrrcc",
    "rrkooooooo",    "krrkkkkrkr",    "kkrrrkkrrr",    "krrkrkkkrr",    "rrkkrkoorr",    "ckkooookrk",    "cckkrkkkrk",    "kcckrrrrrk"])
]

