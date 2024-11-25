# Rapport de Projet d'Approfondissement - HES-SO

[le template de base](https://github.com/mdemierre/hesso-latextemplate-thesis/blob/master/thesis.pdf)

le pdf du rapport est disponible [ici](./rapport.pdf)

## Structure de dossiers et fichiers

- `figs` : l'endroits où stocker les images
- `templates` : La partie LaTeX du rapport.
- `text` : le rapport en markdown
- `config.yaml` : config du rapport
- `my.bib` : la bibliographie zotero ->  [@un_nom_dans_my_bib]
- `text/ZZ-glossaire.md`: le glossaire (voir le lien dans le fichier pour la doc)

## Compilation du rapport

`./run.sh`

## Indications d'usage

- les tableaux: `Table: <la légende du tableau>`
- les notes de bas de page: `word[^0]` et en bas du fichier: `[^0]: yes \url{https://github.com/thomasdgr}` 
- les liens: `[word](matching link)`
- les images:
```latex
% Insère une image (et l'ajoute dans la table des figures) :
\cimg{figs/enonce_1.png}{scale=0.5}{légende}{Source : tiré de \url{myurl.ch}, ref. URL01}
```
- la bibliographie: `word [@ref_in_my.bib]`
- mettre du code:
  ```c
  int main(){
      return 0;
  }
  ```
- citer une figure: `![This is the caption\label{mylabel}](/url/of/image.png) See figure \ref{mylabel}`.
- insérer du markdown:
```md
<table>
    <tr>
        <td>entry</td>
    </tr>
</table>
```
- pour tout le reste: [la documentation Pandoc](https://pandoc.org/MANUAL.html)