"""Japanese seasons for the stamp book calendar: the 24 solar terms (二十四節気) and the 72 micro-seasons (七十二候),
with their usual start dates (a day earlier or later in some years), and the dishes in season each month."""

# solar term: kanji, reading, French, English
SEKKI = [
    ('立春', 'りっしゅん', 'début du printemps', 'start of spring'),
    ('雨水', 'うすい', 'eaux de pluie', 'rain water'),
    ('啓蟄', 'けいちつ', 'réveil des insectes', 'insects awaken'),
    ('春分', 'しゅんぶん', 'équinoxe de printemps', 'spring equinox'),
    ('清明', 'せいめい', 'clarté pure', 'pure and clear'),
    ('穀雨', 'こくう', 'pluie des céréales', 'grain rain'),
    ('立夏', 'りっか', 'début de l’été', 'start of summer'),
    ('小満', 'しょうまん', 'petite plénitude', 'lesser ripening'),
    ('芒種', 'ぼうしゅ', 'grains à barbe', 'grain in ear'),
    ('夏至', 'げし', 'solstice d’été', 'summer solstice'),
    ('小暑', 'しょうしょ', 'petites chaleurs', 'lesser heat'),
    ('大暑', 'たいしょ', 'grandes chaleurs', 'greater heat'),
    ('立秋', 'りっしゅう', 'début de l’automne', 'start of autumn'),
    ('処暑', 'しょしょ', 'fin des chaleurs', 'end of heat'),
    ('白露', 'はくろ', 'rosée blanche', 'white dew'),
    ('秋分', 'しゅうぶん', 'équinoxe d’automne', 'autumn equinox'),
    ('寒露', 'かんろ', 'rosée froide', 'cold dew'),
    ('霜降', 'そうこう', 'descente du givre', 'frost descends'),
    ('立冬', 'りっとう', 'début de l’hiver', 'start of winter'),
    ('小雪', 'しょうせつ', 'petite neige', 'lesser snow'),
    ('大雪', 'たいせつ', 'grande neige', 'greater snow'),
    ('冬至', 'とうじ', 'solstice d’hiver', 'winter solstice'),
    ('小寒', 'しょうかん', 'petit froid', 'lesser cold'),
    ('大寒', 'だいかん', 'grand froid', 'greater cold'),
]

# micro-season: month, day, name, reading (spaces between words, for the romaji), French, English, then a line of explanation in each
_KO = """
2|4|東風解凍|はるかぜ こおり を とく|le vent d’est dégèle|east wind melts the ice|Le premier vent de printemps commence à faire fondre la glace des étangs.|The first spring wind starts to melt the ice on ponds.
2|9|黄鶯睍睆|うぐいす なく|la bouscarle chante|the bush warbler sings|On entend dans les montagnes le chant de l’uguisu, l’oiseau qui annonce le printemps.|The uguisu, the bird that heralds spring, starts singing in the hills.
2|14|魚上氷|うお こおり を いずる|les poissons sautent sur la glace|fish rise through the ice|La glace se fend et les poissons remontent près de la surface.|The ice cracks and fish swim up close to the surface.
2|19|土脉潤起|つち の しょう うるおい おこる|la terre s’humidifie|the soil grows damp|La pluie remplace la neige et la terre redevient souple.|Rain replaces snow and the soil softens again.
2|24|霞始靆|かすみ はじめて たなびく|la brume s’étire|mist starts to linger|Une brume légère flotte sur les champs et les montagnes.|A light haze hangs over fields and hills.
3|1|草木萌動|そうもく めばえ いずる|les plantes bourgeonnent|plants begin to sprout|Les premiers bourgeons et brins d’herbe apparaissent.|The first buds and shoots appear.
3|6|蟄虫啓戸|すごもり むし と を ひらく|les insectes ouvrent leur porte|hibernating insects emerge|Les insectes cachés sous terre pendant l’hiver ressortent.|Insects that slept underground through winter come out.
3|11|桃始笑|もも はじめて さく|les pêchers « sourient »|peach trees start to bloom|Les fleurs de pêcher s’ouvrent : en japonais ancien, une fleur qui s’ouvre « sourit ».|Peach blossoms open; in old Japanese, a flower that opens “smiles”.
3|16|菜虫化蝶|なむし ちょう と なる|les chenilles deviennent papillons|caterpillars become butterflies|Les chenilles du chou se changent en papillons blancs.|Cabbage caterpillars turn into white butterflies.
3|21|雀始巣|すずめ はじめて すくう|les moineaux font leur nid|sparrows start to nest|Les moineaux ramassent des brindilles pour leur nid.|Sparrows gather twigs for their nests.
3|26|櫻始開|さくら はじめて ひらく|les cerisiers fleurissent|cherry blossoms open|Les premières fleurs de cerisier s’ouvrent : c’est la saison des hanami.|The first cherry blossoms open: time for hanami.
3|31|雷乃発声|かみなり すなわち こえ を はっす|le tonnerre élève la voix|thunder raises its voice|On entend les premiers orages de printemps.|The first spring thunder rolls.
4|5|玄鳥至|つばめ きたる|les hirondelles arrivent|swallows return|Les hirondelles reviennent du sud et nichent sous les toits.|Swallows come back from the south and nest under the eaves.
4|10|鴻雁北|こうがん かえる|les oies repartent au nord|wild geese fly north|Les oies sauvages qui ont passé l’hiver au Japon repartent vers le nord.|Wild geese that wintered in Japan head back north.
4|15|虹始見|にじ はじめて あらわる|les arcs-en-ciel apparaissent|rainbows first appear|L’air plus humide fait revenir les arcs-en-ciel après les averses.|Moister air brings rainbows back after showers.
4|20|葭始生|あし はじめて しょうず|les roseaux poussent|reeds start to sprout|Les jeunes pousses de roseau sortent au bord de l’eau.|Young reed shoots appear at the water’s edge.
4|25|霜止出苗|しも やみて なえ いずる|fin du givre, les semis lèvent|frost ends, seedlings grow|Plus de gelées : les plants de riz poussent dans les pépinières.|No more frost: rice seedlings grow in the nursery beds.
4|30|牡丹華|ぼたん はな さく|les pivoines fleurissent|peonies bloom|Les grandes fleurs de pivoine s’ouvrent.|The large peony flowers open.
5|5|蛙始鳴|かわず はじめて なく|les grenouilles chantent|frogs start to sing|Les grenouilles chantent dans les rizières fraîchement inondées.|Frogs sing in the freshly flooded rice fields.
5|10|蚯蚓出|みみず いずる|les vers de terre sortent|earthworms surface|Les vers de terre remontent dans la terre réchauffée.|Earthworms come up through the warmed soil.
5|15|竹笋生|たけのこ しょうず|les pousses de bambou sortent|bamboo shoots sprout|Saison des takenoko, les pousses de bambou qu’on mange en ce moment.|Season of takenoko, the bamboo shoots eaten right now.
5|21|蚕起食桑|かいこ おきて くわ を はむ|les vers à soie mangent le mûrier|silkworms feast on mulberry|Les vers à soie se réveillent et dévorent les feuilles de mûrier.|Silkworms wake and devour mulberry leaves.
5|26|紅花栄|べにばな さかう|le carthame fleurit|safflowers bloom|Le carthame, qui donnait la teinture rouge, est en fleur.|Safflower, once used for red dye, is in bloom.
5|31|麦秋至|むぎ の とき いたる|l’« automne » du blé|wheat harvest arrives|Le blé est mûr et doré : on l’appelle l’automne du blé.|The wheat is ripe and golden: the “autumn” of wheat.
6|6|蟷螂生|かまきり しょうず|les mantes éclosent|praying mantises hatch|Les petites mantes religieuses sortent de leurs œufs.|Tiny praying mantises hatch from their eggs.
6|11|腐草為螢|くされたる くさ ほたる と なる|l’herbe pourrie devient luciole|rotten grass becomes fireflies|Les lucioles brillent au-dessus des herbes humides ; on croyait qu’elles en naissaient.|Fireflies glow above damp grass; people thought they were born from it.
6|16|梅子黄|うめ の み きばむ|les prunes jaunissent|plums turn yellow|Les prunes ume mûrissent, en pleine saison des pluies (tsuyu).|Ume plums ripen in the middle of the rainy season.
6|21|乃東枯|なつかれくさ かるる|la brunelle se fane|self-heal withers|La brunelle, une herbe médicinale, sèche en plein été.|Self-heal, a medicinal herb, dries up in midsummer.
6|26|菖蒲華|あやめ はな さく|les iris fleurissent|irises bloom|Les iris fleurissent au bord des étangs.|Irises bloom along the ponds.
7|2|半夏生|はんげ しょうず|le hange pousse|crow-dipper sprouts|Les rizières sont plantées ; c’est la fin des repiquages.|Rice planting is finished.
7|7|温風至|あつかぜ いたる|le vent chaud arrive|warm winds blow|Le vent devient chaud : la saison des pluies se termine.|The wind turns warm as the rainy season ends.
7|12|蓮始開|はす はじめて ひらく|les lotus s’ouvrent|lotuses start to open|Les fleurs de lotus s’ouvrent tôt le matin.|Lotus flowers open early in the morning.
7|17|鷹乃学習|たか すなわち わざ を ならう|les jeunes faucons apprennent|young hawks learn to fly|Les jeunes faucons apprennent à voler et à chasser.|Young hawks learn to fly and hunt.
7|23|桐始結花|きり はじめて はな を むすぶ|le paulownia forme ses fruits|paulownia forms seeds|Le paulownia, arbre des armoiries, forme ses fruits.|The paulownia, a crest tree, sets its seeds.
7|28|土潤溽暑|つち うるおうて むしあつし|la terre moite, chaleur lourde|damp soil, sticky heat|Chaleur humide et étouffante, le cœur de l’été.|Heavy, humid heat: the heart of summer.
8|2|大雨時行|たいう ときどき ふる|de grosses averses|great rains sometimes fall|Les orages d’été éclatent l’après-midi.|Summer storms break in the afternoon.
8|7|涼風至|すずかぜ いたる|un vent frais arrive|cool winds blow|Le soir, un premier vent frais annonce l’automne.|In the evening, a first cool breeze hints at autumn.
8|12|寒蝉鳴|ひぐらし なく|les cigales du soir chantent|evening cicadas sing|Les cigales higurashi chantent au crépuscule.|Higurashi cicadas sing at dusk.
8|17|蒙霧升降|ふかき きり まとう|un épais brouillard s’installe|thick fog descends|Le brouillard couvre les vallées le matin.|Fog fills the valleys in the morning.
8|23|綿柎開|わた の はなしべ ひらく|les capsules de coton s’ouvrent|cotton bolls open|Les capsules de coton s’ouvrent sur leur bourre blanche.|Cotton bolls split open on their white fluff.
8|28|天地始粛|てんち はじめて さむし|le ciel et la terre se calment|heat starts to die down|La chaleur retombe enfin.|The heat finally eases.
9|2|禾乃登|こくもの すなわち みのる|le riz mûrit|rice ripens|Les épis de riz se courbent sous leur poids.|Rice ears bend under their weight.
9|7|草露白|くさ の つゆ しろし|la rosée blanchit l’herbe|dew glistens white on grass|La rosée du matin brille sur les herbes.|Morning dew shines on the grass.
9|12|鶺鴒鳴|せきれい なく|les bergeronnettes chantent|wagtails sing|Les bergeronnettes chantent au bord des rivières.|Wagtails sing by the rivers.
9|17|玄鳥去|つばめ さる|les hirondelles partent|swallows leave|Les hirondelles repartent vers le sud.|Swallows head back south.
9|23|雷乃収声|かみなり すなわち こえ を おさむ|le tonnerre se tait|thunder ceases|Plus d’orages : l’air devient sec et clair.|No more thunder: the air turns dry and clear.
9|28|蟄虫坏戸|むし かくれて と を ふさぐ|les insectes ferment leur porte|insects seal their burrows|Les insectes s’enterrent et bouchent l’entrée pour l’hiver.|Insects burrow and seal the entrance for winter.
10|3|水始涸|みず はじめて かるる|on vide l’eau des rizières|fields are drained|On assèche les rizières avant la récolte.|Rice fields are drained before the harvest.
10|8|鴻雁来|こうがん きたる|les oies sauvages arrivent|wild geese arrive|Les oies sauvages reviennent du nord pour l’hiver.|Wild geese come from the north for winter.
10|13|菊花開|きく の はな ひらく|les chrysanthèmes fleurissent|chrysanthemums bloom|Saison des chrysanthèmes, la fleur du sceau impérial.|Season of the chrysanthemum, the imperial crest flower.
10|18|蟋蟀在戸|きりぎりす と に あり|les grillons chantent à la porte|crickets chirp by the door|Les grillons chantent tout près des maisons.|Crickets chirp right by the houses.
10|23|霜始降|しも はじめて ふる|le premier givre|first frost|Le premier givre blanchit les champs au petit matin.|The first frost whitens the fields at dawn.
10|28|霎時施|こさめ ときどき ふる|de petites pluies passent|light rains pass|De courtes averses froides vont et viennent.|Short, cold showers come and go.
11|2|楓蔦黄|もみじ つた きばむ|érables et lierres jaunissent|maples and ivy turn|Les érables rougissent : c’est la saison des momiji.|Maples turn red: momiji season.
11|7|山茶始開|つばき はじめて ひらく|les camélias s’ouvrent|camellias start to bloom|Les fleurs de sazanka, un camélia d’hiver, s’ouvrent.|Sazanka, a winter camellia, starts to bloom.
11|12|地始凍|ち はじめて こおる|la terre commence à geler|the ground starts to freeze|Les premières gelées durcissent la terre le matin.|The first frosts harden the ground in the morning.
11|17|金盞香|きんせんか さく|les narcisses embaument|daffodils bloom|Les narcisses fleurissent et sentent bon.|Fragrant daffodils bloom.
11|22|虹蔵不見|にじ かくれて みえず|les arcs-en-ciel se cachent|rainbows hide|Le soleil d’hiver est bas et l’air sec : plus d’arc-en-ciel avant le printemps.|The winter sun is low and the air dry: no rainbows until spring.
11|27|朔風払葉|きたかぜ このは を はらう|le vent du nord balaie les feuilles|north wind blows the leaves|Le vent du nord fait tomber les dernières feuilles.|The north wind strips the last leaves.
12|2|橘始黄|たちばな はじめて きばむ|les tachibana jaunissent|tachibana citrus turn yellow|Les petits agrumes tachibana jaunissent.|Small tachibana citrus turn yellow.
12|7|閉塞成冬|そら さむく ふゆ と なる|le ciel se ferme, c’est l’hiver|skies close, winter sets in|Ciel gris et lourd : l’hiver s’installe.|Grey, heavy skies: winter settles in.
12|12|熊蟄穴|くま あな に こもる|les ours entrent dans leur tanière|bears retreat to dens|Les ours s’enferment pour hiberner.|Bears shut themselves in to hibernate.
12|16|鱖魚群|さけ の うお むらがる|les saumons remontent en bancs|salmon gather and swim upstream|Les saumons remontent les rivières pour frayer.|Salmon swim upriver to spawn.
12|21|乃東生|なつかれくさ しょうず|la brunelle repousse|self-heal sprouts|Au solstice, la brunelle repousse sous la neige.|At the solstice, self-heal sprouts under the snow.
12|26|麋角解|さわしか の つの おつる|les cerfs perdent leurs bois|deer shed their antlers|Les cerfs perdent leurs bois.|Deer shed their antlers.
12|31|雪下出麦|ゆき わたりて むぎ のびる|le blé pousse sous la neige|wheat sprouts under snow|Sous la neige, le blé d’hiver pousse déjà.|Under the snow, winter wheat is already growing.
1|5|芹乃栄|せり すなわち さかう|le persil japonais pousse|parsley flourishes|Le seri pousse au bord de l’eau ; on le met dans le nanakusa-gayu du 7 janvier.|Seri grows by the water; it goes into the nanakusa rice porridge on 7 January.
1|10|水泉動|しみず あたたか を ふくむ|les sources se réchauffent|springs thaw|Sous la glace, l’eau des sources recommence à couler.|Under the ice, spring water starts to flow again.
1|15|雉始雊|きじ はじめて なく|le faisan appelle|pheasants start to call|Le faisan mâle lance son cri.|The male pheasant calls.
1|20|款冬華|ふき の はな さく|le pétasite fleurit|butterbur flowers|Les boutons de fuki sortent de la neige.|Fuki buds push through the snow.
1|25|水沢腹堅|さわみず こおり つめる|les marais gèlent en profondeur|ice thickens on streams|C’est le plus froid de l’année : l’eau gèle en épaisseur.|The coldest time of year: water freezes thick.
1|30|鶏始乳|にわとり はじめて とや に つく|les poules recommencent à pondre|hens start to lay|Les poules couvent à nouveau : le printemps approche.|Hens start laying again: spring is near.
"""
KO = []
for _line in _KO.strip().splitlines():
    m, d, name, rd, fr, en, xfr, xen = _line.split('|')
    KO.append([int(m), int(d), name, rd, fr, en, xfr, xen])
assert len(KO) == 72
# each solar term starts on its first micro-season (every third one, from 立春 on 4 February)
for _i, _k in enumerate(KO):
    _k.append(SEKKI[_i // 3][0] if _i % 3 == 0 else '')

# dishes in season, by month (words from the menus)
SHUN = {
    1: ['鰤', '湯豆腐', '水炊き', '熱燗', '蟹', '善哉'],
    2: ['焼牡蠣', '鰤', 'もつ鍋', '湯豆腐', '熱燗', '苺'],
    3: ['苺', '草餅', '山菜蕎麦', '帆立', '苺タルト', '桜'],
    4: ['鰹のたたき', '草餅', '山菜蕎麦', '帆立', '苺パフェ', '新茶'],
    5: ['新茶', '鰹のたたき', '鯵', '抹茶パフェ', '冷茶', '山菜蕎麦'],
    6: ['鯵', '梅酒', '冷やしトマト', '冷茶', '穴子', '鮎'],
    7: ['鰻丼', '鰻重', '冷やし中華', '冷麺', '宇治金時', '枝豆'],
    8: ['氷', '宇治金時', '冷やし中華', '枝豆', '冷奴', 'ゴーヤチャンプルー'],
    9: ['芋煮', '和栗のモンブラン', '月見蕎麦', '銀杏', '鮭', 'モンブラン'],
    10: ['芋煮', '鮭', '銀杏', '和栗のモンブラン', 'きりたんぽ鍋', '椎茸焼'],
    11: ['牡蠣フライ', '鰤', '熱燗', 'おでん', 'もつ鍋', '肉まん'],
    12: ['石狩鍋', '鰤', '蟹', '熱燗', '牡蠣フライ', 'おでん'],
}

# public holidays named on the calendar: reading, French, English, a line on each
HOLIDAYS = {
    '元日': ['がんじつ', 'Jour de l’an', 'New Year’s Day', 'Le premier jour de l’année. Beaucoup de boutiques ferment jusqu’au 3 janvier, et on mange les plats froids de l’osechi.', 'The first day of the year. Many shops close until 3 January, and families eat the cold osechi dishes.'],
    '成人の日': ['せいじんのひ', 'Jour de la majorité', 'Coming of Age Day', 'On fête ceux qui deviennent adultes dans l’année, souvent en kimono, avec une cérémonie en mairie.', 'Celebrates those who come of age this year, often in kimono, with a ceremony at the town hall.'],
    '建国記念の日': ['けんこくきねんのひ', 'Fondation du pays', 'National Foundation Day', 'Commémore la fondation légendaire du Japon par l’empereur Jinmu.', 'Marks the legendary founding of Japan by Emperor Jinmu.'],
    '天皇誕生日': ['てんのうたんじょうび', 'Anniversaire de l’empereur', 'Emperor’s Birthday', 'La date suit l’empereur en place ; le palais ouvre ses portes au public ce jour-là.', 'The date follows the reigning emperor; the palace opens to the public that day.'],
    '春分の日': ['しゅんぶんのひ', 'Équinoxe de printemps', 'Spring Equinox Day', 'Le jour et la nuit sont égaux. On rend visite aux tombes de la famille, et on mange des botamochi.', 'Day and night are equal. Families visit their graves and eat botamochi.'],
    '昭和の日': ['しょうわのひ', 'Jour de Shōwa', 'Shōwa Day', 'Ancien anniversaire de l’empereur Shōwa. Il ouvre la Golden Week, la semaine des grands départs.', 'The former birthday of Emperor Shōwa. It opens Golden Week, the big holiday week.'],
    '憲法記念日': ['けんぽうきねんび', 'Jour de la Constitution', 'Constitution Day', 'Commémore la Constitution de 1947.', 'Marks the 1947 Constitution.'],
    'みどりの日': ['みどりのひ', 'Jour de la verdure', 'Greenery Day', 'Un jour pour profiter de la nature, au milieu de la Golden Week.', 'A day to enjoy nature, in the middle of Golden Week.'],
    'こどもの日': ['こどものひ', 'Jour des enfants', 'Children’s Day', 'Les carpes en tissu (koinobori) flottent au vent, et on mange des kashiwa-mochi.', 'Cloth carp streamers (koinobori) fly in the wind, and people eat kashiwa-mochi.'],
    '海の日': ['うみのひ', 'Jour de la mer', 'Marine Day', 'Remercie la mer, le troisième lundi de juillet ; l’été commence vraiment.', 'Gives thanks to the sea, on the third Monday of July; summer really begins.'],
    '山の日': ['やまのひ', 'Jour de la montagne', 'Mountain Day', 'Un jour pour la montagne, juste avant les congés d’Obon.', 'A day for the mountains, just before the Obon holidays.'],
    '敬老の日': ['けいろうのひ', 'Jour du respect des aînés', 'Respect for the Aged Day', 'On honore les personnes âgées, le troisième lundi de septembre.', 'Honours the elderly, on the third Monday of September.'],
    '秋分の日': ['しゅうぶんのひ', 'Équinoxe d’automne', 'Autumn Equinox Day', 'Le jour et la nuit sont égaux. On rend visite aux tombes de la famille, et on mange des ohagi.', 'Day and night are equal. Families visit their graves and eat ohagi.'],
    'スポーツの日': ['スポーツのひ', 'Jour du sport', 'Sports Day', 'Rappelle l’ouverture des Jeux de Tōkyō 1964 ; les écoles organisent leurs fêtes sportives.', 'Recalls the opening of the 1964 Tōkyō Olympics; schools hold their sports days.'],
    '文化の日': ['ぶんかのひ', 'Jour de la culture', 'Culture Day', 'On remet les décorations culturelles, et les musées sont souvent gratuits.', 'Cultural honours are awarded, and museums are often free.'],
    '勤労感謝の日': ['きんろうかんしゃのひ', 'Jour de remerciement du travail', 'Labour Thanksgiving Day', 'Vient d’une ancienne fête des récoltes, où l’empereur goûte le riz nouveau.', 'Comes from an old harvest festival, where the emperor tastes the new rice.'],
    '振替休日': ['ふりかえきゅうじつ', 'Jour férié reporté', 'Substitute holiday', 'Un jour férié tombé un dimanche est reporté au jour suivant.', 'A holiday that falls on a Sunday moves to the next day.'],
    '国民の休日': ['こくみんのきゅうじつ', 'Jour du peuple', 'Citizens’ holiday', 'Un jour coincé entre deux jours fériés devient férié lui aussi.', 'A day squeezed between two holidays becomes a holiday too.'],
}
