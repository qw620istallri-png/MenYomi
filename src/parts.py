"""Phrases split into their words, so a phrase's detail gives the meaning of each word before its kanji.
Format: a phrase line, then one '- surface|reading|French|English' line per word, in order."""
P = {}
_SRC = """
営業中
- 営業|えいぎょう|activité commerciale, ouverture|business, being open
- 中|ちゅう|en cours|in progress
準備中
- 準備|じゅんび|préparation|preparation
- 中|ちゅう|en cours|in progress
本日休業
- 本日|ほんじつ|aujourd’hui (formel)|today (formal)
- 休業|きゅうぎょう|fermeture, relâche|closed for business
定休日
- 定休|ていきゅう|fermeture régulière|regular closing
- 日|び|jour|day
営業時間
- 営業|えいぎょう|ouverture, activité|business, being open
- 時間|じかん|heures, durée|hours, time
全席禁煙
- 全席|ぜんせき|toutes les places|every seat
- 禁煙|きんえん|non-fumeur|no smoking
喫煙席
- 喫煙|きつえん|fumer|smoking
- 席|せき|place assise|seat
現金のみ
- 現金|げんきん|espèces|cash
- のみ|のみ|seulement|only
食券制
- 食券|しょっけん|ticket repas|meal ticket
- 制|せい|système, règle|system
お持ち帰り
- お|お|préfixe de politesse|polite prefix
- 持ち帰り|もちかえり|emporter (litt. porter et rentrer)|taking home (lit. carry and return)
予約席
- 予約|よやく|réservation|reservation
- 席|せき|place assise|seat
ご予約
- ご|ご|préfixe de politesse|polite prefix
- 予約|よやく|réservation|reservation
お一人様
- お|お|préfixe de politesse|polite prefix
- 一人|ひとり|une personne|one person
- 様|さま|titre honorifique (Monsieur, Madame)|honorific title (Mr, Ms)
お手洗い
- お|お|préfixe de politesse|polite prefix
- 手洗い|てあらい|toilettes (litt. lavage des mains)|toilet (lit. hand washing)
お会計
- お|お|préfixe de politesse|polite prefix
- 会計|かいけい|addition, comptes|bill, accounts
ご注文
- ご|ご|préfixe de politesse|polite prefix
- 注文|ちゅうもん|commande|order
お冷
- お|お|préfixe de politesse|polite prefix
- 冷|ひや|froid, ici l’eau fraîche|cold, here cold water
お冷はセルフ
- お冷|おひや|eau fraîche offerte|free cold water
- は|は|particule de thème : « quant à »|topic particle: “as for”
- セルフ|セルフ|libre-service (de l’anglais self)|self-service (from English)
ご自由にどうぞ
- ご自由に|ごじゆうに|librement|freely
- どうぞ|どうぞ|je vous en prie, allez-y|please, go ahead
ラストオーダー
- ラスト|ラスト|dernier (de l’anglais last)|last (from English)
- オーダー|オーダー|commande (de l’anglais order)|order (from English)
焼きたて
- 焼き|やき|cuit, grillé|baked, grilled
- たて|たて|tout juste fait|freshly done
いらっしゃいませ
- いらっしゃい|いらっしゃい|venir (verbe honorifique)|come (honorific verb)
- ませ|ませ|terminaison polie d’invitation|polite request ending
何名様ですか
- 何|なん|combien, quoi|how many, what
- 名|めい|compteur de personnes|counter for people
- 様|さま|titre honorifique|honorific title
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question, le « ? » parlé|question marker, a spoken “?”
二人です
- 二人|ふたり|deux personnes|two people
- です|です|c’est, nous sommes (forme polie)|it is, we are (polite)
一人です
- 一人|ひとり|une personne|one person
- です|です|c’est, je suis (forme polie)|it is, I am (polite)
こちらへどうぞ
- こちら|こちら|par ici, ce côté|this way, this side
- へ|へ|vers|towards
- どうぞ|どうぞ|je vous en prie|please
お決まりですか
- お決まり|おきまり|décidé (verbe 決まる, poli)|decided (verb 決まる, polite)
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
おすすめは何ですか
- おすすめ|おすすめ|recommandation|recommendation
- は|は|particule de thème : « quant à »|topic particle: “as for”
- 何|なん|quoi|what
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
これは何ですか
- これ|これ|ceci|this
- は|は|particule de thème : « quant à »|topic particle: “as for”
- 何|なん|quoi|what
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
以上です
- 以上|いじょう|ce qui précède, tout ça|the above, all that
- です|です|c’est (forme polie)|it is (polite)
少々お待ちください
- 少々|しょうしょう|un peu, un instant|a little, a moment
- お待ち|おまち|attendre (verbe 待つ, poli)|wait (verb 待つ, polite)
- ください|ください|s’il vous plaît|please
お待たせしました
- お待たせ|おまたせ|faire attendre|making you wait
- しました|しました|j’ai fait (passé poli de する)|I did (polite past of する)
ごゆっくりどうぞ
- ごゆっくり|ごゆっくり|tranquillement, sans vous presser|at your leisure
- どうぞ|どうぞ|je vous en prie|please
お水ください
- お水|おみず|de l’eau|water
- ください|ください|s’il vous plaît|please
持ち帰りで
- 持ち帰り|もちかえり|à emporter|takeaway
- で|で|par, en mode : « en … »|by, as: “as …”
お会計お願いします
- お会計|おかいけい|l’addition|the bill
- お願い|おねがい|demande, faveur|request, favour
- します|します|je fais (forme polie de する)|I do (polite form of する)
別々で
- 別々|べつべつ|séparément|separately
- で|で|par, en mode : « en … »|by, as: “as …”
カードで
- カード|カード|carte (de l’anglais card)|card (from English)
- で|で|par, avec : « par carte »|by, with: “by card”
ごちそうさまでした
- ごちそうさま|ごちそうさま|merci pour le festin|thanks for the feast
- でした|でした|c’était (passé poli de です)|it was (polite past of です)
ありがとうございました
- ありがとう|ありがとう|merci|thank you
- ございました|ございました|forme très polie, au passé|very polite form, past tense
またお越しください
- また|また|encore, de nouveau|again
- お越し|おこし|venue (verbe honorifique)|coming (honorific verb)
- ください|ください|s’il vous plaît|please
店内でお召し上がりですか
- 店内|てんない|dans la boutique|in the shop
- で|で|à, dans (lieu de l’action)|at, in (place of the action)
- お召し上がり|おめしあがり|manger, boire (verbe honorifique)|eat, drink (honorific verb)
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
テイクアウトで
- テイクアウト|テイクアウト|à emporter (de l’anglais take out)|takeaway (from English take out)
- で|で|en mode : « en … »|as: “as …”
店内で
- 店内|てんない|dans la boutique, sur place|in the shop, eat-in
- で|で|à, dans|at, in
ホットとアイスどちらになさいますか
- ホット|ホット|chaud (de l’anglais hot)|hot (from English)
- と|と|et|and
- アイス|アイス|glacé (de l’anglais ice)|iced (from English ice)
- どちら|どちら|lequel des deux|which of the two
- に|に|marque du choix : « pour … »|marks the choice: “for …”
- なさいます|なさいます|faire, choisir (verbe honorifique)|do, choose (honorific verb)
- か|か|marque de question|question marker
アイスで
- アイス|アイス|glacé|iced
- で|で|en mode : « en … »|as: “as …”
ホットで
- ホット|ホット|chaud|hot
- で|で|en mode : « en … »|as: “as …”
こちらでお召し上がりですか
- こちら|こちら|ici|here
- で|で|à, dans (lieu de l’action)|at, in (place of the action)
- お召し上がり|おめしあがり|manger, boire (verbe honorifique)|eat, drink (honorific verb)
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
お持ち帰りですか
- お持ち帰り|おもちかえり|à emporter|takeaway
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
温めますか
- 温め|あたため|réchauffer (verbe 温める)|heat up (verb 温める)
- ます|ます|terminaison polie des verbes|polite verb ending
- か|か|marque de question|question marker
お願いします
- お願い|おねがい|demande, faveur|request, favour
- します|します|je fais (forme polie de する)|I do (polite form of する)
大丈夫です
- 大丈夫|だいじょうぶ|ça va, pas besoin|fine, no need
- です|です|c’est (forme polie)|it is (polite)
お箸おつけしますか
- お箸|おはし|baguettes|chopsticks
- おつけ|おつけ|joindre (verbe 付ける, humble)|attach (verb 付ける, humble)
- します|します|je fais (forme polie de する)|I do (polite form of する)
- か|か|marque de question|question marker
袋はご利用ですか
- 袋|ふくろ|sac|bag
- は|は|particule de thème : « quant à »|topic particle: “as for”
- ご利用|ごりよう|utilisation (polie)|use (polite)
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
ポイントカードはお持ちですか
- ポイントカード|ポイントカード|carte de fidélité (carte à points)|loyalty card (points card)
- は|は|particule de thème : « quant à »|topic particle: “as for”
- お持ち|おもち|avoir sur soi (verbe 持つ, poli)|have with you (verb 持つ, polite)
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
以上でよろしいですか
- 以上|いじょう|ce qui précède, tout ça|the above, all that
- で|で|avec, en restant à|with, staying at
- よろしい|よろしい|convenable, d’accord (poli)|all right (polite)
- です|です|c’est (forme polie)|it is (polite)
- か|か|marque de question|question marker
本日のおすすめ
- 本日|ほんじつ|aujourd’hui (formel)|today (formal)
- の|の|de (lien entre deux noms)|of (links two nouns)
- おすすめ|おすすめ|recommandation|recommendation
本日のコーヒー
- 本日|ほんじつ|aujourd’hui (formel)|today (formal)
- の|の|de (lien entre deux noms)|of (links two nouns)
- コーヒー|コーヒー|café|coffee
鰹のたたき
- 鰹|かつお|bonite|bonito
- の|の|de (lien entre deux noms)|of (links two nouns)
- たたき|たたき|saisi en surface, cru à cœur|seared outside, raw inside
和栗のモンブラン
- 和栗|わぐり|châtaigne japonaise|Japanese chestnut
- の|の|de (lien entre deux noms)|of (links two nouns)
- モンブラン|モンブラン|mont-blanc (le gâteau)|Mont Blanc (the cake)
幕の内弁当
- 幕の内|まくのうち|entracte (litt. dans le rideau)|interval (lit. inside the curtain)
- 弁当|べんとう|repas en boîte|boxed meal
はじめました
- はじめ|はじめ|commencer (verbe 始める)|start (verb 始める)
- ました|ました|terminaison polie au passé|polite past ending
"""
_cur = None
for _line in _SRC.strip().splitlines():
    _line = _line.strip()
    if not _line:
        continue
    if _line.startswith('- '):
        P[_cur].append([x.strip() for x in _line[2:].split('|')])
    else:
        _cur = _line
        P[_cur] = []
for _k, _v in P.items():
    assert ''.join(p[0] for p in _v) == _k, _k
