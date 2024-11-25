import 'package:flutter/material.dart';
import 'package:riverr/media/media.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import '../torrent/torrent.dart';
import '../torrent/tracker.dart';

class Requests {
  // ignore: constant_identifier_names
  static const String HOSTURL = "http://192.168.1.78:3000";

  static Future<List<Torrent>> getTorrents() async {
    // request on HOSTURL/gettorrents
    final response = await http
        .get(Uri.parse('$HOSTURL/gettorrents'))
        .timeout(const Duration(seconds: 7));

    if (response.statusCode != 200) {
      throw Exception('Failed to load torrents');
    }

    final jsonData = json.decode(response.body);

    final List<Torrent> torrents = jsonData.map<Torrent>((data) {
      return Torrent(
          downloadSpeed: data['download_speed'] + .0,
          uploadSpeed: data['upload_speed'] + .0,
          progress: data['progress'] /
              100.0, // API returns 10000 for completed torrent
          name: data['name'],
          id: data['torrent_id']);
    }).toList();
    return torrents;
  }

  static Future<int> addTorrent(String magnetUrl) async {
    final response =
        await http.post(Uri.parse('$HOSTURL/addtorrents?magnet_link=$magnetUrl'));
    return response.statusCode;
  }

  static Future<int> removeTorrent(String id) async {
    final response =
        await http.delete(Uri.parse('$HOSTURL/removetorrents?torrent_id=$id'));
    return response.statusCode;
  }

  static Future<int> pauseTorrent(String id) async {
    final response =
        await http.get(Uri.parse('$HOSTURL/pausetorrents?torrent_id=$id'));
    return response.statusCode;
  }

  static Future<int> resumeTorrent(String id) async {
    final response =
        await http.get(Uri.parse('$HOSTURL/resumetorrents?torrent_id=$id'));
    return response.statusCode;
  }

  static Future<int> editTracker(int id, String tracker) {
    throw UnimplementedError();
  }

  static Future<List<Tracker>> getTrackers() async {
    final response = await http.get(Uri.parse('$HOSTURL/gettrackers'));

    if (response.statusCode != 200) {
      throw Exception('Failed to load trackers');
    }

    final jsonData = json.decode(response.body);

    final List<Tracker> trackers = jsonData.map<Tracker>((data) {
      return Tracker(
          data['id'], data['url'], data['name']);
    }).toList();
    return trackers;
  }

  static Future<int> updateTracker(String id, String newUrl) {
    throw UnimplementedError();
  }

  static Future<int> removeMedia(Media media) async {
    if(media.type == MediaType.movie) {
      return await http.delete(Uri.parse('$HOSTURL/removemovies?title=${media.name.toLowerCase()}')).then((value) => value.statusCode);
    } else {
      return await http.delete(Uri.parse('$HOSTURL/removeseries?title=${media.name.toLowerCase()}')).then((value) => value.statusCode);
    }
  }

  static Future<int> addMedia(Media media) async {
    if(media.type == MediaType.movie) {
      return await http.post(Uri.parse('$HOSTURL/addmovies?title=${media.name.toLowerCase()}')).then((value) => value.statusCode);
    } else {
      return await http.post(Uri.parse('$HOSTURL/addtv?title=${media.name.toLowerCase()}')).then((value) => value.statusCode);
    }
  }

  static void wrapRequest(Future<int> Function() request, String successMessage,
      String errorMessage, BuildContext context) {
    try {
      request().then((value) => value == 200
          ? ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text(successMessage),
              ),
            )
          : ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text(errorMessage),
              ),
            ));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(errorMessage),
        ),
      );
    }
  }
}
