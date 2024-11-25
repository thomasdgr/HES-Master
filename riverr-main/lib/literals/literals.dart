class Literals {
  LanguageLiterals text = EnglishLiterals();
  static final Literals _instance = Literals._internal();
  
  factory Literals() {
    return _instance;
  }
  
  Literals._internal();
}

abstract class LanguageLiterals{
  String get add;
  String get remove;
  String get name;
  String get upload;
  String get download;
  String get progress;
  String get search;
  String get addHint;
  String get removeHint;
  String get updateTrackerHint;  
  String get pause;  
  String get resume;
  String get delete;
  String get update;
  String get movies;
  String get shows;
  String get watched;
  String get recommended;
  String get fetchError;
  String get noResults;
  String get options;
  String get cancel;
  String get updateUrl;
  String get torrentAddError;
  String get torrentAddSuccess;
  String get updateTrackerError;
  String get updateTrackerSuccess;
  String get mediaRemoveError;
  String get mediaRemoveSuccess;
  String get mediaAddError;
  String get mediaAddSuccess;
  String get torrentPauseError;
  String get torrentPauseSuccess;
  String get torrentResumeError;
  String get torrentResumeSuccess;
  String get torrentRemoveError;
  String get torrentRemoveSuccess;
}

class EnglishLiterals extends LanguageLiterals{

  @override
  String get options => "Options";

  @override
  String get noResults => "No results found";

  @override
  String get fetchError => "Failed to fetch data";

  @override
  String get watched => "Watched";

  @override
  String get recommended => "Recommended";

  @override
  String get movies => "Movies";

  @override
  String get shows => "Shows";

  @override
  String get add => "Add";

  @override
  String get addHint => "Add a torrent magnet";

  @override
  String get delete => "Delete";

  @override
  String get download => "Download";

  @override
  String get name => "Name";

  @override
  String get pause => "Pause";

  @override
  String get progress => "Progress";

  @override
  String get remove => "Remove";

  @override
  String get removeHint => "Remove a torrent";

  @override
  String get resume => "Resume";

  @override
  String get search => "Search";

  @override
  String get update => "Update";

  @override
  String get updateTrackerHint => "Update trackers";

  @override
  String get upload => "Upload";
  
  @override
  String get cancel => "Cancel";
  
  @override
  String get updateUrl => "Update URL";
  
  @override
  String get torrentAddError => "Cannot add torrent";
  
  @override
  String get torrentAddSuccess => "Torrent added succesfully";
  
  @override
  String get updateTrackerError => "Could not update tracker";
  
  @override
  String get updateTrackerSuccess => "Tracker updated succesfully";
  
  @override
  String get mediaAddError => "Could not add media";
  
  @override
  String get mediaAddSuccess => "Media added succesfully";
  
  @override
  String get mediaRemoveError => "Could not remove media";
  
  @override
  String get mediaRemoveSuccess => "Media removed succesfully";
  
  @override
  String get torrentPauseError => "Could not pause torrent";
  
  @override
  String get torrentPauseSuccess => "Torrent paused succesfully";
  
  @override
  String get torrentRemoveError => "Could not remove torrent";
  
  @override
  String get torrentRemoveSuccess => "Torrent removed successfully";
  
  @override
  String get torrentResumeError => "Could not resume torrent";
  
  @override
  String get torrentResumeSuccess => "Torrent resumed successfully";
}

class FrenchLiterals extends LanguageLiterals{

  @override
  String get options => "Options";

  @override
  String get noResults => "Aucun résultat trouvé";

  @override
  String get fetchError => "Impossible de récupérer les données";

  @override
  String get watched => "Monitoré";

  @override
  String get recommended => "Recommandé";

  @override
  String get movies => "Films";

  @override
  String get shows => "Séries";

  @override
  String get add => "Ajouter";

  @override
  String get addHint => "Ajouter un magnet torrent";

  @override
  String get delete => "Supprimer";

  @override
  String get download => "Télechargement";

  @override
  String get name => "Nom";

  @override
  String get pause => "Pause";

  @override
  String get progress => "Progression";

  @override
  String get remove => "Supprimer";

  @override
  String get removeHint => "Supprimer un torrent";

  @override
  String get resume => "Reprendre";

  @override
  String get search => "Rechercher";

  @override
  String get update => "Mettre à jour";

  @override
  String get updateTrackerHint => "Mettre à jour le tracker";

  @override
  String get upload => "Téléversement";

  @override
  String get cancel => "Annuler";
  
  @override
  String get updateUrl => "Mettre à jour l'URL";

  @override
  String get torrentAddError => "Erreur d'ajout de torrent";
  
  @override
  String get torrentAddSuccess => "Torrent ajouté correctement";
  
  @override
  String get updateTrackerError => "Impossible de mettre à jour le tracker";
  
  @override
  String get updateTrackerSuccess => "Tracker mis à jour";
  
  @override
  String get mediaAddError => "Impossible d'ajouter le média";
  
  @override
  String get mediaAddSuccess => "Média ajouté";
  
  @override
  String get mediaRemoveError => "Impossible de supprimer le média";
  
  @override
  String get mediaRemoveSuccess => "Média supprimé";
  
  @override
  String get torrentPauseError => "Impossible de mettre en pause le torrent";
  
  @override
  String get torrentPauseSuccess => "Torrent mis en pause";
  
  @override
  String get torrentRemoveError => "Impossible de supprimer le torrent";
  
  @override
  String get torrentRemoveSuccess => "Torrent supprimé";
  
  @override
  String get torrentResumeError => "Impossible de reprendre le torrent";
  
  @override
  String get torrentResumeSuccess => "Torrent repris";
}