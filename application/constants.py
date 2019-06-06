# -*- coding: Utf-8 -*

BASE_STOP_WORDS = [
    "a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs", "ainsi",
    "ait", "allaient", "allo", "allons", "allô", "alors", "anterieur",
    "anterieure", "anterieures", "apres", "après", "as", "assez",
    "attendu", "au", "aucun", "aucune", "aujourd", "aujourd'hui", "aupres",
    "auquel", "aura", "auraient", "aurait", "auront", "aussi", "autre",
    "autrefois", "autrement", "autres", "autrui", "aux", "auxquelles",
    "auxquels", "avaient", "avais", "avait", "avant", "avec", "avoir", "avons",
    "ayant", "b", "bah", "bas", "basee", "bat", "beau", "beaucoup", "bien",
    "bigre", "boum", "bravo", "brrr", "c", "car", "ce", "ceci", "cela",
    "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là",
    "celui", "celui-ci", "celui-là", "cent", "cependant", "certain",
    "certaine", "certaines", "certains", "certes", "ces", "cet", "cette",
    "ceux", "ceux-ci", "ceux-là", "chacun", "chacune", "chaque", "cher",
    "chers", "chez", "chiche", "chut", "chère", "chères", "ci", "cinq",
    "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac", "clic",
    "combien", "comme", "comment", "comparable", "comparables", "compris",
    "concernant", "contre", "couic", "crac", "d", "da", "dans", "de", "debout",
    "dedans", "dehors", "deja", "delà", "depuis", "dernier", "derniere",
    "derriere", "derrière", "des", "desormais", "desquelles", "desquels",
    "dessous", "dessus", "deux", "deuxième", "deuxièmement", "devant",
    "devers", "devra", "different", "differentes", "differents", "différent",
    "différente", "différentes", "différents", "dire", "directe",
    "directement", "dit", "dite", "dits", "divers", "diverse", "diverses",
    "dix", "dix-huit", "dix-neuf", "dix-sept", "dixième", "doit",
    "doivent", "donc", "dont", "douze", "douzième", "dring", "du", "duquel",
    "durant", "dès", "désormais", "e", "effet", "egale", "egalement", "egales",
    "eh", "elle", "elle-même", "elles", "elles-mêmes", "en", "encore", "enfin",
    "entre", "envers", "environ", "es", "est", "et", "etant", "etc", "etre",
    "eu", "euh", "eux", "eux-mêmes", "exactement", "excepté", "extenso",
    "exterieur", "f", "fais", "faisaient", "faisant", "fait", "façon",
    "feront", "fi", "flac", "floc", "font", "g", "gens", "h", "ha", "hein",
    "hem", "hep", "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp",
    "hue", "hui", "huit", "huitième", "hum", "hurrah", "hé", "hélas", "i",
    "il", "ils", "importe", "j", "je", "jusqu", "jusque", "juste", "k", "l",
    "la", "laisser", "laquelle", "las", "le", "lequel", "les", "lesquelles",
    "lesquels", "leur", "leurs", "longtemps", "lors", "lorsque", "lui",
    "lui-meme", "lui-même", "là", "lès", "m", "ma", "maint", "maintenant",
    "mais", "malgre", "malgré", "maximale", "me", "meme", "memes", "merci",
    "mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "minimale",
    "moi", "moi-meme", "moi-même", "moindres", "moins", "mon", "moyennant",
    "multiple", "multiples", "même", "mêmes", "n", "na", "naturel",
    "naturelle", "naturelles", "ne", "neanmoins", "necessaire",
    "necessairement", "neuf", "neuvième", "ni", "nombreuses", "nombreux",
    "non", "nos", "notamment", "notre", "nous", "nous-mêmes", "nouveau", "nul",
    "néanmoins", "nôtre", "nôtres", "o", "oh", "ohé", "ollé", "olé", "on",
    "ont", "onze", "onzième", "ore", "ou", "ouf", "ouias", "oust", "ouste",
    "outre", "ouvert", "ouverte", "ouverts", "o|", "où", "p", "paf", "pan",
    "par", "parce", "parfois", "parle", "parlent", "parler", "parmi",
    "parseme", "partant", "particulier", "particulière", "particulièrement",
    "pas", "passé", "pendant", "pense", "permet", "personne", "peu", "peut",
    "peuvent", "peux", "pff", "pfft", "pfut", "pif", "pire", "plein", "plouf",
    "plus", "plusieurs", "plutôt", "possessif", "possessifs", "possible",
    "possibles", "pouah", "pour", "pourquoi", "pourrais", "pourrait",
    "pouvait", "prealable", "precisement", "premier", "première", "quatre",
    "premièrement", "pres", "probable", "probante", "procedant", "proche",
    "près", "psitt", "pu", "puis", "puisque", "pur", "pure", "q", "qu",
    "quand", "quant", "quant-à-soi", "quanta", "quarante", "quatorze",
    "quatre-vingt", "quatrième", "quatrièmement", "que", "quel", "quelconque",
    "quelle", "quelles", "quelqu'un", "quelque", "quelques", "quels", "qui",
    "quiconque", "quinze", "quoi", "quoique", "r", "rare", "rarement", "rares",
    "relative", "relativement", "remarquable", "rend", "rendre", "restant",
    "reste", "restent", "restrictif", "retour", "revoici", "revoilà", "rien",
    "s", "sa", "sacrebleu", "sait", "sans", "sapristi", "sauf", "se",
    "sein", "seize", "selon", "semblable", "semblaient", "semble", "semblent",
    "sent", "sept", "septième", "sera", "seraient", "serait", "seront", "ses",
    "seul", "seule", "seulement", "si", "sien", "sienne", "siennes", "siens",
    "sinon", "six", "sixième", "soi", "soi-même", "soit", "soixante", "son",
    "sont", "sous", "souvent", "specifique", "specifiques", "speculatif",
    "stop", "strictement", "subtiles", "suffisant", "suffisante", "suffit",
    "suis", "suit", "suivant", "suivante", "suivantes", "suivants", "suivre",
    "superpose", "sur", "surtout", "t", "ta", "tac", "tant", "tardive", "te",
    "tel", "telle", "tellement", "telles", "tels", "tenant", "tend", "tenir",
    "tente", "tes", "tic", "tien", "tienne", "tiennes", "tiens", "toc", "toi",
    "toi-même", "ton", "touchant", "toujours", "tous", "tout", "toute",
    "toutefois", "toutes", "treize", "trente", "tres", "trois", "troisième",
    "troisièmement", "trop", "très", "tsoin", "tsouin", "tu", "té", "u", "un",
    "une", "unes", "uniformement", "unique", "uniques", "uns", "v", "va",
    "vais", "vas", "vers", "via", "vif", "vifs", "vingt", "vivat", "vive",
    "vives", "vlan", "voici", "voilà", "vont", "vos", "votre", "vous",
    "vous-mêmes", "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z", "zut",
    "à", "â", "ça", "ès", "étaient", "étais", "était", "étant", "été",
    "être", "ô"
]


NEW_STOP_WORDS = [
    '', '?', '!', '@', 'ca', 'trouve', 'salut', 'grandpy',
    'connais', 'adresse', 'trouver', 'sais', 'déjà', 'deja', 'déja', 'déjà', ';'
]

APP_STOP_WORDS = BASE_STOP_WORDS + NEW_STOP_WORDS


INSUFFICIENT_INPUT_MSGS = [
    "Désolé loulou, j'ai pas bien compris ce que tu recherches",
    "Désolé mon enfant, va falloir m'en dire plus"
]

START_SEARCH_MSGS = [
    "Attends un peu que je me souvienne ...",
    "Ca me dit ptet' queq'chose, attends voir ...",
    "Minute papillon, faut faire démarrer le moteur ...",
    "Je suis trop vieux pour ces co*** ...",
    "Bouge pas ça va me revenir ..."
]

NO_LOCATION_MSGS = [
    "Ca m'dit un truc mais impossible de m'en souvenir, tu peux être plus \
précis ?",
    "Rah j'ai la mémoire qui flanche, tu peux m'aider un peu en étant plus \
précis ?",
    "T'es sûr que ça existe ça ? C'est vers où ?"
]

LOCATION_FOUND_MSGS = [
    "Si ma mémoire est bonne, l'adresse c'est ",
    "Oula ça me revient, l'adresse c'est "
]

WIKIPEDIA_INTRO_MSGS = [
    "D'ailleurs laisse moi te dire un petit truc à ce propos. ",
    "J'sais pas si tu sais mais laisse moi te raconter un truc. "
]

WIKIPEDIA_NOT_FOUND = [
    "Bon par contre j'ai rien à te dire sur ce lieu",
    "En revanche, je connais pas assez cet endroit pour t'en dire plus"
]

SHOW_OFF_MSGS = [
    "A part ça, je t'ai déjà raconté la fois où j'ai détruit un char en tirant \
dans le canon ?",
    "Sinon je t'ai déjà dit qu'une fois j'ai retrouvé un soldat allié en \
sifflant 'tea for two' sous la douche publique.",
    "Ils sont marrant tes habits, tu me rapelles ce jeune qui, en '55, m'avait\
 dit qu'il venait du futur, c'était un original çui-là.",
    "Sinon aujourd'hui j'ai croisé un grand monsieur, il m'a rapellé un autre,\
 en '84, qui cherchait une Zara Commore, ou quelqu'chose du genre.",
    "A part ça, tu sais qui gagnerait entre Rocky et un serpent ? Rocky, \
Rocky Balboa !",
    "Voilà, maintenant pense bien à mettre des chaussures, j'ai marché sur du \
verre une fois que je combattais des terroristes allemands, ça fait mal",
    "Sinon j'ai été acteur y a 30 ans tu sais ? Je devais faire chaque jour \
des gestes du quotidien dans un village sous une grande sphère de métal"
]
