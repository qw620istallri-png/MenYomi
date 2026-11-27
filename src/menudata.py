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
もも|もも|cuisse de poulet
ささみ|ささみ|filet de poulet (blanc)
せせり|せせり|cou de poulet
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
   sections=[('串焼',['もも','正肉','ねぎま','ささみ','せせり','つくね','皮','砂肝','レバー','手羽先','ハツ','ぼんじり','軟骨','銀杏','椎茸','葱'],(150,330)),
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
             ('一品料理',['赤出汁','茶碗蒸し','上握り','特上握り','お茶漬け'],(250,3800)),
             ('飲物',['日本酒','冷酒','生ビール'],(400,900))]),
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
 ('一人です','ひとりです','je suis seul·e','just me'),
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
 ('現金で','げんきんで','en espèces (pour payer)','in cash (to pay)'),
 ('お会計ご一緒でよろしいですか','おかいけいごいっしょでよろしいですか','vous payez ensemble ?','paying together?'),
 ('お支払いはどうなさいますか','おしはらいはどうなさいますか','comment souhaitez-vous payer ?','how would you like to pay?'),
 ('かしこまりました','かしこまりました','bien noté, entendu (personnel)','certainly, noted (staff)'),
 ('ごちそうさまでした','ごちそうさまでした','formule après le repas, merci','said after eating, thanks'),
 ('ありがとうございました','ありがとうございました','merci beaucoup (au départ du client)','thank you very much'),
 ('またお越しください','またおこしください','revenez nous voir','please come again'),
]
# ---------- modern café (chain style) and Western pastry shop: mostly katakana
CAFE_W = [
 ('カフェ','カフェ','café, salon moderne','café'),
 ('コーヒー','コーヒー','café (la boisson)','coffee'),
 ('本日のコーヒー','ほんじつのコーヒー','café du jour','coffee of the day'),
 ('ドリップコーヒー','ドリップコーヒー','café filtre','drip coffee'),
 ('エスプレッソ','エスプレッソ','expresso','espresso'),
 ('アメリカーノ','アメリカーノ','americano, expresso allongé','americano'),
 ('カフェラテ','カフェラテ','café latte','caffè latte'),
 ('カフェオレ','カフェオレ','café au lait','café au lait'),
 ('カプチーノ','カプチーノ','cappuccino','cappuccino'),
 ('カフェモカ','カフェモカ','café moka au chocolat','caffè mocha'),
 ('キャラメルマキアート','キャラメルマキアート','latte au caramel (macchiato)','caramel macchiato'),
 ('アイスコーヒー','アイスコーヒー','café glacé','iced coffee'),
 ('コールドブリュー','コールドブリュー','café infusé à froid','cold brew'),
 ('ティー','ティー','thé','tea'),
 ('チャイラテ','チャイラテ','chai latte aux épices','chai latte'),
 ('アールグレイ','アールグレイ','thé Earl Grey','Earl Grey tea'),
 ('ココア','ココア','chocolat chaud','hot cocoa'),
 ('レモネード','レモネード','limonade','lemonade'),
 ('フード','フード','à manger','food'),
 ('スコーン','スコーン','scone','scone'),
 ('マフィン','マフィン','muffin','muffin'),
 ('ベーグル','ベーグル','bagel','bagel'),
 ('クロワッサン','クロワッサン','croissant','croissant'),
 ('サンドイッチ','サンドイッチ','sandwich','sandwich'),
 ('パニーニ','パニーニ','panini','panini'),
 ('シナモンロール','シナモンロール','roulé à la cannelle','cinnamon roll'),
 ('ドーナツ','ドーナツ','beignet, donut','doughnut'),
 ('カスタマイズ','カスタマイズ','options à ajouter','extras'),
 ('ホイップ','ホイップ','crème fouettée','whipped cream'),
 ('ショット追加','ショットついか','un expresso en plus','extra shot'),
 ('オーツミルク','オーツミルク','lait d’avoine','oat milk'),
 ('ソイミルク','ソイミルク','lait de soja','soy milk'),
 ('シロップ','シロップ','sirop','syrup'),
 ('デカフェ','デカフェ','déca','decaf'),
 ('サイズアップ','サイズアップ','taille au-dessus','size up'),
 ('ホット','ホット','chaud','hot'),
 ('アイス','アイス','glacé ; aussi « glace »','iced; also “ice cream”'),
 ('季節限定','きせつげんてい','édition de saison','seasonal, limited'),
 ('期間限定','きかんげんてい','pour une durée limitée','limited time only'),
 ('ケーキ','ケーキ','gâteau','cake'),
 ('洋菓子','ようがし','pâtisserie occidentale','Western sweets'),
 ('焼き菓子','やきがし','gâteaux secs, biscuits','baked sweets'),
 ('ドリンク','ドリンク','boissons','drinks'),
 ('苺','いちご','fraise','strawberry'),
 ('ショートケーキ','ショートケーキ','génoise fraises et chantilly','strawberry shortcake'),
 ('苺タルト','いちごタルト','tarte aux fraises','strawberry tart'),
 ('苺パフェ','いちごパフェ','coupe glacée aux fraises','strawberry parfait'),
 ('フルーツタルト','フルーツタルト','tarte aux fruits','fruit tart'),
 ('モンブラン','モンブラン','mont-blanc aux marrons','Mont Blanc chestnut cake'),
 ('和栗のモンブラン','わぐりのモンブラン','mont-blanc aux marrons japonais','Japanese chestnut Mont Blanc'),
 ('チーズケーキ','チーズケーキ','cheesecake','cheesecake'),
 ('ガトーショコラ','ガトーショコラ','gâteau au chocolat','chocolate cake'),
 ('シュークリーム','シュークリーム','chou à la crème','cream puff'),
 ('エクレア','エクレア','éclair','éclair'),
 ('ロールケーキ','ロールケーキ','gâteau roulé','roll cake'),
 ('ミルフィーユ','ミルフィーユ','mille-feuille','mille-feuille'),
 ('ミルクレープ','ミルクレープ','gâteau de crêpes','mille crêpe cake'),
 ('プリン','プリン','crème caramel','custard pudding'),
 ('ティラミス','ティラミス','tiramisu','tiramisu'),
 ('マカロン','マカロン','macaron','macaron'),
 ('マドレーヌ','マドレーヌ','madeleine','madeleine'),
 ('フィナンシェ','フィナンシェ','financier','financier'),
 ('カヌレ','カヌレ','cannelé','canelé'),
 ('クッキー','クッキー','biscuits, cookies','cookies'),
 ('バウムクーヘン','バウムクーヘン','gâteau à la broche (baumkuchen)','baumkuchen'),
 ('オレンジジュース','オレンジジュース','jus d’orange','orange juice'),
]
for w,r,f,e in CAFE_W: W[w]=(r,f)
NEW_W.extend(CAFE_W)
T['cafe']=dict(jp='カフェ', fr='Café moderne', layouts=['slate','card','slate'],
   names=['カフェ {n}','{n}コーヒー','{n}珈琲店'],
   sections=[('コーヒー',['本日のコーヒー','ドリップコーヒー','エスプレッソ','アメリカーノ','カフェラテ','カフェオレ','カプチーノ','カフェモカ','キャラメルマキアート','アイスコーヒー','コールドブリュー'],(330,620)),
             ('ティー',['抹茶ラテ','ほうじ茶ラテ','チャイラテ','アールグレイ','ココア','レモネード'],(400,620)),
             ('フード',['スコーン','マフィン','ベーグル','クロワッサン','サンドイッチ','パニーニ','シナモンロール','ドーナツ'],(220,700)),
             ('カスタマイズ',['ホイップ','ショット追加','オーツミルク','ソイミルク','シロップ','デカフェ','サイズアップ'],(50,80))])
T['patisserie']=dict(jp='洋菓子店', fr='Pâtisserie', layouts=['card','poster','card'],
   names=['パティスリー {n}','洋菓子 {n}','ケーキハウス {n}'],
   sections=[('ケーキ',['ショートケーキ','モンブラン','チーズケーキ','ガトーショコラ','シュークリーム','エクレア','ロールケーキ','ミルフィーユ','ミルクレープ','フルーツタルト','プリン','ティラミス'],(250,700)),
             ('季節限定',['和栗のモンブラン','苺タルト','苺パフェ'],(550,1400)),
             ('焼き菓子',['マドレーヌ','フィナンシェ','カヌレ','マカロン','クッキー','バウムクーヘン'],(180,600)),
             ('ドリンク',['コーヒー','紅茶','カフェラテ','アイスコーヒー','オレンジジュース'],(400,650))])
NAMEPAT_R.update({'カフェ':'カフェ','コーヒー':'コーヒー','珈琲店':'コーヒーてん','パティスリー':'パティスリー','洋菓子':'ようがし','ケーキハウス':'ケーキハウス'})
MENTIONS.extend(['季節限定','期間限定','ホット','アイス'])
CAFE_SIGNS = [
 ('テイクアウト','テイクアウト','à emporter','takeaway'),
 ('イートイン','イートイン','sur place','eat in'),
]
CAFE_TALK = [
 ('店内でお召し上がりですか','てんないでおめしあがりですか','c’est pour consommer sur place ?','is it for here?'),
 ('テイクアウトで','テイクアウトで','à emporter, s’il vous plaît','to go, please'),
 ('店内で','てんないで','sur place, s’il vous plaît','for here, please'),
 ('ホットとアイスどちらになさいますか','ホットとアイスどちらになさいますか','chaud ou glacé ?','hot or iced?'),
 ('アイスで','アイスで','glacé, s’il vous plaît','iced, please'),
 ('ホットで','ホットで','chaud, s’il vous plaît','hot, please'),
 ('こちらでお召し上がりですか','こちらでおめしあがりですか','vous mangez ici ?','will you eat here?'),
 ('お持ち帰りですか','おもちかえりですか','ou c’est à emporter ?','or is it to take away?'),
]
SIGN_W.extend(CAFE_SIGNS); TALK_W.extend(CAFE_TALK)
CAFE_SCENES = [
 [('s','こちらでお召し上がりですか'),('s','お持ち帰りですか'),('c','テイクアウトで'),('s','少々お待ちください')],
 [('s','こちらでお召し上がりですか'),('s','お持ち帰りですか'),('c','店内で'),('s','ごゆっくりどうぞ')],
 [('s','いらっしゃいませ'),('c','{d}を|ください'),('s','ホットとアイスどちらになさいますか'),('c','アイスで')],
 [('c','{d}を|ください'),('s','店内でお召し上がりですか'),('c','テイクアウトで'),('s','少々お待ちください')],
 [('c','{d}を|ください'),('s','店内でお召し上がりですか'),('c','店内で'),('s','少々お待ちください')],
]
# ---------- bakery (パン屋): sweet buns, savoury buns, everyday bread
BAKERY_W = [
 ('パン','パン','pain','bread'),
 ('パン屋','パンや','boulangerie','bakery'),
 ('菓子パン','かしパン','pains sucrés, brioches','sweet buns'),
 ('惣菜パン','そうざいパン','pains salés garnis','savoury buns'),
 ('食事パン','しょくじパン','pains pour les repas','table bread'),
 ('焼きたて','やきたて','tout juste sorti du four','freshly baked'),
 ('食パン','しょくパン','pain de mie','sliced white loaf'),
 ('メロンパン','メロンパン','brioche à croûte de biscuit','melon bread'),
 ('あんパン','あんパン','brioche aux haricots rouges','red bean bun'),
 ('クリームパン','クリームパン','brioche à la crème pâtissière','custard cream bun'),
 ('チョココロネ','チョココロネ','corne fourrée au chocolat','chocolate cornet'),
 ('ジャムパン','ジャムパン','brioche à la confiture','jam bun'),
 ('デニッシュ','デニッシュ','viennoiserie danoise','Danish pastry'),
 ('パンオショコラ','パンオショコラ','pain au chocolat','pain au chocolat'),
 ('カレーパン','カレーパン','beignet fourré au curry','curry bread'),
 ('焼きそばパン','やきそばパン','pain garni de nouilles sautées','yakisoba bun'),
 ('コロッケパン','コロッケパン','pain à la croquette','croquette bun'),
 ('ピザパン','ピザパン','pain façon pizza','pizza bread'),
 ('ベーコンエピ','ベーコンエピ','épi au bacon','bacon épi'),
 ('明太フランス','めんたいフランス','baguette au beurre de mentaiko','mentaiko butter baguette'),
 ('塩パン','しおパン','petit pain beurre et sel','salt butter roll'),
 ('カツサンド','カツサンド','sandwich au porc pané','katsu sandwich'),
 ('バゲット','バゲット','baguette','baguette'),
 ('ラスク','ラスク','pain grillé sucré','rusk'),
 ('ベーカリー','ベーカリー','boulangerie (mot anglais)','bakery'),
 ('パン工房','パンこうぼう','atelier de boulangerie','bread workshop'),
]
for w,r,f,e in BAKERY_W: W[w]=(r,f)
NEW_W.extend(BAKERY_W)
T['bakery']=dict(jp='パン屋', fr='Boulangerie', layouts=['card','poster','slate'],
   names=['ベーカリー {n}','{n}ベーカリー','パン工房 {n}'],
   sections=[('菓子パン',['メロンパン','あんパン','クリームパン','チョココロネ','ジャムパン','デニッシュ','パンオショコラ','クロワッサン'],(150,320)),
             ('惣菜パン',['カレーパン','焼きそばパン','コロッケパン','ピザパン','ベーコンエピ','明太フランス','塩パン','カツサンド','サンドイッチ'],(150,600)),
             ('食事パン',['食パン','バゲット','ベーグル','ラスク'],(200,600)),
             ('ドリンク',['コーヒー','カフェオレ','牛乳','オレンジジュース'],(150,380))])
NAMEPAT_R.update({'ベーカリー':'ベーカリー','パン工房':'パンこうぼう'})
SIGN_W.append(('焼きたて','やきたて','tout juste sorti du four','freshly baked'))
# ---------- konbini (コンビニ): the menu is the till receipt, with handwritten POP cards on the counter.
# No real brands: generic products and a made-up chain. Seasonal goods only change how often they show up.
KONBINI_W = [
 ('コンビニ','コンビニ','supérette ouverte 24 h/24 (konbini)','convenience store'),
 ('ホットスナック','ホットスナック','snacks chauds du comptoir','hot counter snacks'),
 ('フライドチキン','フライドチキン','poulet frit','fried chicken'),
 ('アメリカンドッグ','アメリカンドッグ','saucisse en beignet sur bâton','corn dog'),
 ('コロッケ','コロッケ','croquette de pomme de terre','potato croquette'),
 ('フランクフルト','フランクフルト','saucisse de Francfort sur bâton','frankfurter on a stick'),
 ('フライドポテト','フライドポテト','frites','French fries'),
 ('中華まん','ちゅうかまん','brioches cuites à la vapeur','steamed buns'),
 ('肉まん','にくまん','brioche vapeur à la viande','pork bun'),
 ('あんまん','あんまん','brioche vapeur aux haricots rouges','red bean steamed bun'),
 ('ピザまん','ピザまん','brioche vapeur façon pizza','pizza steamed bun'),
 ('カレーまん','カレーまん','brioche vapeur au curry','curry steamed bun'),
 ('おにぎり','おにぎり','boulette de riz (onigiri)','rice ball'),
 ('梅','うめ','prune salée (umeboshi)','pickled plum'),
 ('昆布','こんぶ','algue kombu','kelp'),
 ('ツナマヨ','ツナマヨ','thon-mayonnaise','tuna mayo'),
 ('赤飯','せきはん','riz gluant aux haricots rouges','red bean rice'),
 ('弁当','べんとう','repas en boîte (bentō)','boxed meal'),
 ('幕の内弁当','まくのうちべんとう','bentō assorti (makunouchi)','assorted bento'),
 ('のり弁','のりべん','bentō au nori et poisson pané','seaweed bento'),
 ('唐揚げ弁当','からあげべんとう','bentō au poulet frit','fried chicken bento'),
 ('生姜焼き弁当','しょうがやきべんとう','bentō au porc sauté au gingembre','ginger pork bento'),
 ('ハンバーグ弁当','ハンバーグべんとう','bentō au steak haché','hamburg steak bento'),
 ('カップ麺','カップめん','nouilles instantanées en pot','cup noodles'),
 ('パスタ','パスタ','pâtes','pasta'),
 ('サラダ','サラダ','salade','salad'),
 ('おでん','おでん','pot-au-feu japonais (oden)','oden stew'),
 ('大根','だいこん','radis blanc (daikon)','daikon radish'),
 ('ちくわ','ちくわ','tube de pâte de poisson grillée','grilled fish cake tube'),
 ('はんぺん','はんぺん','galette moelleuse de poisson','fluffy fish cake'),
 ('こんにゃく','こんにゃく','gelée de konjac','konjac jelly'),
 ('牛すじ','ぎゅうすじ','tendons de bœuf','beef tendon'),
 ('ドリンク','ドリンク','boissons','drinks'),
 ('ミネラルウォーター','ミネラルウォーター','eau minérale','mineral water'),
 ('ホットコーヒー','ホットコーヒー','café chaud','hot coffee'),
 ('缶コーヒー','かんコーヒー','café en canette','canned coffee'),
 ('野菜ジュース','やさいジュース','jus de légumes','vegetable juice'),
 ('缶ビール','かんビール','bière en canette','canned beer'),
 ('缶チューハイ','かんチューハイ','chūhai en canette (alcool pétillant)','canned chūhai'),
 ('エナジードリンク','エナジードリンク','boisson énergisante','energy drink'),
 ('スイーツ','スイーツ','desserts','sweets'),
 ('レジ袋','レジぶくろ','sac en plastique (payant)','plastic bag'),
 # the receipt
 ('レジ','レジ','caisse','till'),
 ('領収証','りょうしゅうしょう','reçu','receipt'),
 ('小計','しょうけい','sous-total','subtotal'),
 ('合計','ごうけい','total','total'),
 ('値引','ねびき','remise','discount'),
 ('現金','げんきん','espèces','cash'),
 ('お預り','おあずかり','somme reçue du client','amount tendered'),
 ('お釣り','おつり','monnaie rendue','change'),
 ('消費税','しょうひぜい','taxe sur la consommation (TVA)','consumption tax'),
 ('軽減税率','けいげんぜいりつ','taux de TVA réduit','reduced tax rate'),
 ('電子マネー','でんしマネー','paiement par carte IC (monnaie électronique)','e-money'),
 ('電話','でんわ','téléphone','phone'),
 ('担当','たんとう','employé en caisse','staff on duty'),
 ('駅前店','えきまえてん','magasin devant la gare','station-front branch'),
 ('東口店','ひがしぐちてん','magasin sortie est','east exit branch'),
 ('中央店','ちゅうおうてん','magasin du centre','central branch'),
 # handwritten POP cards
 ('揚げたて','あげたて','tout juste frit','freshly fried'),
 ('新発売','しんはつばい','nouveauté','new'),
 ('全品','ぜんぴん','tous les articles','all items'),
 ('割引','わりびき','réduction','discount'),
 ('半額','はんがく','moitié prix','half price'),
 ('はじめました','はじめました','on a commencé (un produit de saison)','now serving (seasonal item)'),
]
KONBINI_TALK = [
 ('温めますか','あたためますか','je vous le réchauffe ?','shall I heat it up?'),
 ('お願いします','おねがいします','oui, s’il vous plaît','yes, please'),
 ('大丈夫です','だいじょうぶです','non merci, ça ira','no thanks, I’m fine'),
 ('お箸おつけしますか','おはしおつけしますか','je vous mets des baguettes ?','would you like chopsticks?'),
 ('袋はご利用ですか','ふくろはごりようですか','il vous faut un sac ?','do you need a bag?'),
 ('ポイントカードはお持ちですか','ポイントカードはおもちですか','vous avez une carte de fidélité ?','do you have a point card?'),
 ('以上でよろしいですか','いじょうでよろしいですか','ce sera tout ?','will that be all?'),
 ('はい','はい','oui','yes'),
]
for w,r,f,e in KONBINI_W: W[w]=(r,f)
NEW_W.extend(KONBINI_W)
TALK_W.extend(KONBINI_TALK)
T['konbini']=dict(jp='コンビニ', fr='Konbini', layouts=['receipt'],
   names=['{n}マート','{n}ストア','{n}マート'],
   sections=[('ホットスナック',['フライドチキン','唐揚げ','アメリカンドッグ','コロッケ','フランクフルト','フライドポテト','焼鳥'],(150,260)),
             ('中華まん',['肉まん','あんまん','ピザまん','カレーまん'],(140,200)),
             ('おにぎり',['鮭','梅','昆布','ツナマヨ','明太子','赤飯','焼おにぎり'],(130,190)),
             ('弁当',['幕の内弁当','のり弁','唐揚げ弁当','生姜焼き弁当','ハンバーグ弁当','カップ麺','冷やし中華','パスタ','サラダ','サンドイッチ'],(250,650)),
             ('おでん',['大根','ちくわ','はんぺん','こんにゃく','牛すじ','昆布'],(80,160)),
             ('ドリンク',['緑茶','お茶','ミネラルウォーター','ホットコーヒー','缶コーヒー','野菜ジュース','牛乳','缶ビール','缶チューハイ','エナジードリンク'],(110,280)),
             ('スイーツ',['プリン','シュークリーム','ロールケーキ','エクレア','大福','団子','メロンパン','カレーパン','あんパン'],(130,330))],
   # printed line when it is not the bare word ('{w}' is the word)
   line={**{w:'おにぎり　{w}' for w in ['鮭','梅','昆布','ツナマヨ','明太子','赤飯']},**{w:'おでん　{w}' for w in ['大根','ちくわ','はんぺん','こんにゃく','牛すじ']},'唐揚げ':'{w}　5個入','焼鳥':'{w}　もも'},
   # winter goods are more frequent from October to March, summer goods from June to August; all show up all year
   season={**{w:'w' for w in ['肉まん','あんまん','ピザまん','カレーまん','大根','ちくわ','はんぺん','こんにゃく','牛すじ','ホットコーヒー']},'冷やし中華':'s','缶ビール':'s'},
   rate10=['缶ビール','缶チューハイ','レジ袋'],
   names_n=[('サンライズ','サンライズ'),('グリーン','グリーン'),('デイリー','デイリー'),('ハッピー','ハッピー'),('フレッシュ','フレッシュ'),('スマイル','スマイル'),('エブリ','エブリ'),('ニコニコ','ニコニコ'),('ハロー','ハロー'),('まんぷく','まんぷく')],
   branches=['駅前店','東口店','中央店'])
# half-width katakana, as old receipt printers abbreviate product names (its own review card)
_HW=dict(zip('アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンァィゥェォャュョッー',
 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｬｭｮｯｰ'))
_DK=dict(zip('ガギグゲゴザジズゼゾダヂヅデドバビブベボ','カキクケコサシスセソタチツテトハヒフヘホ')); _HD=dict(zip('パピプペポ','ハヒフヘホ'))
def halfwidth(kana):
  out=''
  for c in kana:
    if 'ぁ'<=c<='ゖ': c=chr(ord(c)+0x60)
    if c in _DK: out+=_HW[_DK[c]]+'ﾞ'
    elif c in _HD: out+=_HW[_HD[c]]+'ﾟ'
    elif c=='ヴ': out+='ｳﾞ'
    else: out+=_HW.get(c,c)
  return out
ABBR_W=['フライドチキン','アメリカンドッグ','フランクフルト','フライドポテト','肉まん','ピザまん','ツナマヨ','幕の内弁当','のり弁','ハンバーグ弁当','カップ麺','ミネラルウォーター','ホットコーヒー','缶コーヒー','野菜ジュース','缶ビール','エナジードリンク','緑茶','シュークリーム','メロンパン','レジ袋']
ABBR={w:halfwidth(W[w][0]) for w in ABBR_W}
ABBR['ツナマヨ']=halfwidth('ツナマヨオニギリ')
T['konbini']['abbr']=ABBR
NAMEPAT_R.update({'マート':'マート','ストア':'ストア'})
KONBINI_SCENES = [
 [('s','いらっしゃいませ'),('s','温めますか'),('c','お願いします'),('s','少々お待ちください')],
 [('s','温めますか'),('c','大丈夫です'),('s','袋はご利用ですか'),('c','お願いします')],
 [('s','お箸おつけしますか'),('c','お願いします'),('s','ポイントカードはお持ちですか'),('c','大丈夫です')],
 [('c','{d}を|ください'),('s','以上でよろしいですか'),('c','はい'),('s','ありがとうございました')],
 [('s','袋はご利用ですか'),('c','大丈夫です'),('s','温めますか'),('c','お願いします')],
 [('c','{d}を|ください'),('s','温めますか'),('c','大丈夫です'),('s','ありがとうございました')],
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
 [('c','お会計お願いします'),('s','お会計ご一緒でよろしいですか'),('c','別々で'),('s','お支払いはどうなさいますか'),('c','カードで')],
 [('c','すみません'),('c','お会計お願いします'),('s','お支払いはどうなさいますか'),('c','現金で'),('s','ありがとうございました')],
 [('c','ごちそうさまでした'),('s','ありがとうございました'),('s','またお越しください')],
 [('c','{d}を|ください'),('s','こちらでお召し上がりですか'),('s','お持ち帰りですか'),('c','持ち帰りで')],
]
PHRASES = dict(signs=[x[0] for x in SIGN_W], talk=[x[0] for x in TALK_W], scenes=SCENES, cafe=CAFE_SCENES, konbini=KONBINI_SCENES)

# Typical prices in yen, tax included (casual places, Tokyo level, 2025–2026). One range per dish so a menu
# never prices 鰻丼 under 牛丼; 'type:word' overrides a dish whose price depends on the kind of place.
PRICES = {
 # izakaya
 '枝豆':(380,480),'冷奴':(300,450),'出汁巻玉子':(480,680),'ポテトサラダ':(380,550),'揚げ出し豆腐':(450,600),'漬物盛合せ':(380,550),
 '塩辛':(380,500),'冷やしトマト':(350,480),'お通し':(300,500),'刺盛':(1280,1980),'唐揚':(550,750),'板わさ':(380,500),'炙りえいひれ':(450,650),
 '焼鳥':(650,980),'ほっけ焼':(680,980),'鯖塩焼':(600,850),'椎茸焼':(380,500),'牛タン焼':(980,1480),
 '唐揚げ':(550,780),'軟骨唐揚げ':(480,600),'天ぷら盛合せ':(880,1380),'串カツ':(450,700),'海老フライ':(680,980),
 '刺身盛合せ':(1280,2480),'鮪刺':(680,1080),'烏賊刺':(550,780),'蛸刺':(550,780),'鰹のたたき':(680,980),
 'お茶漬け':(450,600),'焼おにぎり':(300,450),'雑炊':(550,750),'鶏雑炊':(600,800),
 # drinks
 '生ビール':(550,750),'生中':(550,680),'生':(550,700),'瓶ビール':(600,800),'日本酒':(550,900),'熱燗':(550,850),'冷酒':(600,1000),
 '焼酎':(450,650),'梅酒':(450,600),'酎ハイ':(400,550),'レモンサワー':(420,550),'ハイボール':(450,550),'烏龍茶':(250,380),
 # yakitori, per skewer
 '正肉':(180,260),'ねぎま':(180,260),'つくね':(200,300),'皮':(160,220),'砂肝':(160,220),'レバー':(180,240),'手羽先':(220,320),
 'ハツ':(160,240),'ぼんじり':(180,240),'軟骨':(160,220),'銀杏':(200,280),'椎茸':(180,240),'葱':(150,200),'鶏刺':(680,980),
 'yakitori:親子丼':(850,1100),'yakitori:漬物盛合せ':(300,450),
 # ramen
 '醤油ラーメン':(800,1000),'味噌ラーメン':(900,1100),'塩ラーメン':(850,1000),'豚骨ラーメン':(850,1050),'担々麺':(950,1150),
 'つけ麺':(950,1150),'叉焼麺':(1150,1400),'冷やし中華':(900,1100),'中華そば':(750,950),
 '味玉':(120,150),'叉焼':(250,400),'海苔':(100,150),'ramen:葱':(100,150),'替玉':(120,200),'大盛':(100,200),
 '炒飯':(650,850),'半炒飯':(380,480),'餃子':(380,500),'ライス':(150,250),
 # soba
 'かけ蕎麦':(500,650),'天ぷら蕎麦':(1100,1500),'鴨南蛮':(1300,1700),'月見蕎麦':(650,800),'山菜蕎麦':(700,850),'きつね饂飩':(650,800),
 'たぬき蕎麦':(600,750),'肉饂飩':(850,1050),'カレー南蛮':(900,1100),'盛り蕎麦':(600,800),'ざる蕎麦':(700,900),'天ざる':(1300,1700),
 'おろし蕎麦':(800,950),'茶そば':(850,1100),'天丼':(950,1300),'カツ丼':(900,1200),'親子丼':(850,1100),
 # teishoku
 '日替り定食':(750,950),'生姜焼定食':(850,1050),'唐揚定食':(850,1050),'焼魚定食':(900,1200),'鯖味噌定食':(900,1150),
 '豚カツ定食':(1000,1350),'野菜炒め定食':(800,950),'刺身定食':(1200,1600),
 'teishoku:冷奴':(150,250),'納豆':(80,120),'味噌汁':(100,180),'豚汁':(200,300),'ご飯':(150,250),'小鉢':(150,250),'生卵':(60,90),'玉子焼':(200,300),
 # sushi, per pair
 '鮪':(250,450),'中とろ':(450,700),'大とろ':(700,1100),'鮭':(200,350),'鯛':(300,450),'鰤':(250,400),'鯵':(200,350),'烏賊':(200,330),
 '蛸':(200,330),'海老':(250,400),'穴子':(300,500),'雲丹':(600,1000),'鮑':(700,1200),'帆立':(300,450),'玉子':(120,200),
 '鉄火巻':(500,750),'河童巻':(300,400),'納豆巻':(300,400),'干瓢巻':(300,400),
 '赤出汁':(250,400),'茶碗蒸し':(400,600),'上握り':(2200,3000),'特上握り':(3300,4500),
 'sushi:日本酒':(600,1000),'sushi:冷酒':(700,1100),'sushi:生ビール':(600,800),
 # donburi chains
 '牛丼':(450,600),'豚丼':(500,650),'don:親子丼':(590,850),'don:カツ丼':(650,900),'don:天丼':(650,1000),'海鮮丼':(1200,1800),
 '鉄火丼':(1100,1500),'他人丼':(750,950),'玉子丼':(450,600),'鰻丼':(2500,3800),
 'don:味噌汁':(80,150),'don:豚汁':(180,250),'don:漬物盛合せ':(100,160),'特盛':(200,300),'並':(450,550),
 # kissaten
 '珈琲':(450,600),'紅茶':(450,600),'抹茶':(600,900),'牛乳':(350,450),'果汁':(450,600),'クリームソーダ':(650,800),
 'ナポリタン':(850,1100),'玉子サンド':(700,900),'ホットケーキ':(650,850),'珈琲ゼリー':(500,650),
 # kanmi and tea house
 '餡蜜':(700,900),'善哉':(700,900),'白玉':(550,750),'団子':(200,450),'草餅':(200,350),'宇治金時':(1100,1500),'氷':(800,1200),'葛切り':(900,1200),
 '煎茶':(500,800),'玉露':(900,1500),'ほうじ茶':(500,700),'玄米茶':(500,700),'番茶':(400,550),'茎茶':(500,700),'新茶':(700,1000),
 '和紅茶':(650,900),'冷茶':(550,750),'麦茶':(350,500),'薄茶':(700,1000),'濃茶':(1200,1800),'抹茶ラテ':(600,750),'ほうじ茶ラテ':(600,750),
 '大福':(250,400),'最中':(200,350),'羊羹':(300,450),'わらび餅':(600,850),'茶菓子':(250,400),'抹茶パフェ':(1200,1600),'抹茶アイス':(450,650),
 # okonomiyaki
 'お好み焼':(900,1300),'豚玉':(850,1050),'烏賊玉':(900,1150),'モダン焼':(1100,1400),'葱焼':(1000,1300),'焼蕎麦':(800,1050),'蛸焼':(500,700),
 # sake bar, per gō
 '純米酒':(600,900),'純米吟醸':(800,1200),'大吟醸':(1100,1800),'本醸造':(550,800),'生酒':(700,1000),'原酒':(750,1050),'濁り酒':(700,950),'地酒':(650,1000),
 '冷や':(550,800),'常温':(550,800),'ぬる燗':(600,850),'sakaba:熱燗':(600,850),'sakaba:冷酒':(700,1000),'一合':(600,900),'二合':(1100,1700),
 # regional specialities
 '成吉思汗':(1200,1800),'蟹':(2500,5000),'石狩鍋':(1500,2200),'いくら丼':(1800,2800),'帆立焼':(600,900),'麦飯':(250,350),
 'きりたんぽ鍋':(1300,1800),'芋煮':(500,800),'冷麺':(900,1200),'わんこ蕎麦':(3000,4000),'深川飯':(1000,1400),'もんじゃ焼':(900,1300),
 '江戸前寿司':(2500,4000),'鰻重':(3800,5500),'天麩羅':(1500,2500),'味噌カツ':(1100,1500),'櫃まぶし':(3800,5200),'きしめん':(700,950),
 '味噌煮込み饂飩':(1100,1500),'天むす':(600,900),'湯豆腐':(1200,2000),'湯葉':(700,1200),'鯖寿司':(1500,2500),'鰊蕎麦':(1300,1700),
 '京漬物':(500,800),'肉吸い':(700,900),'土手焼':(450,650),'牡蠣フライ':(1000,1400),'焼牡蠣':(800,1200),'穴子飯':(2000,2800),
 '汁なし担々麺':(750,950),'讃岐饂飩':(350,600),'釜玉':(400,600),'骨付鳥':(1000,1300),'もつ鍋':(1400,1900),'明太子':(500,800),
 '水炊き':(2000,3000),'胡麻鯖':(900,1300),'ゴーヤチャンプルー':(750,950),'沖縄蕎麦':(700,900),'ソーキ蕎麦':(850,1100),'角煮':(650,900),
 '海葡萄':(550,800),'泡盛':(500,700),
}
PRICES.update({
 # modern café, per regular size
 '本日のコーヒー':(350,450),'ドリップコーヒー':(330,450),'エスプレッソ':(330,420),'アメリカーノ':(400,500),'カフェラテ':(430,560),'カフェオレ':(400,520),
 'カプチーノ':(430,560),'カフェモカ':(480,600),'キャラメルマキアート':(500,620),'アイスコーヒー':(350,480),'コールドブリュー':(450,560),
 'cafe:抹茶ラテ':(480,620),'cafe:ほうじ茶ラテ':(480,620),'チャイラテ':(480,600),'アールグレイ':(400,520),'ココア':(420,550),'レモネード':(450,580),
 'スコーン':(280,380),'マフィン':(300,420),'ベーグル':(300,450),'クロワッサン':(250,380),'サンドイッチ':(450,650),'パニーニ':(550,700),
 'シナモンロール':(350,480),'ドーナツ':(200,320),
 'ホイップ':(50,60),'ショット追加':(50,80),'オーツミルク':(50,80),'ソイミルク':(50,60),'シロップ':(50,60),'デカフェ':(50,60),'サイズアップ':(50,60),
 # pastry shop, per piece
 'ショートケーキ':(450,650),'モンブラン':(500,680),'チーズケーキ':(420,580),'ガトーショコラ':(430,600),'シュークリーム':(200,350),'エクレア':(300,420),
 'ロールケーキ':(380,520),'ミルフィーユ':(500,680),'ミルクレープ':(480,620),'フルーツタルト':(550,750),'プリン':(280,420),'ティラミス':(450,600),
 '和栗のモンブラン':(650,900),'苺タルト':(550,750),'苺パフェ':(1000,1500),
 'マドレーヌ':(180,260),'フィナンシェ':(200,280),'カヌレ':(230,330),'マカロン':(200,300),'クッキー':(350,650),'バウムクーヘン':(300,500),
 'patisserie:コーヒー':(450,600),'patisserie:紅茶':(450,650),'patisserie:カフェラテ':(500,650),'patisserie:アイスコーヒー':(450,600),'オレンジジュース':(400,600),
})
PRICES.update({
 # bakery, per piece (bread per loaf)
 'メロンパン':(160,250),'あんパン':(150,230),'クリームパン':(160,250),'チョココロネ':(180,260),'ジャムパン':(150,220),'デニッシュ':(250,380),
 'パンオショコラ':(200,300),'bakery:クロワッサン':(180,280),'カレーパン':(200,300),'焼きそばパン':(200,300),'コロッケパン':(220,320),'ピザパン':(230,330),
 'ベーコンエピ':(250,350),'明太フランス':(250,380),'塩パン':(120,200),'カツサンド':(400,600),'bakery:サンドイッチ':(300,450),
 '食パン':(350,600),'バゲット':(300,420),'bakery:ベーグル':(200,300),'ラスク':(250,400),
 'bakery:コーヒー':(200,350),'bakery:カフェオレ':(250,380),'bakery:牛乳':(150,200),'bakery:オレンジジュース':(200,300),
})
PRICES.update({
 # konbini, tax included (8% food, 10% alcohol and bags)
 'フライドチキン':(200,260),'konbini:唐揚げ':(216,260),'アメリカンドッグ':(130,160),'コロッケ':(90,130),'フランクフルト':(140,180),'フライドポテト':(180,250),'konbini:焼鳥':(120,160),
 '肉まん':(150,200),'あんまん':(140,180),'ピザまん':(150,200),'カレーまん':(150,200),
 'konbini:鮭':(150,190),'梅':(120,150),'昆布':(120,150),'ツナマヨ':(130,160),'konbini:明太子':(150,190),'赤飯':(140,180),'konbini:焼おにぎり':(150,200),
 '幕の内弁当':(500,650),'のり弁':(400,500),'唐揚げ弁当':(450,600),'生姜焼き弁当':(500,620),'ハンバーグ弁当':(500,650),'カップ麺':(200,280),
 'konbini:冷やし中華':(450,550),'パスタ':(450,580),'サラダ':(250,400),'konbini:サンドイッチ':(280,400),
 '大根':(90,120),'ちくわ':(80,120),'はんぺん':(90,130),'こんにゃく':(80,110),'牛すじ':(130,180),'konbini:昆布':(80,110),
 'konbini:緑茶':(130,170),'konbini:お茶':(130,170),'ミネラルウォーター':(100,140),'ホットコーヒー':(110,180),'缶コーヒー':(120,150),'野菜ジュース':(130,170),
 'konbini:牛乳':(150,220),'缶ビール':(220,290),'缶チューハイ':(160,220),'エナジードリンク':(200,250),
 'konbini:プリン':(150,280),'konbini:シュークリーム':(130,200),'konbini:ロールケーキ':(180,280),'konbini:エクレア':(150,220),'konbini:大福':(130,180),'konbini:団子':(120,160),
 'konbini:メロンパン':(130,180),'konbini:カレーパン':(140,190),'konbini:あんパン':(120,160),'レジ袋':(3,5),
})

# ---------- kakigōri (shaved ice) and its flavours, and what the staff says when a flavour has run out
KAKI_W = [
 ('かき氷','かきごおり','glace pilée (kakigōri)','shaved ice'),
 ('味','あじ','goût, parfum','taste, flavour'),
 ('レモン味','レモンあじ','parfum citron','lemon flavour'),
 ('いちご味','いちごあじ','parfum fraise','strawberry flavour'),
 ('メロン味','メロンあじ','parfum melon','melon flavour'),
 ('抹茶味','まっちゃあじ','parfum matcha','matcha flavour'),
 ('練乳','れんにゅう','lait concentré sucré','sweetened condensed milk'),
]
KAKI_TALK = [
 ('売り切れなんです','うりきれなんです','c’est épuisé, désolé (dit le personnel)','it’s sold out, sorry (staff)'),
 ('じゃあ','じゃあ','alors, dans ce cas…','well then…'),
 ('溶けないうちにどうぞ','とけないうちにどうぞ','à déguster avant que ça fonde','enjoy it before it melts'),
 ('温かいうちにどうぞ','あたたかいうちにどうぞ','à déguster tant que c’est chaud','enjoy it while it’s hot'),
]
for w,r,f,e in KAKI_W+KAKI_TALK: W[w]=(r,f)
NEW_W.extend(KAKI_W+KAKI_TALK)
T['kanmi']['sections'].insert(1,('かき氷',['レモン味','いちご味','メロン味','抹茶味','宇治金時','練乳'],(500,950)))
PHRASES['talk'].extend(x[0] for x in KAKI_TALK)
# sweet shops and tea houses: the flavour someone wanted has run out, or the dish is served right away
PHRASES['kanmi'] = [
 [('c','すみません'),('c','{d}を|ください'),('s','すみません、|売り切れなんです'),('c','じゃあ、これを|ください')],
 [('c','{d}を|ください'),('s','少々お待ちください'),('s','お待たせしました'),('s','溶けないうちにどうぞ')],
 [('s','お決まりですか'),('c','{d}を|ください'),('s','すみません、|売り切れなんです'),('c','じゃあ'),('c','これを|ください')],
]
SCENES.append([('s','お待たせしました'),('s','温かいうちにどうぞ'),('c','いただきます')])
PRICES.update({'かき氷':(500,900),'レモン味':(500,800),'いちご味':(500,800),'メロン味':(500,800),'抹茶味':(600,950),'練乳':(100,200)})

# ---------- ordering with a quantity: counters heard at every counter, and lines that use them
COUNT_W = [
 ('一つ','ひとつ','un, une (objet, plat)','one (item, dish)'),
 ('二つ','ふたつ','deux (objets, plats)','two (items, dishes)'),
 ('一本','いっぽん','une (brochette, bouteille)','one (skewer, bottle)'),
 ('二本','にほん','deux (brochettes, bouteilles)','two (skewers, bottles)'),
 ('一杯','いっぱい','un verre, un bol','one glass, one bowl'),
 ('一個','いっこ','une pièce, un morceau','one piece'),
]
for w,r,f,e in COUNT_W: W[w]=(r,f)
NEW_W.extend(COUNT_W)
# a line is 'before|word|after': the middle word is the one the line teaches, {d} is a dish from the menu
SCENES.extend([
 [('s','お決まりですか'),('c','{d}を|一つ|ください'),('s','かしこまりました')],
 [('c','すみません'),('c','{d}|お願いします'),('s','かしこまりました'),('s','少々お待ちください')],
 [('s','お決まりですか'),('c','{d}を|二つ|ください'),('c','以上です'),('s','かしこまりました')],
])
PHRASES['kushi'] = [
 [('s','お決まりですか'),('c','{d}を|二本|ください'),('c','生ビールを|一杯|ください'),('s','かしこまりました')],
 [('c','すみません'),('c','{d}を|一本|ください'),('s','塩とタレ、|どちらになさいますか'),('c','|塩|で')],
 [('c','{d}を|二本|ください'),('s','かしこまりました'),('c','それと、ビールを|一本|ください')],
]
W['どちらになさいますか']=('どちらになさいますか','lequel choisissez-vous ? (poli)'); NEW_W.append(('どちらになさいますか','どちらになさいますか','lequel choisissez-vous ? (poli)','which would you like? (polite)'))
PHRASES['talk'].append('どちらになさいますか')
PHRASES['konbini'].append([('c','{d}を|一個|ください'),('s','温めますか'),('c','お願いします'),('s','かしこまりました')])

# ---------- spellings as they show up on real menus: the common form is the word to learn,
# the rarer forms (old kanji, other okurigana) stand in on a menu now and then, with this probability
CANON = {  # common form -> older or rarer form it replaces in the menus (explanations and English are shared)
 'うどん':'饂飩','焼きそば':'焼蕎麦','たこ焼き':'蛸焼','ジンギスカン':'成吉思汗','ひつまぶし':'櫃まぶし',
 '海ぶどう':'海葡萄','ごまさば':'胡麻鯖','きつねうどん':'きつね饂飩','肉うどん':'肉饂飩',
 '味噌煮込みうどん':'味噌煮込み饂飩','讃岐うどん':'讃岐饂飩','天ぷら':'天麩羅',
}
for new,old in CANON.items(): W[new]=(W[old][0],W[old][1])
def _swap(lst):
  for i,w in enumerate(lst):
    for new,old in CANON.items():
      if w==old: lst[i]=new
for t in T.values():
  for sec in t['sections']: _swap(sec[1])
for reg in R.values(): _swap(reg['items'])
for new,old in CANON.items():
  if old in PRICES and new not in PRICES: PRICES[new]=PRICES[old]
  for k in list(PRICES):
    if k.endswith(':'+old): PRICES[k[:-len(old)]+new]=PRICES[k]
VARIANTS = {w:[(old,.12)] for w,old in CANON.items()}
for w,v in {'焼き鳥':('やきとり','brochettes de poulet grillé','grilled chicken skewers'),'から揚げ':('からあげ','poulet frit à la japonaise','Japanese fried chicken'),
            'お好み焼き':('おこのみやき','crêpe japonaise garnie','savoury Japanese pancake')}.items():
  W[w]=(v[0],v[1]); NEW_W.append((w,v[0],v[1],v[2]))
VARIANTS.update({'焼鳥':[('焼き鳥',.3),('燒鳥',.04)],'唐揚げ':[('から揚げ',.2),('唐揚',.15)],'お好み焼':[('お好み焼き',.35)]})
MENTIONS.extend(['焼き鳥','から揚げ','お好み焼き'])
