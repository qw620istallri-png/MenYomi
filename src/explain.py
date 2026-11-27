# -*- coding: utf-8 -*-
# What the dish actually is: word|français|English (one or two short sentences)
X = {}
def add(s):
    for line in s.strip().splitlines():
        line=line.strip()
        if not line or line.startswith('#'): continue
        w,f,e=[x.strip() for x in line.split('|')]
        X[w]=(f,e)

add("""
# --- izakaya
枝豆|Gousses de soja encore vertes, bouillies et salées, qu’on presse pour faire sortir les fèves. Le premier plat avec la bière.|Young soybean pods, boiled and salted; you squeeze the beans out. The classic first bite with beer.
冷奴|Bloc de tofu soyeux servi froid, garni de ciboule, gingembre râpé et bonite séchée, arrosé de sauce soja.|Chilled silken tofu topped with scallion, grated ginger and bonito flakes, with a dash of soy sauce.
出汁巻玉子|Omelette roulée en couches fines, très moelleuse, où les œufs sont battus avec du bouillon dashi.|Rolled omelette cooked in thin layers, soft and juicy because the eggs are beaten with dashi stock.
ポテトサラダ|Purée de pommes de terre à la mayonnaise japonaise, avec concombre, carotte et jambon. Un classique de comptoir.|Mashed potato salad with Japanese mayonnaise, cucumber, carrot and ham. A bar-counter staple.
揚げ出し豆腐|Tofu enrobé de fécule et frit, servi dans un bouillon dashi chaud avec radis râpé et ciboule.|Tofu dusted in starch and fried, served in hot dashi with grated daikon and scallion.
漬物盛合せ|Petit plateau de légumes saumurés : radis jaune, concombre, chou, prune umeboshi selon la maison.|A small plate of pickled vegetables: yellow daikon, cucumber, cabbage, sometimes umeboshi plum.
塩辛|Lamelles de calmar fermentées dans leur propre foie salé. Très fort, on en mange un peu avec le saké.|Squid strips fermented in their own salted liver. Pungent; eaten in small bites with sake.
冷やしトマト|Tomate bien froide coupée en quartiers, servie avec un peu de sel ou de mayonnaise.|An ice-cold tomato cut in wedges, served with salt or mayonnaise.
焼鳥|Morceaux de poulet en brochette grillés au charbon, au sel (塩) ou laqués à la sauce (タレ).|Chicken pieces on skewers grilled over charcoal, either salted (shio) or glazed with sauce (tare).
ほっけ焼|Hokke, un poisson du nord ouvert à plat, séché une nuit puis grillé entier. Chair grasse et feuilletée.|Atka mackerel from the north, butterflied, dried overnight and grilled whole. Rich, flaky flesh.
焼魚|Poisson grillé du jour, souvent servi avec du radis râpé et un trait de sauce soja.|Grilled fish of the day, usually with grated daikon and a little soy sauce.
鯖塩焼|Filet de maquereau salé puis grillé jusqu’à ce que la peau croustille.|Salted mackerel fillet grilled until the skin crackles.
椎茸焼|Gros champignons shiitake grillés, assaisonnés de sel ou de sauce soja.|Large shiitake mushrooms grilled with salt or soy sauce.
牛タン焼|Fines tranches de langue de bœuf grillées, servies au sel et citron. Spécialité de Sendai.|Thin slices of beef tongue grilled and served with salt and lemon. A Sendai speciality.
唐揚げ|Morceaux de cuisse de poulet marinés (soja, gingembre, ail), enrobés de fécule et frits. Croustillants et juteux.|Chicken thigh marinated in soy, ginger and garlic, coated in starch and fried. Crisp outside, juicy inside.
軟骨唐揚げ|Petits morceaux de cartilage de poulet frits, croquants. Très apprécié avec la bière.|Bite-size chicken cartilage, fried and crunchy. A beer snack.
天ぷら盛合せ|Crevettes, poisson et légumes dans une pâte très légère, frits minute. À tremper dans un bouillon ou dans du sel.|Shrimp, fish and vegetables in a very light batter, fried to order. Dip in broth or salt.
串カツ|Brochettes de viande ou de légumes panées et frites. À Ōsaka, on ne trempe qu’une fois dans la sauce commune.|Breaded, deep-fried skewers of meat or vegetables. In Osaka, no double-dipping in the shared sauce.
海老フライ|Grosses crevettes panées à la chapelure, servies avec une sauce tartare.|Large breaded fried shrimp served with tartar sauce.
刺身盛合せ|Plateau de poissons crus en tranches choisis par le chef, avec radis en fils et wasabi.|The chef’s selection of raw fish slices, with shredded daikon and wasabi.
鮪刺|Tranches de thon cru, à tremper légèrement dans la sauce soja avec un peu de wasabi.|Slices of raw tuna, dipped lightly in soy sauce with a touch of wasabi.
烏賊刺|Calmar cru coupé en fines lanières, un peu sucré et croquant.|Raw squid cut into thin strips, slightly sweet and crunchy.
蛸刺|Poulpe cuit puis tranché finement, servi froid.|Octopus, boiled then sliced thin and served cold.
鰹のたたき|Bonite saisie à la flamme à l’extérieur, crue dedans, servie avec ail, ciboule et sauce aux agrumes.|Bonito seared over flame outside and raw inside, with garlic, scallion and citrus soy sauce.
お茶漬け|Riz chaud arrosé de thé vert ou de bouillon, garni de saumon, prune ou algue. Pour finir la soirée.|Hot rice with green tea or broth poured over, topped with salmon, plum or seaweed. A night-closing dish.
焼おにぎり|Boulette de riz badigeonnée de sauce soja et grillée jusqu’à former une croûte.|A rice ball brushed with soy sauce and grilled until it forms a crust.
雑炊|Riz mijoté dans le bouillon qui reste du ragoût, lié à l’œuf. Souvent servi en fin de repas.|Rice simmered in leftover hotpot broth and bound with egg. Often the last course.
生ビール|Bière blonde à la pression, servie très froide dans une chope.|Lager on tap, served ice-cold in a mug.
生中|La chope moyenne de bière pression, la taille la plus commandée.|The medium mug of draft beer, the most ordered size.
瓶ビール|Grande bouteille de bière à partager, avec de petits verres.|A large bottle of beer to share, with small glasses.
日本酒|Saké, l’alcool de riz fermenté. Se boit froid, à température ambiante ou chaud.|Sake, the fermented rice drink. Served cold, at room temperature or warm.
熱燗|Saké chauffé à environ 50 °C, servi en carafe. Idéal en hiver.|Sake heated to about 50 °C and served in a flask. A winter favourite.
冷酒|Saké servi bien frais, souvent les plus parfumés.|Sake served chilled, often the more aromatic kinds.
焼酎|Alcool distillé (patate douce, orge, riz…), autour de 25°. Se boit sec, à l’eau, à l’eau chaude ou sur glace.|Distilled spirit from sweet potato, barley, rice and more, around 25%. Drunk neat, with water, hot water or on ice.
梅酒|Liqueur de prunes ume macérées. Douce et acidulée, souvent sur glace.|A liqueur of steeped ume plums. Sweet and tart, often on the rocks.
酎ハイ|Shōchū allongé d’eau gazeuse et parfumé aux fruits.|Shochu topped with soda water and flavoured with fruit.
レモンサワー|Shōchū, eau gazeuse et citron pressé. La boisson phare des izakaya actuels.|Shochu, soda water and squeezed lemon. Today’s izakaya favourite.
ハイボール|Whisky japonais allongé d’eau gazeuse dans un grand verre de glace.|Japanese whisky topped with soda in a tall glass of ice.
烏龍茶|Thé oolong servi froid, la boisson sans alcool par défaut.|Iced oolong tea, the default soft drink.
お湯割り|Shōchū coupé d’eau chaude, souvent avec une prune ume dedans.|Shochu cut with hot water, often with an ume plum in it.
水割り|Alcool (shōchū ou whisky) allongé d’eau froide.|A spirit (shochu or whisky) cut with cold water.
# --- yakitori
正肉|Morceaux de cuisse de poulet seuls sur la brochette.|Plain chicken thigh pieces on a skewer.
ねぎま|Morceaux de poulet alternés avec des tronçons de poireau japonais.|Chicken pieces alternating with lengths of Japanese leek.
つくね|Boulettes ou bâtonnet de poulet haché, souvent laqués et servis avec un jaune d’œuf cru.|Minced chicken meatballs or a stick, often glazed and served with a raw yolk to dip.
皮|Peau de poulet enroulée sur la brochette et grillée jusqu’à être croustillante.|Chicken skin wound on a skewer and grilled until crisp.
砂肝|Gésier de poulet, ferme et croquant, souvent au sel.|Chicken gizzard, firm and crunchy, usually salted.
レバー|Foie de poulet grillé à peine cuit, fondant, souvent à la sauce.|Chicken liver grilled just done, creamy, usually with sauce.
手羽先|Pointe d’aile de poulet grillée ou frite, la peau très croustillante.|Chicken wing tips, grilled or fried with very crisp skin.
ハツ|Cœur de poulet, texture ferme et goût léger.|Chicken heart, firm with a mild taste.
ぼんじり|Croupion de poulet, la partie la plus grasse et juteuse.|Chicken tail, the fattiest and juiciest cut.
軟骨|Cartilage de poulet grillé, croquant.|Grilled chicken cartilage, crunchy.
銀杏|Noix de ginkgo grillées sur une brochette, vertes et légèrement amères.|Ginkgo nuts grilled on a skewer, green and slightly bitter.
鶏刺|Poulet cru ou juste saisi en fines tranches, servi avec gingembre et sauce soja.|Raw or lightly seared chicken slices, with ginger and soy sauce.
鶏雑炊|Riz mijoté dans un bouillon de poulet avec de l’œuf.|Rice simmered in chicken broth with egg.
親子丼|Poulet et oignon mijotés puis liés à l’œuf, posés sur du riz. « Parent et enfant ».|Chicken and onion simmered then set with egg over rice. “Parent and child”.
# --- ramen
醤油ラーメン|Ramen dans un bouillon clair à la sauce soja, le style le plus classique.|Ramen in a clear soy-sauce broth, the most classic style.
味噌ラーメン|Ramen dans un bouillon au miso, épais et chaud, souvent avec du maïs et du beurre. Né à Sapporo.|Ramen in a thick, warming miso broth, often with corn and butter. Born in Sapporo.
塩ラーメン|Ramen dans un bouillon clair simplement salé, le plus léger.|Ramen in a clear, salt-seasoned broth, the lightest kind.
豚骨ラーメン|Ramen dans un bouillon d’os de porc bouilli des heures, blanc et crémeux. Spécialité de Fukuoka.|Ramen in a white, creamy broth of pork bones boiled for hours. A Fukuoka speciality.
担々麺|Nouilles dans un bouillon au sésame et à l’huile pimentée, avec du porc haché.|Noodles in a sesame and chili-oil broth with minced pork.
つけ麺|Nouilles servies à part, à tremper dans un bouillon très concentré.|Noodles served on the side to dip into a very concentrated broth.
叉焼麺|Ramen garni de plusieurs tranches de porc braisé.|Ramen topped with several slices of braised pork.
冷やし中華|Nouilles froides garnies de jambon, omelette et concombre, sauce vinaigrée. Plat d’été.|Cold noodles topped with ham, omelette and cucumber in a tangy dressing. A summer dish.
中華そば|Nom à l’ancienne du ramen, souvent un bouillon soja léger et nostalgique.|The old name for ramen, usually a light, nostalgic soy broth.
味玉|Œuf mollet mariné dans la sauce soja, jaune coulant.|A soft-boiled egg marinated in soy sauce, with a runny yolk.
叉焼|Porc roulé, braisé dans la sauce soja puis tranché.|Rolled pork belly braised in soy sauce and sliced.
海苔|Feuille d’algue séchée, posée sur le bord du bol.|A sheet of dried seaweed, set on the edge of the bowl.
葱|Ciboule ou poireau japonais émincé, en garniture.|Chopped scallion or Japanese leek as a topping.
替玉|Portion de nouilles ajoutée dans le bouillon qui reste. On la commande avant de finir.|An extra serving of noodles dropped into your leftover broth. Order it before you finish.
炒飯|Riz sauté au wok avec œuf, ciboule et porc.|Wok-fried rice with egg, scallion and pork.
半炒飯|Demi-portion de riz sauté, à côté d’un ramen.|A half portion of fried rice alongside ramen.
餃子|Raviolis au porc et chou, grillés dessous et cuits à la vapeur dessus. Sauce soja, vinaigre et huile pimentée.|Pork and cabbage dumplings, pan-fried underneath and steamed on top. Dip in soy, vinegar and chili oil.
ライス|Bol de riz blanc nature.|A plain bowl of white rice.
# --- soba / udon
蕎麦|Nouilles fines de sarrasin, servies froides avec une sauce ou chaudes en bouillon.|Thin buckwheat noodles, served cold with a dipping sauce or hot in broth.
饂飩|Nouilles de blé épaisses et souples, en bouillon chaud ou froides.|Thick, chewy wheat noodles, hot in broth or cold.
かけ蕎麦|Soba dans un bouillon chaud, sans garniture : la base.|Soba in hot broth with no topping: the basic bowl.
天ぷら蕎麦|Soba chaudes avec une grosse crevette tempura posée dessus.|Hot soba topped with a large shrimp tempura.
鴨南蛮|Soba chaudes au canard et au poireau grillé.|Hot soba with duck and grilled leek.
月見蕎麦|Soba chaudes avec un œuf cru au centre, comme la pleine lune.|Hot soba with a raw egg in the middle, like a full moon.
山菜蕎麦|Soba chaudes aux pousses et fougères de montagne.|Hot soba with mountain shoots and fern fronds.
きつね饂飩|Udon chaudes avec une grande tranche de tofu frit sucré. Le renard (kitsune) aimerait ça.|Hot udon with a large slice of sweet fried tofu, said to be the fox’s favourite.
たぬき蕎麦|Soba chaudes parsemées de miettes de pâte à tempura.|Hot soba sprinkled with crunchy tempura batter bits.
肉饂飩|Udon chaudes au bœuf mijoté sucré-salé.|Hot udon with sweet-savoury simmered beef.
カレー南蛮|Soba dans un bouillon au curry japonais épaissi, avec poireau.|Soba in a thickened Japanese curry broth with leek.
盛り蕎麦|Soba froides sur un plateau, à tremper dans une sauce froide.|Cold soba on a tray, dipped in a cold sauce.
ざる蕎麦|Soba froides sur une claie en bambou, avec des lamelles de nori.|Cold soba on a bamboo tray, topped with strips of nori.
天ざる|Soba froides servies avec un assortiment de tempura.|Cold soba served with assorted tempura.
おろし蕎麦|Soba avec du radis daikon râpé, frais et un peu piquant.|Soba with grated daikon, fresh and slightly sharp.
# --- don / teishoku
天丼|Tempura de crevettes et légumes sur du riz, nappée d’une sauce sucrée.|Shrimp and vegetable tempura over rice with a sweet sauce.
カツ丼|Porc pané mijoté avec oignon et œuf, posé sur du riz.|Breaded pork cutlet simmered with onion and egg over rice.
生姜焼定食|Formule autour de tranches de porc sautées au gingembre et soja, avec riz, soupe et chou.|Set meal of pork slices fried with ginger and soy, with rice, soup and cabbage.
唐揚定食|Formule poulet frit avec riz, soupe miso et chou émincé.|Set meal of fried chicken with rice, miso soup and shredded cabbage.
焼魚定食|Formule poisson grillé avec riz, soupe et petits accompagnements.|Set meal of grilled fish with rice, soup and small sides.
鯖味噌定食|Formule maquereau mijoté dans une sauce miso sucrée.|Set meal of mackerel simmered in sweet miso sauce.
豚カツ定食|Formule porc pané épais, avec chou émincé à volonté et sauce tonkatsu.|Set meal of thick breaded pork with refillable shredded cabbage and tonkatsu sauce.
野菜炒め定食|Formule légumes sautés au wok avec un peu de porc.|Set meal of wok-fried vegetables with a little pork.
刺身定食|Formule sashimi avec riz, soupe miso et pickles.|Set meal of sashimi with rice, miso soup and pickles.
日替り定食|La formule qui change chaque jour, souvent la moins chère.|The set meal that changes daily, often the cheapest.
納豆|Soja fermenté gluant au goût fort, mélangé à la sauce et à la moutarde, sur du riz.|Sticky, strong-tasting fermented soybeans, stirred with sauce and mustard, eaten on rice.
味噌汁|Bouillon dashi au miso avec tofu, algue ou légumes. Accompagne presque chaque repas.|Dashi broth with miso and tofu, seaweed or vegetables. Comes with almost every meal.
豚汁|Soupe miso copieuse au porc et légumes racines.|A hearty miso soup with pork and root vegetables.
ご飯|Bol de riz blanc. Au Japon, souvent resservi gratuitement.|A bowl of white rice. In Japan often refilled for free.
小鉢|Petit bol d’accompagnement : légumes mijotés, salade, tofu…|A small side bowl: simmered vegetables, salad, tofu and so on.
生卵|Œuf cru à battre et verser sur le riz chaud avec un peu de sauce soja.|A raw egg to beat and pour over hot rice with a little soy sauce.
玉子焼|Omelette roulée, sucrée ou salée selon la région.|Rolled omelette, sweet or savoury depending on the region.
牛丼|Fines tranches de bœuf et d’oignon mijotées sucré-salé sur du riz. Rapide et pas cher.|Thin beef and onion simmered sweet-savoury over rice. Fast and cheap.
海鮮丼|Bol de riz vinaigré couvert de poissons crus et d’œufs de poisson.|Vinegared rice covered with raw fish and roe.
鉄火丼|Bol de riz vinaigré couvert de thon cru.|Vinegared rice covered with raw tuna.
豚丼|Porc grillé laqué à la sauce sucrée sur du riz. Spécialité d’Obihiro.|Grilled pork glazed in sweet sauce over rice. An Obihiro speciality.
他人丼|Comme l’oyakodon mais au bœuf ou au porc : la viande et l’œuf sont des « étrangers ».|Like oyakodon but with beef or pork: the meat and egg are “strangers”.
玉子丼|Oignon et bouillon liés à l’œuf, sur du riz.|Onion and broth set with egg over rice.
鰻丼|Anguille grillée laquée à la sauce sucrée, sur du riz.|Grilled eel glazed with sweet sauce, over rice.
# --- sushi
握り|Sushi en forme de boulette de riz vinaigré pressée à la main, avec une tranche de poisson dessus.|Sushi made of a hand-pressed mound of vinegared rice topped with a slice of fish.
巻物|Riz et garniture roulés dans une feuille de nori.|Rice and filling rolled in a sheet of nori.
鮪|Le thon rouge, maigre (akami) et rouge vif.|Bluefin tuna, the lean red cut (akami).
中とろ|Partie mi-grasse du ventre de thon, fondante.|The medium-fatty belly of tuna, melting.
大とろ|La partie la plus grasse du ventre de thon, très fondante et chère.|The fattiest part of the tuna belly, very rich and expensive.
鮭|Saumon, souvent servi gras et orangé.|Salmon, usually fatty and bright orange.
鯛|Daurade, chair blanche et fine, poisson des fêtes.|Sea bream, delicate white fish served at celebrations.
鰤|Sériole, poisson gras surtout bon en hiver.|Yellowtail, a rich fish at its best in winter.
鯵|Chinchard, poisson brillant servi avec gingembre et ciboule.|Horse mackerel, a silver fish served with ginger and scallion.
烏賊|Calmar cru, un peu collant et sucré.|Raw squid, slightly sticky and sweet.
蛸|Poulpe cuit, ferme et élastique.|Boiled octopus, firm and springy.
海老|Crevette, cuite ou crue (amaebi sucrée).|Shrimp, cooked or raw (sweet amaebi).
穴子|Congre mijoté, très tendre, nappé d’une sauce sucrée.|Simmered sea eel, very tender, brushed with sweet sauce.
雲丹|Oursin, crémeux et iodé, souvent présenté en gunkan entouré de nori.|Sea urchin, creamy and briny, often served in a nori-wrapped gunkan.
鮑|Ormeau, coquillage ferme et cher.|Abalone, a firm and pricey shellfish.
帆立|Noix de Saint-Jacques crue, douce et fondante.|Raw scallop, sweet and tender.
玉子|Épaisse omelette sucrée sur du riz : on dit qu’elle révèle le niveau du chef.|A thick sweet omelette on rice, said to reveal the chef’s skill.
鉄火巻|Maki fin au thon cru.|A thin roll filled with raw tuna.
河童巻|Maki fin au concombre, nommé d’après le kappa, esprit des rivières qui adore le concombre.|A thin cucumber roll, named after the kappa, a river spirit fond of cucumber.
納豆巻|Maki fin au soja fermenté.|A thin roll filled with natto.
干瓢巻|Maki fin à la courge séchée mijotée sucrée.|A thin roll of sweet simmered dried gourd.
赤出汁|Soupe miso au miso rouge foncé, souvent aux petits coquillages.|Miso soup made with dark red miso, often with small clams.
茶碗蒸し|Flan salé à l’œuf et au dashi, cuit à la vapeur en tasse, avec crevette, champignon et ginkgo.|A savoury egg and dashi custard steamed in a cup, with shrimp, mushroom and ginkgo.
上握り|Assortiment de nigiri de gamme supérieure.|A superior set of nigiri.
特上握り|L’assortiment de nigiri le plus luxueux, avec toro et oursin.|The most luxurious nigiri set, with toro and sea urchin.
江戸前寿司|Sushi à la manière de Tōkyō (Edo) : poissons de la baie, souvent marinés ou mijotés.|Tokyo-style sushi: fish from the bay, often cured or simmered.
鮨|Sushi, écrit avec le caractère traditionnel des enseignes haut de gamme.|Sushi, written with the traditional character used by upscale shops.
鮓|Sushi, graphie ancienne qui désignait le poisson fermenté dans le riz.|Sushi, an old spelling for fish fermented in rice.
# --- boulangerie
パン|Pain, du portugais pão : un des plus vieux mots étrangers du japonais.|Bread, from Portuguese pão: one of the oldest loanwords in Japanese.
パン屋|Boulangerie : on prend un plateau et une pince, on se sert, puis on paie à la caisse.|Bakery: you take a tray and tongs, help yourself, then pay at the till.
菓子パン|Pains sucrés et brioches fourrées, la spécialité des boulangeries japonaises.|Sweet and filled buns, the speciality of Japanese bakeries.
惣菜パン|Pains salés garnis d’un plat : curry, croquette, nouilles…|Savoury buns filled with a dish: curry, croquette, noodles…
食事パン|Pains simples pour accompagner les repas : pain de mie, baguette.|Plain bread to eat with meals: white loaf, baguette.
焼きたて|« Tout juste cuit » : affiché quand une fournée sort du four, souvent avec l’heure.|“Just baked”: posted when a batch comes out of the oven, often with the time.
食パン|Pain de mie très moelleux, vendu entier ou en tranches épaisses.|A very soft white loaf, sold whole or in thick slices.
メロンパン|Brioche couverte d’une croûte de biscuit quadrillée, qui rappelle un melon. Souvent sans goût de melon.|A bun under a crisp, criss-crossed cookie crust that looks like a melon. Usually no melon flavour.
あんパン|Brioche fourrée de pâte de haricots rouges, créée à Tōkyō en 1874.|A bun filled with sweet red bean paste, created in Tokyo in 1874.
クリームパン|Brioche fourrée de crème pâtissière.|A bun filled with custard cream.
チョココロネ|Pain en spirale, en forme de corne, rempli de crème au chocolat.|A spiral horn of bread filled with chocolate cream.
ジャムパン|Brioche fourrée à la confiture, souvent de fraise.|A bun filled with jam, often strawberry.
デニッシュ|Viennoiserie feuilletée garnie de fruits ou de crème.|A flaky pastry topped with fruit or custard.
パンオショコラ|Pain au chocolat, du français.|Pain au chocolat, from French.
カレーパン|Pain fourré au curry japonais, pané et frit.|Bread filled with Japanese curry, breaded and fried.
焼きそばパン|Petit pain fendu garni de nouilles sautées. Un classique des écoles.|A split roll stuffed with fried noodles. A school-canteen classic.
コロッケパン|Petit pain avec une croquette de pomme de terre et sauce.|A roll with a potato croquette and sauce.
ピザパン|Pain garni comme une pizza : sauce tomate, fromage, saucisse.|Bread topped like a pizza: tomato sauce, cheese, sausage.
ベーコンエピ|Pain en épi de blé avec du bacon à l’intérieur.|Bread shaped like an ear of wheat with bacon inside.
明太フランス|Baguette tartinée de beurre aux œufs de colin épicés (mentaiko), puis grillée.|Baguette spread with spicy pollock-roe butter, then toasted.
塩パン|Petit pain roulé autour de beurre, avec du sel sur le dessus. Très populaire.|A roll wrapped around butter with salt on top. Hugely popular.
カツサンド|Sandwich de porc pané avec sauce tonkatsu, sur pain de mie.|Breaded pork cutlet with tonkatsu sauce in white bread.
バゲット|Baguette à la française. On voit aussi フランスパン, « pain français ».|A French baguette. Also called フランスパン, “French bread”.
ラスク|Tranches de pain séchées au four avec beurre et sucre.|Slices of bread oven-dried with butter and sugar.
# --- café moderne / pâtisserie
カフェ|Café moderne, souvent une chaîne, avec carte en katakana venue de l’anglais et de l’italien.|A modern café, often a chain, with a menu in katakana borrowed from English and Italian.
コーヒー|Café, du néerlandais koffie. Le même mot que 珈琲 écrit en kanji dans les cafés rétro.|Coffee, from Dutch koffie. The same word as 珈琲, which retro cafés write in kanji.
本日のコーヒー|Le café filtre du jour : un grain différent chaque jour, au prix le plus bas de la carte.|Today’s drip coffee: a different bean each day, usually the cheapest drink on the board.
ドリップコーヒー|Café filtre, versé à travers un filtre papier.|Coffee brewed by pouring water through a paper filter.
エスプレッソ|Café court et serré, de l’italien espresso. Les petits ッ marquent la double consonne.|A short, strong coffee, from Italian espresso. The small ッ marks the doubled consonant.
アメリカーノ|Expresso allongé d’eau chaude. Le ー allonge la voyelle : a-me-ri-kā-no.|Espresso topped up with hot water. The ー lengthens the vowel: a-me-ri-kā-no.
カフェラテ|Expresso et beaucoup de lait chaud.|Espresso with plenty of steamed milk.
カフェオレ|Café filtre et lait chaud à parts égales, du français.|Drip coffee and hot milk in equal parts, from French.
カプチーノ|Expresso avec une épaisse mousse de lait.|Espresso under a thick layer of milk foam.
カフェモカ|Latte au chocolat, souvent avec crème fouettée.|A chocolate latte, often topped with whipped cream.
キャラメルマキアート|Lait vanillé, expresso versé par-dessus et filet de caramel. ャ est un petit ya : kya.|Vanilla milk with espresso poured on top and a caramel drizzle. ャ is a small ya: kya.
アイスコーヒー|Café glacé. アイス (ice) devant un mot veut dire « version glacée ».|Iced coffee. アイス (ice) in front of a drink means the iced version.
コールドブリュー|Café infusé longuement à l’eau froide, plus doux. ュ est un petit yu : ryu.|Coffee steeped slowly in cold water, smoother. ュ is a small yu: ryu.
ティー|Thé, de l’anglais tea. Le petit ィ forme le son « ti » absent du japonais.|Tea, from English. The small ィ makes the “ti” sound Japanese lacks.
チャイラテ|Thé noir aux épices et lait chaud.|Spiced black tea with steamed milk.
アールグレイ|Thé noir parfumé à la bergamote.|Black tea scented with bergamot.
ココア|Chocolat chaud.|Hot chocolate.
レモネード|Limonade au citron pressé.|Lemonade made with fresh lemon.
フード|« Food » : la partie à manger de la carte.|“Food”: the things to eat on the board.
スコーン|Scone, à la confiture ou à la crème.|A scone, with jam or cream.
マフィン|Muffin.|A muffin.
ベーグル|Bagel, nature ou garni.|A bagel, plain or filled.
クロワッサン|Croissant, du français.|A croissant, from French.
サンドイッチ|Sandwich.|A sandwich.
パニーニ|Sandwich italien pressé et grillé.|A pressed, toasted Italian sandwich.
シナモンロール|Brioche roulée à la cannelle.|A cinnamon roll.
ドーナツ|Beignet en anneau.|A doughnut.
カスタマイズ|« Customize » : les suppléments payants à ajouter à une boisson.|“Customize”: paid extras added to a drink.
ホイップ|Crème fouettée ajoutée sur la boisson.|Whipped cream on top of the drink.
ショット追加|Un expresso de plus dans la boisson. 追加 : ajout.|An extra espresso shot. 追加 means addition.
オーツミルク|Lait d’avoine à la place du lait de vache.|Oat milk instead of cow’s milk.
ソイミルク|Lait de soja à la place du lait de vache. On voit aussi 豆乳.|Soy milk instead of cow’s milk. Also written 豆乳.
シロップ|Sirop ajouté : vanille, caramel, noisette…|Added syrup: vanilla, caramel, hazelnut…
デカフェ|Version décaféinée, du français.|Decaffeinated, from French.
サイズアップ|Passer à la taille supérieure pour un petit supplément.|Go up one size for a small extra charge.
ホット|Chaud. Souvent en face de アイス sur la carte, avec deux prix.|Hot. Often paired with アイス on the board, with two prices.
アイス|Glacé, version froide d’une boisson. Seul, ça peut aussi vouloir dire glace (アイスクリーム).|Iced, the cold version of a drink. On its own it can also mean ice cream.
季節限定|« Limité à la saison » : produit qui ne reste que quelques semaines, comme les marrons en automne.|“Limited to the season”: on sale only for a few weeks, like chestnut in autumn.
期間限定|« Pour une période limitée » : offre temporaire.|“For a limited period”: a temporary item.
ケーキ|Gâteau, de l’anglais cake. Dans une pâtisserie, on choisit les parts dans la vitrine.|Cake. In a pastry shop you pick slices from the display case.
洋菓子|« Douceurs occidentales » : 洋 l’Occident, 菓子 friandise. L’opposé de 和菓子.|“Western sweets”: 洋 the West, 菓子 sweets. The opposite of 和菓子.
焼き菓子|« Douceurs cuites au four » : madeleines, financiers, biscuits, souvent en sachet cadeau.|“Baked sweets”: madeleines, financiers, cookies, often sold in gift bags.
ドリンク|« Drinks » : boissons.|“Drinks”.
苺|Fraise. Souvent écrit en hiragana いちご ; la fraise est la reine des gâteaux japonais.|Strawberry. Often written いちご in hiragana; the star of Japanese cakes.
ショートケーキ|Génoise légère, chantilly et fraises entières. Le gâteau japonais par excellence.|Light sponge, whipped cream and whole strawberries. The classic Japanese cake.
苺タルト|Tarte à la crème pâtissière couverte de fraises.|A custard tart covered with strawberries.
苺パフェ|Grande coupe en couches avec fraises, glace, crème et biscuits.|A tall layered glass of strawberries, ice cream, cream and crumbs.
フルーツタルト|Tarte à la crème couverte de fruits de saison.|A custard tart topped with seasonal fruit.
モンブラン|Crème de marrons en vermicelles sur une base meringue ou génoise.|Chestnut cream piped in strands over meringue or sponge.
和栗のモンブラン|Mont-blanc aux marrons japonais, plus parfumés : un classique d’automne.|Mont Blanc made with Japanese chestnuts, more fragrant: an autumn favourite.
チーズケーキ|Cheesecake, cuit, léger « soufflé » ou cru.|Cheesecake, baked, light soufflé-style or no-bake.
ガトーショコラ|Gâteau au chocolat dense, du français.|A dense chocolate cake, from French.
シュークリーム|Chou à la crème, du français « chou à la crème ».|A cream puff, from French chou à la crème.
エクレア|Éclair au chocolat.|A chocolate éclair.
ロールケーキ|Génoise roulée autour de crème fouettée.|Sponge rolled around whipped cream.
ミルフィーユ|Mille-feuille. ィ et ュ sont petits : mi-ru-fī-yu.|Mille-feuille. Small ィ and ュ: mi-ru-fī-yu.
ミルクレープ|Gâteau fait de fines crêpes empilées avec de la crème.|A cake of thin crêpes stacked with cream.
プリン|Crème caramel, de l’anglais pudding. Très populaire au Japon.|Custard pudding with caramel. Hugely popular in Japan.
ティラミス|Tiramisu au mascarpone et café.|Tiramisu with mascarpone and coffee.
マカロン|Macaron à la française.|A French-style macaron.
マドレーヌ|Madeleine.|A madeleine.
フィナンシェ|Financier aux amandes et beurre noisette.|An almond financier with browned butter.
カヌレ|Cannelé bordelais, croûte caramélisée.|A canelé from Bordeaux with a caramelised crust.
クッキー|Biscuits, souvent en sachet ou en boîte.|Cookies, often in bags or tins.
バウムクーヘン|Gâteau allemand cuit en couches sur une broche : des cernes comme un arbre. Cadeau classique.|A German cake baked in layers on a spit, ringed like a tree. A classic gift.
オレンジジュース|Jus d’orange.|Orange juice.
テイクアウト|À emporter, de l’anglais take out. Plus courant que お持ち帰り dans les chaînes.|Takeaway, from English take out. More common than お持ち帰り in chains.
イートイン|Sur place, de l’anglais eat in.|Eat in, from English.
店内でお召し上がりですか|Question au comptoir : « Vous consommez sur place ? ». お召し上がり est le verbe manger en langage respectueux (sonkeigo) : le personnel l’emploie pour le client, mais le client n’a jamais à le dire, seulement à le reconnaître.|Asked at the counter: “For here?”. お召し上がり is the respectful (sonkeigo) verb for eating: staff use it about the customer, who never needs to say it, only to recognise it.
こちらでお召し上がりですか|« Vous mangez ici ? » La question classique au comptoir, souvent suivie de お持ち帰りですか.|“Will you eat here?” The classic counter question, often followed by お持ち帰りですか.
お持ち帰りですか|« Ou c’est à emporter ? » La deuxième moitié de la question du comptoir.|“Or is it to take away?” The second half of the counter question.
テイクアウトで|Réponse : « À emporter ».|Answer: “To go”.
店内で|Réponse : « Sur place ».|Answer: “For here”.
ホットとアイスどちらになさいますか|« Chaud ou glacé, lequel prendrez-vous ? » Question très fréquente au comptoir.|“Hot or iced, which would you like?” A very common counter question.
アイスで|Réponse : « Glacé ».|Answer: “Iced”.
ホットで|Réponse : « Chaud ».|Answer: “Hot”.
# --- konbini
コンビニ|Supérette ouverte jour et nuit : repas, boissons, timbres, colis, factures. On en trouve à chaque coin de rue.|A shop open day and night: meals, drinks, stamps, parcels, bills. There is one on every corner.
ホットスナック|Les fritures gardées au chaud près de la caisse : on les demande au vendeur.|The fried snacks kept warm by the till: you ask the clerk for them.
フライドチキン|Morceau de poulet pané et frit, vendu à l’unité près de la caisse.|A piece of breaded fried chicken, sold one at a time by the till.
アメリカンドッグ|Saucisse enrobée de pâte sucrée et frite, sur un bâton. On ajoute ketchup et moutarde.|A sausage in sweet batter, fried on a stick. Add ketchup and mustard.
コロッケ|Croquette panée de purée de pomme de terre et de viande hachée, du français « croquette ».|A breaded croquette of mashed potato and minced meat, from French “croquette”.
フランクフルト|Grosse saucisse grillée sur un bâton.|A big grilled sausage on a stick.
フライドポテト|Frites, souvent servies dans un petit gobelet.|French fries, often in a small cup.
中華まん|« Brioche chinoise » : brioches à la vapeur gardées dans une vitrine chauffante en hiver.|“Chinese bun”: steamed buns kept in a heated case in winter.
肉まん|Brioche vapeur farcie de porc haché et d’oignon. Le classique de l’hiver.|A steamed bun filled with minced pork and onion. The winter classic.
あんまん|Brioche vapeur à la pâte de haricots rouges sucrée.|A steamed bun with sweet red bean paste.
ピザまん|Brioche vapeur à la tomate et au fromage, souvent teintée en orange.|A steamed bun with tomato and cheese, often tinted orange.
カレーまん|Brioche vapeur au curry japonais, souvent teintée en jaune.|A steamed bun with Japanese curry, often tinted yellow.
おにぎり|Boule ou triangle de riz garni, enveloppé de nori. L’emballage s’ouvre en trois tirettes numérotées.|A ball or triangle of rice with a filling, wrapped in nori. The wrapper opens with three numbered tabs.
梅|Prune japonaise salée et acide (umeboshi), garniture classique de l’onigiri.|A salty, sour Japanese plum (umeboshi), a classic onigiri filling.
昆布|Algue kombu, mijotée sucrée-salée dans l’onigiri, ou nouée dans l’oden.|Kelp, simmered sweet and salty in onigiri, or tied in a knot in oden.
ツナマヨ|Thon et mayonnaise : la garniture d’onigiri la plus vendue.|Tuna and mayonnaise: the best-selling onigiri filling.
赤飯|Riz gluant cuit avec des haricots azuki, qui le teintent de rose. Plat de fête.|Sticky rice cooked with azuki beans, which tint it pink. A festive dish.
弁当|Repas complet en boîte : riz, plat et petits accompagnements. On vous propose de le réchauffer.|A full meal in a box: rice, a main and small sides. The clerk offers to heat it up.
幕の内弁当|Bentō assorti à petites portions variées, né pour les entractes (幕の内) du théâtre.|An assorted bento of small varied portions, born for theatre intermissions (幕の内).
のり弁|Riz recouvert de nori, avec poisson pané et chikuwa frit. Le bentō le moins cher.|Rice covered in nori, with breaded fish and fried chikuwa. The cheapest bento.
唐揚げ弁当|Bentō au poulet frit, avec riz et petit accompagnement.|A fried chicken bento with rice and a small side.
生姜焼き弁当|Bentō au porc sauté au gingembre et à la sauce soja.|A bento of pork stir-fried with ginger and soy sauce.
ハンバーグ弁当|Bentō au steak haché nappé de sauce.|A bento with a hamburg steak in sauce.
カップ麺|Nouilles instantanées en pot : on ajoute l’eau chaude de la bouilloire près de la caisse.|Instant noodles in a cup: add hot water from the kettle by the till.
おでん|Pot-au-feu au dashi : on choisit ses morceaux dans le bac près de la caisse, d’octobre à mars surtout.|A dashi stew: you pick your pieces from the tray by the till, mostly from October to March.
大根|Grosse rondelle de radis blanc qui a longuement mijoté dans le bouillon. La star de l’oden.|A thick round of white radish simmered long in the broth. The star of oden.
ちくわ|Tube de pâte de poisson grillée, creux au milieu.|A tube of grilled fish paste, hollow in the middle.
はんぺん|Galette blanche de poisson et d’igname, légère comme une guimauve.|A white cake of fish and yam, light as a marshmallow.
こんにゃく|Gelée ferme de konjac, sans goût mais qui prend celui du bouillon.|A firm konjac jelly, tasteless but soaking up the broth.
牛すじ|Tendons de bœuf sur un pique, fondants après mijotage.|Beef tendon on a skewer, melting after simmering.
ドリンク|« Drink » : rubrique des boissons.|“Drink”: the drinks section.
ミネラルウォーター|Eau minérale en bouteille.|Bottled mineral water.
ホットコーヒー|Café chaud, souvent servi par une machine en libre-service après paiement.|Hot coffee, often from a self-service machine once you’ve paid.
缶コーヒー|Café en canette, vendu chaud en hiver et froid en été.|Canned coffee, sold hot in winter and cold in summer.
野菜ジュース|Jus de légumes mélangés, souvent avec des fruits.|Mixed vegetable juice, often with fruit.
缶ビール|Bière en canette. Taxée à 10 % comme tout alcool.|Canned beer. Taxed at 10% like all alcohol.
缶チューハイ|Alcool de base (shōchū) et soda aux fruits, en canette.|Shōchū with fruit soda, in a can.
エナジードリンク|Boisson énergisante.|Energy drink.
スイーツ|« Sweets » : rayon des desserts frais.|“Sweets”: the chilled desserts shelf.
レジ袋|Sac en plastique, payant depuis 2020 : quelques yens, taxés à 10 %.|A plastic bag, charged since 2020: a few yen, taxed at 10%.
レジ|La caisse, de l’anglais « register ».|The till, from English “register”.
領収証|Reçu officiel. En haut du ticket ; on peut aussi demander un 領収書 nominatif.|An official receipt. At the top of the ticket; you can also ask for a named 領収書.
小計|Sous-total avant remises et taxes.|Subtotal, before discounts and tax.
合計|Total à payer, imprimé en grand.|The total to pay, printed large.
値引|Remise : apparaît sous un article soldé, avec le montant en négatif.|Discount: shows under a marked-down item, with a negative amount.
現金|Espèces.|Cash.
お預り|La somme que vous avez tendue, « reçue en dépôt ».|The money you handed over, “received in trust”.
お釣り|La monnaie rendue.|Your change.
消費税|Taxe sur la consommation : 10 %, ou 8 % pour la nourriture à emporter. Déjà incluse dans les prix.|Consumption tax: 10%, or 8% for take-away food. Already in the prices.
軽減税率|Taux réduit de 8 % pour la nourriture à emporter. Les articles concernés portent une marque ※ ou 軽.|The reduced 8% rate for take-away food. Items under it carry a ※ or 軽 mark.
電子マネー|Paiement sans contact par carte IC ou téléphone.|Contactless payment by IC card or phone.
電話|Téléphone : le numéro du magasin, sous son nom.|Phone: the shop’s number, under its name.
担当|L’employé qui a tenu la caisse, souvent par un numéro.|The clerk who ran the till, often by a number.
駅前店|« Magasin devant la gare » : les chaînes nomment chaque magasin par son quartier.|“In front of the station”: chains name each shop after its spot.
東口店|« Magasin de la sortie est » d’une gare.|“East exit branch” of a station.
中央店|« Magasin du centre ».|“Central branch”.
揚げたて|« Tout juste frit » : sur les affichettes près des fritures.|“Freshly fried”: on the cards next to the fried food.
新発売|« Nouvelle sortie » : produit qui vient d’arriver en rayon.|“Newly released”: a product just on the shelves.
全品|« Tous les articles » : 全品70円 veut dire que tout est à 70 yens.|“All items”: 全品70円 means everything is 70 yen.
割引|Réduction, souvent en pourcentage : 10%割引.|A discount, often in percent: 10%割引.
半額|Moitié prix : l’étiquette collée le soir sur les bentō et plats du jour.|Half price: the sticker put on bento and daily dishes in the evening.
はじめました|« On a commencé » : annonce qu’un produit de saison est de nouveau servi, comme 冷やし中華はじめました en été.|“We’ve started”: announces a seasonal item is being served again, like 冷やし中華はじめました in summer.
温めますか|« Je vous le réchauffe ? » : on vous le demande pour les bentō et les plats.|“Shall I heat it up?”: asked for bento and ready meals.
お願いします|« S’il vous plaît » : pour dire oui à une proposition.|“Please”: to say yes to an offer.
大丈夫です|« Ça ira » : la façon polie de dire non merci.|“I’m fine”: the polite way to say no thanks.
お箸おつけしますか|« Je vous mets des baguettes ? »|“Shall I add chopsticks?”
袋はご利用ですか|« Vous utiliserez un sac ? » Le sac est payant.|“Will you use a bag?” Bags cost extra.
ポイントカードはお持ちですか|« Avez-vous une carte de fidélité ? » On répond souvent 大丈夫です.|“Do you have a point card?” People often answer 大丈夫です.
以上でよろしいですか|« Ce sera tout ? »|“Will that be all?”
はい|Oui.|Yes.
# --- kissaten / kanmi
珈琲|Café filtre, souvent torréfié foncé dans les cafés rétro.|Drip coffee, usually dark-roasted in retro cafés.
紅茶|Thé noir, servi avec lait ou citron.|Black tea, with milk or lemon.
抹茶|Thé vert en poudre fouetté, mousseux et un peu amer.|Powdered green tea whisked until frothy, slightly bitter.
牛乳|Lait.|Milk.
果汁|Jus de fruits, souvent orange ou pomme.|Fruit juice, usually orange or apple.
ナポリタン|Spaghetti sautés au ketchup avec saucisse, oignon et poivron. Une invention japonaise des cafés.|Spaghetti fried with ketchup, sausage, onion and pepper. A Japanese café invention.
玉子サンド|Sandwich de pain de mie très moelleux, garni d’œufs à la mayonnaise ou d’omelette épaisse.|A soft white-bread sandwich filled with egg mayonnaise or a thick omelette.
珈琲ゼリー|Gelée de café servie avec de la crème.|Coffee jelly served with cream.
ホットケーキ|Pancakes épais avec beurre et sirop.|Thick pancakes with butter and syrup.
クリームソーダ|Soda vert au melon surmonté d’une boule de glace vanille.|Green melon soda topped with a scoop of vanilla ice cream.
餡蜜|Cubes de gelée d’agar, fruits, pâte de haricots rouges, arrosés de sirop de sucre noir.|Agar jelly cubes, fruit and sweet red bean paste, with black sugar syrup.
善哉|Soupe chaude de haricots rouges sucrés avec des boulettes de mochi.|A hot sweet red bean soup with mochi dumplings.
白玉|Petites boulettes de farine de riz gluant, lisses et élastiques.|Small glutinous rice flour dumplings, smooth and chewy.
団子|Boulettes de riz gluant en brochette, nappées de sauce sucrée-salée ou de pâte de haricots.|Rice dumplings on a skewer, with sweet soy glaze or bean paste.
草餅|Mochi vert parfumé à l’armoise, fourré de pâte de haricots rouges. Un goût de printemps.|Green mochi flavoured with mugwort and filled with red bean paste. A taste of spring.
宇治金時|Glace pilée au sirop de thé vert matcha (Uji) et haricots rouges sucrés.|Shaved ice with matcha syrup from Uji and sweet red beans.
氷|Glace pilée arrosée de sirop. Le drapeau 氷 devant une boutique annonce l’été.|Shaved ice with syrup. A 氷 flag outside a shop means summer.
葛切り|Nouilles translucides d’amidon de kuzu, trempées dans un sirop de sucre noir. Spécialité de Kyōto.|Translucent kudzu-starch noodles dipped in black sugar syrup. A Kyoto speciality.
# --- okonomiyaki
お好み焼|Galette de pâte et de chou cuite sur plaque, garnie au choix, nappée de sauce, mayonnaise et bonite.|A batter and cabbage pancake cooked on a griddle, filled to taste and topped with sauce, mayo and bonito.
豚玉|Okonomiyaki au porc, le plus classique.|Okonomiyaki with pork, the classic.
烏賊玉|Okonomiyaki au calmar.|Okonomiyaki with squid.
葱焼|Galette très garnie de ciboule, servie avec sauce soja et citron.|A pancake packed with scallion, served with soy and lemon.
焼蕎麦|Nouilles de blé sautées sur la plaque avec chou, porc et sauce épaisse.|Wheat noodles fried on the griddle with cabbage, pork and thick sauce.
蛸焼|Boulettes de pâte avec un morceau de poulpe, cuites dans une plaque à alvéoles. Spécialité d’Ōsaka.|Batter balls with a piece of octopus, cooked in a dimpled pan. An Osaka speciality.
モダン焼|Okonomiyaki avec une couche de nouilles sautées dedans.|Okonomiyaki with a layer of fried noodles inside.
もんじゃ焼|Pâte très liquide cuite sur la plaque et mangée avec une petite spatule. Spécialité de Tsukishima à Tōkyō.|A runny batter cooked on the griddle and eaten with a tiny spatula. From Tsukishima in Tokyo.
鉄板焼|Viandes, fruits de mer et légumes cuits devant vous sur une plaque.|Meat, seafood and vegetables cooked in front of you on a griddle.
# --- régions
成吉思汗|Mouton grillé sur un dôme en fonte avec des légumes. Spécialité d’Hokkaidō.|Mutton grilled on a domed iron pan with vegetables. A Hokkaido speciality.
帆立焼|Saint-Jacques grillées dans leur coquille avec beurre et soja.|Scallops grilled in the shell with butter and soy.
蟹|Crabe, souvent servi bouilli ou en ragoût en hiver.|Crab, usually boiled or in hotpot in winter.
石狩鍋|Ragoût de saumon, chou et tofu dans un bouillon au miso. Hokkaidō.|Salmon, cabbage and tofu hotpot in miso broth. Hokkaido.
いくら丼|Riz couvert d’œufs de saumon marinés, qui éclatent sous la dent.|Rice covered with marinated salmon roe that pops in the mouth.
麦飯|Riz cuit avec de l’orge, souvent servi avec de l’igname râpée.|Rice cooked with barley, often served with grated yam.
きりたんぽ鍋|Bâtonnets de riz grillés en ragoût de poulet. Akita.|Grilled rice sticks in a chicken hotpot. Akita.
芋煮|Ragoût de taro et de bœuf cuisiné en plein air à l’automne. Yamagata.|Taro and beef stew cooked outdoors in autumn. Yamagata.
冷麺|Nouilles élastiques dans un bouillon froid avec kimchi et fruit. Morioka.|Chewy noodles in a cold broth with kimchi and fruit. Morioka.
わんこ蕎麦|Petites bouchées de soba qu’on vous resert sans arrêt jusqu’à ce que vous couvriez le bol. Iwate.|Small mouthfuls of soba refilled nonstop until you cover your bowl. Iwate.
深川飯|Riz ou bouillon aux palourdes et miso, plat des pêcheurs de Tōkyō.|Rice or broth with clams and miso, the Tokyo fishermen’s dish.
鰻重|Anguille grillée sur du riz dans une boîte laquée, plus chic que le donburi.|Grilled eel over rice in a lacquered box, smarter than a donburi.
天麩羅|Tempura, écrit avec ses kanji d’origine.|Tempura, written with its old kanji.
味噌カツ|Porc pané nappé d’une sauce au miso rouge. Nagoya.|Breaded pork with red miso sauce. Nagoya.
櫃まぶし|Anguille sur riz qu’on mange en trois temps : nature, avec condiments, puis en bouillon. Nagoya.|Eel on rice eaten three ways: plain, with condiments, then with broth. Nagoya.
きしめん|Nouilles de blé larges et plates en bouillon. Nagoya.|Wide, flat wheat noodles in broth. Nagoya.
味噌煮込み饂飩|Udon fermes mijotées dans un pot en terre au miso rouge. Nagoya.|Firm udon simmered in red miso in a clay pot. Nagoya.
天むす|Petite boulette de riz avec une crevette tempura dedans. Nagoya.|A small rice ball with a shrimp tempura inside. Nagoya.
湯豆腐|Tofu chauffé dans un bouillon d’algue kombu, à tremper dans une sauce. Kyōto.|Tofu warmed in kombu broth and dipped in sauce. Kyoto.
湯葉|Fine peau qui se forme sur le lait de soja chauffé, servie fraîche ou séchée. Kyōto.|The thin skin that forms on heated soy milk, eaten fresh or dried. Kyoto.
鯖寿司|Maquereau mariné pressé sur du riz vinaigré et coupé en tranches. Kyōto.|Cured mackerel pressed on vinegared rice and cut into slices. Kyoto.
鰊蕎麦|Soba chaudes avec un hareng séché mijoté sucré. Kyōto.|Hot soba with a sweet simmered dried herring. Kyoto.
京漬物|Légumes saumurés de Kyōto, fins et peu salés.|Kyoto pickled vegetables, delicate and lightly salted.
肉吸い|Le bouillon d’une udon au bœuf, sans les nouilles. Ōsaka.|The broth of beef udon without the noodles. Osaka.
土手焼|Tendons de bœuf mijotés longuement au miso. Ōsaka.|Beef tendon slow-simmered in miso. Osaka.
牡蠣フライ|Huîtres panées et frites, servies avec sauce tartare.|Breaded fried oysters with tartar sauce.
焼牡蠣|Huîtres grillées dans leur coquille. Hiroshima.|Oysters grilled in the shell. Hiroshima.
穴子飯|Congre grillé sur du riz. Miyajima.|Grilled sea eel over rice. Miyajima.
汁なし担々麺|Nouilles au sésame et poivre du Sichuan sans bouillon, à bien mélanger. Hiroshima.|Brothless noodles with sesame and Sichuan pepper, mixed well. Hiroshima.
讃岐饂飩|Udon très fermes et élastiques de Kagawa.|Very firm, springy udon from Kagawa.
釜玉|Udon chaudes juste égouttées, mélangées à un œuf cru et un peu de soja.|Hot udon straight from the pot, tossed with a raw egg and a little soy.
骨付鳥|Cuisse de poulet rôtie entière, à l’ail et au poivre. Kagawa.|A whole roasted chicken leg with garlic and pepper. Kagawa.
もつ鍋|Ragoût de tripes de bœuf, chou et ciboulette à l’ail. Fukuoka.|Beef offal hotpot with cabbage, chives and garlic. Fukuoka.
明太子|Œufs de colin marinés au piment. Fukuoka.|Pollock roe marinated with chili. Fukuoka.
水炊き|Poulet mijoté dans un bouillon blanc, à tremper dans une sauce aux agrumes. Fukuoka.|Chicken simmered in a white broth, dipped in citrus sauce. Fukuoka.
胡麻鯖|Maquereau cru très frais dans une sauce au sésame. Fukuoka.|Very fresh raw mackerel in sesame sauce. Fukuoka.
ゴーヤチャンプルー|Sauté de melon amer, tofu, œuf et porc. Okinawa.|Stir-fry of bitter melon, tofu, egg and pork. Okinawa.
沖縄蕎麦|Nouilles de blé épaisses dans un bouillon porc et bonite, sans sarrasin. Okinawa.|Thick wheat noodles in pork and bonito broth, no buckwheat. Okinawa.
ソーキ蕎麦|Nouilles d’Okinawa avec des côtes de porc mijotées.|Okinawa noodles with simmered pork ribs.
角煮|Gros cubes de poitrine de porc mijotés longuement sucré-salé.|Thick cubes of pork belly slow-braised sweet and savoury.
海葡萄|Algue en petites grappes qui éclatent comme du caviar. Okinawa.|Seaweed in tiny clusters that pop like caviar. Okinawa.
泡盛|Alcool distillé de riz d’Okinawa, fort et parfois vieilli des années.|Okinawa’s distilled rice spirit, strong and sometimes aged for years.
煎茶|Thé vert en feuilles infusé, le thé de tous les jours.|Steeped leaf green tea, the everyday tea.
# --- saké
純米酒|Saké fait seulement de riz, d’eau et de koji, sans alcool ajouté. Goût plein.|Sake made only from rice, water and koji, with no added alcohol. Full-bodied.
純米吟醸|Saké pur riz dont les grains sont polis à 60 % ou moins. Parfumé et fruité.|Pure rice sake from grains polished to 60% or less. Fragrant and fruity.
大吟醸|Saké au riz poli à 50 % ou moins, le plus fin et le plus aromatique.|Sake from rice polished to 50% or less, the finest and most aromatic.
本醸造|Saké avec une petite part d’alcool ajouté, plus léger et sec. Bon chaud.|Sake with a little added alcohol, lighter and drier. Good warm.
生酒|Saké non pasteurisé, vif et frais. À garder au froid.|Unpasteurised sake, lively and fresh. Keep it cold.
原酒|Saké non coupé d’eau, autour de 18–20°.|Undiluted sake, around 18–20%.
濁り酒|Saké laiteux où restent des particules de riz. Doux et épais.|Milky sake with rice solids left in. Sweet and thick.
地酒|Saké d’une brasserie locale de la région.|Sake from a local regional brewery.
お猪口|Petite coupe en céramique pour le saké. On sert les autres, jamais soi-même.|A small ceramic sake cup. You pour for others, never for yourself.
徳利|Carafe à col étroit pour servir le saké, chaud ou froid.|A narrow-necked flask for serving sake, warm or cold.
升|Boîte carrée en bois de cèdre, ancienne mesure. On y pose parfois le verre qu’on fait déborder.|A square cedar box, an old measure. A glass is sometimes set in it and overfilled.
冷や|Saké à température ambiante. Attention : ce n’est pas « froid ».|Sake at room temperature. Careful: it does not mean chilled.
ぬる燗|Saké tiède, autour de 40 °C, qui fait ressortir le riz.|Lukewarm sake around 40 °C, which brings out the rice.
お通し|Petit plat servi d’office en arrivant à l’izakaya et facturé, comme un droit de table.|A small dish served automatically when you sit at an izakaya and charged like a cover fee.
板わさ|Tranches de kamaboko (pâté de poisson) avec du wasabi et de la sauce soja.|Slices of kamaboko fish cake with wasabi and soy sauce.
炙りえいひれ|Nageoire de raie séchée, grillée, à tremper dans la mayonnaise au piment. Parfait avec le saké.|Dried stingray fin, toasted and dipped in chili mayo. Made for sake.
""")

# Shop signs: what the words of a restaurant's name mean (type word or the shop's own name)

add("""
# --- notices posted in the shop
営業中|Pancarte accrochée à la porte : on peut entrer. Souvent sur un panneau en bois réversible.|Sign hung on the door: you can come in. Often a reversible wooden board.
準備中|Le revers de 営業中 : le service n’a pas commencé, ou c’est la pause entre midi et soir.|The back of 営業中: service hasn’t started, or it’s the break between lunch and dinner.
本日休業|« Aujourd’hui, fermé » : 本日 aujourd’hui, 休業 relâche.|“Closed today”: 本日 today, 休業 suspension of business.
定休日|Le jour où le restaurant ferme chaque semaine, souvent suivi du jour : 定休日 月曜.|The day the restaurant closes every week, often followed by the day: 定休日 月曜.
営業時間|Suivi des heures : 11:00〜15:00 pour le midi, 17:00〜 pour le soir.|Followed by the hours: 11:00–15:00 for lunch, 17:00– for dinner.
満席|« Places pleines » : posé à l’entrée quand on ne peut plus vous asseoir.|“Seats full”: put at the entrance when there’s no room left.
禁煙|禁 interdit, 煙 fumée. Presque partout aujourd’hui.|禁 forbidden, 煙 smoke. Nearly everywhere today.
全席禁煙|全席 toutes les places : aucune table fumeur.|全席 every seat: no smoking table at all.
喫煙席|喫煙 fumer, 席 place. De plus en plus rare, parfois une petite pièce à part.|喫煙 smoking, 席 seat. Increasingly rare, sometimes a small separate room.
現金のみ|« Espèces seulement » : fréquent dans les petites échoppes. のみ veut dire « uniquement ».|“Cash only”: common in small places. のみ means “only”.
食券|On l’achète au distributeur à l’entrée, puis on le tend au comptoir. Courant pour les rāmen, soba et gyūdon.|Bought at the machine by the door, then handed over at the counter. Common for ramen, soba and gyudon.
券売機|La machine à tickets : on choisit le plat, on paie, le ticket tombe.|The ticket machine: pick the dish, pay, the ticket drops out.
食券制|« Système de tickets » : on ne commande pas à table, on passe par le distributeur.|“Ticket system”: no ordering at the table, you go through the machine.
お持ち帰り|« Emporter » en version polie. Le contraire est 店内, sur place.|Polite “takeaway”. The opposite is 店内, eat in.
店内|店 boutique, 内 dedans. À la caisse on vous demande 店内 ou お持ち帰り.|店 shop, 内 inside. At the till you’re asked 店内 or お持ち帰り.
予約席|Petit chevalet posé sur une table : elle est déjà prise.|Small stand on a table: it’s already taken.
ご予約|ご rend le mot poli. ご予約の方 : « les personnes qui ont réservé ».|ご makes the word polite. ご予約の方: “guests with a booking”.
お一人様|Façon polie de dire « une personne ». お一人様歓迎 : les clients seuls sont bienvenus.|Polite way to say “one person”. お一人様歓迎: solo diners welcome.
お手洗い|« Se laver les mains » : le mot poli pour les toilettes. On voit aussi トイレ.|“Hand washing”: the polite word for the toilet. You also see トイレ.
お会計|L’addition. On le dit au personnel, ou on le lit au-dessus de la caisse.|The bill. You say it to the staff, or read it above the till.
ご注文|La commande. ご注文はお決まりですか : « avez-vous choisi ? »|The order. ご注文はお決まりですか: “are you ready to order?”
お冷|L’eau fraîche servie d’office et gratuite. Mot de restaurant, on ne dit pas お水 au comptoir d’un ancien.|The cold water served automatically and free. A restaurant word.
お冷はセルフ|« L’eau, c’est self » : une carafe et des verres sont posés quelque part, on se sert soi-même.|“Water is self-service”: a jug and glasses are set out somewhere, help yourself.
ご自由にどうぞ|À côté des condiments ou de l’ail : servez-vous autant que vous voulez.|Next to condiments or garlic: take as much as you like.
ラストオーダー|Heure de la dernière commande, souvent 30 minutes avant la fermeture. Abrégé L.O.|Time of last orders, often 30 minutes before closing. Shortened to L.O.
# --- what is said
いらっしゃいませ|Lancé par tout le personnel quand on entre. On ne répond pas, un petit signe de tête suffit.|Called out by all the staff when you walk in. No need to answer, a small nod is enough.
何名様ですか|La première question : combien êtes-vous ? On peut répondre en montrant les doigts.|The first question: how many of you? You can answer by holding up fingers.
二人です|二人 deux personnes. Attention : 一人 ひとり, 二人 ふたり, puis 三人 さんにん.|二人 two people. Careful: 一人 hitori, 二人 futari, then 三人 sannin.
一人です|一人 une personne : ひとり, lecture irrégulière.|一人 one person: hitori, an irregular reading.
こちらへどうぞ|こちら par ici, どうぞ je vous en prie. On suit la personne jusqu’à la table.|こちら this way, どうぞ please. Follow them to the table.
お決まりですか|Version courte de ご注文はお決まりですか : « vous avez choisi ? »|Short for ご注文はお決まりですか: “have you decided?”
すみません|Pour appeler le personnel, à voix haute, main levée. Au Japon, c’est normal.|To call the staff, out loud with a hand raised. Perfectly normal in Japan.
ください|Se colle après ce qu’on veut avec を : ラーメンをください. Ajouter un nombre : ビールを二つください.|Goes after what you want, with を: ラーメンをください. Add a number: ビールを二つください.
おすすめは何ですか|おすすめ recommandation, 何 quoi. Réponse fréquente : la rubrique 本日のおすすめ.|おすすめ recommendation, 何 what. Common answer: the 本日のおすすめ section.
これは何ですか|これ ceci. Pratique en montrant la carte du doigt.|これ this. Handy while pointing at the menu.
以上です|« C’est tout » : pour finir sa commande. Le serveur répète souvent la liste.|“That’s all”: to close your order. The server often repeats the list.
少々お待ちください|少々 un petit peu, お待ちください veuillez attendre. Réponse classique du personnel.|少々 a little, お待ちください please wait. The staff’s standard reply.
お待たせしました|Dit en posant le plat, même s’il est arrivé vite.|Said while setting down the dish, even if it came fast.
ごゆっくりどうぞ|« Prenez votre temps » : dit après avoir tout servi.|“Take your time”: said once everything is served.
いただきます|Mains jointes, avant la première bouchée : « je reçois ». On le dit pour soi.|Hands together, before the first bite: “I humbly receive”. Said to yourself.
美味しい|Se dit pendant le repas, aussi en kana おいしい. Au comptoir, ça fait plaisir au cuisinier.|Said during the meal, also written おいしい. At the counter, the cook will be pleased.
お水ください|Si l’eau n’est pas servie. Dans un restaurant, on peut aussi dire お冷ください.|If water isn’t served. In a restaurant you can also say お冷ください.
持ち帰りで|« À emporter » en commandant. Pour manger sur place : 店内で.|“To go” when ordering. To eat in: 店内で.
お会計お願いします|L’addition, s’il vous plaît. Souvent on paie à la caisse près de la porte, pas à table.|The bill, please. You usually pay at the till by the door, not at the table.
別々で|Pour payer chacun sa part. Pas toujours accepté aux heures de pointe.|To pay separately. Not always accepted at rush hour.
カードで|« Par carte ». Si on vous répond 現金のみ, c’est espèces seulement.|“By card”. If the answer is 現金のみ, it’s cash only.
ごちそうさまでした|Dit en partant ou en reposant les baguettes : merci pour ce festin.|Said when leaving or putting down your chopsticks: thanks for the feast.
ありがとうございました|Le merci du personnel quand vous partez, au passé : « merci d’être venus ».|The staff’s thanks as you leave, in the past: “thank you for coming”.
またお越しください|« Revenez » : souvent lancé juste après ありがとうございました.|“Come again”: often called out right after ありがとうございました.
かき氷|Glace pilée arrosée de sirop, le dessert de l’été. Le fanion 氷 (glace) devant la boutique annonce qu’on en sert.|Shaved ice drenched in syrup, the summer dessert. A 氷 (ice) banner outside means the shop serves it.
味|« Goût ». Après un nom, 〜味 indique le parfum : レモン味, parfum citron.|“Taste”. After a noun, 〜味 gives the flavour: レモン味, lemon flavour.
レモン味|Sirop au citron, acidulé et jaune pâle.|Lemon syrup, tangy and pale yellow.
いちご味|Sirop à la fraise, rouge vif : le parfum le plus demandé.|Strawberry syrup, bright red: the most popular flavour.
メロン味|Sirop au melon, d’un vert éclatant.|Melon syrup, a vivid green.
抹茶味|Sirop au matcha, plus amer et moins sucré. Avec des haricots rouges, cela devient un 宇治金時.|Matcha syrup, more bitter and less sweet. With red beans it becomes 宇治金時.
練乳|Lait concentré sucré versé par-dessus, en supplément ou déjà compris.|Sweetened condensed milk poured on top, as an extra or included.
売り切れなんです|« C’est épuisé, désolé ». 売り切れ : vendu jusqu’au dernier ; 〜なんです adoucit en expliquant. Souvent précédé d’un すみません. Plus formel : 申し訳ございません、売り切れてしまいました.|“It’s sold out, sorry”. 売り切れ: sold to the last one; 〜なんです softens it as an explanation. Usually after a すみません. More formal: 申し訳ございません、売り切れてしまいました.
じゃあ|« Alors, dans ce cas » : pour changer d’avis ou se rabattre sur autre chose.|“Well then”: to change your mind or settle for something else.
溶けないうちにどうぞ|« À déguster avant que ça fonde », en servant une glace pilée. 〜ないうちに : avant que… ne.|“Enjoy it before it melts”, said when serving shaved ice. 〜ないうちに: before it starts to….
温かいうちにどうぞ|« Prenez-le tant que c’est chaud », en servant un plat qui sort du feu.|“Have it while it’s hot”, said when serving a dish fresh from the stove.
""")

NX = {}
for line in """
居酒屋|« Maison où l’on reste boire » : 居 rester, 酒 alcool, 屋 boutique. Bistrot japonais où l’on boit et partage des petits plats.|“A shop where you stay to drink”: 居 stay, 酒 alcohol, 屋 shop. A Japanese pub where you drink and share small plates.
酒処|« Lieu du saké » : 処 veut dire endroit. Formule ancienne et chaleureuse pour un bar à saké.|“Place of sake”: 処 means place. An old, warm way to name a sake bar.
炉端|« Au bord du foyer » : le cuisinier grille devant vous et tend les plats sur une longue pelle en bois.|“By the hearth”: the cook grills in front of you and passes dishes on a long wooden paddle.
焼鳥|« Oiseau grillé » : brochettes de poulet au charbon. Le mot sert aussi de nom de boutique.|“Grilled bird”: chicken skewers over charcoal. The word doubles as a shop name.
炭火焼鳥|Yakitori « au feu de charbon » : 炭 charbon, 火 feu. Gage de qualité, souvent du binchōtan.|Yakitori “over charcoal fire”: 炭 charcoal, 火 fire. A sign of quality, often binchōtan.
鳥|« Oiseau » : ici, le poulet. Nom court typique des petites échoppes de yakitori.|“Bird”: here, chicken. A typical short name for small yakitori stalls.
麺屋|« Boutique de nouilles » : presque toujours un restaurant de ramen moderne.|“Noodle shop”: nearly always a modern ramen place.
らーめん|Ramen écrit en hiragana, avec un trait d’allongement : un air artisanal et familier.|Ramen written in hiragana with a long-vowel bar: a homely, artisanal feel.
中華そば|« Soba chinoises » : l’ancien nom des ramen. Annonce un bouillon de soja à l’ancienne.|“Chinese soba”: the old name for ramen. Promises an old-style soy broth.
手打ち蕎麦|« Soba coupées à la main » : la pâte est étalée et taillée sur place.|“Hand-cut soba”: the dough is rolled and cut on site.
そば処|« Lieu de soba », en hiragana pour un ton simple et accueillant.|“Place of soba”, in hiragana for a plain, friendly tone.
庵|« Ermitage » : suffixe classique des restaurants de soba, qui évoque le calme et la tradition.|“Hermitage”: a classic suffix for soba restaurants, evoking calm and tradition.
食堂|« Salle à manger » : cantine populaire aux menus simples et pas chers.|“Dining hall”: a cheap, no-frills local canteen.
定食|« Repas fixe » : un plateau complet avec riz, soupe miso, plat et pickles.|“Set meal”: a full tray with rice, miso soup, a main and pickles.
鮨|Sushi écrit avec 魚 poisson et 旨 délicieux : graphie élégante des comptoirs haut de gamme.|Sushi written with 魚 fish and 旨 delicious: the elegant spelling of upscale counters.
寿司処|« Lieu de sushi ». 寿司 est un jeu de kanji porte-bonheur : 寿 longévité, 司 diriger.|“Place of sushi”. 寿司 is a lucky kanji pun: 寿 long life, 司 to govern.
すし|Sushi en hiragana : ton décontracté, souvent un comptoir simple ou un kaiten.|Sushi in hiragana: casual, often a simple counter or conveyor belt place.
鮓|Graphie ancienne de sushi, du temps où le poisson était fermenté dans le riz.|An old spelling of sushi, from when fish was fermented in rice.
丼|« Bol » : un bol de riz garni. Le kanji représente un puits avec quelque chose dedans.|“Bowl”: a topped rice bowl. The kanji shows a well with something in it.
どんぶり|« Grand bol » écrit en entier, pour une enseigne ronde et populaire.|“Big bowl” spelled out, for a round, homely sign.
喫茶|« Boire le thé » : le café de quartier rétro, avec sandwichs et café filtre.|“Drinking tea”: the retro neighborhood café with sandwiches and drip coffee.
珈琲|Café écrit en kanji, choisis pour le son : un style rétro de l’ère Shōwa.|Coffee written in kanji picked for their sound: a retro Shōwa style.
純喫茶|« Café pur » : à l’origine sans alcool ni hôtesses, aujourd’hui synonyme de café vintage.|“Pure café”: first meant no alcohol or hostesses, now a byword for vintage cafés.
甘味処|« Lieu des douceurs » : salon de desserts japonais, anmitsu, dango, glace pilée.|“Place of sweets”: a Japanese dessert parlour, anmitsu, dango, shaved ice.
茶房|« Salle de thé » : salon de thé raffiné, souvent avec des douceurs.|“Tea room”: a refined tea salon, often with sweets.
茶屋|« Maison de thé » : halte traditionnelle où l’on boit un thé avec des dango.|“Tea house”: a traditional stop for tea and dango.
お好み焼|« Grillé comme vous l’aimez » : galette de chou garnie, cuite sur plaque.|“Grilled how you like it”: a cabbage pancake with toppings, cooked on a griddle.
鉄板焼|« Grillé sur plaque de fer » : cuisine sur une plaque chaude devant le client.|“Grilled on an iron plate”: cooking on a hot griddle in front of you.
酒場|« Lieu à alcool » : bar populaire et bon marché, souvent bruyant et chaleureux.|“Drinking place”: a cheap, lively, popular bar.
地酒処|« Lieu des sakés locaux » : 地 terre, région. On y boit des sakés des brasseries du coin.|“Place of local sake”: 地 land, region. Pours sake from nearby breweries.
一休|« Une pause ». C’est aussi Ikkyū, moine zen célèbre pour son humour.|“A short rest”. Also Ikkyū, a Zen monk famous for his wit.
大黒|Daikoku, dieu de la prospérité et de la cuisine, l’un des sept dieux du bonheur.|Daikoku, god of wealth and the kitchen, one of the Seven Lucky Gods.
福助|Fukusuke, poupée porte-bonheur qui salue les clients à l’entrée des boutiques.|Fukusuke, a lucky doll who bows to customers at shop doors.
宝|« Trésor ».|“Treasure”.
千鳥|« Mille oiseaux » : les pluviers en vol, motif classique des tissus japonais.|“A thousand birds”: plovers in flight, a classic Japanese textile pattern.
花月|« Fleur et lune » : la beauté des saisons.|“Flower and moon”: the beauty of the seasons.
日の出|« Lever du soleil » : un départ prospère.|“Sunrise”: a prosperous start.
富士|Le mont Fuji.|Mount Fuji.
満月|« Pleine lune ».|“Full moon”.
鶴亀|La grue et la tortue, symboles de longue vie.|Crane and turtle, symbols of long life.
竹|« Bambou ». Aussi le rang du milieu dans 松竹梅 (pin, bambou, prunier) sur les menus.|“Bamboo”. Also the middle grade in 松竹梅 (pine, bamboo, plum) on menus.
桜|« Cerisier ».|“Cherry blossom”.
縁|« Le lien » : les rencontres dues au destin, et le lien avec les clients.|“The bond”: fated encounters, and the tie with regulars.
楽|« Plaisir, détente ».|“Pleasure, ease”.
一番|« Numéro un ».|“Number one”.
大将|« Le chef » : surnom affectueux du patron derrière le comptoir.|“The boss”: a fond nickname for the owner behind the counter.
吉田|Nom de famille (« rizière heureuse ») : le patron a donné son nom à la boutique.|A family name (“lucky rice field”): the owner named the shop after himself.
山本|Nom de famille (« au pied de la montagne ») : le nom du patron.|A family name (“foot of the mountain”): the owner’s name.
長寿|« Longue vie ».|“Long life”.
松葉|« Aiguilles de pin » : toujours vertes, symbole de constance.|“Pine needles”: evergreen, a sign of constancy.
カフェ|« Café » en katakana : nom d’enseigne moderne.|“Café” in katakana: a modern shop name.
コーヒー|« Coffee » : souvent après le nom, comme une marque.|“Coffee”: often after the name, like a brand.
珈琲店|« Maison du café » : 珈琲 café, 店 boutique.|“Coffee shop”: 珈琲 coffee, 店 shop.
パティスリー|« Pâtisserie », du français, très prisé des enseignes.|“Pâtisserie”, from French, a favourite for shop names.
洋菓子|« Douceurs occidentales » : 洋 l’Occident, 菓子 friandise.|“Western sweets”: 洋 the West, 菓子 sweets.
ケーキハウス|« Cake house » : nom des pâtisseries de quartier.|“Cake house”: a name for neighbourhood cake shops.
ベーカリー|« Bakery » en katakana : nom courant des boulangeries.|“Bakery” in katakana: a common shop name.
パン工房|« Atelier à pain » : 工房 veut dire atelier d’artisan.|“Bread workshop”: 工房 means a craftsman’s workshop.
""".strip().splitlines():
    w,f,e=[x.strip() for x in line.split('|')]; NX[w]=(f,e)

# --- tea
add("""
お茶|Le thé, avec le お de politesse. Au restaurant, du thé vert est souvent servi gratuitement.|Tea, with the polite お. In restaurants, green tea is often free.
日本茶|Le thé japonais en général, presque toujours du thé vert.|Japanese tea in general, almost always green tea.
緑茶|Thé vert. Au Japon, les feuilles sont étuvées, ce qui donne un goût d’herbe fraîche.|Green tea. In Japan the leaves are steamed, which gives a fresh grassy taste.
煎茶|Le thé vert le plus courant : feuilles étuvées puis roulées, infusées à l’eau pas trop chaude.|The most common green tea: steamed, rolled leaves brewed in water that is not too hot.
ほうじ茶|Thé vert torréfié : brun, doux, au goût grillé, avec peu de caféine. On l’écrit aussi 焙じ茶.|Roasted green tea: brown, mellow and toasty, with little caffeine. Also written 焙じ茶.
玄米茶|Thé vert mélangé à du riz complet grillé, parfois soufflé. Goût de pop-corn.|Green tea mixed with roasted brown rice, sometimes popped. Tastes a bit like popcorn.
番茶|Thé vert de tous les jours, fait de grandes feuilles cueillies tard. Léger et bon marché.|Everyday green tea from large, late-picked leaves. Light and cheap.
玉露|Thé vert de luxe : les théiers sont couverts quelques semaines avant la récolte. Très doux et riche en umami, infusé tiède.|Luxury green tea: the bushes are shaded for weeks before picking. Sweet and full of umami, brewed lukewarm.
新茶|Thé de la première récolte du printemps (avril-mai). Frais et parfumé.|First tea of the spring harvest (April-May). Fresh and fragrant.
茎茶|Thé fait des tiges et des nervures des feuilles. Léger et sucré.|Tea made from stems and leaf veins. Light and sweet.
麦茶|Tisane d’orge grillée, sans caféine, bue froide l’été. Souvent servie gratuitement.|Roasted barley tea, caffeine-free, drunk cold in summer. Often served for free.
冷茶|Thé vert servi froid.|Green tea served cold.
和紅茶|Thé noir cultivé au Japon, plus doux et moins tannique que les thés indiens.|Black tea grown in Japan, softer and less tannic than Indian teas.
薄茶|Matcha léger et mousseux, la préparation habituelle.|Light frothy matcha, the usual way it is made.
濃茶|Matcha épais comme une crème, avec beaucoup de poudre, servi pendant la cérémonie du thé.|Matcha as thick as cream, made with lots of powder, served at the tea ceremony.
抹茶ラテ|Matcha mélangé à du lait chaud ou froid, souvent sucré.|Matcha mixed with hot or cold milk, often sweetened.
ほうじ茶ラテ|Thé torréfié avec du lait, doux et grillé.|Roasted tea with milk, mellow and toasty.
和菓子|Pâtisseries japonaises traditionnelles, souvent à base de pâte de haricots rouges et de riz gluant.|Traditional Japanese sweets, often made with red bean paste and glutinous rice.
茶菓子|Petite douceur servie avec le thé pour équilibrer son amertume.|A small sweet served with tea to balance its bitterness.
大福|Boule de mochi fourrée de pâte de haricots rouges, parfois avec une fraise (苺大福).|A mochi ball filled with red bean paste, sometimes with a strawberry (苺大福).
最中|Deux gaufrettes de riz croustillantes autour de pâte de haricots rouges.|Two crisp rice wafers around red bean paste.
羊羹|Bloc de pâte de haricots rouges gélifiée à l’agar, coupé en tranches.|A block of red bean paste set with agar, cut into slices.
わらび餅|Gelée tremblante d’amidon de fougère, roulée dans la poudre de soja grillé (kinako).|A wobbly bracken starch jelly rolled in roasted soy flour (kinako).
抹茶パフェ|Grande coupe en couches : glace au matcha, gelée, haricots rouges, mochi et crème.|A tall layered glass: matcha ice cream, jelly, red beans, mochi and cream.
抹茶アイス|Glace au matcha.|Matcha ice cream.
茶そば|Nouilles de sarrasin parfumées au thé vert, d’un vert pâle, souvent servies froides.|Buckwheat noodles flavoured with green tea, pale green, often served cold.
""")
for line in """
日本茶カフェ|« Café de thé japonais » : salon moderne où l’on goûte des thés et des douceurs.|“Japanese tea café”: a modern place to taste teas and sweets.
茶寮|« Pavillon de thé » : 茶 thé, 寮 pavillon. Nom élégant pour un salon de thé.|“Tea pavilion”: 茶 tea, 寮 lodge. An elegant name for a tea house.
日本茶|« Thé japonais » : la boutique vend et sert du thé.|“Japanese tea”: the shop sells and serves tea.
園|« Jardin, plantation » : beaucoup de maisons de thé portent le nom de leur plantation, comme 〇〇園.|“Garden, plantation”: many tea houses are named after their plantation, like 〇〇園.
マート|« Mart » : nom courant des supérettes.|“Mart”: a common name for convenience stores.
ストア|« Store » : magasin.|“Store”: shop.
サンライズ|« Sunrise », lever de soleil.|“Sunrise”.
グリーン|« Green », vert.|“Green”.
デイリー|« Daily », de tous les jours.|“Daily”.
ハッピー|« Happy », heureux.|“Happy”.
フレッシュ|« Fresh », frais.|“Fresh”.
スマイル|« Smile », sourire.|“Smile”.
エブリ|« Every », chaque (jour).|“Every” (day).
ニコニコ|Onomatopée du sourire.|The sound of a smile.
ハロー|« Hello », bonjour.|“Hello”.
まんぷく|« Ventre plein ».|“Full belly”.
""".strip().splitlines():
    w,f,e=[x.strip() for x in line.split('|')]; NX[w]=(f,e)

add("""
天ぷら|Poissons, crevettes et légumes enrobés d’une pâte très légère et frits. Sur les menus, 天 seul veut souvent dire tempura : 天丼, 天ざる.|Fish, prawns and vegetables in a very light batter, deep-fried. On menus 天 alone often means tempura: 天丼, 天ざる.
もも|Morceaux de cuisse de poulet sur la brochette, le classique. Sur beaucoup de menus, c’est l’étiquette de 正肉.|Chicken thigh pieces on a skewer, the classic. Many menus label 正肉 this way.
ささみ|Filet de poulet, très maigre, souvent servi rosé avec du wasabi ou de la prune.|Chicken tenderloin, very lean, often served pink with wasabi or plum.
せせり|Cou de poulet : petits morceaux fermes et juteux, un favori des habitués.|Chicken neck: small, firm, juicy pieces, a regulars’ favourite.
現金で|« En espèces » : 現金 argent liquide, で par.|“In cash”: 現金 cash, で by.
お会計ご一緒でよろしいですか|« Vous payez ensemble ? » ご一緒 : ensemble, en version polie. On répond 一緒で ou 別々で.|“Paying together?” ご一緒: together, the polite way. Answer 一緒で or 別々で.
お支払いはどうなさいますか|« Comment souhaitez-vous payer ? » なさる est le verbe faire en langage respectueux : on répond カードで ou 現金で.|“How would you like to pay?” なさる is the respectful verb for do: answer カードで or 現金で.
かしこまりました|« Bien noté » : la réponse du personnel à une commande, plus respectueuse que わかりました.|“Certainly”: the staff’s reply to an order, more deferential than わかりました.
どちらになさいますか|« Lequel choisissez-vous ? » どちら : lequel des deux ; なさいます : faire, choisir (respectueux).|“Which would you like?” どちら: which of the two; なさいます: do, choose (respectful).
一つ|« Un » pour commander n’importe quel objet ou plat : 一つ, 二つ, 三つ… On le place après le plat : 餃子を一つください.|“One” for ordering any item or dish: 一つ, 二つ, 三つ… It comes after the dish: 餃子を一つください.
二つ|« Deux » objets ou plats. 〜つ marche jusqu’à dix sans réfléchir au compteur.|“Two” items or dishes. 〜つ works up to ten without picking a counter.
一本|« Un » pour les choses longues : brochette, bouteille. Attention à la lecture : いっぽん.|“One” for long things: a skewer, a bottle. Note the reading: いっぽん.
二本|« Deux » brochettes ou bouteilles. Au yakitori, on commande souvent par deux : ねぎま二本.|“Two” skewers or bottles. At yakitori people often order in twos: ねぎま二本.
一杯|« Un » verre ou bol : bière, saké, ramen. Lecture いっぱい, comme « plein ».|“One” glass or bowl: beer, sake, ramen. Read いっぱい, like “full”.
一個|« Une » pièce : un gyoza, une croquette, un onigiri. 〜個 compte les petites choses rondes.|“One” piece: a gyoza, a croquette, an onigiri. 〜個 counts small round things.
""")
