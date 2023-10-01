from loguru import logger
from mitmproxy.io import FlowReader

PREFIX_FOLDER = "ErjSDev-framework/mitmproxy"

filename = f'{PREFIX_FOLDER}/renaldook'

DMAP = {}

REMARK = {"FROMNSDFFDSSFD": "SDFFFFFFFFFFFFFFFFFFFFFFFFFFFF"}

with open(filename, 'rb') as fp:
    reader = FlowReader(fp)

    for flow in reader.stream():
        # ic(flow.request.url)
        if flow.response and flow.response.headers:
            flow.response.headers.update(REMARK)
            DMAP[flow.request.url] = [flow.response.status_code, flow.response.headers, flow.response.content]

with open(f"{PREFIX_FOLDER}/abba.19.js", 'rb') as fp:
    DMAP["https://www.gstatic.com/_/mss/boq-translate/_/js/k=boq-translate.TranslateWebserverUi.en_US.Zja1E8X2iVI.es5.O/ck=boq-translate.TranslateWebserverUi.rg3AtMzd_04.L.B1.O/am=jxgApmaDBQEB/d=1/exm=_b,_r,_tp/excm=_b,_r,_tp,mainview/ed=1/wt=2/ujg=1/rs=ANkVxDmyVsnRq7AwGS4u1c0e7xmgi-GehA/ee=EVNhjf:pw70Gc;EmZ2Bf:zr1jrb;Erl4fe:FloWmf;JsbNhc:Xd8iUd;LBgRLc:SdcwHb;Me32dd:MEeYgc;NPKaK:SdcwHb;NSEoX:lazG7b;Oj465e:KG2eXe;Pjplud:EEDORb;QGR0gd:Mlhmy;SNUn3:ZwDk9d;a56pNe:JEfCwb;cEt90b:ws9Tlc;dIoSBb:SpsfSb;eBAeSb:zbML3c;g8nkx:U4MzKc;iFQyKf:QIhFr;io8t5d:yDVVkb;kMFpHd:OTA3Ae;kbAm9d:MkHyGd;nAFL3:s39S4;oGtAuc:sOXFj;pXdRYb:XBRlNc;qddgKe:xQtZb;sP4Vbe:VwDzFe;uY49fb:COQbmf;ul9GGd:VDovNc;wQlYve:aLUfP;wR5FRb:O1Gjze;xqZiqf:BBI74;yEQyxe:p8L0ob;yxTchf:KUM7Z;zxnPse:duFQFc/m=n73qwf,UUJqVe,ws9Tlc,IZT63,TzmfU,CHCSlb,O1Gjze,byfTOb,lsjVmc,xUdipf,OTA3Ae,COQbmf,fKUV3e,aurFic,U0aPgd,ZwDk9d,V3dDOb,WO9ee,mI3LFb,K4PcAe,j4UNFc,m9oV,p8L0ob,i5dxUd,UECOXe,pKzUve,rCcCxc,GSlykd,yCWm5b,tjiVBd,gWGePc,O6y8ed,mzzZzc,MpJwZc,PrPYRd,LEikZe,NwH0H,OmgaI,lazG7b,RAnnUd,fmklff,s39S4,msAMEf,XVMNvd,KUM7Z,Mlhmy,L1AAkb,hB8iWe,Izs65d,duFQFc,lwddkf,E2VjNc,gychg,w9hDv,EEDORb,RMhBfe,uu7UOe,Ru0Pgb,pw70Gc,SdcwHb,aW3pY,QqJ8Gd,UWMmZb,EFQ78c,Ulmmrd,ZfAoz,mdR7q,soHxf,ehH0Pd,gJzDyc,MnwvSb,xQtZb,I6YDgd,n391td,N2mfec,glibvb,bD99Db,MMbfFd,XBRlNc,JNoxi,kWgXee,MI6k7c,kjKdXe,MJWMce,QIhFr,BVgquf,g8fAWe,YrN4Fb,yi1Dad,ovKuLd,hKSk3e,bYHiff,yDVVkb,hc6Ubd,SpsfSb,PJgxJf,G0j0Je,MDB2J,KG2eXe,jl0Zdc,s2VbJb,zbML3c,VwDzFe,lWpni,KOuY1b,rPRh8e,GiFjve,AV6dJd,AJZZxc,V8JnLd,zr1jrb,JE2clc,UthHZe,Id96Vc,NotTJb,pvoWvc,JPvYpc,gNRIbd,SNtCZb,A7fCU,VETAO,FZTbYc,Uas9Hd,TJQ3Ud,mmcjze,Qnj3Pe,AKLKy,mNvcvf,pjICDe"][2] = fp.read()

with open(f"{PREFIX_FOLDER}/abba.54.js", 'rb') as fp:
    DMAP["https://www.gstatic.com/_/mss/boq-translate/_/js/k=boq-translate.TranslateWebserverUi.en_US.Zja1E8X2iVI.es5.O/am=jxgApmaDBQEB/d=1/excm=_b,_r,_tp,mainview/ed=1/dg=0/wt=2/ujg=1/rs=ANkVxDnL4-iheBWSBZ_aEha-cY7Yvk_LKA/m=_b,_tp,_r"][2] = fp.read()


class Cather:
    def request(self, flow):
        ...
        # print(flow.request)

    def response(self, flow):
        print(flow.response)
        if flow.request.url in DMAP:
            logger.debug(f"URL FOUND: {flow.request.url}")
            flow.response.status_code, flow.response.headers, flow.response.content = DMAP[flow.request.url][0], DMAP[flow.request.url][1], DMAP[flow.request.url][2]
        else:
            pass
            # ic(f"URL NOT FOUND: {flow.request.url}")
