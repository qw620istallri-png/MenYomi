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
""".strip().splitlines():
    w,f,e=[x.strip() for x in line.split('|')]; NX[w]=(f,e)
