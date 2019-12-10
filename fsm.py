from transitions.extensions import GraphMachine
from utils import send_text_message,send_image_url,movie,photo,send_image
class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        
    def is_going_to_hello(self, event):
        text = event.message.text
        return text== "你好"

    def on_enter_hello(self, event):
        reply_token = event.reply_token       
        send_text_message(reply_token, "你好，我是東京女子診斷機器人，想知道你屬於哪個都市的女子類型嗎？？那就趕快輸入「東京女子診斷」，即可開始遊戲，輸入「我要看電影」，即可顯示最新電影資訊")        
        self.go_back()

    def is_going_to_husband(self, event):
        text = event.message.text
        return text== "我要看老公"
    def on_enter_husband(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入老公的IG帳號")
        self.go_back()    
    def is_going_to_photo(self, event):
        global t
        t = event.message.text
        return True
    
    def on_enter_photo(self, event):
        reply_token = event.reply_token
        a=photo(t)
        send_image(reply_token,a)
        self.go_back()   
        
    def is_going_to_movie(self, event):
        text = event.message.text
        return text== "我要看電影"
    def on_enter_movie(self, event):
        reply_token = event.reply_token
        a=movie()
        send_text_message(reply_token, a)
        self.go_back()      
        
    def is_going_to_q1(self, event):
        text = event.message.text
        return text== "東京女子診斷"
    def on_enter_q1(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "認為自己個性像男生還是女生\n1.女生 2.男生")
        self.go_back()      
        
    def is_going_to_q2(self, event):
        text = event.message.text
        return text.lower()== "女生"
    def on_enter_q2(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "男生最終會喜歡的類型\n1.外表好看 2.可愛撒嬌")
        self.go_back()       
        
    def is_going_to_q3(self, event):
        text = event.message.text
        return text.lower()== "男生"
    def on_enter_q3(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "能夠好惡分明\n1.可以 2.不行")
        self.go_back()
        
    def is_going_to_q4(self, event):
        text = event.message.text
        return text.lower()== "外表好看"
    def on_enter_q4(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "對整形的想法\n1.想嘗試 2.覺得可怕")
        self.go_back()
        
    def is_going_to_q5(self, event):
        text = event.message.text
        return text.lower()== "可愛撒嬌"
    def on_enter_q5(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "和潮男約會時你的打扮是\n1.少女風 2.簡約風")
        self.go_back()
        
    def is_going_to_q6(self, event):
        text = event.message.text
        return text.lower()== "可以"
    def on_enter_q6(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "每月花費最多的地方\n1.交際費 2.美容費")
        self.go_back()
        
    def is_going_to_q7(self, event):
        text = event.message.text
        return text.lower()== "不行"
    def on_enter_q7(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "和人交往相處\n1.很喜歡 2.覺得麻煩")
        self.go_back()
        
    def is_going_to_q8(self, event):
        text = event.message.text
        return text.lower()== "想嘗試"
    def on_enter_q8(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "認為哪一種臉蛋可愛\n1.混血風 2.韓國風")
        self.go_back()
        
    def is_going_to_q9(self, event):
        text = event.message.text
        return text.lower()== "覺得可怕"
    def on_enter_q9(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "面對都會的人群時\n1.不太在意 2.覺得困擾")
        self.go_back()
        
    def is_going_to_q10(self, event):
        text = event.message.text
        return text.lower()== "少女風" or text.lower()== "覺得麻煩"
    def on_enter_q10(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "如果能工作\n1.做喜歡的事 2.不想工作")
        self.go_back()
        
    def is_going_to_q11(self, event):
        text = event.message.text
        return (text.lower()== "簡約風" or text.lower()== "美容費" or text.lower()== "很喜歡")
    def on_enter_q11(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "現在有令你沈迷的事嗎\n1.有 2.沒有")
        self.go_back()
        
    def is_going_to_q12(self, event):
        text = event.message.text
        return text.lower()== "交際費"
    def on_enter_q12(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "重視衣服或化妝品等東西的品牌嗎\n1.還是會比較品牌 2.只要可愛都可以")
        self.go_back()
        
    def is_going_to_q13(self, event):
        text = event.message.text
        return text.lower()== "混血風"
    def on_enter_q13(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "會使用比較粗魯、粗俗的語言\n1.會 2.不會")
        self.go_back()
        
    def is_going_to_q14(self, event):
        text = event.message.text
        return text.lower()== "韓國風"
    def on_enter_q14(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "至少懂得6句以上的韓文\n1.懂 2.不懂")
        self.go_back()
        
    def is_going_to_q15(self, event):
        text = event.message.text
        return text.lower()== "不太在意"
    def on_enter_q15(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "為了減肥會做\n1.騎腳踏車 2.做熱瑜珈")
        self.go_back()
        
    def is_going_to_q16(self, event):
        text = event.message.text
        return text.lower()== "覺得困擾"
    def on_enter_q16(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "假日如果只有一個人過的話會\n1.在家看電影 2.去公園發呆")
        self.go_back()
        
    def is_going_to_q17(self, event):
        text = event.message.text
        return text.lower()== "做喜歡的事"
    def on_enter_q17(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "喜歡在哪舉辦聚會\n1.熱鬧的場所 2.可以兩三人悠閒度過的地方")
        self.go_back()
        
    def is_going_to_q18(self, event):
        text = event.message.text
        return text.lower()== "不想工作"
    def on_enter_q18(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "被怎樣的人邀請吃飯會動心\n1.帥氣 2.有錢")
        self.go_back()
        
    def is_going_to_q19(self, event):
        text = event.message.text
        return text.lower()== "有"
    def on_enter_q19(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "可以馬上說出自己好的地方還是壞的地方\n1.好的地方 2.壞的地方")
        self.go_back()
        
    def is_going_to_q20(self, event):
        text = event.message.text
        return text.lower()== "沒有"
    def on_enter_q20(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "喜歡怎樣消磨時間\n1.一個人度過 2.和朋友一起")
        self.go_back()
        
    def is_going_to_q21(self, event):
        text = event.message.text
        return text.lower()== "還是會比較品牌"
    def on_enter_q21(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "關於未來的具體規劃\n1.有計畫 2.還不清楚")
        self.go_back()
        
    def is_going_to_q22(self, event):
        text = event.message.text
        return text.lower()== "只要可愛都可以"
    def on_enter_q22(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "面對失落的人時會\n1.傾聽 2.給予鼓勵")
        self.go_back()
        
    #中目黑
    def is_going_to_a1(self, event):
        text = event.message.text
        return text.lower()== "在家看電影" or text.lower()=="可以兩三人悠閒度過的地方"
    def on_enter_a1(self, event):
        reply_token = event.reply_token
        text="你是中目黑女子\n・一個人獨處的時間很重要\n・比起到處遊玩，更喜歡靜靜地待在一個地方\n・喜歡咖啡店，一有機會就會去咖啡店\n・對聚集一堆人的活動不感興趣\n・喜歡隨性、不過度打扮的時尚風格\n・比較常自己煮菜做飯\n・喜歡自己這種生活方式"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0108.jpg",text)
        self.go_back()
        
    #吉祥寺
    def is_going_to_a2(self, event):
        text = event.message.text
        return text.lower()== "去公園發呆"
    def on_enter_a2(self, event):
        reply_token = event.reply_token
        text="你是吉祥寺女子\n・喜歡自然有機的東西\n・有明確的興趣\n・不穿貼身的穿搭，有自己的步調、以自身為優先\n・不想被認為很注重外表\n・喜歡公園\n・從小地方就能感受到季節變換\n・想悠閒地度過時間"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0109.jpg",text)
        self.go_back()
        
    #下北澤
    def is_going_to_a3(self, event):
        text = event.message.text
        return text.lower()== "好的地方"
    def on_enter_a3(self, event):
        reply_token = event.reply_token
        text="你是下北澤女子\n・喜歡次文化\n・清楚自己的定位\n・我就是自己的偶像\n・喜歡音樂、LIVE、電影\n・基本上不穿高跟鞋\n・喜歡復古、懷舊\n・喜歡底片相機\n・自我主張強烈卻又多愁善感"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0112.jpg",text)
        self.go_back()
    
    #表參道
    def is_going_to_a4(self, event):
        text = event.message.text
        return text.lower()== "做熱瑜珈"
    def on_enter_a4(self, event):
        reply_token = event.reply_token
        text="你是表參道女子\n・不想被說愛跟風的人，但其實很想跟上流行\n・想成為成熟女子\n・執著於Instagram照片排版\n・想成為氣場強大、自然受到禮讓的女子\n・會嘗試正在流行的美容方法\n・喜歡專櫃彩妝\n・喜歡在聚會中看起來神彩奕奕的自己"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0107.jpg",text)
        self.go_back()
        
    #高圓寺
    def is_going_to_a5(self, event):
        text = event.message.text
        return text.lower()== "壞的地方"
    def on_enter_a5(self, event):
        reply_token = event.reply_token
        text="你是高圓寺女子\n・喜歡去LIVE HOUSE\n・喜歡感人系的文字、話語\n・頗善於自嘲\n・喜歡離市中心遠一點的小酒館\n・喜歡古著也喜歡T-shirt\n・能與男女老少親近\n・喜歡破爛的街道和有點厭世的自己"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0113.jpg",text)
        self.go_back()
        
    #惠比壽
    def is_going_to_a6(self, event):
        text = event.message.text
        return text.lower()== "帥氣"
    def on_enter_a6(self, event):
        reply_token = event.reply_token
        text="你是惠比壽女子\n・跟女生就約便宜居酒屋、跟男生則約高級酒吧\n・百分之百都會型女子\n・女子味滿點\n・想受眾人歡迎，也想被眾人稱讚\n・幾乎不自己煮菜做飯\n・喜歡帥哥但也喜歡有地位的人\n・有不知名的生活費贊助者\n・幾乎沒有存款"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0111.jpg",text)
        self.go_back()
        
    #六本木
    def is_going_to_a7(self, event):
        text = event.message.text
        return text.lower()== "騎腳踏車" or text.lower()=="還不清楚"
    def on_enter_a7(self, event):
        reply_token = event.reply_token
        text="你是六本木女子\n・都會肉食系女子\n・超級愛參加派對活動\n・妝很濃\n・喜歡盛大的場面和活動\n・很重視一期一會\n・不想阿諛奉承\n・不在意被太陽曬黑\n・每到夏天Instagram更新速度會更快"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0106.jpg",text)
        self.go_back()
        
    #銀座
    def is_going_to_a8(self, event):
        text = event.message.text
        return text.lower()== "有計畫"
    def on_enter_a8(self, event):
        reply_token = event.reply_token
        text="你是銀座女子\n・會在意自己的一舉一動與說話方式\n・朋友常常諮詢自己的意見\n・個性很好、懂人情世故，但不太深入干涉別人私事\n・會仔細做人生規劃\n・氛圍很沈穩\n・不知道為什麼無法和喜歡的人交往順利\n・不擅長唸書，但很聰明"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0115.jpg",text)
        self.go_back()
        
    #三軒茶屋
    def is_going_to_a9(self, event):
        text = event.message.text
        return text.lower()== "熱鬧的場所" or text.lower()=="和朋友一起"
    def on_enter_a9(self, event):
        reply_token = event.reply_token
        text="你是三軒茶屋女子\n・覺得所有人類都是朋友、酒是與人交流的工具\n・隨時都在揪人\n・朋友超多，人脈很廣\n・朋友圈裡的男生女生都很多\n・喜歡跟鄰居寒暄。只要住得近，都可以變好朋友\n・基本上怕寂寞"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0110.jpg",text)
        self.go_back()

    #西麻布
    def is_going_to_a10(self, event):
        text = event.message.text
        return text.lower()== "不會" or text.lower()=="有錢"
    def on_enter_a10(self, event):
        reply_token = event.reply_token
        text="你是西麻布女子\n・受男生歡迎的衣服是戰鬥服裝\n・錢不是「賺」來的，是「拿」來的\n・不想做辛苦的事，看起來善於處世之道，其實偶爾會失敗\n・朋友基本上臉都很可愛\n・去旅行都要靠別人幫忙\n・總之就是要稱讚對方\n・正牌男友常常是廢人"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0104.jpg",text)
        self.go_back()        
    
    #赤羽
    def is_going_to_a11(self, event):
        text = event.message.text
        return text.lower()== "傾聽"
    def on_enter_a11(self, event):
        reply_token = event.reply_token
        text="你是赤羽女子\n・是歐吉桑女子，也是大姐頭女子\n・酒可以解決所有事\n・外表是女子，但內心是大叔\n・大叔朋友很多\n・比起漂亮的店，有點髒的店待起來更舒服\n・重視價格，喜歡便宜的東西\n・喝酒的時候跟工作的時候，完全是不同人\n・希望別人覺得自己是女子，覺得掙扎"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0116.jpg",text)
        self.go_back()
        
    #新大久保
    def is_going_to_a12(self, event):
        text = event.message.text
        return text.lower()== "懂"
    def on_enter_a12(self, event):
        reply_token = event.reply_token
        text="你是大久保女子\n・喜歡韓國，總之喜歡韓國\n・化妝風格、彩妝品都是韓貨\n・可以的話想要整形\n・比起日本的演藝圈，更熟韓國偶像\n・會用韓文的hashtag、去韓國旅遊的頻率高得嚇人\n・可是還是喜歡日本"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0105.jpg",text)
        self.go_back()
        
    #八王子
    def is_going_to_a13(self, event):
        text = event.message.text
        return text.lower()== "給予鼓勵"
    def on_enter_a13(self, event):
        reply_token = event.reply_token
        text="你是八王子女子\n・不擅長去人多的地方\n・內心很佛\n・想要打扮得很潮，但穿戴潮物又覺得害羞\n・人類能量滿強的\n・有個性的人滿多的\n・喜歡家人\n・可以的話想永遠青春"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0117.jpg",text)
        self.go_back()
        
    #初台
    def is_going_to_a14(self, event):
        text = event.message.text
        return text.lower()== "一個人度過"
    def on_enter_a14(self, event):
        reply_token = event.reply_token
        text="你是初台女子\n・喜歡看電影、舞台劇\n・中階管理職女子\n・在不同組織中兼職\n・配合別人不會覺得痛苦\n・走路意外地很輕快\n・工作、私人生活分得很清楚\n・喜歡讓自己能放鬆的地方\n・不擅長跟很多人接觸"
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0114.jpg",text)
        self.go_back()
        
    #歌舞伎町
    def is_going_to_a15(self, event):
        text = event.message.text
        return text.lower()== "會" or text.lower()=="不懂"
    def on_enter_a15(self, event):
        reply_token = event.reply_token
        text="你是歌舞伎町女子\n・活動時間在晚上\n・喜歡自己賺錢，花在喜歡的事情\n・很愛漂亮，誠實面對自己的慾望\n・不是在整形，就是在整形的路上\n・跟男公關混在一起\n・活在當下\n・人很強勢，但是戀愛時異常弱勢\n・因為怕寂寞，常常把事情搞砸 "
        send_image_url(reply_token, "https://cdn.mamaclub.com/wp-content/uploads/2019/09/20190919_G0103.jpg",text)
        self.go_back()
        

   
