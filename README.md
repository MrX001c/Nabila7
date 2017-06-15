# bayu
gr = client._client.getGroup(GROUPID)   member = gr.members   for g in member:     client._client.kickoutFromGroup(0, GROUPID, [g.mid]) except:   print "Max kick is 50 per a day"
