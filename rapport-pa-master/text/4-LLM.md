# Les Large Language Models (LLM)

## Description Générale

Les Large Language Models (+LLM_a), représentent une classe de systèmes d' (+IA_a) dotés de capacités avancées dans le domaine du traitement automatique du langage naturel, aussi appelé (+NLP_a). Ils se caractérisent par leur aptitude à analyser, comprendre et générer du texte, simulant ainsi les compétences linguistiques humaines. Ces modèles sont capables de telles prouesses du fait qu'ils sont entraînés sur de très vastes ensembles de données textuelles.

L'émergence des (+LLM_a) est intrinsèquement liée aux progrès fulgurants de l' (+IA_a). Une étude menée par Deng Cai [@RAG_recent_advances] sur les récents avancements des (+RAG_a) évoque des avancées significatives dans le domaine de l'apprentissage automatique et de la data science qui sont à l'origine de ces évolutions. Notamment dues à la disponibilité croissante de puissantes infrastructures informatiques et des (+GPU_a) de plus en plus performants, ces dernières ont surtout bénéficié de l'abondance de données accessibles en ligne. Coïncidant avec des percées majeures dans la conception d'architectures de réseaux de neurones profonds, les (+LLM_a) ont réellement émergé à la fin des années 2010 grâce à des outils révolutionnaires tels que les transformers proposés par Vaswani et al. en 2017.

Cependant, il faut attendre le début des années 2020 pour les voir devenir des outils incontournables. Ils jouent, par exemple, un rôle essentiel dans l'automatisation de tâches, la traduction automatique ou encore la rédaction de contenu. Ils bénéficient de leurs immenses corpus de données utilisés pour les entrainer afin de produire un langage fluide et cohérent dans une multitude de langues. 

Un exemple concret d'application et d'utilisation des (+LLM_a) est celui des assistants virtuels (chatbots). Capables de répondre aux questions des utilisateurs avec une grande précision grâce à leur aptitude à comprendre le langage naturel, ils interagissent de manière efficace et personnalisée comme le fait ChatGPT-4 d'OpenAI.

## Fonctionnement détaillé

Un (+LLM_a) peut se voir comme une boite noire qui prend en entrée un certain nombre de phrases et qui répond par d'autres phrases. En réalité, le fonctionnement peut être découpé en deux étapes clés : la tokenisation et la génération de texte.

### La tokenisation

Ce premier processus consiste à découper un texte écrit par l'utilisateur en unités discrètes appelées "tokens". Le (+LLM_a) n'etant pas capable de comprendre le texte à proprement parler, il se base sur ces tokens pour traiter le texte. Basés sur des réseaux de neurones profonds, ce type de modèle n'est pas en mesure de traiter autre chose que des nombres. Il existe donc différentes stratégies permettant de transformer un texte en une séquence de tokens (de nombres) compréhensible par le modèle. Mais toute la complexité derrière cette tâche réside dans le fait que le sens des mots et des phrases doit être préservé à mesure que la dimensionnalité du texte réduit. En d'autres termes, même si le modèle transforme le texte en nombres, il doit être capable de comprendre le sens des phrases initiales pour générer une réponse pertinente.

La découpe du texte peut être faite de différentes manières, un token pouvant aussi bien représenter un mot, une sous-unité de mot ou même un seul caractère. Des procédés extrêmement simples peuvent être utilisés, comme la séparation des mots par des espaces. Ici, chaque mot est donc associé à un token. D'autres approches comme la décomposition en "subword tokens" permettent de gérer des structures grammaticales un peu plus complexes en ramenant les mots à leur forme canonique (aussi appelée "lemme"). On parle alors de lemmatisation, comme dans le cas du mot "manger" qui serait ramené à son lemme "mange" plutôt que sa racine "mang".

Bien qu'elles réduisent la taille du vocabulaire, ces méthodes ne permettent cependant pas de gérer avec une grande précision les structures de phrases plus complexes. Introduit en 1994 par Philip Gage dans un article intitulé "A New Algorithm for Data Compression", le Byte Pair Encoding (+BPE_a) se démarque alors comme une technique de compression de données qui découpe le texte en groupes de caractères. Très majoritairement utilisée aujourd'hui, elle permet de réduire la dimensionnalité du texte tout en conservant le sens général des phrases dans lesquelles ces mots sont employés. 

Cette solution a été adaptée pour le traitement du langage naturel afin de devenir sans conteste la méthode de tokenisation la plus performante. Dans le cadre des (+LLM_a), le (+BPE_a) n'est alors plus utilisé uniquement pour compresser des données, mais aussi et surtout pour décomposer astucieusement le texte en tokens, facilitant ainsi le traitement linguistique opéré par la suite.

Cette technique commence par traiter chaque caractère comme un token, puis fusionne progressivement les paires de tokens les plus fréquemment adjacentes pour former de nouveaux tokens plus grands. Ce processus itératif se poursuit jusqu'à ce qu'un vocabulaire ciblé soit atteint. Le (+BPE_a) réduit efficacement la taille du vocabulaire nécessaire en traitant à la fois des mots entiers fréquents et en décomposant des mots rares en sous-chaînes gérables par le (+LLM_a). Voici un exemple de tokenisation avec (+BPE_a):

\cimg{figs/tokenisation.png}{width=\textwidth}{Exemple de tokenisation avec GPT-3}{Source : OpenAI, ref. URL01}

Cette image permet de constater que le texte est découpé en groupes de caractères de différentes tailles. Au premier abord, il semblerait que la séparation n'ait aucun sens, mais en réalité, c'est une méthode très efficace pour que le modèle puisse comprendre le sens global du texte. Cette image montre une technique de tokenisation propre à OpenAI et ses modèles GPT intitulée tiktoken[^2]. C'est une variante de (+BPE_a), open source, pour laquelle un token généré correspond à environ quatre caractères et 100 tokens valent environ 75 mots. 

D'autres dérivations de (+BPE_a) existent, comme SentencePiece[^3] qui combine (+BPE_a) et Unigram pour offrir davantage de flexibilité dans la taille du vocabulaire. Cette méthode est connue pour permettre d'avoir une meilleure représentation des contextes, de réduire l'ambiguïté et de s'adapter à différentes langues. C'est notamment la méthode utilisée par les modèles Llama du groupe Meta AI. Basée sur des modèles de langues plus complexes, elle combine (+BPE_a) et Unigram pour offrir plus de flexibilité au niveau de la taille du vocabulaire. À l'inverse, tiktoken possède l'avantage de gérer beaucoup plus efficacement les mots fréquents et rares tout en réduisant la taille du vocabulaire.

Des librairies Python comme SpaCy[^4] ou NLTK[^5] proposent des outils pour réaliser ce genre de tâche, mais elles ne sont que très rarement implémentées dans les (+LLM_a) à cause de leur complexité et de leur coût en ressources.

Comprendre comment fonctionne la tokenisation d'un (+LLM_a) que l'on utilise est essentiel pour utiliser le modèle de manière efficace. D'après une conférence réalisée par Andrej Karpathy [@Andrej_Karpathy], ancien directeur de l' (+IA_a) chez Tesla et spécialiste en Deep Learning chez OpenAI, la tokenisation explique à elle seule pourquoi les (+LLM_a) ne sont pas toujours capables d'épeler des mots, ne sont pas aussi bons dans une autre langue que l'anglais, ou encore pourquoi ils ne sont pas capables de faire des calculs arithmétiques simples. 

Si les techniques de tokenisation sont souvent des "boites noires" dans l'architecture des (+LLM_a), une étude approfondie menée par Mehdi Ali et Michael Fromm [@tokenizer_choice] montre que le choix du tokeniser peut avoir un impact significatif sur les performances du modèle, les coûts d'entraînement ainsi que l'inférence. En effet, une mauvaise tokenisation pourrait avoir comme effet de ne pas bien comprendre le sens des phrases. D'autre part, une mauvaise réduction du vocabulaire pourrait augmenter la taille du modèle et donc les coûts d'entraînement. 

Un exemple fréquemment évoqué est celui de la tokenisation multilingue. Un modèle dont le tokeniser est centré sur l'anglais pourrait avoir des difficultés à traiter d'autres langues. Toujours selon cette étude, il semble que les tokenisers multilingues entraînés sur les cinq langues européennes les plus fréquentes nécessitent une augmentation de la taille du vocabulaire de trois fois par rapport à l'anglais. C'est donc un prix à payer pour permettre une meilleure polyvalence du modèle.

### L'embedding

Les mots maintenant transformés en tokens, il reste à les représenter de manière que le modèle puisse les manipuler. Les tokens sont représentés dans un espace latent, c'est-à-dire un espace de dimension réduite, comme des vecteurs. Ce sont précisément ces vecteurs qui sont utilisés par le modèle pour apprendre les relations entre les tokens.

Cette phase d'apprentissage est réalisée par des réseaux de neurones profonds qui sont des modèles mathématiques inspirés du fonctionnement du cerveau humain. Ce sont des unités de calcul interconnectées capables d'apprendre des représentations hiérarchiques de données. Voici un exemple de représentation vectorielle de tokens :

\pagebreak

\cimg{figs/word_embedding.png}{width=\textwidth}{Exemple de représentation vectorielle de tokens}{Source : Blent.ai, ref. URL02}

Cette image montre comment les mots sont représentés dans un espace latent. L'embedding est infimement lié à la tokenisation, car c'est à partir des tokens que les vecteurs d'embeddings sont générés. Après une phase d'apprentissage permettant de capturer les relations sémantiques et syntaxiques entre les tokens, le modèle est capable de générer du texte cohérent avec les tokens qu'il a reçus en entrée.

### La génération de texte

La génération de texte n'est en réalité ni plus ni moins qu'un assemblage de tokens qui ont, eux-mêmes, été appris par le modèle. Lorsque le (+LLM_a) répond à une question, il ne fait rien d'autre que de générer des tokens selon un processus itératif où le choix du token suivant est conditionné par la probabilité de s'intégrer au mieux dans le sens de la phrase. 

L'ensemble du texte donné en entrée du modèle est appelé contexte. Ce dernier, décomposé en tokens, est passé à travers plusieurs couches de neurones qui permettent de capturer les relations entre les tokens et de comprendre, d'une certaine manière, le sens du texte. De cette manière, le modèle est capable de générer des tokens qui s'intègrent bien dans le contexte initial. Par exemple, si le modèle reçoit en entrée "Quelle est la capitale de la Suisse", il est capable de générer "Berne" en sortie.

\pagebreak

Le modèle est capable de faire cela grâce à cette même étape de capture des relations entre les tokens qui a été faite pendant la phase d'entrainement. En supposant que le corpus de texte qui lui a été donné d'apprendre est suffisamment grand pour qu'il puisse avoir appris à un moment où à un autre que les mots "capitale" et "Suisse" sont fortement liés au mot "Berne" dans l'espace latent, il prédira que le mot "Berne" est le plus probable de répondre à la question. Bien évidemment, le modèle ne répond pas tel quel, il est entrainé à répondre de manière plus complexe, en générant des phrases entières. 

En réalité, les vecteurs d'embedding sont passés à travers des couches de neurones qui permettent de générer des logits. Ces derniers sont ensuite transformés en probabilités par une fonction softmax. Le choix du token le plus adapté est alors fait en fonction de la probabilité conditionnelle la plus élevée associée aux vecteurs d'embedding. Cette technique est appelée échantillonnage stochastique :

\cimg{figs/generation.png}{width=\textwidth}{Exemple de génération de token avec GPT-3}{Source : OpenAI, ref. URL01}

Cette simple étape d'échantillonnage n'est cependant pas assez fiable pour être utilisée telle quelle. En effet, il n'est pas du tout garanti que le token le plus probable soit le plus adapté. C'est pourquoi d'autres techniques sont utilisées pour améliorer la qualité de la génération de texte. On note principalement trois méthodes qui sont le Greedy Sampling, le Beam Search et le Random Sampling. Ce sont tous des mécanismes d'attention qui aident à pondérer l'importance des tokens en fonction du contexte complet. D'après [@greedy_vs_beam_search] qui référence plusieurs heuristiques, le Greedy Sampling, le plus simple, choisit le token le plus probable à chaque étape sans explorer d'autres possibilités. Sur le plan computationnel, c'est une méthode très efficace, mais cela peut conduire à des résultats peu diversifiés, voire déterministes. D'autre part, le Beam Search (ou recherche par faisceaux) est une amélioration du Greedy Sampling qui garde en mémoire les k tokens les plus probables à chaque étape. Voici une comparaison entre ces deux méthodes :

\pagebreak

\cimg{figs/beam_vs_greedy.png}{scale=0.4}{Comparaison entre une recherche Greedy et Beam}{Source : HuggingFace, ref. URL03}

Cette image permet de mettre en avant les différences entre les deux solutions, autant du point de vue de la complexité algorithmique que de la qualité de la séquence produite. Le Beam Search est, en effet, plus complexe, mais permet d'obtenir des résultats plus diversifiés et plus cohérents. 

Une étude réalisée sur les différentes méthodes de génération de texte neuronal [@neural_text_generation] évoque aussi une troisième méthode, le Random Sampling, qui consiste à choisir un token de manière aléatoire en fonction de sa probabilité. C'est une méthode qui permet d'obtenir des résultats très diversifiés, mais qui peut être difficile à contrôler. C'est pourquoi, il est souvent utilisé en combinaison avec d'autres méthodes pour obtenir des résultats plus cohérents comme le Top-k Sampling ou le Nucleus Sampling.

### L'entraînement des modèles

Pour comprendre la manière dont les tokens sont déterminés pour la génération de texte, il a été fait mention plus tôt d'une phase d'entrainement du modèle. Cette dernière permet de capturer les relations entre les tokens, qui, eux-mêmes, réduisent la dimensionnalité de l'immense corpus de texte sur lequel le modèle doit être entrainé. Les ressources nécessaires pour réaliser cette tâche sont donc plus que considérables. Un entraînement de (+LLM_a) se fait généralement en deux étapes : le pré-entraînement et le fine-tuning.

Lors du pré-entraînement, le modèle ingère de vastes ensembles de données textuelles non labellisées, souvent non structurées, et s'entraine à capturer la structure et les schémas du langage. On parle alors d'apprentissage auto-supervisé. C'est précisément cette étape qui est la plus coûteuse en ressources.

\pagebreak

Dans cette phase souvent décrite comme un apprentissage par transformer, le modèle est exposé à des exemples de données pour lesquels les poids des connexions entre les neurones sont ajustés afin de minimiser l'erreur de prédiction. Cela revient à capturer les relations sémantiques et syntaxiques entre les tokens, qui permettront, par la suite, de choisir les tokens suivants en fonction des logits. 

Les corpus de textes comprennent généralement des articles en ligne, des livres ou des extraits de conversations, dans le but d'acquérir une compréhension approfondie des relations syntaxiques et sémantiques du langage. Le but est de représenter de la façon la plus fidèle possible la structure du langage naturel en capturant tout type de structure grammaticale, traditionnellement dans plusieurs langues. Pour la plupart des (+LLM_a) connus du grand public, il ne semble pas possible de savoir dans les détails sur quoi ces derniers sont entraînés. Il est cependant estimé que les modèles les plus performants soient entraînés sur des corpus de plusieurs centaines de milliards de tokens, comme GPT-3 qui a été entraîné sur 570 Go de texte brut, soit environ 45 To de données tokenisées.

À la fin du pré-entraînement, le modèle est en théorie capable d'être utilisé comme une auto-complétion de texte. Pour qu'il puisse être utilisé dans des tâches plus complexes, il est alors nécessaire de le fine-tuner sur des tâches spécifiques à l'aide de données labellisées. Cette phase de fine tuning supervisée vise à adapter les poids du modèle pour une tâche particulière, telle que la traduction automatique, la génération de résumés ou la classification de texte.

En d'autres termes, quand un utilisateur pose une question à un (+LLM_a), il faut que le modèle soit capable de reprendre les mots de la question pour générer une réponse qui se rapproche au mieux de ce qu'un humain pourrait faire. Pour cela, il est nécessaire de lui fournir des exemples de questions et de réponses de sorte qu'il puisse apprendre à générer des réponses pertinentes.

Selon le (+LLM_a), la façon de labelliser les données peut changer, mais l'objectif et la démarche restent toujours les mêmes. Pour rentrer dans les détails architecturaux, le modèle entraîné peut être vu comme une superposition de couches qui possèdent chacune des rôles précis. Les couches supérieures du modèle sont généralement dédiées à l'apprentissage de tâches spécifiques comme la traduction ou la réponse aux questions, tandis que les couches inférieures, pré-entraînées sur des données non labellisées, conservent leur structure initiale. Cette approche permet d'exploiter les connaissances linguistiques générales acquises lors du pré-entraînement, tout en adaptant le modèle aux particularités des tâches que l'on souhaite le voir réaliser, comme de la traduction automatique ou de la génération de texte.

\pagebreak

Contrairement au fine tuning supervisé traditionnel, qui se concentre sur l'optimisation des performances objectives en fonction de métriques prédéfinies, le fine tuning basé sur les préférences humaines vise à ajuster le modèle pour produire des résultats qui correspondent donc aux préférences subjectives des utilisateurs. 

Cette approche implique nécessairement de solliciter des retours humains sur les sorties générées par le modèle et d'utiliser ces informations pour mettre à jour les poids du réseau. Par exemple, dans le domaine de la génération de texte, les utilisateurs peuvent fournir des commentaires sur la qualité, la pertinence ou la cohérence des phrases générées, ce qui permet d'ajuster progressivement le comportement du modèle pour mieux répondre aux attentes des utilisateurs. C'est aussi à cette étape qu'on intervient pour interdire certains cas d'utilisation ou pour corriger des biais.

## Etude comparative

Il peut s'avérer très judicieux de comparer les modèles les plus connus et les plus actuels afin d'identifier des métriques de comparaison pertinentes et intemporelles, même si l'analyse ne compte que les modèles sortis avant Avril 2024.

### GPT-4

Développé par OpenAI et inauguré en mars 2023, GPT-4 se présente comme un jalon remarquable dans le domaine de l'intelligence artificielle conversationnelle, s'établissant rapidement comme une référence grâce à sa notoriété auprès du grand public. Cette prouesse technologique repose sur une architecture de type transformer, dotée de 1,5 trillion de paramètres qui témoigne de sa capacité à modéliser le langage naturel. 

Entraîné sur des immenses corpus de données analogues à WebText, GPT-4 se distingue par ses performances inégalées sur divers benchmarks comme [@HELM_evaluation], attestant de ses compétences avancées en compréhension et en génération de texte. Accessible via l'(+API_a) d'OpenAI, il offre un support multilingue très poussé et permet de customiser les prompts afin d'améliorer significativement ses performances sur des tâches spécifiques grâce à une quantité folle de 128 000 tokens de contexte. 

Les différentes techniques de fine-tuning utilisées telles que le Reinforcement Learning from Human Feedback (RLHF) ou la maîtrise du contrôle de température et de max_tokens affirment la position de GPT-4 comme leader dans l'évolution des systèmes de compréhension et de génération du langage naturel. La grande taille de ce modèle peut toutefois poser de gros défis en termes de déploiement, à tel point qu'il n'est disponible que via (+API_a).

### Gemini

Lancé par Google en réponse directe aux avancées réalisées par OpenAI avec ChatGPT, Gemini se positionne comme un acteur significatif dans l'espace des (+LLM_a) avec une architecture sophistiquée dotée de 1.6 trillion de paramètres, entraîné, lui aussi, sur un corpus similaire à WebText. L'un des objectifs principaux de l'entraînement de Gemini réside dans l'exécution de tâches nécessitant un raisonnement très approfondi, ce qui lui permet de se distinguer par sa capacité à générer des explications scientifiquement précises et détaillées. 

Sa conception est particulièrement axée sur l'apport de réponses dans des domaines nécessitant une expertise spécifique, marquant ainsi une évolution notable dans l'habileté des modèles de langage à traiter et à fournir des informations complexes. L'accessibilité de Gemini se fait via (+API_a) mais n'est pas disponible en Suisse pour l'instant. 

Les possibilités de personnalisation et d'accès restent davantage restreints, en raison de la nature propriétaire de la technologie. Si l'une de ses forces est son aspect multimodal, il est souvent mentionné que le multilingue peut être limité comparé aux autres solutions propriétaires.

### LLaMA-2

En juillet 2023, Meta AI propose LLaMA-2 qui vient se positionner comme une innovation majeure dans le paysage des (+LLM_a). Avec des modèles allant de sept à 70 milliards de paramètres, ce dernier incarne une architecture avancée et entraînée sur un corpus comprenant divers contenus extraits d'Internet. Voici un graphique montrant son fonctionnement général :

\cimg{figs/llama-2}{scale=0.4}{Schématisation du fonctionnement de Llama-2}{Source : Meta, ref. URL04}

Ce graphique aide à visualiser la manière dont le modèle fonctionne, en particulier comment il traite les données et comment fonctionne son entraînement. L'objectif central derrière LLama-2 est d'accorder une attention particulière à la modélisation linguistique, soutenue par des capacités multimodales très avancées.

Celles-ci permettent à LLaMA-2 de traiter et de générer du texte en association avec d'autres modalités sensorielles, étendant ainsi son application au-delà des simples tâches textuelles pour inclure des interactions impliquant des données visuelles ou auditives.

Offrant des optimisations pour réduire les exigences en matière de puissance de calcul, Meta AI propose ce modèle de manière open source avec une limite fixée à 4 000 tokens de contexte. Surtout utilisée pour le fine-tuning, cette version open source est appréciée pour sa polyvalence et sa capacité à s'adapter à diverses applications.

### Mistral

Mistral AI se présente comme une initiative innovante dans le domaine des modèles d'intelligence artificielle, en mettant l'accent sur le développement de modèles plus petits et efficaces, tels que Mistral 7B et Mixtral, des modèles de Sparse Mixture of Experts. Cette orientation vers l'efficacité ne compromet pas la performance, au contraire, Mistral AI affiche une compétitivité vraiment remarquable avec les modèles de pointe en offrant des capacités d'inférence rapide grâce à des techniques d'attention par requêtes groupées et par fenêtre glissante. 

Cependant, c'est surtout pour ses compétences avancées en matière de codage que Mistral AI se distingue aux yeux du grand public. Sous licence Apache 2.0, disponible sur HuggingFace et déployable sur des plateformes cloud, c'est le modèle qui offre la plus grande flexibilité en termes d’intégration pour les utilisateurs. Voici un graphique des scores proposés par Mistral AI :

\cimg{figs/mistral-ai}{scale=0.5}{Mistral AI comparés aux autres modèles du même rang}{Source : Mistral AI, ref. URL05}

\pagebreak

D'après ce graphique, il semblerait que Mistral AI se positionne comme un modèle très performant comparé à ses concurrents directs accessibles via (+API_a). Avec une fenêtre de contexte étendue à 8 000 tokens, ces modèles se prêtent bien à des applications nécessitant une compréhension approfondie, telles que les applications de chat ou la compréhension et la génération de code. Mistral AI dispose de modèles de plus petite taille, comme Mistral 7B ou 8x7B qui permettent de réduire les coûts de calcul afin de faciliter le déploiement sur des appareils avec des ressources limitées.

### Quelques autres modèles

D'autres modèles peuvent présenter un certain intérêt comme Flan-UL2, BLOOM ou Anthropic (Claude 3). Développé par Google Research, Flan-UL2 est un modèle de 20 milliards de paramètres qui s'appuie sur une méthode d'entraînement innovante, la Mixture-of-Denoisers (MoD), le rendant universellement efficace sur une variété de tâches de traitement du langage naturel (NLP). Bien que dépourvu de capacités multimodales, il excelle dans le traitement et la génération de texte en plusieurs langues, mais son accessibilité n'est pas précisée. 

BLOOM, développé par le BigScience Workshop, est un modèle massif de 176 milliards de paramètres entraîné sur un corpus web multilingue qui se distingue par ses compétences d'optimisation du texte en fonction du style, du ton ou de la lisibilité. Modèle open source, il dispose d'une fenêtre de contexte de 2 000 tokens. 

Enfin, Claude 3, proposé par Anthropic se démarque par son orientation vers la sécurité et l'alignement des valeurs dans l'IA, offrant des capacités multilingues, de traitement de la vision et de facilité de direction. Certains benchmarks comme [@HELM_evaluation] le place devant Llama-2 en termes de performance bien qu'il ne soit pas possible de tester ce modèle actuellement.

### Plusieurs axes de comparaison

Après avoir vu plusieurs modèles aux architectures et objectifs variés, il semble intéressant de les comparer pour mieux comprendre leurs différences. Au premier abord, les modèles comme GPT-4, Gemini et LLaMA-2 se distinguent par leur taille et leur capacité à traiter des tâches complexes, tandis que Mistral se démarque par son efficacité et sa flexibilité. Les modèles comme Flan-UL2, BLOOM et Anthropic (Claude 3) offrent des fonctionnalités spécifiques qui les rendent attrayants pour des applications particulières. On distingue déjà une première séparation marquée par la différence entre les modèles open-source et les modèles propriétaires. 

\pagebreak

Souvent optimisés pour une utilisation en production, les modèles propriétaires sont rarement autorisés à être inspectés, modifiés ou personnalisés. D'après [@LLM_overview], ils ne sont pas toujours disponibles gratuitement et ne permettent pas aux utilisateurs de contrôler les données qui sont utilisées pour l'entraînement. 

Ces derniers doivent donc faire confiance au propriétaire du modèle pour garantir un engagement envers la protection de la vie privée des données et l'utilisation responsable de l'IA. Les modèles propriétaires sont fréquemment beaucoup plus grands du fait qu'ils bénéficient de plus de ressources pour leur développement. Cela ne garantit cependant pas toujours des performances supérieures. 

On retrouve dans cette catégorie les modèles d'OpenAI, Google Gemini ou Claude 3. Avec le nombre estimé d'utilisateurs actifs de ChatGPT dépassant les 180 millions et un nombre récent de mises à jour époustouflantes, il est facile d'oublier qu'il existe en réalité de nombreux autres (+LLM_a). En fait, il y a même plus de modèles open source qui ont été publiés dernièrement que de modèles propriétaires. 

Voici un graphique qui montre le nombre de modèles open source et propriétaires introduits au fil des années :

\cimg{figs/llm_comparaisons.png}{scale=0.4}{Répartition des nouveaux LLM depuis 2019}{Source : A Comprehensive Overview of LLM, ref. URL06}

Ce graphique montre que le nombre de modèles open source introduits a augmenté de manière significative ces dernières années, ce qui suggère une tendance croissante vers l'ouverture et la collaboration dans le domaine des (+LLM_a). Mis à disposition du public, ils peuvent être modifiés et personnalisés, mais ne sont pas toujours aussi optimisés et performants que les modèles propriétaires. 

\pagebreak

On retrouve dans cette catégorie des modèles comme LLaMA-2, Mistral ou Flan-UL2. L'aspect open-source de ces modèles permet une plus grande transparence et une plus grande confiance dans les résultats produits, bien qu'ils puissent être plus difficiles à déployer et à maintenir, car ils nécessitent souvent des ressources supplémentaires pour être utilisés efficacement. 

Les modèles open-source sont généralement plus scalables et plus accessibles, ce qui les rend attrayants pour les chercheurs et les développeurs qui souhaitent personnaliser les modèles pour des tâches spécifiques. Des outils comme CodeGen pour les langages de programmation ou BloombergGPT pour la finance montrent une tendance vers le développement de modèles plus spécialisés pour une performance améliorée dans des domaines spécifiques et soutenus par la nature open-source de ces modèles. HuggingFace propose plusieurs benchmarks, dont [@HG_llm_leaderboard] pour comparer les performances des modèles open-source.

Du point de vue des performances, il est difficile de départager les modèles. Les benchmarks comme [@LLM_overview] ou [@HG_llm_leaderboard] montrent que les performances des modèles varient en fonction des tâches et des métriques utilisées :

\cimg{figs/helm_benchmark.png}{scale=0.23}{HELM Leaderboard}{Source : Stanford.edu, ref. URL07}

\pagebreak

Avec cet extrait du classement des (+LLM_a) réalisé le 01 Mars 2024, il paraît clair que les modèles propriétaires comme GPT-4 ou Gemini sont souvent en tête des classements, mais les modèles open-source comme LLaMA-2 ou Mistral ne sont pas loin derrière. Les performances des modèles dépendent de nombreux facteurs, notamment la taille du modèle, la qualité des données d'entraînement, les hyperparamètres utilisés, etc. 

L'utilisation de mécanismes d'attention, de fonctions d'activation (par exemple, ReLU, GeLU, variantes de GLU) et de techniques de normalisation des couches est fréquemment retrouvée dans les architectures des modèles les plus performants.

Le HELM leaderboard [@LLM_overview] (pour Holistic Evaluation of Language Models) est un bon exemple pour avoir une idée générale des performances des modèles. Il montre que les modèles propriétaires comme GPT-4 sont généralement en tête des classements, mais que les modèles open-source comme LLaMA-2 ou Mixtral ne sont pas loin derrière. 

On retrouve des métriques comme l'Exact Match (EM) pour évaluer la précision des réponses, le F1 pour évaluer la qualité des réponses, le BLEU-4 pour évaluer la qualité des traductions, le AI2 Reasoning Challenge (ARC) pour évaluer la capacité de raisonnement des modèles, etc. Ces métriques permettent de comparer les performances des modèles sur une variété de tâches et de domaines, ce qui donne une idée générale de leurs capacités.

## Des défis à relever

Cette section sur les (+LLM_a) permet de mettre la lumière sur la multitude de modèles disponibles et leurs caractéristiques spécifiques. Des solutions propriétaires qui garantissent des performances de pointe à des modèles open-source qui offrent une plus grande transparence et une plus grande flexibilité, il existe une variété de choix pour répondre aux besoins des utilisateurs. 

Les performances des modèles varient en fonction des tâches et des métriques utilisées, mais il est clair que les (+LLM_a) ont révolutionné le domaine du traitement automatique du langage naturel en offrant des capacités de compréhension et de génération de texte sans précédent. 

Cependant, malgré leur puissance et leur polyvalence, ces modèles sont confrontés à plusieurs défis critiques qui limitent leur fiabilité et leur applicabilité dans des scénarios du monde réel. 

\pagebreak

Entrainés sur d'énormes corpus de texte collectés sur Internet, les (+LLM_a) sont inévitablement exposés à des biais présents dans ces données d'entraînement. D'après [@LLM_overview], il est important de comprendre comment les biais se propagent dans les modèles de langage et comment ils peuvent être atténués pour garantir des résultats fiables. 

De plus, [@LLM_overview] précise que les (+LLM_a) ont tendance à générer du texte qui ne présente parfois pas de sens. Ces cas d'utilisation sont souvent provoqués par le fait que les informations apprises par le modèle ne sont plus forcément à jour ou simplement qu'il ne connaisse pas la réponse mais essaye d'y répondre quand même en fournissant de fausses informations. 

Dans une toute autre mesure, [@LLM_overview] évoque aussi des considérations éthiques qui englobent une gamme de problématiques, allant de la transparence de l'entraînement des modèles et de leur fonctionnement à l'impact sociétal de leur déploiement. Les questions relatives à la vie privée des données, au consentement implicite dans les données d'entraînement et à l'autonomie dans la prise de décision soulignent la complexité de ces enjeux. 

On parle généralement de considérations réfléchies et mesurées dans le développement des (+LLM_a) puisque le choix des données d'entraînement peut avoir un impact majeur sur le comportement du modèle qui peut s'avérer discriminatoire dans des conditions extrêmes.

Lorsque les résultats sont incorrects, beaucoup parlent d'un phénomène d'hallucination associé aux données générales utilisées pour l'entraînement. Ce terme fait référence à la tendance des (+LLM_a) à générer des informations fausses ou non vérifiées présentées comme des faits. Les réponses à des questions posées sont présentées de manière convaincante, même en l'absence de bases factuelles solides. Elles peuvent compromettre la fiabilité des applications basées sur des (+LLM_a), notamment dans des domaines sensibles tels que la santé, le droit et l'information, où la précision des données est cruciale.

Toutes ces préoccupations ont conduit à l'exploration de solutions plus avancées telles que les (+RAG_a). Ces modèles hybrides, qui proposent des capacités de génération augmentée de texte grâce à une récupération d'informations externes, offrent une voie prometteuse pour surmonter les limites des (+LLM_a) traditionnels et améliorer leur précision et leur fiabilité. 

C'est aussi une manière très efficace d'utiliser les (+LLM_a) pour des tâches beaucoup plus spécifiques comme l'apprentissage d'une documentation spécifique à une entreprise. La section suivante se penchera sur l'analyse des (+RAG_a) en explorant leur fonctionnement et en essayant de répondre à toutes les questions qui peuvent se poser à leur sujet.

\pagebreak

[^2]: Disponible à l'adresse: \url{https://github.com/openai/tiktoken}
[^3]: Disponible à l'adresse: \url{https://github.com/google/sentencepiece}
[^4]: Disponible à l'adresse: \url{https://spacy.io/}
[^5]: Disponible à l'adresse: \url{https://www.nltk.org/}