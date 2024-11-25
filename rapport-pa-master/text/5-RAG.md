# Les Retrieval Augmented Generation Systems

## Description Générale

Si les (+LLM_a) offrent effectivement des capacités de compréhension et de génération de texte sans précédent, il n'en reste pas moins que certaines questions restent en suspens. La multiplication des données disponibles ainsi que la facilité d'accès en ligne font que les modèles peuvent être très rapidement rendus obsolètes. Il est souvent question de déterminer de quelle manière maintenir à jour les données utilisées. Un fine-tuning plus régulier pourrait aider, mais cela demanderait des ressources très importantes, ce n'est clairement pas une solution viable.

Plusieurs questions peuvent donc se poser quant à la fiabilité des réponses générées : est-ce que les informations sont encore fiables au moment où la question est posée ? Que se passe-t-il si le modèle ne connait tout simplement pas la réponse ? Dans quelles mesures est-il capable de produire des fausses réponses ? Ce genre de problématiques sont habituellement corrélées avec l'effet d'hallucination qui décrit la manière dont les (+LLM_a) mettent en avant d'inexactes informations pour tenter de répondre à tout prix.


En outre, il est fréquemment fait mention de limites au niveau de la taille du contexte des (+LLM_a). Si elle suffit généralement à tenir une discussion, elle peut être une forte limitation dans certains cas. Lorsqu'on demande au modèle de résumer un livre, par exemple, l'ensemble de son contenu est copié-collé dans le contexte. Selon la taille du contexte, il est assez facile de dépasser la limite des tokens autorisés. Dans ce cas, le modèle pourrait répondre sans tenir compte de l'ensemble des informations ou même refuser de répondre. C'est notamment le comportement de ChatGPT qui notifie un dépassement de la taille du contexte et coupe la discussion.

\pagebreak

La partie précédente a montré que le contexte est généralement limité entre 2 000 et 8 000 tokens en fonction des modèles. Pour la plupart des tokenisers actuels, cela veut dire que les utilisateurs sont limités à environ 12 pages de texte, ce qui peut s'avérer très contraignant. À travers cet ensemble de problèmes, les constats effectués montrent que les (+LLM_a) ne devraient pas uniquement se baser sur leurs connaissances générales pour répondre à des questions. C'est dans ce contexte que le groupe Meta fait émerger l'idée des (+RAG_a).

L'objectif de ces derniers est de mieux contextualiser les questions posées en allant chercher des informations vers des sources de données externes. Une étude sur l'utilisation des (+RAG_a) menée par Patrick Lewis en 2021 et supportée par le laboratoire de recherche en IA de Facebook [@RAG_for_NLP_tasks] fait une description du fonctionnement des (+RAG_a) qui pourrait être schématisée par la figure suivante :

\cimg{figs/rag_schema.png}{scale=0.4}{Schématisation du fonctionnement d'un RAG}{Source : Thomas Dagier}

Ce schéma mets en avant une architecture d'un (+RAG_a) divisée en trois modules : le chat, qui sert d'interface utilisateur, le (+LLM_a) qui est le modèle de génération de texte et la base de données qui contient les informations externes sur lesquelles s'appuyer avant de passer par le (+LLM_a). L'idée est de pouvoir ajouter des informations contextuelles à la question posée pour garantir des réponses plus précises.

\pagebreak

## Fonctionnement détaillé

### L'embedding des données

Pour aider les (+LLM_a) à répondre, il est donc indispensable d'ajouter au contexte des informations pertinentes provenant de documents qui ne sont pas publics ou qui seraient trop spécifiques pour être intégrés dans les connaissances générales des (+LLM_a).

Il n'est pas difficile d'imaginer que les informations mises à disposition des étudiants de la (+HEIAFR_a) n'ont probablement pas été utilisées pour entrainer un (+LLM_a). Même si c'était le cas, ces données sont susceptibles de changer régulièrement. Un (+LLM_a) seul ne suffit pas pour venir en aide aux étudiants. Par contre, couplé à un (+RAG_a), il serait capable de mettre en forme une réponse sans compter uniquement sur ses connaissances générales.
Sachant que le contexte est très limité, l'enjeu est de trouver un moyen de stocker des données de manière efficace, accessibles rapidement et qui permette d'identifier les informations les plus pertinentes à retourner au (+LLM_a). 

Comme pour ces derniers, il faut faire appel à des techniques d'embeddings. Il est possible de se baser sur des embeddings pré-entrainés ou de les générer à la volée (ce qui est souvent le cas pour les (+RAG_a) car les données sont assez spécifiques). Plusieurs techniques d'embeddings peuvent être utilisées pour générer des représentations numériques des documents. BERT (pour Bidirectional Encoder Representations from Transformers) est de loin l'algorithme le plus utilisé dans le contexte des (+RAG_a) du fait qu'il permette de générer des embeddings contextuels en traitant le texte dans les deux directions simultanément. Cette caractéristique le rend particulièrement efficace pour comprendre le contexte des mots dans une phrase.

Une variante de BERT, RoBERTa (pour Robustly Optimized BERT approach) est un modèle avec des hyperparamètres optimisés qui lui permettent d'obtenir de meilleures performances sur une variété de tâches de traitement du langage naturel. Plus coûteux en ressources que BERT, qui l'est déjà beaucoup, il nécessite un grand corpus de texte pour être entrainé. Toujours dans le même style que BERT, Sentence-BERT (SBERT) permet de générer des embeddings en réduisant la dimensionnalité afin d'accélérer la recherche d'informations bien qu'elle soit moins précise.

Moins utilisé, mais très efficace, Dense Passage Retrieval (DPR) est spécifiquement conçu pour améliorer la récupération d'informations dans les systèmes de questions-réponses. Grâce à des embeddings denses, DRP index et récupère des passages avec une très grande rapidité, mais peut s'avérer moins flexible que les autres solutions dans des domaines de (+NLP_a) différents.

\pagebreak

Bien que BM25 ne soit pas un algorithme d'embedding au sens traditionnel, il peut tout de même être intéressant de le mentionner en combinaison avec Elasitcsearch puisqu'il reste très performant sur de la recherche par mots-clés et très simple à mettre en place. Basé sur des embeddings denses, il reste néanmoins moins performant que DRP pour comprendre le contexte ou la sémantique profonde.

Dans un tout autre registre, les modèles GPT-3 et suivants montrent de très bons résultats pour générer des embeddings de texte grâce à leur conception leur permettant de comprendre et générer des réponses basées sur une vaste gamme de contextes et de styles de texte. Extrêmement polyvalent, les coûts d'inférence et d'enregistrement des données sont cependant très élevés.

Parmi toutes ces possibilités, les techniques intrinsèques de génération d'embeddings semblent cependant toutes s'inspirer d'une manière ou d'une autre du (+BPE_a) et du clustering de caractères. L'idée est de regrouper des caractères entre eux, puis d'en faire des regroupements cohérents pour finalement faire de l'overlap entre les séquences de texte pour conserver un minimum de contexte entre deux blocs successifs.

Plutôt que de réimplémenter ces techniques, il est possible de se tourner vers des frameworks d'embedding qui offrent des solutions prêtes à l'emploi. OpenAI propose divers modèles d'embedding, comme Ada, qui s'appuient sur des architectures de transformation avancées inspirées de GPT et d'autres modèles transformer. Sa facilité d'utilisation, sa polyvalence et le soutien d'une infrastructure cloud puissante en font un choix populaire pour les applications de (+NLP_a) bien que les utilisateurs dépendent des API d'OpenAI, ce qui peut impliquer des coûts ou des limitations d'utilisation.

Instructor-xl est un autre framework d'embedding qui se concentre sur des capacités d'attention à grande échelle et des architectures transformer optimisées pour des tâches d'embedding spécifiques. Bien que les détails spécifiques sur "Instructor-xl" soient moins communs dans la littérature publique, les modèles tendent à être optimisés pour des tâches spécifiques ou des performances accrues sur certains types de données. Son utilisation peut cependant nécessiter une familiarisation avec l'architecture pour une utilisation optimale.

Bien plus répandu, Multilingual-e5-large est un modèle conçu pour générer des embeddings de texte efficaces sur plusieurs langues, basé sur des architectures transformer telles que celles utilisées dans BERT ou ses variantes multilingues. Ce type de modèle est essentiel dans les applications nécessitant un support multilingue, offrant une compréhension et une représentation transversales des langues. Parfois moins précis pour des tâches spécifiques dans une langue unique, il reste cependant la méthode la plus accessible pour un public global.

\pagebreak

Peu importe la méthode ou le framework utilisé, un point crucial à prendre en compte pour générer des embeddings de qualité est la qualité des données en entrée. Il est essentiel de nettoyer les données pour éliminer les erreurs, les doublons et les informations inutiles, de même que les données bruitées ou mal formatées. Souvent chronophage, ce processus est relativement subjectif et doit être testé pas à pas en fonction des besoins spécifiques de chaque application.

La technique d'embedding qui est la plus connue et la plus utilisée dans le domaine du (+NLP_a) est sans doute celle de Word2Vec. Elle permet de générer des embeddings de mots en se basant sur la distribution des mots dans un corpus de texte. Les mots qui apparaissent fréquemment ensemble sont considérés comme similaires et sont donc représentés par des vecteurs proches dans l'espace vectoriel. Cette technique est très efficace pour capturer les relations sémantiques entre les mots et est généralement utilisée comme point de départ pour des tâches plus complexes. Cependant, elle n'est pas très évoquée ici, car elle n'est pas particulièrement intégrée dans les frameworks d'embedding modernes qui privilégient des approches plus avancées.

En plus du choix du framework, il est aussi très important de prendre en considération certaines politiques de sécurité et de confidentialité des données. Les données sensibles ou privées doivent être protégées et stockées uniquement lorsque cela est absolument nécessaire, puisqu'elles seront retournées telles quelles par le (+RAG_a) si elles sont stockées dans la base de données vectorielle.

### Les bases de données vectorielles

Les vecteurs d'embeddings sont des données numériques qui peuvent être stockées dans des bases de données vectorielles. Ces dernières sont des outils permettant de manipuler efficacement des vecteurs d'embeddings tout en établissant des relations sémantiques entre eux. C'est un peu l'équivalent de l'espace latent d'un (+LLM_a) mais pour des données structurées et stockées de manière persistante.

Le choix de cet outil est crucial pour répondre aux besoins du (+RAG_a) qui sont la rapidité de recherche et la pertinence des résultats retournés. Une étude paru en 2023 sur l'idée d'augmenter le contexte des (+LLM_a) réalisée par Bowen Peng [@LLM_context] a montré que la qualité des réponses générées est de moins en moins bonne à mesure que la taille du contexte augmente. Cela s'explique par le fait que les modèles ont parfois du mal à se concentrer sur les informations qui aident réellement à répondre à la question. 

\pagebreak

Dans la question : "Bonjour, je souhaiterais savoir quelle est la capitale de la Suisse, car un ami me l'a demandé avant-hier alors que nous étions au bar...", on retrouve beaucoup d'informations inutiles qui viennent perturber l'échantillonage stochastique (comme le fait que l'utilisateur était au bar) et qui peuvent mener à des réponses moins précises. Le (+RAG_a) venant nécessairement augmenter la taille du contexte, il est indispensable de trouver l'équilibre entre quantité et qualité lorsque l'on utilise la base de données vectorielle.

Une base de données vectorielle peut être décomposée en une phase d'indexation et une phase de recherche. L'indexation consiste à stocker les vecteurs d'embeddings de manière à ce qu'ils soient facilement accessibles lors de la recherche. Cette étape qui intervient à la suite de la génération des embeddings est cruciale pour garantir des temps de réponse rapides. Plusieurs algorithmes d'indexation peuvent être utilisés pour organiser les vecteurs dans l'espace vectoriel, tels que les KD-Trees, les arbres de recherche HNSW ou les index GIST.

L'utilisation des KD-Trees (arbres k dimensionnels) est particulièrement répandue pour l'indexation de données vectorielles qui concerne des documents texte. Ces arbres permettent de partitionner l'espace en régions pour une recherche efficace du plus proche voisin ou des recherches par intervalle. Bien que les KD-Trees soient plus efficaces avec des données de faible dimensionnalité, ils peuvent être utilisés conjointement avec des techniques de réduction de dimensionnalité quand les données sont complexes. 

Plusieurs frameworks et systèmes exploitent les KD-Trees pour l'indexation et la récupération efficaces de données spatiales. Scikit-learn, par exemple, est une bibliothèque Python populaire qui fournit des implémentations de KD-Trees. FLANN (pour Fast Library for Approximate Nearest Neighbors) et ANN (Approximate Nearest Neighbor) sont d'autres bibliothèques qui utilisent les KD-Trees pour l'indexation de données de haute dimension. 

Bien qu'il ne soit pas une base de données vectorielle au sens strict, Elasticsearch peut utiliser les KD-Trees (en réalité, les BKD-Trees) pour indexer et rechercher des vecteurs de grande dimension à travers son type "dense_vector". Une autre possibilité open-source, PostgreSQL, utilise les R-Trees pour l'indexation de données spatiales. Bien que n'étant pas directement une base de données vectorielle, cela montre l'adaptabilité des structures d'arbres dans les tâches d'indexation.

Enfin, Faiss (pour Facebook AI Similarity Search) qui utilise principalement des méthodes basées sur la quantification pour indexer plutôt que des KD-Trees, fournit un ensemble d'outils pour une indexation efficace et un clustering de vecteurs denses.

\pagebreak

Les KD-Trees sont des structures très intéressantes pour comprendre comment sont indexées les données dans une base de données vectorielle. Cependant, il est important de noter qu'à mesure que la dimensionnalité des données augmente, l'efficacité des KD-Trees diminue en raison du "curse of dimensionality". Dans de tels cas, d'autres structures de données ou méthodes d'indexation, telles que celles utilisées dans Faiss, peuvent offrir des solutions plus efficaces. 

La phase de recherche quant à elle consiste à interroger la base de données pour récupérer les vecteurs les plus pertinents en fonction de la question posée. Le choix des vecteurs d'embeddings à retourner dépend de la similarité entre les vecteurs stockés et ceux générés à partir du contexte venant du module de chat. Plusieurs métriques peuvent être utilisées pour évaluer la distance entre les vecteurs, telles que la similarité cosinus, la distance de Manhattan (L1) ou la distance euclidienne (L2).

Dans le cadre du projet, il n'est clairement pas intéressant de réimplémenter tout cela. Il est donc préférable de se tourner vers des bases de données vectorielles qui offrent des solutions prêtes à l'emploi. ChromaDB, par exemple, utilise des techniques avancées de partitionnement de l'espace vectoriel pour une indexation efficace de grandes bases de données. Cet outil est optimisé pour des performances élevées avec un accent particulier sur le traitement en parallèle et la distribution des données. Il supporte une large variété de types de données vectorielles et vise une intégration haute performance. C'est de loin la solution la plus performante pour des bases de données de grande taille et pour une intégration rapide dans un projet.

Pgvector, une extension de PostgreSQL, repose sur des approches linéaires et des index GIST pour l'indexation de données vectorielles. Plus adaptée pour des applications basées sur PostgreSQL, elle offre une bonne intégration avec des recherches vectorielles directement depuis une base de données existante. La performance de Pgvector est substantielle et dépend de la configuration du serveur de base de données. Sa force est sa faculté à stocker des vecteurs numériques comme extension de types de données PostgreSQL, ce qui facilite l'intégration avec des applications existantes. 

Qdrant, quant à lui, supporte plusieurs algorithmes, y compris les KD-Trees et HNSW pour l'indexation efficace de grandes bases de données vectorielles. C'est une solution conçue pour gérer efficacement des millions de vecteurs et offrir des temps de réponse rapides même avec de grandes bases de données. Cependant, la qualité des réponses dépendra beaucoup de l'implémentation qui peut s'avérer plus complexe que les autres solutions. Dans un autre registre, Redis possède une extension (RediSearch) supportant les vecteurs et possède un runtime extrêmement rapide en raison de son stockage en mémoire, idéal pour des opérations à faible latence. Limitée par la mémoire disponible, elle est très rapide pour des ensembles de données de taille modérée.

Il est important de noter que les bases de données vectorielles peuvent être exécutées localement, comme ChromaDB ou FAISS, mais aussi dans le Cloud, comme Pinecone ou Weaviate. Ces dernières offrent des solutions managées pour la gestion des données vectorielles, permettant de se concentrer sur le développement des applications plutôt que sur l'infrastructure sous-jacente.

En théorie, il est intéressant de noter que rien n'oblige à utiliser une base de données vectorielle pour construire un (+RAG_a). Cependant, il est clairement la norme dans le domaine du (+NLP_a) vu la rapidité et l'efficacité de ces outils. Évidemment, cette technique ne garantit pas à 100% que le (+LLM_a) réponde toujours bien, mais elle augmente considérablement les chances et permet de répondre à des questions qui n'auraient pas pu être répondues autrement.

### Le module de chat

Le module de chat est relativement équivalent à un chatbot classique. Il prend en input la question posée par l'utilisateur. Ces données que l'on appelle "contexte" subissent un pré-traitement pour être formatées de manière à être utilisées pour extraire des informations pertinentes de la base de données vectorielle. Une fois la phase de pré-traitement terminée, les données sont tokenisées puis transformées en embeddings pour être utilisées par le (+RAG_a).

Ce passage des tokens vers les embeddings, souvent appelé "incorporation", est réalisé à partir de modèles pré-entraînés comme Word2Vec ou GloVe, mais peut aussi être fait à l'aide de modèles de langage plus avancés comme BERT ou GPT évoqués plus tôt. Avec ces embeddings, le système peut identifier avec une haute précision les intentions derrière la question de l'utilisateur et extraire des informations pertinentes de la base de données vectorielle. Pour identifier quels tokens sont pertinents par rapport à la question posée, le système utilise des modèles de traitement du langage naturel (NLP) comme BERT ou ses variantes. 

Ensuite, le système prépare une requête de recherche optimisée pour interroger la base de données vectorielle et trouver des documents ou des passages pertinents. Cette requête peut dépendre des spécificités de l'algorithme de recherche ou de la base de données utilisée mais retourne, dans tous les cas, des passages de texte qui sont ensuite récupérés par le module de chat pour être passés au (+LLM_a).

Pour garder un maximum de cohérence entre la question posée et les données extraites en lien, le module de chat doit être capable de formater correctement les données pour les passer au (+LLM_a). Cela peut impliquer de reformuler la question, de supprimer des informations inutiles ou de préciser au (+LLM_a) comment traiter les données.

\pagebreak

La plupart des modèles de langage communiquent avec des requêtes possédant des flags spécifiques pour indiquer comment traiter ces dernières. On parle alors de "system prompt" lorsque l'on veut indiquer au modèle une manière particulière de se comporter. Sinon, on parle de "user prompt" pour indiquer au modèle de se comporter de manière standard et de répondre aux questions posées.

Un exemple de system prompt pourrait être : "Tu es un assistant qui fait ceci, je vais te poser des questions sur cela, tu auras des passages à disposition pour t'aider à répondre, cite-les de cette manière, etc.".

La requête est maintenant complète et peut être passée au (+LLM_a) pour générer une réponse. Étant donné que le projet est un chatbot, il est nécessaire de conserver un historique des questions posées et des réponses générées pour garantir une conversation cohérente. Généralement, cela est gardé en mémoire vive et concaténé à chaque nouvelle question posée dans le contexte envoyé au (+LLM_a). Il faut donc réfléchir à toute une stratégie permettant de n'utiliser que la dernière question pour aller chercher des informations dans la base de données vectorielle et, dans le même temps, conserver l'historique des questions posées pour tout envoyer au (+LLM_a).

### Le LLM

Le (+LLM_a) est le cœur du système. C'est lui qui va générer les réponses à partir des informations contextuelles fournies par le module de chat. Ces dernières, envoyées de manière textuelle, sont généralement accompagnées de différents paramètres qui permettent de contrôler la qualité de la réponse. On retrouve notamment le "stop sequence" qui indique au modèle quand arrêter de générer du texte, la "température" qui contrôle le niveau de créativité ou d'imprévisibilité dans les réponses ou encore le "max tokens" qui détermine le nombre maximum de tokens que le modèle peut générer en réponse. 

D'autres paramètres moins fréquents peuvent être utilisés pour affiner les interactions avec le modèle et obtenir des réponses qui correspondent mieux aux intentions ou aux besoins spécifiques de l'utilisateur. On peut citer le "presence penalty" qui réduit la probabilité de répéter des tokens qui sont déjà apparus dans la réponse, le "frequency penalty" qui réduit la probabilité de répéter des tokens qui sont apparus plusieurs fois dans la réponse, le "best of" qui permet de générer plusieurs réponses à un prompt et de sélectionner la meilleure selon certains critères ou encore le "beam search" qui explore plusieurs chemins de génération de texte en parallèle pour trouver une réponse plus optimale.

Il est important de démarrer chaque nouvelle conversation avec le (+LLM_a) par une requête "system prompt" afin de rappeler au modèle comment il doit se comporter. Dans un second temps, toutes les requêtes futures peuvent être envoyées avec un "user prompt" pour indiquer au modèle de répondre de manière standard.

## Reflexions sur l'architecture

Maintenant que les (+LLM_a) et les (+RAG_a) ont été présentés dans les détails, il serait intéressant de se poser les premières questions sur les choix architecturaux à adopter pour le projet.

### Le LLM

Le premier choix très important est de déterminer quel (+LLM_a) il serait judicieux d'utiliser. Il est clair que les modèles de la famille d'OpenAI ou d'Anthropic sont les plus performants pour générer du texte. Cependant, ce sont des solutions propriétaires qui peuvent s'avérer très coûteuses en fonction de l'utilisation qui en est faite. Il est donc important de bien réfléchir à l'impact financier que cela pourrait avoir sur le projet. D'autre part, des modèles open-source comme ceux proposés Mistral ou Meta peuvent tout autant répondre aux besoins du projet à condition de pouvoir héberger les modèles localement. Dans ce cas, on risque d'être limité en termes de performances, mais cela peut être un compromis acceptable.

Le gros problème qui se pose actuellement avec le choix des (+LLM_a) à utiliser, c'est qu'il y en a de plus en plus et qu'ils sont de plus en plus performants. De nouveaux modèles sortent chaque jour et rendent les précédents souvent obsolètes. Pour ce projet, il est donc judicieux de choisir une architecture permettant de facilement changer de modèle. Pour des solutions propriétaires, on passe fréquemment par des (+API_a) privées qui nécessitent une clé d'accès. Pour des solutions open source, on peut passer par des libraires Python comme HuggingFace ou Llama qui permettent de charger un type de modèle spécifique rapidement. Dans tous les cas, l'objectif reste le même, éviter toute dépendance à un (+LLM_a) spécifique.

Dans une première phase exploratoire, il serait intéressant de comparer les performances de différents modèles open-source. Beaucoup de benchmarks et de métriques peuvent donner une idée de la performance d'un modèle sur une tâche spécifique. Un papier sur les récents avancements dans les (+RAG_a) [@RAG_recent_advances] propose un rapide état de l'art des (+LLM_a) dans lequel il est fait mention de la complexité à trouver le bon modèle pour une tâche donnée. 

Souvent, les benchmarks sont des questions de compréhension de texte ou de génération de texte qui ne sont pas toujours représentatives de la performance d'un modèle dans un contexte réel. Par exemple, les modèles Gemini de Google ont des scores très élevés en compréhension massive et multitâche du langage (MMLU). C'est un benchmark très prisé qui mesure la qualité d'un modèle multimodal. Cependant, il semblerait qu'en pratique ChatGPT-4 soit meilleur, mais cela reste presque impossible à prouver. La théorie la plus probable est que les tests aient fuité dans l'entrainement de Gemini mais ce n'est ni prouvé ni vérifiable, car c'est basé sur des ressentis, certes généralisés, mais pas suffisamment fiables pour être pris en compte.

En réalité, et même si beaucoup de métriques existent, il paraîtrait que rien ne soit aussi fiable qu'un classement réalisé sur les ressentis humains. C'est d'ailleurs ce que propose le ranking by elo de Hugging Face [@HG_LLM_elo] dont voici un extrait daté du 15 Mars 2023 :

\cimg{figs/hg_ranking.png}{scale=0.4}{Classement des LLM par Elo sur Hugging Face}{Source : HuggingFace, ref. URL03}

Cette image montre le classement des meilleurs (+LLM_a) par Elo. On remarque que les modèles GPT-4 sont clairement en tête, suvis de près par les modèles Claude. Mais ce qui est très intéressant, c'est de regarder les lignes marquées en jaune qui représentent les modèles open-source de Mistral. Mixtral-8x7B se positionne même en huitième position devant GPT-3.5, les modèles Llama de Meta ou encore Gemini de Google. Cela montre que les modèles open-source peuvent être tout aussi performants, voire meilleurs que les modèles propriétaires.

Cependant, ce classement ne tient pas compte de la taille des modèles. Il se trouve que la taille des modèles, donc leur nombre de paramètres, est un facteur très fortement lié à la performance d'un modèle et à la quantité de ressources nécessaires pour le faire tourner.
L'immense avantage de Mistral est de proposer des modèles open-source avec des performances plus que remarquables tout en étant beaucoup plus petits que les modèles propriétaires. Par exemple, un modèle comme Llama-2 avec 70 milliards de paramètres nécessite au minimum deux cartes graphiques Nvidia 4080 Ti pour tourner.

\pagebreak

Pour avoir des modèles aussi petits, mais aussi performants, Mistral fait des compromis sur le risque d'hallucination, comme le montrent les benchmarks BBQ et Bold qui mesurent un taux d'hallucination plus élevé pour les modèles 7B que pour les modèles 70B. Cela n'est cependant pas un problème puisque le (+RAG_a) va permettre de compenser ce défaut.

Mistral propose essentiellement deux types de modèles qui peuvent être intéressants pour le projet : les modèles 7B et les Mixture of Experts. Ces derniers, dont Mixtral-8x7B peuvent être vus comme une combinaison de plusieurs modèles 7B qui sont spécialisés dans des tâches spécifiques. Cela permet d'avoir des performances très élevées sur une grande variété de tâches et c'est très probablement de cette manière que fonctionne GPT-4. Avec cette technique, au moment de la génération de texte, seulement quelques sous-modèles sont activés pour répondre à la question posée. En termes de ressources, cela revient à profiter des performances d'un modèle de 56 milliards de paramètres tout en ne nécessitant la puissance de calcul que d'un modèle de 14 milliards de paramètres.

En termes de performance, un énorme avantage des modèles de Mistral est l'extrême rapidité de génération de texte. Même si le modèle Mixtral-8x7B semble très performant, les ressources disponibles pour le projet ne permettent pas de déployer un modèle de plus de sept milliards de paramètres. Il peut donc être intéressant de se tourner vers un modèle plus léger comme OpenHermes-2.5 qui est un modèle 7B amélioré par la communauté Hugging Face. Il est très performant et peut être déployé sur un laptop ou un serveur sans problème.

### Le RAG System

Au regard des premières recherches effectuées, il semble que ChromaDB et Faiss soient les deux solutions de base de données vectorielles les plus adaptées au projet. Le choix déterminant va dépendre des performances en pratique. Il est important de mesurer la rapidité d'inférence des deux solutions en fonction de la quantité de documents à vectoriser. A priori, le choix de Faiss semble plus cohérent pour le projet, puisqu'il faut être à la fois rapide et performant. 

ChromaDB qui est aussi une bonne solution, parait plus adapté lorsque l'on possède des bases de données externes, ce qui ne sera pas le cas ici. Tout comme les (+LLM_a), il est très important de ne pas dépendre d'une solution spécifique, étant donné que les outils disponibles et les techniques d'embedding évoluent très rapidement. Pour s'adapter aux différents outils disponibles, il est nécessaire d'utiliser un framework qui intègre des alternatives comme Langchain. C'est de loin le framework le plus intéressant pour intégrer des (+LLM_a) dans une application et faire du (+RAG_a). Comparé à Pinecone, par exemple, il intègre un ensemble de modèles d'embeddings pré-entraînés comme BERT, GPT, etc. Il permet aussi d'importer des (+LLM_a) avec différentes libraires Python comme Ollama.

## Des défis à relever

À travers la prochaine section consacrée au travail réalisé, il sera question de répondre à plusieurs questions évoquées dans le cahier des charges. Premièrement, il peut être intéressant de s'attarder sur l'étude du comportement des (+RAG_a) de manière générale. 

Par exemple, lorsque le système ne connait pas la réponse exacte à une question, comment va-t-il réagir ? Va-t-il donner, inventer une réponse à partir de ses connaissances générales, va-t-il dire qu'il ne sait pas ? Cela peut être très important pour la crédibilité du système. De plus, la qualité des documents à vectoriser peut avoir un impact important sur la pertinence des réponses. La question du contexte peut aussi être cruciale. Faut-il privilégier un contexte plus large ou plus précis ? 

En réalité, certaines questions ne peuvent être répondues qu'en pratique, c'est pourquoi il est important de tester plusieurs architectures et de réaliser plusieurs itérations pour trouver la solution la plus adaptée au projet.

\pagebreak