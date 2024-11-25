import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import '../media/media.dart';
import '../media/media_widget.dart';
import '../literals/literals.dart';

class Fetchers {
  static const String HOSTURL = "http://192.168.1.78:3000";

  static Future<List<MediaViewModel>> fetchWatched(
    MediaType mediaType, BuildContext context) async {
    var literals = Literals();
    var type = typeToString(mediaType);
    try {
      final response = await http
          .get(Uri.parse('$HOSTURL/get$type'))
          .timeout(const Duration(seconds: 7));
      if (response.statusCode == 200) {
        final jsonData = json.decode(response.body);
        final List<MediaViewModel> movies =
            jsonData.map<MediaViewModel>((data) {
          return MediaViewModel(
            Media(
              name: data['name'],
              thumbnail: data['thumbnail'],
              synopsis: data['synopsis'],
              rating: data['rating'],
              length: data['length'],
              watched: data['watched'],
              type: mediaType
            ),
          );
        }).toList();

        return movies;
      } else {
        return [];
      }
    } catch (error) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(literals.text.fetchError),
        ),
      );
      return [];
    }
  }

   static Future<List<MediaViewModel>> fetchRecommended(
      MediaType mediaType, BuildContext context) async {
    var literals = Literals();
    var type = typeToString(mediaType);
    try {
      final response = await http
          .get(Uri.parse('$HOSTURL/reco$type'))
          .timeout(const Duration(seconds: 7));
      if (response.statusCode == 200) {
        final jsonData = json.decode(response.body);
        final List<MediaViewModel> movies =
            jsonData.map<MediaViewModel>((data) {
          return MediaViewModel(
            Media(
              name: data['name'],
              thumbnail: data['thumbnail'],
              synopsis: data['synopsis'],
              rating: data['rating'],
              length: data['length'],
              watched: data['watched'],
              type: mediaType,
            ),
          );
        }).toList();

        return movies;
      } else {
        return [];
      }
    } catch (error) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(literals.text.fetchError),
        ),
      );
      return [];
    }
  }

  static Future<List<MediaViewModel>> searchMedia(
    MediaType mediaType, String query, BuildContext context) async {
    var literals = Literals();
    var type = typeToString(mediaType);

    String url = '$HOSTURL/search$type?title=$query';
    try {
      var response =
          await http.get(Uri.parse(url)).timeout(const Duration(seconds: 7));

      if (response.statusCode == 200) {
        final jsonData = json.decode(response.body);
        final List<MediaViewModel> searchResults =
            jsonData.map<MediaViewModel>((data) {
          return MediaViewModel(
            Media(
              name: data['name'],
              thumbnail: data['thumbnail'],
              synopsis: data['synopsis'],
              rating: data['rating'],
              length: data['length'],
              watched: data['watched'],
              type: mediaType,
            ),
          );
        }).toList();
        return searchResults;
      } else {
        return [];
      }
    } catch (error) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(literals.text.fetchError),
        ),
      );
      return [];
    }
  }

  static String typeToString(MediaType type){
    switch(type){
      case MediaType.movie:
        return 'movies';
      case MediaType.tv:
        return 'tv';
    }
  }
}
