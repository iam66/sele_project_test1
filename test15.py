def make_albums(singer,album,count=''):
    make_album={}
    if count:
        make_album[singer]=album
        make_album['count']=count
    else:
        make_album[singer]=ablum
    return make_album

ablum=make_albums('jj','gogo',4)
print(ablum)
ablum1=make_albums('tt','go')
print(ablum1)
