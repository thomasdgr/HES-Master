import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:marquee/marquee.dart';
import 'dart:convert';

import '../backend/requests.dart';
import '../literals/literals.dart';
import 'media.dart';

class MediaViewModel {
  final Media media;

  MediaViewModel(this.media);

  String get name => media.name;
  String get thumbnailUrl => media.thumbnail;
  String get synopsis => media.synopsis;
  String get rating => media.rating;
  String get length => media.length;
  bool get watched => media.watched;

  void onPressed(BuildContext context) {
    if (watched) {
      Requests.wrapRequest(
          () => Requests.removeMedia(media),
          Literals().text.mediaRemoveSuccess,
          Literals().text.mediaRemoveError,
          context);
    } else {
      Requests.wrapRequest(
          () => Requests.addMedia(media),
          Literals().text.mediaAddSuccess,
          Literals().text.mediaAddError,
          context);
    }
  }
}

class MediaList extends StatelessWidget {
  final Future<List<MediaViewModel>> Function() fetcher;
  final double itemHeight;
  final double itemWidth;

  const MediaList(
      {required this.fetcher,
      required this.itemHeight,
      required this.itemWidth,
      Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<MediaViewModel>>(
      future: fetcher(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const CircularProgressIndicator();
        } else if (snapshot.hasError) {
          return Text('Error: ${snapshot.error}');
        } else {
          final List<MediaViewModel> medias = snapshot.data!;
          if (medias.isEmpty) {
            return Text(Literals().text.noResults);
          }
          return ListView.builder(
            scrollDirection: Axis.horizontal,
            itemCount: medias.length,
            itemBuilder: (BuildContext context, int index) {
              final mediaViewModel = medias[index];

              return Padding(
                padding: const EdgeInsets.all(8.0),
                child: Column(
                  children: [
                    Expanded(
                      child: GestureDetector(
                        child: ClipRRect(
                          child: Image.network(
                            mediaViewModel.thumbnailUrl,
                            height: itemHeight,
                            width: itemWidth,
                            fit: BoxFit.cover,
                          ),
                        ),
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => MediaDetail(
                                mediaViewModel: mediaViewModel,
                                key: Key(mediaViewModel.name),
                              ),
                            ),
                          );
                        },
                      ),
                    ),
                    const SizedBox(height: 8),
                    SizedBox(
                      height: 20,
                      width: itemWidth, // Set a fixed width for the container
                      child: Marquee(
                        text: mediaViewModel.name,
                        scrollAxis: Axis.horizontal,
                        crossAxisAlignment: CrossAxisAlignment.start,
                        blankSpace: 30.0,
                        velocity: 25.0,
                      ),
                    ),
                  ],
                ),
              );
            },
          );
        }
      },
    );
  }
}

class MediaDetail extends StatelessWidget {
  final MediaViewModel mediaViewModel;

  const MediaDetail({required this.mediaViewModel, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var imageHeight = MediaQuery.of(context).size.height / 3;
    var imageWidth = MediaQuery.of(context).size.width / 2;

    return Scaffold(
      appBar: AppBar(
        title: Text(mediaViewModel.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(
                  width: imageWidth,
                  height: imageHeight,
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(8),
                    child: Image.network(
                      mediaViewModel.thumbnailUrl,
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                const SizedBox(width: 16.0),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        mediaViewModel.name,
                        style: const TextStyle(
                          fontSize: 18.0,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 8.0),
                      Text(
                        mediaViewModel.length,
                        style: const TextStyle(fontSize: 16.0),
                      ),
                      const SizedBox(height: 4.0),
                      Text(
                        "Rating: ${mediaViewModel.rating}/10",
                        style: const TextStyle(fontSize: 16.0),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 8.0),
            const Divider(),
            const SizedBox(height: 8.0),
            Text(mediaViewModel.synopsis),
            Expanded(
              child: Align(
                alignment: Alignment.bottomCenter,
                child: ElevatedButton(
                  onPressed: () => mediaViewModel.onPressed(context),
                  child: Text(mediaViewModel.watched ? 'Remove' : 'Add'),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
