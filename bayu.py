# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from gtts import gTTS
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, wikipedia, tweepy

cl = LINETCR.LINE()
cl.login(token="Em4tekKxePikSrhRZMp2.Skq32mqBkuNH3J/isSmUaG.iAyzUpvYly2BdxsidWYPnMeYL4ypPYPFmofRFJ+On7A=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="Em0iFFDUJ1CJde4sdY93.fJw80/Syx5/6pE2qki4riW.PPS8y0jwSdPUHLrxFEoyJDM7hqbU1jIdiGNDDudlGkA=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EmJgwc5qQHniVdycMumf.HWzb6NVs6n8K32bL6KC3ZW.xNt/znq/kWSebpzk8XQ2AhqZN2Ei9svdykoJ5xIRw+4=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EmI4fLxc7SzXQHuBiX05.3V6C4Vi0/5iV3v0y/wAe9q.lpgYIIY0hPeDvnRSphdW3D88m3wHUTqRKzMmHyON+lk=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EmMgHDQvnJrcRDerg2S4.gverIQ60Hdx+5CvqmcCv5a.6SM4LUu6fKBlBqg+vQwvNQSKrrwUQwyMWwDMjpoQudY=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EmYItoqUPOQqpjFSLz84.cuU1vPcgGwBoaep7TZjova.v8ZeRrcVHctUoMR94ePl72GlIX7mec4wN4FoI/yt4Oo=")
ki5.loginResult()

#ki6 = LINETCR.LINE
#ki6.login(token="EmsiniXnvxcuV8giurSd.lCX3mfpj65dajYCa6Pbj3q.2LjYzoUFFPRCY8z2KYklO6mo9iPSJdB7guHlqDi2MJY=")
#ki6.loginResult()

#ki7 = LINETC.LINE
#ki7.login(qr=True)
#ki7.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔═¶═◙¶═════════════════
❂͜͡☆➣「Selfbots Command」
╠═¶═◙¶═════════════════
║"͡Me 「Send Your Contact」
║"͡Mid「Send Your ID」
║"͡͡TL:「Update Your timeline」
║"͡͡Myname:「Set Your name」
║"͡͡Mybio: 「Set Your Status」
║"͡͡Allbio:「Set Bots Status」
║"͡͡Allbots:「Set Bots Name」
║"͡͡Copy @「Clone People」
║"͡͡Backup「Backup Profile」
║"͡͡@Tags 「Tag All Members」
║"͡͡Mybots「Send Bots Contact」
║"͡͡Ginfo 「Groups Info」
║"͡͡Gid   「Groups ID」
║"͡͡Cancel 「Cancel Invite」
║"͡͡Gn  「Change Name Groups」
║"͡͡Url 「URL Invite Groups」
║"͡͡Ourl 「Open URL Groups」
║"͡͡Curl 「Close URL Groups」
║"͡͡/pic 「Profile Pictures」
║"͡͡/cover 「Cover Photos」
║"͡͡/stalk 「Instagram」
║"͡͡/youtube 「Youtube」
║"͡͡/music 「Mp3 Music」
║"͡͡/lyrics 「Songs Lyrics」
║"͡͡/wikipedia 「Wikipedia」
║"͡͡/reboot「Restart Your Programs」
╠═¶═◙¶═════════════════
❂͜͡☆➣「Protection Command」
╠═¶═◙¶═════════════════
║"͡͡Like on/off
║"͡͡Protect on/off
║"͡͡Cancel on/off
║"͡͡Invite on/off
║"͡͡Qr on/off
║"͡͡Add on/off
║"͡͡Share on/off
║"͡͡Contact on/off
╠═¶═◙¶═════════════════
❂͜͡☆➣「Other Commads」
╠═¶═◙¶═════════════════
║"͡͡/「」
║"͡͡/「」
║"͡͡/「」
║"͡͡/「」
║"͡͡/spam 「Text Here」
║"͡͡BroadcastFriends 「Text Here」
║"͡͡BroadcastGroups 「Text Here」
║"͡͡Mimic「Set Target」
║"͡͡Mcheck「Checking Banlist」
║"͡͡/clearban 「Clear Banlist」
╠═¶═◙¶═════════════════
❂͜͡☆➣「JustFunForMe」
╠═¶═◙¶═════════════════
❂͜͡☆➣「Not Order」
╠═¶═◙¶═════════════════
❂͜͡☆➣「⌐FadhiL™¬」
╚═¶═◙¶═════════════════"""
KAC=[ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
#ki6mid = ki6.getProfile().mid
#ki7mid = ki7.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,"ub0a437d8c41b2949e1de3f884ac32e02","u8ab7154f68d4b0943b76b26c04a52cac"] #jika mau menambahkan bot jgn lupa taroh disini cth. ki5mid didalem [] jangan lupa tanda koma
admsa = "ub0a437d8c41b2949e1de3f884ac32e02"
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"""тнαикѕ fσя α∂∂ιиg мє αѕ α fяιєи∂
    line.me/ti/p/~.-youknowmela_""",
    "lang":"JP",
    "comment":"Autolike by line.me/ti/p/~.-youknowmela_",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "likeOn":False,

}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mimic = {
    "status":False,
    "target":{}
    }

#---------------------------------------------------------------------------------------------------------------------------------------
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for tex in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#----------------------------------------------------------------------------------------------------------------------------------------
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
#----------------------------------------------------------------------------------------------------------------------------------------
def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
#----------------------------------------------------------------------------------------------------------------------------------------
def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.post_content(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True
#----------------------------------------------------------------------------------------------------------------------------------------
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
#----------------------------------------------------------------------------------------------------------------------------------------
def sendContact(self, to, mid):
      msg = Message()
      msg.to = to
      msg.text = None
      msg.contentType = 13
      msg.contentMetadata = {'mid': mid}
      return self.Talk.client.sendMessage(0, msg)
#---------------------------------------------------------------------------------------------------------------------------------------
def sendImage2(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self._client.sendMessage(M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
#----------------------------------------------------------------------------------------------------------------------------------------
def sendImageWithURL(self, to_, url):
        """Send a image with given image url

        :param url: image url to send
        """
        path = 'tmp/pythonLine.data'

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download image failure.')

        try:
            self.sendImage(to_, path)
        except Exception as e:
            raise e

def sendAudio(self, to_, path):
      M = Message(to=to_,contentType = 3)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'audio',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload audio failure.')
      return True
#----------------------------------------------------------------------------------------------------------------------------------------
def sendAudioWithURL(self, to_, url):
        path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True)
        if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
        else:
         raise Exception('Download audio failure.')
        try:
         self.sendAudio(to_, path)
        except Exception as e:
         raise e
#----------------------------------------------------------------------------------------------------------------------------------------
def autolike():
     for zx in range(0,50):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Likes By line.me/ti/p/~.whome_")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Likes By line.me/ti/p/~.whome_")
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Likes By line.me/ti/p/~.whome_")
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Likes By line.me/ti/p/~.whome_")
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Likes By line.me/ti/p/~.whome_")
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Likes By line.me/ti/p/~.whome_")
            #ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Likes By line.me/ti/p/~.whome_")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#----------------------------------------------------------------------------------------------------------------------------------------
def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          #ki6.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
#----------------------------------------------------------------------------------------------------------------------------------------
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 11:
           if wait["linkprotect"] == True:
               if op.param2 not in Bots:
                   G = random.choice(KAC).getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(KAC).updateGroup(G)
        if op.type == 11:
            if wait["blackliist"] == True:
                   print "Blacklist"
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("�1�7�1�7",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("·",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 18:
            if wait["blacklist"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(op.param3)
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
        if op.type == 18:
            if wait["blacklist"] == True:
                print "blacklist"
        if op.type == 19:
            if op.param2 not in Bots:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 32:
            if wait["cancelprotect"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(op.param3)
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 13:
           if wait["inviteprotect"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) == wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) == wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#----------------------------------------------------------------------------------------------------------------------------------------
        #if op.type == 15:
            #random.choice(KAC).sendText(op.param1, "Good Bye :)")
            #print op.param3 + "has left the group"
#----------------------------------------------------------------------------------------------------------------------------------------
        #if op.type == 17:
            #group = cl.getGroup(op.param1)
            #cb = Message()
            #cb.to = op.param1
            #cb.text = cl.getContact(op.param2).displayName + " Selamat Datang di " + group.name
            #cl.sendMessage(cb)
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admsa:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = ki.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        except:
                            ki.sendText(msg.to,"error")
#----------------------------------------------------------------------------------------------------------------------------------------
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1001)
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki3.like(url[25:58], url[66:], likeType=1001)
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki5.like(url[25:58], url[66:], likeType=1001)
#----------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already on my blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Already on my blacklist")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Not in My blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
#----------------------------------------------------------------------------------------------------------------------------------------
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#----------------------------------------------------------------------------------------------------------------------------------------
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "User Post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "User Posting URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "User Posting URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "User Posting URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "/bots @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in admsa:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bots @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        ki.findAndAddContactsByMid(target)
                        ki2.findAndAddContactsByMid(target)
                        ki3.findAndAddContactsByMid(target)
                        ki4.findAndAddContactsByMid(target)
                        ki5.findAndAddContactsByMid(target)
                      except:
                        ki.sendText(msg.to,"")
              else:
                ki.sendText(msg.to,"Perintah Ditolak")
                ki.sendText(msg.to,"Perintah ini Hana Untuk Owner Kami")
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"This Command only work in Groups")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"This Command only work in Groups")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                ki.findAndAddContactsByMid
                ki.kickoutFromGroup(msg.to,[midd])
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Invite:on:" in msg.text:
                midd = msg.text.replace("Invite:on:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
                ki4.findAndAddContactsByMid(midd)
                ki4.inviteIntoGroup(msg.to,[midd])
                ki5.findAndAddContactsByMid(midd)
                ki5.inviteIntoGroup(msg.to,[midd])
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Mybots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': ki6mid}
                #cl.sendMessage(msg)
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': ki7mid}
                #cl.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Bots1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Bots2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "Bots3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Bots3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Bots4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "Bots5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["All gift","Gift all"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                #ki6.sendMessage(msg)
                #ki7.sendMessage(msg)
                
            elif msg.text.lower() == 'please':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7115454",
                                     "STKPKGID": "5029",
                                     "STKVER": "7" }
                cl.sendMessage(msg)

            elif msg.text.lower() == 'wtf?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7115455",
                                     "STKPKGID": "5029",
                                     "STKVER": "1" }
                cl.sendMessage(msg)

            elif msg.text.lower() == 'argh':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7115465",
                                     "STKPKGID": "5029",
                                     "STKVER": "1" }
                cl.sendMessage(msg)

            elif msg.text.lower() == 'apa?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7115460",
                                     "STKPKGID": "5029",
                                     "STKVER": "1" }
                cl.sendMessage(msg)

            elif msg.text.lower() == 'pulang':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7115462",
                                     "STKPKGID": "5029",
                                     "STKVER": "1" }
                cl.sendMessage(msg)

            elif msg.text.lower() == '/bye':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "22087",
                                     "STKPKGID": "1252",
                                     "STKVER": "7" }
                cl.sendMessage(msg)

            elif msg.text.lower() == 'iss':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "22099",
                                     "STKPKGID": "1252",
                                     "STKVER": "7" }
                cl.sendMessage(msg)

            elif msg.text.lower() == '..':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "22090",
                                     "STKPKGID": "1252",
                                     "STKVER": "7" }
                cl.sendMessage(msg)

            elif msg.text.lower() == '...':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7115453",
                                     "STKPKGID": "5029",
                                     "STKVER": "7" }
                cl.sendMessage(msg)

            elif msg.text in ["kam","Welkam","Kam"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                #ki6.sendMessage(msg)
                #ki7.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in["Jembot","hm","Hm","wtf","Wtf"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.to = msg.to
                cl.sendMessage(cnt)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in["lol","@Tag","@Tags","@tag","@tags"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, jml = [], [], [], len(nama)
                if jml <= 100:
                   mention(msg.to, nama)
                if jml > 100 and jml < 200:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, len(nama)-1):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                if jml > 200  and jml < 300:
                   for i in range(0, 99):
                       nm1 += [nama[i]]
                   mention(msg.to, nm1)
                   for j in range(100, 199):
                       nm2 += [nama[j]]
                   mention(msg.to, nm2)
                   for k in range(200, len(nama)-1):
                       nm3 += [nama[k]]
                   mention(msg.to, nm3)
                if jml > 300:
                    print "Terlalu Banyak Men 300+"
                cnt = Message()
                cnt.to = msg.to
                cl.sendMessage(cnt)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["B Cancel","Cancel say","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Ga ada pendingan BosQ ")
                        else:
                            ki.sendText(msg.to,"Invite people inside not")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Ga ada pendingan BosQ")
                    else:
                        ki.sendText(msg.to,"Ga ada pendingan BosQ")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"")
                        else:
                            cl.sendText(msg.to,"")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
            elif msg.text.lower() == '/reboot':
                    print "[Command]Restart"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif "/say " in msg.text:
                say = msg.text.replace("/say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Ourl"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to," ")
                    else:
                        cl.sendText(msg.to," ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Boss")
                    else:
                        cl.sendText(msg.to,"Done Boss")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to," ")
                    else:
                        cl.sendText(msg.to," ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done boss ")
                    else:
                        cl.sendText(msg.to,"Done Boss ")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "Bots mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Allbots:" in msg.text:
                string = msg.text.replace("Allbots:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    cl.sendText(msg.to,"All Name of MyBots Was Updated " + string + "" )
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio✓ :" + string + " done BossQ")
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿All Bio of Bots Was Updated " + string + " ")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names " + string + " ")
            elif "/removechat" in msg.text.lower():
                if msg.from_ in admsa:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Copy @" in msg.text:
             if msg.from_ in admsa:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Succes Copy profile~")
                            except Exception as e:
                                print e

            elif msg.text in ["Backup","backup"]:
               if msg.from_ in admsa:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Profile back..")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "/pic @" in msg.text:
                if msg.from_ in admsa:
                   _name = msg.text.replace("/pic @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except Exception as e:
                               cl.sendText(msg.to, str(e))
                              
            elif "/cover @" in msg.text:
                if msg.from_ in admsa:
                    _name = msg.text.replace("/cover @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                cl.sendImageWithURL(msg.to, path)
                            except Exception as e:
                               cl.sendText(msg.to, str(e))
                               
            elif '/stalk ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/stalk ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                 cl.sendText(msg.to, str(njer))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif '/music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[3]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "/youtube " in msg.text:
                 query = msg.text.replace("/youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#---------------------------------------------------------------------------------------------------------------------------------------
            elif '/lyrics ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lyrics ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif '/wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("/wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() == '/ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() == '/system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() == '/kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() == '/cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#---------------------------------------------------------------------------------------------------------------------------------------

            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Contact on","contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact on")
                    else:
                        cl.sendText(msg.to,"Contact on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already on")
                    else:
                        cl.sendText(msg.to,"Contact Already on")
            elif msg.text in ["Contact off","contact off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already")
                    else:
                        cl.sendText(msg.to,"Contact Already")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already off")
                    else:
                        cl.sendText(msg.to,"Contact Already off")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Protect on","protect on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection on")
                    else:
                        cl.sendText(msg.to,"Protection on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection set to on")
            elif msg.text in ["Protect off","protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection off")
                    else:
                        cl.sendText(msg.to,"Protection off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection set to off")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Qr on","qr on"]:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect on")
                    else:
                        cl.sendText(msg.to,"Link Protect on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect set to on")
                    else:
                        cl.sendText(msg.to,"Link Protect set to on")
            elif msg.text in ["Qr off","qr off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect off")
                    else:
                        cl.sendText(msg.to,"Link Protect off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect set to off")
                    else:
                        cl.sendText(msg.to,"Link Protect set to off")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Autoadd on","autoadd on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd on")
                    else:
                        cl.sendText(msg.to,"Autoadd on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd set to on")
                    else:
                        cl.sendText(msg.to,"Autoadd set to on")
            elif msg.text in ["Autoadd off","autoadd off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd off")
                    else:
                        cl.sendText(msg.to,"Autoadd off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd set to off")
                    else:
                        cl.sendText(msg.to,"Autoadd set to off")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Invite on","invite on"]:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection on")
                    else:
                        cl.sendText(msg.to,"Invite Protection on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection set to on")
                    else:
                        cl.sendText(msg.to,"Invite Protection set to on")
            elif msg.text in ["Invite off","invite off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection off")
                    else:
                        cl.sendText(msg.to,"Invite Protection off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection set to off")
                    else:
                        cl.sendText(msg.to,"Invite Protection set to off")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Cancel on","cancel on"]:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Members Invitation on")
                    else:
                        cl.sendText(msg.to,"Cancel Members Invitation on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel set to on")
                    else:
                        cl.sendText(msg.to,"Cancel set to on")
            elif msg.text in ["Cancel off","cancel off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Members Invitation off ")
                    else:
                        cl.sendText(msg.to,"Cancel Members Invitation off ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Members set to off ")
                    else:
                        cl.sendText(msg.to,"Cancel Members set to off ")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Autojoin on","autojoin on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Groups on ")
                    else:
                        cl.sendText(msg.to,"Auto join Groups on ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on ")
                    else:
                        cl.sendText(msg.to,"Autojoin set to on ")
            elif msg.text in ["Autojoin off","autojoin off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Groups off ")
                    else:
                        cl.sendText(msg.to,"Auto join Groups off ")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off ")
                    else:
                        cl.sendText(msg.to,"Autojoin set to off ")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Groups Invite Members Will Canceled Auto ")
                        else:
                            cl.sendText(msg.to,"Groups Invite Members Will Canceled Auto ")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Groups Invite Members Will Canceled Auto ")
                        else:
                            cl.sendText(msg.to,strnum + "Groups Invite Members Will Canceled Auto ")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Weird value ")
                    else:
                        cl.sendText(msg.to,"Weird value ")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Auto leave on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave Room on ")
                    else:
                        cl.sendText(msg.to,"Leave Room on ")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoleave Room Already on ")
                    else:
                        cl.sendText(msg.to,"Autoleave Room Already on ")
            elif msg.text in ["Auto leave off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Leave Room off ")
                    else:
                        cl.sendText(msg.to,"Leave Room off ")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoleave Room Already off ")
                    else:
                        cl.sendText(msg.to,"Autoleave Room Already off ")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Post on ")
                    else:
                        cl.sendText(msg.to,"Share Post on ")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Post Already on ")
                    else:
                        cl.sendText(msg.to,"Share Post Already on ")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Post off ")
                    else:
                        cl.sendText(msg.to,"Share Post off ")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Post Already off ")
                    else:
                        cl.sendText(msg.to,"Share Post Already off ")
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Blacklist","blacklist"]:
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="Check\n\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Help","help","Keys","keys"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="͡☆➣ ✓ Contact \n"
                else: md+="͡☆➣ × Contact \n"
                if wait["autoJoin"] == True: md+="͡☆➣ ✓ Autojoin \n"
                else: md +="͡☆➣ × Autojoin\n"
                if wait["leaveRoom"] == True: md+="͡☆➣ ✓ Leave \n"
                else: md+="͡☆➣ × Leave \n"
                if wait["timeline"] == True: md+="͡☆➣ ✓ Share \n"
                else:md+="͡☆➣ × Share \n"
                if wait["autoAdd"] == True: md+="͡☆➣ ✓ Autoadd \n"
                else:md+="͡☆➣ × Autoadd \n"
                if wait["protect"] == True: md+="͡☆➣ ✓ Protection \n"
                else:md+="͡☆➣ × Protection \n"
                if wait["linkprotect"] == True: md+="͡☆➣ ✓ Protectlink \n"
                else:md+="͡☆➣ × Protectlink \n"
                if wait["inviteprotect"] == True: md+="͡☆➣ ✓ Protectinvite \n"
                else:md+="͡☆➣ × Protectinvite \n"
                if wait["cancelprotect"] == True: md+="͡☆➣ ✓ Protectcancel \n"
                else:md+="͡☆➣ × Protectcancel \n"
                if wait["likeOn"] == True: md+="͡☆➣ ✓ Autolike\n"
                else:md+="͡☆➣ × Autolike"
                cl.sendText(msg.to,md)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif cms(msg.text,["me","Me"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa }
                cl.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif cms(msg.text,["Creator","creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u8ab7154f68d4b0943b76b26c04a52cac"}
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots out","bots out"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "/byee" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye "  +  str(ginfo.name)  +"")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots1 out","bots1 out"]:
                gid = ki.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"")
                else:
                    ki.sendText(msg.to,"")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots2 out","bots2 out"]:
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                    ki2.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki2.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki2.sendText(msg.to,"He declined all invitations")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots3 out","bots3 out"]:
                gid = ki3.getGroupIdsJoined()
                for i in gid:
                    ki3.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki3.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki3.sendText(msg.to,"He declined all invitations")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots4 out","bots4 out"]:
                gid = ki4.getGroupIdsJoined()
                for i in gid:
                    ki4.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki4.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki4.sendText(msg.to,"He declined all invitations")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots5 out","bots5 out"]:
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki5.leaveGroup(i)
                if wait["lang"] == "JP":
                    ki5.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    ki5.sendText(msg.to,"He declined all invitations")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["rejectall","Rejectall","reject","Reject","CleansInvite"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    ki.rejectGroupInvitation(i)
                    ki2.rejectGroupInvitation(i)
                    ki3.rejectGroupInvitation(i)
                    ki4.rejectGroupInvitation(i)
                    ki5.rejectGroupInvitation(i)
                    #ki6.rejectGroupInvitation(i)
                    #ki7.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"I Reject all Groups Invitation")
                else:
                    cl.sendText(msg.to,"I declined all invitations")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We Changed the Message Confirmation")
            elif "Pesan add:" in msg.text:
                wait["message"] = msg.text.replace("Pesan add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"We Changed the Message Confirmation")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Message check","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan Auto add Telah Ditetapkan sbg Berikut \n\n" + wait["message"])
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Comset:" in msg.text:
                c = msg.text.replace("Comset:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"It Can't be Change")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Pesan auto komentar ✓\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Switch on")
                    else:
                        cl.sendText(msg.to,"Switch on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Switch on")
                    else:
                        cl.sendText(msg.to,"")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Set to off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Turn off")
                    else:
                        cl.sendText(msg.to,"Turn off")
            elif msg.text in ["Comen","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut: \n\n" + str(wait["comment"]))
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
  #---------------------------------------------------------------------------------------------------------------------------------------
            elif "/spam " in msg.text:
              if msg.from_ in admsa:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("/spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 60:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 100:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
            elif msg.text.lower() in ["mid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Bots invite:" in msg.text:
              if msg.from_ in admsa:
                gid = msg.text.replace("Bots1 invite:","")
                if gid == "":
                  ki.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki.findAndAddContactsByMid(msg.from_)
                    ki.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Send Contact 􀜁􀇔􏿿")
            elif msg.text in ["Bandel"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Send Contact 􀜁􀇔􏿿")
            elif msg.text in ["Becek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist 􀜁􀇔􏿿")
                else:
                    cl.sendText(msg.to,"The following is a blacklist 􀜁􀇔􏿿")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Send Contact 􀜁􀇔􏿿")
            elif msg.text in ["Bandel"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Send Contact 􀜁􀇔􏿿")
            elif msg.text in ["Becek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist 􀜁􀇔􏿿")
                else:
                    cl.sendText(msg.to,"The following is a blacklist 􀜁􀇔􏿿")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Clock on","clock on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Clocks on 􀜁􀇔􏿿")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Clock on 􀜁􀇔􏿿")
            elif msg.text in ["Clock off","clock off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Clock off 􀜁􀇔􏿿")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Already off 􀜁􀇔􏿿")
            elif "Clock say:" in msg.text:
                n = msg.text.replace("Clock say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Your Clock name Has Changed \n􀜁􀇔􏿿 °" + n)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Nk " in msg.text:
              if msg.from_ in admsa:
                ulti0 = msg.text.replace("Nk ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                random.choice(KAC).acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendText(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                            if target not in Bots:
                                try:
                                        random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                        random.choice(KAC).leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        random.choice(KAC).sendText(msg.to,"")
                                        random.choice(KAC).sendText(msg.to,"")
                                        random.choice(KAC).leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    print "hm"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"Good Bye (*´･ω･*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"What you mean?")
                    else:
                        for target in targets:
                          if target not in Bots:
                             try:
                                 klist=[ki,ki2,ki3,ki4,ki5]
                                 kicker=random.choice(klist)
                                 kicker.kickoutFromGroup(msg.to,[target])
                                 print (msg.to,[g.mid])
                             except:
                                 ki.sendText(msg.to,"Group cleanse (*´･ω･*)")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif ("Kamu " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
#---------------------------------------------------------------------------------------------------------------------------------------
	    elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Locked ! 􀇔􏿿")
                            except:
                                cl.sendText(msg.to,"Error")
#---------------------------------------------------------------------------------------------------------------------------------------
	    elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked ! 􀜁􀇔􏿿")
                            except:
                                cl.sendText(msg.to,"Error")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Ban:" in msg.text:
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked ! 􀇔􏿿")
                                except:
                                    cl.sendText(msg.to,"Locked !🔒")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Unban:" in msg.text:
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked 􀜁􀇔􏿿")
                                except:
                                    cl.sendText(msg.to,"Unlocked")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["/clearban"]:
              if msg.from_ in admsa:
                cl.sendText(msg.to,"Waiting for clearing Ban "+ str(len(wait["blacklist"]))+ " users ...")
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Clear ban users done ~")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "/kepo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Responsename","responsename"]:
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + ""
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + ""
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + ""
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + ""
                ki5.sendText(msg.to, text)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact 􀜁􀇔􏿿")
            elif msg.text in ["mcheck","Mcheck"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"Following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "􀜁􀇔􏿿Nakal" +cl.getContact(mi_d).displayName + "\n􀜁􀅔􏿿 "
                    cl.sendText(msg.to,mc)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Banlist","banlist"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "Nakal\n 􀜁􀅔􏿿" +cl.getContact(mm).displayName + "\n􀜁􀅔􏿿 "
                    cl.sendText(msg.to,cocoa + "Daftar Hitam 􀜁􀅔􏿿 ")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Purge","purge"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Banlist user Nothing")
                        return
                    for jj in matched_list:
                        try:
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Dudul come","dudul come","kuylah","Kuylah"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Hush","hush","Pulang","pulang","dah gitu aja"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Welcome","welcome"]:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Groups Name]\n" + str(ginfo.name) )
                cl.sendText(msg.to,"Welcome to 👥" + str(ginfo.name) + " 👥 Groups")
                cl.sendText(msg.to,"Group Creator " + str(ginfo.name) + " :\n👤 " + ginfo.creator.displayName )
                cl.sendMessage(msg)
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
            elif msg.text in ["Ping","ping"]:
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿 Bales PM boss Gue oi ! ")
            elif msg.text in ["Sp","Speed","sp"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
            elif msg.text in ["Botspeed","Botsp","Bspeed"]:
                start = time.time()
                ki.sendText(msg.to, "Wait Boss..")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%s second" % (elapsed_time))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "BroadcastGroups " in msg.text:
                 bctxt = msg.text.replace("BroadcastGroups ", "")
                 n = cl.getGroupIdsJoined()
                 for manusia in n:
                      cl.sendText(manusia, (bctxt))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif "BroadcastFriends " in msg.text:
                 bctxt = msg.text.replace("BroadcastFriends ", "")
                 t = cl.getAllContactIds()
                 for manusia in t:
                      cl.sendText(manusia, (bctxt))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["My Groups"]: #Melihat List Group
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👥 "+str(len(cl.getGroup(i).members)))
                cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
#---------------------------------------------------------------------------------------------------------------------------------------
            elif msg.text in ["Bots Groups"]:
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                     h += "[•]%s Member\n" % (ki.getGroup(i).name   +"👥 "+str(len(ki.getGroup(i).members)))
                ki.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
            elif msg.text in ["Bots2 Groups"]:
                gid = ki2.getGroupIdsJoined()
                h = ""
                for i in gid:
                     h += "[•]%s Member\n" % (ki2.getGroup(i).name   +"👥 "+str(len(ki2.getGroup(i).members)))
                ki2.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
            elif msg.text in ["Bots3 Groups"]:
                gid = ki3.getGroupIdsJoined()
                h = ""    
                for i in gid:
                     h += "[•]%s Member\n" % (ki3.getGroup(i).name   +"👥 "+str(len(ki3.getGroup(i).members)))
                ki.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
            elif msg.text in ["Bots4 Groups"]:
                gid = ki4.getGroupIdsJoined()
                h = ""
                for i in gid:
                     h += "[•]%s Member\n" % (ki4.getGroup(i).name   +"👥 "+str(len(ki4.getGroup(i).members)))
                ki4.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
            elif msg.text in ["Bots5 Groups"]:
                gid = ki5.getGroupIdsJoined()
                h = ""
                for i in gid:
                     h += "[•]%s Member\n" % (ki5.getGroup(i).name   +"👥 "+str(len(ki5.getGroup(i).members)))
                ki5.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gid)))
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)




                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True



                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        wait["blacklist"][op.param2] = True
            except:
                pass
#---------------------------------------------------------------------------------------------------------------------------------------
	elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
             text = msg.text
             if text is not None:
              ki.sendText(msg.to,text)
              ki2.sendText(msg.to,text)
              ki3.sendText(msg.to,text)
              ki4.sendText(msg.to,text)
              ki5.sendText(msg.to,text)
             else:
              if msg.contentType == 7:
               msg.contentType = 7
               msg.text = None
               msg.contentMetadata = {
                      "STKID": "110",
                      "STKPKGID": "1",
                      "STKVER": "100" }
               ki.sendMessage(msg)
               ki2.sendMessage(msg)
               ki3.sendMessage(msg)
               ki4.sendMessage(msg)
               ki5.sendMessage(msg)
              elif msg.contentType == 13:
               msg.contentType = 13
               msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
               ki.sendMessage(msg)
               ki2.sendMessage(msg)
               ki3.sendMessage(msg)
               ki4.sendMessage(msg)
               ki5.sendMessage(msg)

	elif "Bots " in msg.text:
             if msg.from_ in admsa:
              cmd = msg.text.replace("Bots ","")
              if cmd == "tt mau?":
               if mimic["status"] == False:
                mimic["status"] = True
                ki.sendText(msg.to,"Mauuuuuuu bosss 􀜁􀇔􏿿")
               else:
                ki.sendText(msg.to,"ini lagi nenen boss 􀜁􀇔􏿿")
              elif cmd == "udah":
               if mimic["status"] == True:
                mimic["status"] = False
                ki.sendText(msg.to,"Belum puass bossss")
               else:
                ki.sendText(msg.to,"pengen nenen lagi 😚😚")
              elif "nenen" in cmd:
               target0 = msg.text.replace("Bots nenen","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  mimic["target"][target] = True
                  ki.sendText(msg.to,"Nenen 🤤🤤")
                  break
                 except:
                  break
              elif "del" in cmd:
               target0 = msg.text.replace("Bots del","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = ki.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                ki.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  del mimic["target"][target]
                  ki.sendText(msg.to,"Udah kurus dia boss, ga ada nenen lagi 􀜁􀇔􏿿􀜁􀇔􏿿􀜁􀇔􏿿")
                  break
                 except:
                  pass
#---------------------------------------------------------------------------------------------------------------------------------------
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki.updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admsa + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 32:
	    if op.param2 not in Bots:
	        pass
	    elif wait["cancelprotect"] == True:
	        wait ["blacklist"][op.param2] = True
	        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
	    else:
	        cl.sendText(op.param1,"")
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#---------------------------------------------------------------------------------------------------------------------------------------

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)