# -*- coding: utf-8 -*-
# Menu vocabulary: word -> (reading, sens FR)
W = {}
def add(s):
    for line in s.strip().splitlines():
        line=line.strip()
        if not line or line.startswith('#'): continue
        w,r,f=[x.strip() for x in line.split('|')]
        W[w]=(r,f)

add("""
# --- base / en-têtes
お品書き|おしながき|la carte
品書き|しながき|la carte
本日のおすすめ|ほんじつのおすすめ|suggestions du jour
本日|ほんじつ|aujourd’hui
一品料理|いっぴんりょうり|petits plats à la carte
焼物|やきもの|grillades
揚物|あげもの|fritures
刺身|さしみ|poisson cru en tranches
飲物|のみもの|boissons
〆|しめ|pour finir le repas
串焼|くしやき|brochettes grillées
麺類|めんるい|nouilles
ご飯物|ごはんもの|plats de riz
定食|ていしょく|formule repas complète
単品|たんぴん|à la carte (sans accompagnement)
握り|にぎり|sushi nigiri
巻物|まきもの|makis (rouleaux)
丼物|どんぶりもの|bols de riz garnis
甘味|かんみ|douceurs japonaises
軽食|けいしょく|en-cas
鉄板焼|てっぱんやき|cuisine à la plaque
名物|めいぶつ|spécialité locale
当店自慢|とうてんじまん|fierté de la maison
温かいお蕎麦|あたたかいおそば|soba chaudes
冷たいお蕎麦|つめたいおそば|soba froides
時価|じか|prix du marché
税込|ぜいこみ|taxes comprises
各種|かくしゅ|plusieurs variétés
大盛|おおもり|grande portion
特盛|とくもり|très grande portion
並|なみ|portion normale
特上|とくじょう|qualité supérieure
上|じょう|qualité supérieure (gamme)
ご飯大盛無料|ごはんおおもりむりょう|grande portion de riz gratuite
飲み放題|のみほうだい|boissons à volonté
塩|しお|au sel
タレ|タレ|à la sauce sucrée-salée
# --- izakaya
枝豆|えだまめ|edamame, soja vert
冷奴|ひややっこ|tofu froid
出汁巻玉子|だしまきたまご|omelette roulée au dashi
ポテトサラダ|ポテトサラダ|salade de pommes de terre
揚げ出し豆腐|あげだしどうふ|tofu frit en bouillon
漬物盛合せ|つけものもりあわせ|assortiment de pickles
塩辛|しおから|calmar fermenté salé
冷やしトマト|ひやしトマト|tomate froide
焼鳥|やきとり|brochettes de poulet grillé
ほっけ焼|ほっけやき|poisson hokke grillé
焼魚|やきざかな|poisson grillé
鯖塩焼|さばしおやき|maquereau grillé au sel
椎茸焼|しいたけやき|shiitake grillés
牛タン焼|ぎゅうタンやき|langue de bœuf grillée
唐揚げ|からあげ|poulet frit à la japonaise
軟骨唐揚げ|なんこつからあげ|cartilage de poulet frit
天ぷら盛合せ|てんぷらもりあわせ|assortiment de tempura
串カツ|くしカツ|brochettes panées frites
海老フライ|えびフライ|crevettes panées
刺身盛合せ|さしみもりあわせ|assortiment de sashimi
鮪刺|まぐろさし|sashimi de thon
烏賊刺|いかさし|sashimi de calmar
蛸刺|たこさし|sashimi de poulpe
鰹のたたき|かつおのたたき|bonite snackée
お茶漬け|おちゃづけ|riz arrosé de thé
焼おにぎり|やきおにぎり|boulette de riz grillée
雑炊|ぞうすい|soupe de riz
生ビール|なまビール|bière pression
生中|なまちゅう|bière pression moyenne
瓶ビール|びんビール|bière en bouteille
日本酒|にほんしゅ|saké
熱燗|あつかん|saké chaud
冷酒|れいしゅ|saké froid
焼酎|しょうちゅう|shōchū (alcool distillé)
梅酒|うめしゅ|liqueur de prune
酎ハイ|ちゅうハイ|shōchū au soda
レモンサワー|レモンサワー|sour au citron
ハイボール|ハイボール|whisky soda
烏龍茶|ウーロンちゃ|thé oolong
お湯割り|おゆわり|allongé à l’eau chaude
水割り|みずわり|allongé à l’eau
# --- yakitori
正肉|しょうにく|cuisse de poulet
ねぎま|ねぎま|poulet et poireau
つくね|つくね|boulette de poulet
皮|かわ|peau de poulet
砂肝|すなぎも|gésier
レバー|レバー|foie
手羽先|てばさき|aile de poulet
ハツ|ハツ|cœur
ぼんじり|ぼんじり|croupion
軟骨|なんこつ|cartilage
銀杏|ぎんなん|noix de ginkgo
椎茸|しいたけ|shiitake
鶏刺|とりさし|sashimi de poulet
鶏雑炊|とりぞうすい|soupe de riz au poulet
親子丼|おやこどん|bol de riz poulet et œuf
# --- ramen
醤油ラーメン|しょうゆラーメン|ramen à la sauce soja
味噌ラーメン|みそラーメン|ramen au miso
塩ラーメン|しおラーメン|ramen au bouillon salé
豚骨ラーメン|とんこつラーメン|ramen au bouillon d’os de porc
担々麺|たんたんめん|nouilles épicées au sésame
つけ麺|つけめん|nouilles à tremper
叉焼麺|チャーシューめん|ramen au porc braisé
冷やし中華|ひやしちゅうか|nouilles froides garnies
中華そば|ちゅうかそば|ramen (style ancien)
味玉|あじたま|œuf mariné
叉焼|チャーシュー|porc braisé
海苔|のり|algue nori
葱|ねぎ|ciboule
替玉|かえだま|portion de nouilles en plus
炒飯|チャーハン|riz sauté
半炒飯|はんチャーハン|demi-portion de riz sauté
餃子|ぎょうざ|raviolis grillés (gyoza)
ライス|ライス|bol de riz
# --- soba / udon
蕎麦|そば|nouilles de sarrasin
饂飩|うどん|nouilles de blé épaisses
かけ蕎麦|かけそば|soba en bouillon
天ぷら蕎麦|てんぷらそば|soba et tempura
鴨南蛮|かもなんばん|soba au canard et poireau
月見蕎麦|つきみそば|soba à l’œuf cru (« contempler la lune »)
山菜蕎麦|さんさいそば|soba aux plantes de montagne
きつね饂飩|きつねうどん|udon au tofu frit sucré
たぬき蕎麦|たぬきそば|soba aux miettes de tempura
肉饂飩|にくうどん|udon au bœuf
カレー南蛮|カレーなんばん|soba au curry
盛り蕎麦|もりそば|soba froides
ざる蕎麦|ざるそば|soba froides à la nori
天ざる|てんざる|soba froides et tempura
おろし蕎麦|おろしそば|soba au radis râpé
天丼|てんどん|bol de riz et tempura
カツ丼|カツどん|bol de riz au porc pané
# --- teishoku
生姜焼定食|しょうがやきていしょく|formule porc sauté au gingembre
唐揚定食|からあげていしょく|formule poulet frit
焼魚定食|やきざかなていしょく|formule poisson grillé
鯖味噌定食|さばみそていしょく|formule maquereau au miso
豚カツ定食|とんかつていしょく|formule porc pané
野菜炒め定食|やさいいためていしょく|formule légumes sautés
刺身定食|さしみていしょく|formule sashimi
日替り定食|ひがわりていしょく|formule du jour
納豆|なっとう|soja fermenté
味噌汁|みそしる|soupe miso
豚汁|とんじる|soupe miso au porc
ご飯|ごはん|bol de riz
小鉢|こばち|petit accompagnement
生卵|なまたまご|œuf cru
玉子焼|たまごやき|omelette roulée
# --- sushi
鮪|まぐろ|thon
中とろ|ちゅうとろ|ventre de thon mi-gras
大とろ|おおとろ|ventre de thon gras
鮭|さけ|saumon
鯛|たい|daurade
鰤|ぶり|sériole
鯵|あじ|chinchard
烏賊|いか|calmar
蛸|たこ|poulpe
海老|えび|crevette
穴子|あなご|congre
雲丹|うに|oursin
鮑|あわび|ormeau
帆立|ほたて|coquille Saint-Jacques
玉子|たまご|omelette (sushi)
鉄火巻|てっかまき|maki au thon
河童巻|かっぱまき|maki au concombre
納豆巻|なっとうまき|maki au natto
干瓢巻|かんぴょうまき|maki à la courge séchée
赤出汁|あかだし|soupe miso rouge
茶碗蒸し|ちゃわんむし|flan salé à la vapeur
上握り|じょうにぎり|assortiment de nigiri supérieur
特上握り|とくじょうにぎり|assortiment de nigiri de luxe
# --- don
牛丼|ぎゅうどん|bol de riz au bœuf
海鮮丼|かいせんどん|bol de fruits de mer
鉄火丼|てっかどん|bol de thon cru
豚丼|ぶたどん|bol de porc grillé
他人丼|たにんどん|bol bœuf et œuf (« étrangers »)
玉子丼|たまごどん|bol à l’œuf
鰻丼|うなどん|bol d’anguille grillée
# --- kissaten
珈琲|コーヒー|café
紅茶|こうちゃ|thé noir
抹茶|まっちゃ|thé vert en poudre
牛乳|ぎゅうにゅう|lait
果汁|かじゅう|jus de fruits
ナポリタン|ナポリタン|spaghetti napolitaine
玉子サンド|たまごサンド|sandwich aux œufs
珈琲ゼリー|コーヒーゼリー|gelée de café
ホットケーキ|ホットケーキ|pancakes
クリームソーダ|クリームソーダ|soda à la glace
# --- kanmi
餡蜜|あんみつ|gelée, fruits et pâte de haricots
善哉|ぜんざい|soupe sucrée de haricots rouges
白玉|しらたま|boulettes de riz gluant
団子|だんご|brochette de boulettes de riz
草餅|くさもち|mochi à l’armoise
宇治金時|うじきんとき|glace pilée thé vert et haricots rouges
氷|こおり|glace pilée
葛切り|くずきり|nouilles de kuzu au sirop
# --- okonomiyaki
お好み焼|おこのみやき|crêpe japonaise garnie
豚玉|ぶたたま|okonomiyaki au porc
烏賊玉|いかたま|okonomiyaki au calmar
葱焼|ねぎやき|crêpe aux poireaux
焼蕎麦|やきそば|nouilles sautées
蛸焼|たこやき|boulettes de poulpe
モダン焼|モダンやき|okonomiyaki aux nouilles
# --- régions
成吉思汗|ジンギスカン|mouton grillé (Hokkaidō)
帆立焼|ほたてやき|Saint-Jacques grillées
蟹|かに|crabe
石狩鍋|いしかりなべ|ragoût de saumon au miso
いくら丼|いくらどん|bol d’œufs de saumon
麦飯|むぎめし|riz à l’orge
きりたんぽ鍋|きりたんぽなべ|ragoût aux bâtonnets de riz
芋煮|いもに|ragoût de taro
冷麺|れいめん|nouilles froides (Morioka)
わんこ蕎麦|わんこそば|soba servies en petits bols
深川飯|ふかがわめし|riz aux palourdes
もんじゃ焼|もんじゃやき|galette fondante (Tōkyō)
江戸前寿司|えどまえずし|sushi à la mode d’Edo
鰻重|うなじゅう|anguille sur riz en boîte laquée
天麩羅|てんぷら|tempura
味噌カツ|みそカツ|porc pané sauce miso
櫃まぶし|ひつまぶし|anguille sur riz, trois façons
きしめん|きしめん|nouilles plates (Nagoya)
味噌煮込み饂飩|みそにこみうどん|udon mijotées au miso
天むす|てんむす|onigiri à la tempura
湯豆腐|ゆどうふ|tofu chaud en bouillon
湯葉|ゆば|peau de lait de soja
鯖寿司|さばずし|sushi pressé au maquereau
鰊蕎麦|にしんそば|soba au hareng
京漬物|きょうつけもの|pickles de Kyōto
肉吸い|にくすい|bouillon au bœuf
土手焼|どてやき|tendons mijotés au miso
牡蠣フライ|かきフライ|huîtres panées
焼牡蠣|やきがき|huîtres grillées
穴子飯|あなごめし|riz au congre
汁なし担々麺|しるなしたんたんめん|tantanmen sans bouillon
讃岐饂飩|さぬきうどん|udon de Sanuki
釜玉|かまたま|udon à l’œuf
骨付鳥|ほねつきどり|cuisse de poulet rôtie
もつ鍋|もつなべ|ragoût de tripes
明太子|めんたいこ|œufs de colin épicés
水炊き|みずたき|pot-au-feu de poulet
胡麻鯖|ごまさば|maquereau cru au sésame
ゴーヤチャンプルー|ゴーヤチャンプルー|sauté de melon amer
沖縄蕎麦|おきなわそば|nouilles d’Okinawa
ソーキ蕎麦|ソーキそば|nouilles aux côtes de porc
角煮|かくに|porc braisé
海葡萄|うみぶどう|raisins de mer (algue)
泡盛|あわもり|alcool de riz d’Okinawa
""")

# Restaurant types: id -> dict
T = {
 'izakaya': dict(jp='居酒屋', fr='Izakaya', layouts=['tanzaku','wood','sheet'],
   names=['居酒屋 {n}','酒処 {n}','炉端 {n}'],
   sections=[('一品料理',['枝豆','冷奴','出汁巻玉子','ポテトサラダ','揚げ出し豆腐','漬物盛合せ','塩辛','冷やしトマト'],(280,580)),
             ('焼物',['焼鳥','ほっけ焼','鯖塩焼','椎茸焼','牛タン焼'],(380,980)),
             ('揚物',['唐揚げ','軟骨唐揚げ','天ぷら盛合せ','串カツ','海老フライ'],(380,880)),
             ('刺身',['刺身盛合せ','鮪刺','烏賊刺','蛸刺','鰹のたたき'],(480,1480)),
             ('〆',['お茶漬け','焼おにぎり','雑炊'],(350,580)),
             ('飲物',['生ビール','生中','瓶ビール','日本酒','熱燗','冷酒','焼酎','梅酒','酎ハイ','レモンサワー','ハイボール','烏龍茶'],(300,750))]),
 'yakitori': dict(jp='焼鳥屋', fr='Yakitori', layouts=['wood','tanzaku'],
   names=['焼鳥 {n}','炭火焼鳥 {n}','鳥{n}'],
   sections=[('串焼',['正肉','ねぎま','つくね','皮','砂肝','レバー','手羽先','ハツ','ぼんじり','軟骨','銀杏','椎茸','葱'],(150,330)),
             ('一品料理',['鶏刺','冷奴','枝豆','漬物盛合せ'],(300,680)),
             ('〆',['鶏雑炊','親子丼','焼おにぎり'],(450,850)),
             ('飲物',['生ビール','日本酒','焼酎','梅酒','ハイボール','烏龍茶'],(300,700))]),
 'ramen': dict(jp='ラーメン屋', fr='Ramen', layouts=['poster','wood'],
   names=['麺屋 {n}','らーめん {n}','中華そば {n}'],
   sections=[('麺類',['醤油ラーメン','味噌ラーメン','塩ラーメン','豚骨ラーメン','担々麺','つけ麺','叉焼麺','冷やし中華','中華そば'],(750,1300)),
             ('トッピング',['味玉','叉焼','海苔','葱','替玉','大盛'],(100,350)),
             ('ご飯物',['炒飯','半炒飯','餃子','ライス'],(150,750)),
             ('飲物',['生ビール','瓶ビール','烏龍茶'],(300,650))]),
 'soba': dict(jp='蕎麦屋', fr='Soba / udon', layouts=['wood','sheet'],
   names=['手打ち蕎麦 {n}','そば処 {n}','{n}庵'],
   sections=[('温かいお蕎麦',['かけ蕎麦','天ぷら蕎麦','鴨南蛮','月見蕎麦','山菜蕎麦','きつね饂飩','たぬき蕎麦','肉饂飩','カレー南蛮'],(500,1600)),
             ('冷たいお蕎麦',['盛り蕎麦','ざる蕎麦','天ざる','おろし蕎麦'],(550,1700)),
             ('丼物',['天丼','カツ丼','親子丼'],(800,1300)),
             ('飲物',['日本酒','瓶ビール','冷酒'],(500,900))]),
 'teishoku': dict(jp='定食屋', fr='Teishoku (cantine)', layouts=['poster','tanzaku'],
   names=['食堂 {n}','{n}食堂','定食 {n}'],
   sections=[('定食',['日替り定食','生姜焼定食','唐揚定食','焼魚定食','鯖味噌定食','豚カツ定食','野菜炒め定食','刺身定食'],(650,1200)),
             ('単品',['冷奴','納豆','味噌汁','豚汁','ご飯','小鉢','生卵','玉子焼'],(60,400)),
             ('飲物',['瓶ビール','烏龍茶'],(200,600))]),
 'sushi': dict(jp='寿司屋', fr='Sushi', layouts=['wood'],
   names=['{n}鮨','寿司処 {n}','すし {n}'],
   sections=[('握り',['鮪','中とろ','大とろ','鮭','鯛','鰤','鯵','烏賊','蛸','海老','穴子','雲丹','鮑','帆立','玉子'],(150,900)),
             ('巻物',['鉄火巻','河童巻','納豆巻','干瓢巻'],(300,800)),
             ('一品料理',['赤出汁','茶碗蒸し','上握り','特上握り'],(250,3800)),
             ('飲物',['日本酒','冷酒','生ビール','お茶漬け'],(400,900))]),
 'don': dict(jp='丼物屋', fr='Donburi', layouts=['poster','wood'],
   names=['丼 {n}','{n}丼','どんぶり {n}'],
   sections=[('丼物',['牛丼','親子丼','カツ丼','天丼','海鮮丼','鉄火丼','豚丼','他人丼','玉子丼','鰻丼'],(450,2200)),
             ('単品',['味噌汁','豚汁','生卵','漬物盛合せ','特盛','並'],(60,300))]),
 'kissaten': dict(jp='喫茶店', fr='Café rétro (kissaten)', layouts=['slate','card'],
   names=['喫茶 {n}','珈琲 {n}','純喫茶 {n}'],
   sections=[('飲物',['珈琲','紅茶','抹茶','牛乳','果汁','クリームソーダ'],(400,750)),
             ('軽食',['ナポリタン','玉子サンド','ホットケーキ','珈琲ゼリー'],(450,950))]),
 'kanmi': dict(jp='甘味処', fr='Salon de douceurs', layouts=['sheet','tanzaku'],
   names=['甘味処 {n}','茶房 {n}','{n}茶屋'],
   sections=[('甘味',['餡蜜','善哉','白玉','団子','草餅','宇治金時','氷','葛切り'],(350,950)),
             ('飲物',['抹茶','煎茶','珈琲'],(350,700))]),
 'okonomiyaki': dict(jp='お好み焼屋', fr='Okonomiyaki', layouts=['poster','slate'],
   names=['お好み焼 {n}','鉄板焼 {n}','{n}'],
   sections=[('鉄板焼',['お好み焼','豚玉','烏賊玉','モダン焼','葱焼','焼蕎麦','蛸焼'],(500,1200)),
             ('飲物',['生ビール','酎ハイ','レモンサワー','烏龍茶'],(300,600))]),
}
W['煎茶']=('せんちゃ','thé vert infusé')
W['トッピング']=('トッピング','suppléments')

R = {
 'hokkaido': dict(jp='北海道',fr='Hokkaidō',items=['成吉思汗','味噌ラーメン','海鮮丼','帆立焼','蟹','石狩鍋','いくら丼','ほっけ焼','豚丼']),
 'tohoku': dict(jp='東北',fr='Tōhoku (Sendai, Akita…)',items=['牛タン焼','麦飯','きりたんぽ鍋','芋煮','冷麺','わんこ蕎麦']),
 'tokyo': dict(jp='東京',fr='Tōkyō',items=['深川飯','もんじゃ焼','江戸前寿司','鰻重','天麩羅','ざる蕎麦']),
 'nagoya': dict(jp='名古屋',fr='Nagoya',items=['味噌カツ','手羽先','櫃まぶし','きしめん','味噌煮込み饂飩','天むす']),
 'kyoto': dict(jp='京都',fr='Kyōto',items=['湯豆腐','湯葉','鯖寿司','鰊蕎麦','抹茶','京漬物']),
 'osaka': dict(jp='大阪',fr='Ōsaka',items=['蛸焼','お好み焼','串カツ','きつね饂飩','肉吸い','土手焼']),
 'hiroshima': dict(jp='広島',fr='Hiroshima',items=['お好み焼','牡蠣フライ','焼牡蠣','穴子飯','汁なし担々麺']),
 'kagawa': dict(jp='香川',fr='Kagawa (Shikoku)',items=['讃岐饂飩','釜玉','骨付鳥','かけ蕎麦']),
 'fukuoka': dict(jp='福岡',fr='Fukuoka',items=['豚骨ラーメン','替玉','もつ鍋','明太子','水炊き','胡麻鯖']),
 'okinawa': dict(jp='沖縄',fr='Okinawa',items=['ゴーヤチャンプルー','沖縄蕎麦','ソーキ蕎麦','角煮','海葡萄','泡盛']),
}
NAMES = [('一休','いっきゅう'),('大黒','だいこく'),('福助','ふくすけ'),('宝','たから'),('千鳥','ちどり'),('花月','かげつ'),('日の出','ひので'),('富士','ふじ'),('満月','まんげつ'),('鶴亀','つるかめ'),('竹','たけ'),('桜','さくら'),('縁','えにし'),('楽','らく'),('一番','いちばん'),('大将','たいしょう'),('吉田','よしだ'),('山本','やまもと'),('長寿','ちょうじゅ'),('松葉','まつば')]
NAMEPAT_R = {'居酒屋':'いざかや','酒処':'さけどころ','炉端':'ろばた','焼鳥':'やきとり','炭火焼鳥':'すみびやきとり','鳥':'とり','麺屋':'めんや','らーめん':'らーめん','中華そば':'ちゅうかそば','手打ち蕎麦':'てうちそば','そば処':'そばどころ','庵':'あん','食堂':'しょくどう','定食':'ていしょく','鮨':'ずし','寿司処':'すしどころ','すし':'すし','丼':'どん','どんぶり':'どんぶり','喫茶':'きっさ','珈琲':'コーヒー','純喫茶':'じゅんきっさ','甘味処':'かんみどころ','茶房':'さぼう','茶屋':'ちゃや','お好み焼':'おこのみやき','鉄板焼':'てっぱんやき'}

# ---- v6: sake bar, abbreviations, old spellings, menu notices
NEW_W = [
 ('純米酒','じゅんまいしゅ','saké de riz pur','pure rice sake'),
 ('純米吟醸','じゅんまいぎんじょう','saké pur riz, poli (ginjō)','premium pure rice sake (ginjō)'),
 ('大吟醸','だいぎんじょう','saké très haut de gamme','super-premium sake'),
 ('本醸造','ほんじょうぞう','saké avec un peu d’alcool ajouté','sake with a little added alcohol'),
 ('生酒','なまざけ','saké non pasteurisé','unpasteurised sake'),
 ('原酒','げんしゅ','saké non dilué','undiluted sake'),
 ('濁り酒','にごりざけ','saké trouble, non filtré','cloudy unfiltered sake'),
 ('地酒','じざけ','saké local','local sake'),
 ('辛口','からくち','sec (saké)','dry (sake)'),
 ('甘口','あまくち','doux (saké)','sweet (sake)'),
 ('飲み方','のみかた','façons de boire','ways to drink it'),
 ('冷や','ひや','saké à température ambiante','sake at room temperature'),
 ('常温','じょうおん','à température ambiante','room temperature'),
 ('ぬる燗','ぬるかん','saké tiède','lukewarm sake'),
 ('一合','いちごう','un gō (180 ml)','one gō (180 ml)'),
 ('二合','にごう','deux gō (360 ml)','two gō (360 ml)'),
 ('徳利','とっくり','carafe à saké','sake flask'),
 ('お猪口','おちょこ','petite coupe à saké','small sake cup'),
 ('升','ます','boîte carrée en bois','square wooden cup'),
 ('肴','さかな','plats pour accompagner l’alcool','snacks to go with drinks'),
 ('お通し','おとおし','amuse-bouche imposé et payant','compulsory paid starter'),
 ('刺盛','さしもり','assortiment de sashimi (abrégé)','sashimi platter (short form)'),
 ('唐揚','からあげ','poulet frit (graphie courte)','fried chicken (short spelling)'),
 ('盛合','もりあわせ','assortiment (abrégé)','assortment (short form)'),
 ('板わさ','いたわさ','kamaboko au wasabi','fish cake with wasabi'),
 ('炙りえいひれ','あぶりえいひれ','nageoire de raie grillée','grilled stingray fin'),
 ('生','なま','bière pression (abrégé)','draught beer (short form)'),
 ('鮨','すし','sushi (graphie traditionnelle)','sushi (traditional spelling)'),
 ('鮓','すし','sushi (graphie ancienne, sushi fermenté)','sushi (old spelling, fermented sushi)'),
 ('燒鳥','やきとり','yakitori (forme ancienne de 焼)','yakitori (old form of 焼)'),
 ('売切','うりきれ','épuisé','sold out'),
 ('品切れ','しなぎれ','plus disponible','out of stock'),
 ('本日終了','ほんじつしゅうりょう','terminé pour aujourd’hui','finished for today'),
 ('限定','げんてい','en quantité limitée','limited'),
 ('一人前','いちにんまえ','une portion','one portion'),
 ('お代わり','おかわり','resservir','refill'),
]
for w,r,f,e in NEW_W: W[w]=(r,f)
T['sakaba']=dict(jp='酒場', fr='Bar à saké', layouts=['tanzaku','wood','slate'],
   names=['酒場 {n}','地酒処 {n}','{n}'],
   sections=[('日本酒',['純米酒','純米吟醸','大吟醸','本醸造','生酒','原酒','濁り酒','地酒'],(600,1600)),
             ('飲み方',['冷や','常温','ぬる燗','熱燗','冷酒','一合','二合'],(500,1200)),
             ('肴',['お通し','刺盛','唐揚','板わさ','炙りえいひれ','塩辛','冷奴'],(300,900))])
T['izakaya']['sections'][0][1].extend(['お通し','刺盛','唐揚'])
T['izakaya']['sections'][5][1].append('生')
T['sushi']['names'].append('鮓 {n}')
NAMEPAT_R.update({'酒場':'さかば','地酒処':'じざけどころ','鮓':'すし'})
MENTIONS=['税込','時価','各種','売切','品切れ','本日終了','限定','一人前','お代わり','大盛','特盛','並','〆','お通し','刺盛','唐揚','盛合','生','生中','鮨','鮓','燒鳥','飲み放題','ご飯大盛無料','単品']

# ---- tea: Japanese teas, tea sweets, and a tea house type
TEA_W = [
 ('お茶','おちゃ','thé','tea'),
 ('日本茶','にほんちゃ','thé japonais','Japanese tea'),
 ('緑茶','りょくちゃ','thé vert','green tea'),
 ('ほうじ茶','ほうじちゃ','thé vert torréfié','roasted green tea'),
 ('玄米茶','げんまいちゃ','thé vert au riz grillé','green tea with roasted rice'),
 ('番茶','ばんちゃ','thé vert de tous les jours','everyday green tea'),
 ('玉露','ぎょくろ','thé vert de luxe, cultivé à l’ombre','premium shade-grown green tea'),
 ('新茶','しんちゃ','thé de la première récolte','first-flush tea'),
 ('茎茶','くきちゃ','thé de tiges','stem tea'),
 ('麦茶','むぎちゃ','tisane d’orge grillée','roasted barley tea'),
 ('冷茶','れいちゃ','thé vert froid','cold green tea'),
 ('和紅茶','わこうちゃ','thé noir japonais','Japanese black tea'),
 ('薄茶','うすちゃ','matcha léger','thin matcha'),
 ('濃茶','こいちゃ','matcha épais','thick matcha'),
 ('抹茶ラテ','まっちゃラテ','latte au matcha','matcha latte'),
 ('ほうじ茶ラテ','ほうじちゃラテ','latte au thé torréfié','roasted tea latte'),
 ('和菓子','わがし','pâtisseries japonaises','Japanese sweets'),
 ('茶菓子','ちゃがし','douceur servie avec le thé','sweet served with tea'),
 ('大福','だいふく','mochi fourré aux haricots rouges','mochi filled with red bean'),
 ('最中','もなか','gaufrette fourrée aux haricots rouges','wafer filled with red bean'),
 ('羊羹','ようかん','pâte de haricots rouges gélifiée','red bean jelly'),
 ('わらび餅','わらびもち','gelée de fougère au kinako','bracken jelly with kinako'),
 ('抹茶パフェ','まっちゃパフェ','parfait au matcha','matcha parfait'),
 ('抹茶アイス','まっちゃアイス','glace au matcha','matcha ice cream'),
 ('茶そば','ちゃそば','soba au thé vert','green tea soba'),
]
for w,r,f,e in TEA_W: W[w]=(r,f)
NEW_W.extend(TEA_W)
T['chaya']=dict(jp='日本茶カフェ', fr='Salon de thé', layouts=['sheet','tanzaku','card'],
   names=['茶寮 {n}','日本茶 {n}','{n}園'],
   sections=[('日本茶',['煎茶','玉露','ほうじ茶','玄米茶','番茶','茎茶','新茶','和紅茶','冷茶','麦茶'],(450,1200)),
             ('抹茶',['薄茶','濃茶','抹茶ラテ','ほうじ茶ラテ'],(550,1400)),
             ('和菓子',['大福','最中','羊羹','わらび餅','団子','白玉','茶菓子'],(250,700)),
             ('甘味',['抹茶パフェ','抹茶アイス','餡蜜','宇治金時'],(600,1400)),
             ('軽食',['茶そば','お茶漬け'],(800,1300))])
T['kanmi']['sections'][0][1].extend(['大福','わらび餅','抹茶パフェ'])
T['kanmi']['sections'][1][1].extend(['ほうじ茶','玄米茶'])
T['teishoku']['sections'][2][1].append('麦茶')
T['soba']['sections'][1][1].append('茶そば')
R['kyoto']['items'].append('抹茶パフェ')
NAMEPAT_R.update({'茶寮':'さりょう','日本茶':'にほんちゃ','園':'えん'})

# ---------- restaurant phrases: notices posted in the shop, and what staff and customers say
SIGN_W = [
 ('営業中','えいぎょうちゅう','ouvert','open'),
 ('準備中','じゅんびちゅう','en préparation, pas encore ouvert','getting ready, not open yet'),
 ('本日休業','ほんじつきゅうぎょう','fermé aujourd’hui','closed today'),
 ('定休日','ていきゅうび','jour de fermeture habituel','regular day off'),
 ('営業時間','えいぎょうじかん','horaires d’ouverture','opening hours'),
 ('満席','まんせき','complet','full'),
 ('禁煙','きんえん','non-fumeur','no smoking'),
 ('全席禁煙','ぜんせききんえん','non-fumeur à toutes les places','no smoking at any seat'),
 ('喫煙席','きつえんせき','places fumeurs','smoking seats'),
 ('現金のみ','げんきんのみ','espèces uniquement','cash only'),
 ('食券','しょっけん','ticket repas','meal ticket'),
 ('券売機','けんばいき','distributeur de tickets','ticket machine'),
 ('食券制','しょっけんせい','on paie au distributeur avant de commander','pay at the ticket machine first'),
 ('お持ち帰り','おもちかえり','à emporter','takeaway'),
 ('店内','てんない','sur place, dans la salle','inside, eat in'),
 ('予約席','よやくせき','table réservée','reserved table'),
 ('ご予約','ごよやく','réservation','reservation'),
 ('お一人様','おひとりさま','une personne, client seul','one person, solo diner'),
 ('お手洗い','おてあらい','toilettes','restroom'),
 ('お会計','おかいけい','l’addition, la caisse','the bill, checkout'),
 ('ご注文','ごちゅうもん','commande','order'),
 ('お冷','おひや','eau fraîche offerte','free cold water'),
 ('お冷はセルフ','おひやはセルフ','l’eau est en libre-service','water is self-service'),
 ('ご自由にどうぞ','ごじゆうにどうぞ','servez-vous librement','help yourself'),
 ('ラストオーダー','ラストオーダー','dernière commande','last orders'),
]
TALK_W = [
 ('いらっしゃいませ','いらっしゃいませ','bienvenue (accueil du personnel)','welcome (staff greeting)'),
 ('何名様ですか','なんめいさまですか','combien de personnes ?','how many people?'),
 ('二人です','ふたりです','nous sommes deux','two of us'),
 ('一人です','ひとりです','je suis seul','just me'),
 ('こちらへどうぞ','こちらへどうぞ','par ici, je vous prie','this way, please'),
 ('お決まりですか','おきまりですか','vous avez choisi ?','ready to order?'),
 ('すみません','すみません','excusez-moi (pour appeler)','excuse me (to call staff)'),
 ('ください','ください','… s’il vous plaît (pour demander)','… please (to ask for something)'),
 ('おすすめは何ですか','おすすめはなんですか','que recommandez-vous ?','what do you recommend?'),
 ('これは何ですか','これはなんですか','qu’est-ce que c’est ?','what is this?'),
 ('以上です','いじょうです','ce sera tout','that’s all'),
 ('少々お待ちください','しょうしょうおまちください','un instant, s’il vous plaît','one moment, please'),
 ('お待たせしました','おまたせしました','merci d’avoir patienté (en servant)','sorry to keep you waiting'),
 ('ごゆっくりどうぞ','ごゆっくりどうぞ','prenez votre temps','take your time, enjoy'),
 ('いただきます','いただきます','formule avant de manger','said before eating'),
 ('美味しい','おいしい','délicieux','delicious'),
 ('お水ください','おみずください','de l’eau, s’il vous plaît','water, please'),
 ('持ち帰りで','もちかえりで','à emporter (en commandant)','to go'),
 ('お会計お願いします','おかいけいおねがいします','l’addition, s’il vous plaît','the bill, please'),
 ('別々で','べつべつで','séparément (pour payer)','separately (to pay)'),
 ('カードで','カードで','par carte','by card'),
 ('ごちそうさまでした','ごちそうさまでした','formule après le repas, merci','said after eating, thanks'),
 ('ありがとうございました','ありがとうございました','merci beaucoup (au départ du client)','thank you very much'),
 ('またお越しください','またおこしください','revenez nous voir','please come again'),
]
for w,r,f,e in SIGN_W+TALK_W: W[w]=(r,f)
NEW_W.extend(SIGN_W+TALK_W)
# who says it: s staff, c customer. {d} is a dish from the menu on the wall
SCENES = [
 [('s','いらっしゃいませ'),('s','何名様ですか'),('c','二人です'),('s','こちらへどうぞ')],
 [('s','いらっしゃいませ'),('s','何名様ですか'),('c','一人です'),('s','こちらへどうぞ')],
 [('s','お決まりですか'),('c','{d}を|ください'),('c','以上です'),('s','少々お待ちください')],
 [('c','すみません'),('c','おすすめは何ですか'),('c','{d}を|ください'),('s','少々お待ちください')],
 [('c','すみません'),('c','これは何ですか'),('c','お水ください'),('s','少々お待ちください')],
 [('s','お待たせしました'),('s','ごゆっくりどうぞ'),('c','いただきます'),('c','美味しい')],
 [('c','{d}を|ください'),('c','持ち帰りで'),('s','少々お待ちください'),('s','ありがとうございました')],
 [('c','お会計お願いします'),('c','別々で'),('c','カードで'),('c','ごちそうさまでした'),('s','ありがとうございました')],
 [('c','ごちそうさまでした'),('s','ありがとうございました'),('s','またお越しください')],
]
PHRASES = dict(signs=[x[0] for x in SIGN_W], talk=[x[0] for x in TALK_W], scenes=SCENES)
