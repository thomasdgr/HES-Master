# Cahier des charges

## Mise en contexte

Avec l'essor des (+LLM_a), le domaine de l'intelligence artificielle a fait un grand bond en avant en offrant des capacités de compréhension et de génération de texte sans précédent. Dotés de facultés de traitement du langage naturel hors norme, ces modèles permettent d'accéder à une quantité d'informations quasi illimitée en un temps record et avec une simplicité déconcertante. Ils peuvent être perçus comme des sources d'informations massives, capables de répondre à une immense variété de questions et de problèmes. Mais est-ce vraiment la solution miracle ? Est-il possible de faire 100 % confiance à un (+LLM_a) ? Comment être sûr que les réponses fournies sont correctes et à jour ? Que se passe-t-il si le modèle ne dispose pas des informations nécessaires pour répondre à une question ?

En règle générale, les (+LLM_a) sont limités par les données sur lesquelles ils ont été entraînés à un instant T. Cela signifie qu'ils ne sont probablement pas capables de donner le score du derby Nantes-Rennes (pourtant soldé par un glorieux 0-3 !) datant du 20 avril 2024. De la même manière, il y a peu de chance que ces modèles soient en mesure d'indiquer à un étudiant quand est son prochain cours et dans quelle salle. Ces différents cas de figure illustrent tous deux des problématiques récurrentes dans l'utilisation des (+LLM_a) : il reste relativement compliqué d'accorder une totale confiance à ces modèles, notamment lorsqu'il s'agit de questions récentes ou très spécifiques.

Il est très fréquent d'être confronté à ce genre de problème lorsqu'on utilise un assistant virtuel. Par exemple, lorsqu'il précise dans sa réponse : "Je ne suis pas en mesure de répondre à cette question, car mes connaissances sont limitées au 20.10.2023", ou encore quand il source une information avec un document ou un site web qui n'existe en réalité pas. Ces situations sont problématiques et peuvent être source de confusion pour l'utilisateur. Dans un contexte où l'information accessible en ligne est de plus en plus abondante, il est donc essentiel de trouver des solutions pour garantir la fiabilité des réponses fournies par ces modèles qui deviennent omniprésents au quotidien. 

Actuellement, les meilleurs (+LLM_a) sont souvent ceux qui possèdent les corpus de données les plus vastes à entraîner. Ce processus demande des investissements colossaux, ce qui explique en partie pourquoi les modèles proposés par OpenAI, Google ou Meta sont généralement les plus performants. Cependant, il pourrait être intéressant de se demander si la norme future ne serait pas plutôt d'avoir des petits modèles, mais très spécialisés dans un domaine spécifique. 

Imaginons un modèle dont la spécialité serait d'aider les étudiants de la (+HEIAFR_a) à trouver des informations sur les cours, les horaires, le règlement, etc. Ce modèle serait entraîné sur des données spécifiques à l'école, il n'y aurait pas besoin de lui apprendre à faire des dissertations à notre place, pas besoin non plus de lui donner un énorme corpus de données pour qu'il sache répondre à des questions sur la physique quantique. Plus petit, plus rapide et beaucoup moins coûteux, il ferait finalement exactement ce qu'on attend de lui.

Mais en réalité, cette solution n'est probablement pas optimale dans la mesure où le modèle ne serait jamais pas capable de répondre avec une qualité linguistique aussi élevée que les modèles actuels. Cependant, des mécanismes existent pour permettre aux (+LLM_a) existants d'aller chercher des informations ailleurs que dans leurs données d'entraînement. C'est notamment ce que permettent les (+RAG_a) qui fournissent un accès à des sources de données externes comme des PDF, des sites web, des bases de données, etc. pour combler les lacunes des (+LLM_a).

Florence Meyer, responsable du service académique à la (+HEIAFR_a), a soulevé une problématique concernant l'accès aux informations pour les étudiants de l'école. De sorte à améliorer leur expérience, elle souhaite mettre en place un assistant virtuel capable de répondre à leurs questions et de les rediriger vers les services adéquats. En marge d'un projet essentiellement tourné vers la recherche et l'analyse des technologies de (+LLM_a) et de (+RAG_a), le développement d'un assistant virtuel constitue un (+POC_a) visant à poser les bases d'une finalité plus ambitieuse. En prenant en compte le temps à disposition, il convient de formaliser toutes les étapes nécessaires à la réalisation de ce projet dans sa globalité et de définir les objectifs à atteindre dans le cadre de ce travail.

## Methodologie et Objectifs

L'objectif premier de ce projet est d'explorer en détail la notion de (+RAG_a) : cette nouvelle méthode visant à améliorer les performances et la fiabilité des (+LLM_a). Le travail à réaliser constitue une grande part de recherche et d'expérimentation nécessitant d'investiguer sur les technologies sous-jacentes, les stratégies de préparation des données, et les méthodes d'intégration dans un cas pratique. Les résultats de ces recherches et de ces implémentations aideront à répondre à certaines questions ouvertes telles que :

1. La sélection d'une architecture optimale au regard des critères de coût, d'efficacité, et de précision.
2. Les stratégies de préparation, nettoyage, et filtrage des données pour maximiser l'efficacité de l'utilisation des (+RAG_a).
3. L'étude des stratégies de formulation de prompts pour les (+LLM_a) et leur impact.
4. La gestion des cas où les réponses fournies par le (+RAG_a) ne figurent pas dans les données du (+LLM_a) ou contredisent ses connaissances intégrées.
5. Les méthodes de structuration des données pour optimiser l'accessibilité.
6. La sélection des sources de données externes les plus adéquates et leur intégration dans le modèle.
7. L'exploration de la capacité du système à initier la collecte d'informations et la génération de réponses via le chat.
8. L'évaluation des avantages financiers et environnementaux d'une solution combinant (+LLM_a) et (+RAG_a).
9. L'ajustement du poids accordé aux sources de données externes par rapport aux connaissances intégrées du (+LLM_a).

La méthodologie agile ainsi que des revues régulières avec les parties prenantes permettront d'ajuster les objectifs en fonction des découvertes, des progrès réalisés, du temps, des ressources disponibles et surtout des nouveautés émergentes dans le domaine de l' (+IA_a) générative.  

## Planification

### Phase 1: Mise en place du projet (2 semaines)

Semaine 1: Mise en place du projet
```md
- Définition des objectifs et des questions clés à aborder
- Premières lectures sur les LLM et les RAG
- Mise en place de la documentation.
```

Semaine 2: Formalisation du cahier des charges, définition des objectifs et planification des tâches pour les sprints
```md
- Réunion avec Florence Meyer pour parler du projet
- Cahier des charges et planification des tâches pour les sprints
- Réalisation d'un mini projet pilote pour tester les technologies
  et comprendre leur fonctionnement.
```

### Phase 2: Approfondissement (3 semaines)

Semaine 3: Exploration et étude du fonctionnement des (+LLM_a)
```md
- Comprendre comment fonctionne les LLM
- Tester différentes implémentations de LLM
- Faire une étude comparative entre les modèles.
```

Semaine 4: Exploration et étude du fonctionnement des (+RAG_a)
```md
- Comprendre comment fonctionne les RAG
- Tester différentes implémentations de RAG
- Faire une étude comparative entre les systèmes.
```

Semaine 5: Exploration et étude du fonctionnement des bases de données vectorielles
```md
- Faire une étude comparative sur les bdd vectorielles
  existantes (algo, runtime, framework, embeddings ...)
- Spécifications de l'architecture du projet.
```

### Phase 3: Sprints Itératifs (3 semaines par sprint)

Sprint 1: Proposer un prototype de base (Semaines 6 à 8)
```md
- Faire une API intégrant les documents envoyés par Florence.
- Faire un front-end pour exposer le chatbot.
Objectif: montrer un MVP et identifier les points d'amélioration.
```

Sprint 2: Amélioration du prototype (Semaines 9 à 11)
```md
- Répondre aux questions 2. 5. 6. ou 7. à travers des recherches.
- Modifier le prototype en conséquence.
Objectif: améliorer le prototype et comprendre comment gérer les données.
```

Sprint 3: Optimisation et Évaluation (Semaines 12 à 14)
```md
- Répondre aux questions 3. 4. 8. ou 9. à travers des recherches.
- Modifier le prototype en conséquence.
- Evaluer les performances du système selon différentes métriques.
Objectif: améliorer le prototype et comprendre comment interagir avec le 
LLM en optimisant le fonctionnement du RAG.
```

\pagebreak

### Revues et Ajustements

Chaque sprint est clôturé par un bilan sur l'avancée pour évaluer les progrès, discuter des défis rencontrés et ajuster les objectifs des sprints suivants. Cela inclut également la mise à jour de la documentation. La planification est voulue flexible, permettant des ajustements en fonction de l'évolution des besoins du projet et des technologies tout en favorisant les phases de recherches mises au service du développement de l'assistant virtuel.

### Gantt prévisionnel

\cimg{figs/gantt.png}{width=\textwidth}{Gantt prévisionnel du projet}{Source : Thomas Dagier}

\pagebreak