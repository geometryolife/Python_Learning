class Card(object):
    def __init__(self, cardid, cardpasswd, cardmoney):
        self.cardid = cardid  # 银行卡号
        self.cardpasswd = cardpasswd  # 银行卡密码
        self.cardmoney = cardmoney  # 卡内余额
        self.cardlock = False  # 是否被锁定
