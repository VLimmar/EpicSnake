import json as js
import testosteron as tt
import excel as ex
def ixzists(sname):
    ses = ex.Sess(bind = ex.unreal)
    wh = ses.query(ex.Table)
    for temp in wh:
        if temp.name == sname:
            return True
    return False
@tt.deco
def filesave(fname, sname, score):
    # file = open(fname, "r")
    # slovar = js.load(file)
    # file.close()
    # slovar[sname] = score
    # file = open(fname, "w")
    # js.dump(slovar, file)
    # file.close()
    if ixzists(sname) is False:
        ses = ex.Sess(bind = ex.unreal)
        chair = ex.Table(name = sname, score = score)
        ses.add(chair)
        ses.commit()
    else:
        ses = ex.Sess(bind = ex.unreal)
        obj = ses.query(ex.Table).filter(ex.Table.name == sname)
        obj[0].score = score
        ses.commit()
    ses.close()

@tt.deco
def fileread(fname, sname):
    # file = open(fname, "r")
    # pslovar = js.load(file)
    # file.close()
    # try:
    #     return(pslovar[sname])
    # except KeyError:
    #     return 0
    ses = ex.Sess(bind = ex.unreal)
    wh = ses.query(ex.Table)
    for temp in wh:
        if temp.name == sname:
            return temp.score
    return 0
    ses.close()
@tt.deco
def top(fname, count):
    # file = open(fname, "r")
    # slovar = js.load(file)
    # pls = []
    # for temp in slovar:
    #     i = slovar[temp]
    #     j = (i, temp)
    #     pls.append(j)
    # nesort(pls)
    # return pls[0:count]
    ses = ex.Sess(bind = ex.unreal)
    wh = ses.query(ex.Table)
    sclist = []
    for temp in wh:
        i = (temp.score, temp.name)
        sclist.append(i)
    nesort(sclist)
    return sclist[0:count]

@tt.deco
def nesort(a):
    b = 0
    for temp in range(0, len(a)):
        for timp in range(0, len(a)):
            if a[temp] > a[timp]:
                b = a[temp]
                a[temp] = a[timp]
                a[timp] = b
    return a
def topdef():
    a = 0
    ind = 0
    b = []
    c = []
    file = open("time.txt", "r")
    for temp in file:
        b.append(temp.split(":")[0])
    for temp in b:
        c.append(b.count(temp))
    for temp in range (0, len(c)):
        if c[temp] > a:
            a = c[temp]
            ind = temp
    file.close()
    return b[ind]
filesave("", "potatoes", 8)