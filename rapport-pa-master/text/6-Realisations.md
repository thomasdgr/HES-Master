# Réalisations

## Description générale

Le but du projet est de mettre à disposition des étudiants un assistant virtuel capable de répondre à des questions précises sur le contenu des documents de la (+HEIAFR_a). Dans le cadre de ce travail, l'objectif premier, est essentiellement de mettre en place une pipeline fonctionnelle qui servirait de base pour des développements futurs. Au vu du temps et des ressources disponibles, il est important de pouvoir dissocier le travail réalisable du travail complet.

### Les besoins

Florence Meyer exprime un besoin fondamental de séparer les dépendances entre le service académique et le service informatique, en veillant à ce que l'application soit accessible même pour les utilisateurs sans compétences techniques. L'interface doit être simple et intuitive, facilitant la saisie des questions et l'obtention de réponses. Sur le plan technique, l'application doit être fiable, dotée de mécanismes de monitoring et de redéploiement automatique pour assurer une gestion autonome en cas de problème serveur. La gestion des documents sources est cruciale, permettant l'ajout, la vérification, l'indexation et le stockage sécurisé de divers formats (PDF, sites web, textes, JSON, CSV, etc.) dans une base de données vectorielle. 

La transformation des documents Excel en texte brut ou CSV pour une meilleure indexation est également envisagée. Florence Meyer souhaite aussi développer des interfaces web et mobiles similaires en termes de fonctionnalité et de graphisme, adaptées aux contraintes spécifiques de chaque plateforme. La sélection des technologies devra être validée par des benchmarks rigoureux pour garantir des performances optimales, tant en termes de temps de réponse que de qualité. 

\pagebreak

Les réponses fournies doivent être pertinentes, bien citées, et non paraphrasées, avec un historique des interactions pour chaque utilisateur, permettant une gestion multi-utilisateurs avec différents rôles (étudiant, professeur, administrateur, etc.). 

Un système de retour utilisateur simple (pouce en l'air, pouce en bas, étoiles) permettra de mesurer la satisfaction et d'améliorer continuellement les réponses du modèle. L'architecture doit rester flexible, permettant de modifier le choix des technologies sans affecter l'application. Enfin, les réponses doivent être de qualité et fournies rapidement, avec des citations précises des sources documentaires.

### Les contraintes

Le projet est soumis à des contraintes de temps et de ressources, limitant l'étendue des fonctionnalités à implémenter. La qualité des documents sources (horaires, fichiers Excel, sites web) pose un défi majeur, nécessitant une vérification rigoureuse pour garantir des réponses pertinentes et à jour. La séparation des dépendances entre les services académiques et informatiques doit être maintenue pour une gestion autonome par les utilisateurs non techniques. De plus, il est crucial de privilégier l'utilisation de services open-source, excluant l'utilisation des API de ChatGPT-4 ou de Gemini en production. L'application doit être conçue de manière à permettre une gestion flexible et indépendante des technologies utilisées (modèles LLM, algorithmes d'embedding, bases de données vectorielles), sans impacter son comportement global.

## Description détaillée

En supposant que le temps et les ressources mises à disposition du projet permettent de réaliser l'ensemble de l'application, il faudrait prévoir plusieurs interfaces (web et mobile) permettant aux étudiants d'interagir avec l'assistant virtuel. Il faudrait aussi prévoir une interface de monitoring, mise à disposition du service académique, pour gérer l'indexation des documents à utiliser par le (+RAG_a). Cette interface permettrait aussi de gérer le système de feddback à utiliser lorsque l'application n'est pas en mesure de répondre de manière précise, sourcée et pertinente à une question posée. Dans les cas où cette situation arriverait, il faudrait retourner cette question dans l'interface de monitoring afin qu'un expert puisse y répondre et que la réponse puisse être ajoutée à la base de données pour les prochaines fois.

\pagebreak

En plus des interfaces et d'un point de vue plus technique, il faudrait se pencher sur le backend et l'architecture globale du projet. Une pipeline de déploiement et de redéploiement automatique serait nécessaire pour garantir une disponibilité continue de l'application. Cette dernière serait aussi utilisée pour mettre à jour l'application lorsque des documents sont indexés ou supprimés par le service académique. 

Les choix technologiques cruciaux devraient être faits en fonction des performances et des benchmarks réalisés sur les différentes solutions disponibles. Il faudrait donc prévoir du temps à investir pour réaliser des batteries de tests et des benchmarks de qualité afin de s'assurer que les choix technologiques permettent d'atteindre les objectifs fixés.

Ne disposant pas de suffisamment de temps et de ressources pour réaliser l'ensemble de l'application, l'application proposée est essentiellement un prototype fonctionnel qui permet de répondre aux besoins de base exprimés par Florence Meyer. Cette dernière est alors composée d'un frontend web très simple, un backend qui gère le (+RAG_a) et expose une API contenant toutes les fonctionnalités nécessaires pour répondre aux questions posées par les utilisateurs. Le choix des technologies et de l'architecture à déployer est optimisé pour la performance et la simplicité, sans nécessairement prendre en compte la scalabilité de l'application. L'objectif premier est essentiellement de garantir un temps de réponse très court et une qualité de réponse optimale.

Les choix technologiques, qui concernent essentiellement le choix de l'algorithme d'embedding et celui du (+LLM_a) sont effectués en mesurant de manière relativement subjective la qualité des réponses. À partir d'une liste de quelques questions type, les réponses générées par les différentes combinaisons d'algorithmes, de (+LLM_a) et de base de données vectorielles sont comparées pour déterminer laquelle offre le meilleur rapport qualité/performance.

Dans une version plus aboutie de l'application, il serait nécessaire de fixer la priorité sur un système de monitoring pour la gestion des documents. Les choix technologiques et ceux liés au déploiement automatique de l'application devraient être revus dans un second temps pour garantir une architecture optimale, mais ne constituent pas une réelle priorité pour le moment.

Enfin, et à mesure que le travail se poursuivrait, il serait nécessaire de se pencher sur la réalisation plus poussée des interfaces web et mobiles afin d'exposer l'application à un plus grand nombre d'utilisateurs.

\pagebreak

### L'interface web

Dans le cadre de la réalisation propre à ce projet, le frontend réalisé pour interagir avec l'assistant virtuel est une application web très simple. Cette dernière est composée d'une page unique contenant un champ de texte pour saisir la question à poser à l'assistant virtuel et un bouton pour envoyer la question. Lorsque la question est envoyée, une requête est faite au backend pour obtenir la réponse. Cette dernière est ensuite affichée à l'utilisateur, accompagnée des sources utilisées pour générer la réponse. Voici un aperçu de l'interface réalisée en HTML/CSS/JS :

\cimg{figs/demo_frontend.png}{width=\textwidth}{Interface du Chatbot}{Source : Thomas Dagier}

Cette image illustre une interaction très simple avec le chatbot et mets en situation un étudiant qui aurait des difficultés à se connecter à IS-Academia, un site web de l'école permettant de consulter les horaires des cours...

### Les embeddings et la base de données

Comme évoqué précédemment, plusieurs alternatives ont été envisagées pour l'embedding des documents et la base de données vectorielle à utiliser. Si le choix du framework se porte naturellement sur Langchain qui permet clairement l'intégration la plus simple et les meilleures performances, plusieurs algorithmes d'embedding ont été testés pour déterminer lequel offrait les meilleures performances. Le premier test a été d'utiliser E5 [@e5_embedding]. Cette solution inspirée de SBERT possède l'avantage d'être très rapide et de fournir des embeddings de qualité. Une alternative à E5 est d'utiliser BGE-M3 [@bgem3_embedding]. Proposé par la Beijing Academy of Artificial Intelligence, ce modèle est plus récent et offre des performances légèrement supérieures à E5. 

Cependant, des discussions en interne ont fait émerger l'idée d'utiliser GPT-3 [@gpt3_embedding] pour l'embedding des documents. En effet, la quantité de données à traiter reste relativement faible et il semblerait que la qualité des embeddings obtenus soit supérieure à celle des autres solutions testées. Étant donné qu'il n'est pas nécessaire de faire plusieurs fois un embedding sur un même document, le choix d'une solution payante, mais à très moindre coût parait être une option viable au regard de la qualité des embeddings obtenus. Pour la version actuelle du projet, cela représente un coût total de 0.16$.

Pour juger la qualité des embeddings, il serait en théorie nécessaire de procéder à diverses mesures de satisfaction qui prendraient en compte le temps de traitement, la taille des embeddings une fois stockés et, surtout, la qualité des réponses obtenues. Florence Meyer mets à disposition une liste de plusieurs questions types qui permettent de comparer la qualité des réponses en fonction des embeddings et des bases de données vectorielles utilisées. 

Il est important de noter que les paramètres des algorithmes d'embeddings sont identiques pour les trois solutions testées. On distingue la taille des chunks qui est de 200 caractères et l'overlap qui est de 20 caractères. Cela signifie qu'un nombre (l'embedding) sera associé à un groupe de maximum 200 caractères et que chaque groupe se chevauche de maximum 20 caractères avec le précédent et le suivant. Ce choix permet de garantir qu'un embedding soit fait sur des groupes de mots suffisamment grands pour faire du sens sémantiquement tout en garantissant une continuité avec les groupes environnant de sorte à garder la cohérence du texte complet. Ensuite, l'algorithme rentre en jeu avec toute une série d'étapes qui permettent de couper intelligemment le texte sur des mots entiers, des phrases entières ou des paragraphes distincts et de supprimer les caractères spéciaux, la mise en forme, et les autres éléments qui ne seraient pas pertinents pour le chatbot.

Voici un exemple des réponses obtenues à partir de la question "Combien de crédits ECTS dois-je valider pour obtenir mon Bachelor en Informatique ?" :

```md
- E5: Les filières Bachelors comptent 180 crédits ECTS et s’organisent sur
6 semestres pour la forme d’études à plein temps et sur 8 semestres pour
la forme d’études en  emploi. La durée de la formation à temps partiel est
variable. La durée maximale de la formation est fixée dans les règlements
de filière. Elle ne peut pas dépasser 12 semestres.
Source: règlement_formation_base_bachelor_master_fr.pdf
```

\pagebreak

```md
- BGE-M3:
3Les filières Bachelors comptent 180 crédits ECTS et s’organisent sur 6
semestres pour la forme d’études à plein temps et sur 8 semestres pour 
la forme d’études en emploi.
Source: règlement_formation_base_bachelor_master_fr.pdf

- GPT-3: Les filières Bachelors comptent 180 crédits ECTS.
Source: règlement_formation_base_bachelor_master_fr.pdf
```

Avec cet exemple, on observe les différentes réponses obtenues avec les embeddings E5, BGE-M3 et GPT-3. Visiblement et à travers l'exemple précédent, il semblerait que E5 ait plus de difficultés à créer des groupes de mots pertinents. Si on regarde le document et l'extrait exact qui a permis de répondre, il se trouve que c'est l'entièreté du paragraphe qui a été utilisée pour répondre à la question. Cela signifie que l'algorithme est moins capable de créer des groupes de mots pertinents et a donc groupé l'ensemble du texte, ce qui peut poser un problème lorsque la question posée est plus longue ou plus complexe.

D'un autre côté, BGE-M3 parait offrir des résultats plus intéressants, mais ouvre la discussion sur un autre problème. Cet algorithme semble avoir quelques lacunes pour identifier le texte pertinent de celui qui l'est moins. On constate que l'index de l'alinéa dans le document est resté dans la réponse. Cela peut poser des problèmes au niveau de la qualité des sources externes utilisées par le (+LLM_a).

Enfin, GPT-3 semble offrir les résultats les plus pertinents et les plus précis sur cet exemple et sur bien d'autres. En effet, la réponse est plus concise et le contenu du texte est plus cohérent avec la question posée. De manière générale, ceci peut s'expliquer par le fait que GPT-3 est un modèle de génération de texte qui a été entrainé sur une quantité de données bien plus importante que les autres algorithmes testés.

Ces choix technologiques concernant les embeddings vont de pair avec le choix de la base de données vectorielle à utiliser. La section précédente, toujours sous l'angle de la simplicité d'implémentation, faisait mention de ChromaDB et Faiss. Ces deux solutions ont été testées à partir de Langchain mais n'ont pas permis d'identifier clairement laquelle offrait les meilleures performances. 

En théorie, ChromaDB est une solution plus adaptée pour des sources de données variées comme des bases de données, des documents, des sites web, etc. Faiss, quant à lui, est plus rapide, mais plus complexe à mettre en place. Toujours en théorie, Faiss pourrait être une solution plus adaptée au projet dans la mesure où la quantité de données à stocker ne sera jamais très importante. En pratique, le choix de Faiss est plus adapté à ce projet car il se combine très bien avec l'intégration du (+LLM_a).

### Le Large Language Model

Dans la section sur les (+LLM_a), le choix de l'open source a été privilégié pour des raisons de coût et de simplicité. Même si l'adoption de GPT-3 comme algorithme d'embedding va quelque peu à l'encontre de l'architecture envisagée pour le projet, ce n'est pas le cas du (+LLM_a) qui se doit d'être open source. En effet, il est crucial de pouvoir supporter une quantité variable, parfois importante de requêtes et le choix d'une solution propriétaire comme GPT-4 d'OpenAI pourrait poser de gros problèmes en termes de coûts.

Le second problème qui se pose avec le (+LLM_a) c'est le fait que des nouveaux modèles sortent régulièrement et qu'il serait, en pratique, très important d'avoir toujours le meilleur modèle open source disponible. Cela signifie que le modèle doit être facilement interchangeable. Langchain intègre une librairie, Ollama qui permet de faire tourner des modèles LLM sur GPU en simulant un serveur avec une API REST. Maintenu très régulièrement à jour, Ollama est une solution qui permet de garantir une certaine pérennité dans le choix du (+LLM_a) à utiliser.

La complexité derrière cette solution réside dans le fait de proposer une architecture plus complexe que celle envisagée initialement. En effet, il est nécessaire de mettre en place un module supplémentaire : un serveur Ollama qui va servir de pont entre le backend de l'application et le (+LLM_a). Cette alternative permet néanmoins de garantir que le modèle soit déployé en utilisant le (+GPU_a) et donc que le temps de réponse soit beaucoup plus court (de l'ordre de 5 secondes par requête contre 30 secondes pour un modèle qui n'utilise par de carte graphique pour fonctionner). Voici un exemple de requêtes permettant de communiquer avec le (+LLM_a) à travers le Ollama serveur:

```sh
curl https://ollama.kube.isc.heia-fr.ch/api/pull -d '{
  "name": "mistral"
}'
```

```sh
curl https://ollama.kube.isc.heia-fr.ch/api/generate -d '{
  "model": "mistral",
  "prompt": "Combien de crédits ECTS faut-il pour valider 
             un Bachelor en informatique ?",
  "stream": false
}'
```

À travers ces deux commandes, on spécifie le modèle que l'on souhaite déployer sur le (+GPU_a) et on envoie une requête pour générer une réponse à partir d'un prompt donné. Ces requêtes sont envoyées au serveur Ollama qui les transmet au (+LLM_a) avant de renvoyer la réponse obtenue. Le modèle utilisé actuellement est donc Mistral puisqu'il est le modèle le plus pertinent à utiliser dans ce cas.

### Le RAG

L'ensemble de l'architecture (+RAG_a) qui compose cette application est finalement relativement simple. Une question posée par l'utilisateur depuis l'interface web servira à extraire des informations pertinentes depuis la base de données vectorielle. La pertinence de ces dernières est évaluée à partir d'algorithmes d'embeddings qui permettent de mesurer la similarité entre la question posée et les passages des différents documents indexés. Ces informations sont utilisées pour compléter un user prompt qui est envoyé au (+LLM_a) à travers une requête API vers le Ollama serveur. 

Le comportement du (+LLM_a) est fixé à partir d'un prompt system afin de garantir que le modèle se comporte comme attendu. Dès lors que la réponse est générée, elle est renvoyée à l'utilisateur avec les sources utilisées pour être affichées dans l'interface web initiale.

Au fur et à mesure que les (+RAG_a) évoluent et deviennent une norme relative à la personnalisation des (+LLM_a), les différents papiers s'accordent à classifier les (+RAG_a) selon leur degré de complexité architecturale. D'après [@gao_retrieval_augmented_2024], il y aurait en réalité trois catégories de (+RAG_a) distinctes dont le Naive RAG, le Advanced RAG et le Modular RAG : 

\cimg{figs/rag_categories.png}{width=\textwidth}{Différentes catégories de RAG}{Source : Retrieval-Augmented Generation for Large Language Models: A Survey, ref. URL08}

\pagebreak

Ce schéma permet de rendre compte des différentes étapes qui composent chaque catégorie de (+RAG_a) et met en lumière la notion de procédé de pre-retrieval et post-retrieval. Ces stratégies n'existant pas dans le Naive RAG répondent à une problématique du (+LLM_a) qui ne se base plus que sur les données externes pour générer une réponse et non plus sur ses connaissances générales. On parle de Naive RAG lorsque le système ne fait que répéter ce qui lui est inscrit dans son user prompt sans chercher à générer une réponse plus complète.

En réalité, l'utilisation d'un système prompt est, déjà en soi, une forme de pre-retrieval qui permet de guider le modèle dans la génération de la réponse. Pour réaliser de l'Advanced RAG au sens propre, plusieurs techniques peuvent être mises en œuvre comme la réécriture de la question initiale pour matcher les résultats de la recherche sur plusieurs questions très similaires. 

En matière de post-retrieval, il est possible de mettre en place des stratégies de reformulation ou de ré-indexation des chunks de texte pour éviter la surcharge d'informations (on parle alors de reclassement).


L'application développée dans le cadre de ce projet pourrait être vue entre le Naive RAG et l'Advanced RAG. En effet, le système de pre-retrieval est déjà en place et permet de guider le modèle dans la génération de la réponse. Cependant, il n'y a pas de stratégie de post-retrieval pour reformuler la réponse ou indexer à nouveau les chunks de texte.

### Les problèmes rencontrés

Au cours de ce projet, plusieurs problèmes ont été rencontrés. Le premier concerne la lenteur des réponses obtenues avec le (+LLM_a). En effet, le modèle est très gourmand en ressources et nécessite d'être déployé sur un (+GPU_a) pour garantir des temps de réponse acceptables. Le déploiement du modèle sur le cluster de l'école a posé un problème en raison du manque de RAM (+GPU_a) disponible. Il a donc été nécessaire de déployer intelligemment le modèle sur un serveur Kubernetes pour garantir des temps de réponse acceptables. C'est la raison principale pour laquelle le serveur Ollama a été mis en place afin de pouvoir être utilisé par plusieurs projets en même temps.

Un second problème, plus propre aux embeddings concerne la librairie PDFMiner et plus généralement la qualité des documents sources. En effet, les documents sources utilisés pour générer les embeddings ne sont pas toujours de qualité optimale. Certains documents PDF contiennent des emplois du temps ou des tableaux qui peuvent poser un problème à PDFMiner et donc à la génération des embeddings. Certains documents sont presque inexploitables et nécessitent un nettoyage et une préparation des données pour garantir des réponses de qualité. Le problème a été évoqué avec Florence Meyer à qui il a été recommandé de mettre en place des stratégies afin de remplacer les emplois du temps et les tableaux par des documents textes, CSV, ou JSON plus explicites.

Dans une version plus aboutie de l'application, il serait intéressant de rajouter des systèmes de nettoyage et de filtrage des données plus précis pour se rapprocher encore plus d'un Advanced (+RAG_a). Si une première étape serait de transformer les documents difficilement exploitables en fichier texte ou autre structure de données plus simple, il pourrait aussi s'avérer judicieux de réfléchir à d'autres techniques permettant, par exemple, de filtrer les données en amont de l'embedding pour ne garder que les informations les plus pertinentes.

De manière générale, la question de la lecture et de l'interprètation des tableaux est un sujet très ouvert et très complexe dans le domaine du (+NLP_a). La solution la plus simple est donc de faire une copie des documents problématiques et de les transformer en documents textes. Cela permet de garantir que les embeddings générés puissent réellement aider à répondre aux questions comme : "Dans quelle salle se déroule mon cours de mathématiques ?".

Heureusement, cela concerne une petite quantité de documents et il a été possible de trouver une alternative rapidement afin de tout de même bénéficier des informations présentes dans ces derniers.

Dès lors qu'une version stable et fonctionnelle de l'application a pu être déployée, il a été nécessaire de réaliser du prompt engineering pour améliorer la qualité des réponses. En effet, il est apparu que le modèle avait parfois du mal à générer des réponses pertinentes, qu'il paraphrasait les sources ou qu'il ne répondait pas correctement à la question posée. 

Des stratégies de reformulation itérative ont donc été mises en place pour guider le modèle dans la génération de la réponse. Il se trouve que ces stratégies ont permis d'améliorer significativement la qualité des réponses obtenues. 

Elles ouvrent même la discussion sur la possibilité de mettre davantage l'accent sur le prompt engineering et de se demander à quel point le système pourrait encore être amélioré uniquement en travaillant sur le system prompt. Typiquement, une question assez intéressante à se poser, c'est d'évaluer le comportement qu'aurait le (+LLM_a) lorsqu'il n'a pas la réponse à une question. Est-ce qu'il devrait être capable de demander des précisions à l'utilisateur ? Est-ce qu'il devrait être en mesure de répondre n'importe quoi malgré tout ou plutôt dire explicitement qu'il ne connait pas la réponse ? 

Avec un system prompt quelque peu bien construit, il est assez simple de beaucoup influencer le comportement du modèle et de le guider dans la génération de la réponse. On peut, par exemple, influencer son comportement lorsqu'il ne connait pas la réponse, quand il est nécessaire d'utiliser ses connaissances générales, comment éviter la paraphrase tout en citant au mieux les sources, etc. Voici l'exemple qui est utilisé pour le projet :

\pagebreak

```md
Tu as à ta disposition des informations et des réglementations sur la
haute école d'ingénierie et d'architecture de Fribourg en Suisse. Si
la question porte sur un ou plusieurs passages textuels, utilisez-les
pour répondre à la question mais ne les paraphrase pas. Si la question
ne porte sur aucun passage textuel, générez une réponse à partir de tes
connaissances. Assure-toi de toujours fournir la réponse, la source de
l'information et de mentionner dans quel fichier l'information a été
trouvée en utilisant le format suivant:
Document: <document name>
<answer>

# Start of passages
{passages}
# End of passages
```

### Les réponses aux questions ouvertes

La première question à laquelle on pourrait tenter de répondre, c'est d'évaluer les avantages et inconvénients d'une solution moins qualitative du point de vue de l'application déployée, mais qui fonctionnerait entièrement sur un ordinateur portable plutôt qu'un serveur Kubernetes avec des (+GPU_a). En pratique, l'application se veut portable et il est tout à fait possible de faire fonctionner le service en local. 

Évidemment, et c'est ce qui motive l'utilisation du Ollama serveur, les performances sont beaucoup plus élevées lorsque les poids du (+LLM_a) sont chargés dans la RAM (+GPU_a). Une utilisation relativement simple et peu efficace pourrait toutefois être faite sur un ordinateur portable ne possédant pas de (+GPU_a). Toujours en considérant que l'ensemble de l'application serait en local sur un ordinateur portable, la seule vraie limite serait la taille du (+LLM_a) à charger sur le (+GPU_a). En effet, si le modèle était relativement lourd, l'utilisateur serait contraint d'utiliser un modèle plus petit comme Phi3 de Microsoft.

Une autre question qui s'est posée au moment d'intégrer les données externes au contexte du (+LLM_a), c'est de se demander si le choix d'un (+LLM_a) avec plus de contexte aurait un impact sur la qualité des réponses. Relativement aux besoins de l'application, on pourrait estimer que ce n'est pas un critère déterminant, car on fait du (+RAG_a) avec des chunks de petite taille. Augmenter le contexte pourrait aussi avoir un effet négatif sur la précision des réponses, alors qu'il serait plutôt recommandé de travailler avec des prompts courts, mais concis. De plus, les modèles avec beaucoup de contexte sont souvent plus lourds et plus longs à charger, ce qui pourrait poser des problèmes de performances sur le Ollama serveur. C'est donc un bon axe de réflexion, mais qui n'est pas primordial pour la suite.

\pagebreak