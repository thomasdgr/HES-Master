import 'dart:convert';

class Media {
  String name;
  String thumbnail;
  String synopsis;
  String rating;
  String length;
  bool watched;
  MediaType type;

  Media(
    {required this.name,
    required this.thumbnail,
    required this.synopsis,
    required this.rating,
    required this.length,
    required this.watched,
    required this.type,}){
      name = utf8.decode(name.runes.toList());
      synopsis = utf8.decode(synopsis.runes.toList());
      thumbnail = thumbnail;
      rating = rating;
      length = length;
      watched = watched;
      type = type;
    }
}

enum MediaType {
  movie,
  tv,
}