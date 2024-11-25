import 'package:flutter/material.dart';

import 'literals/literals.dart';
import 'media/media.dart';
import 'media/media_widget.dart';
import 'backend/fetchers.dart';
import 'media/searchResultsPage.dart';

class Radarr extends StatefulWidget {
  const Radarr({Key? key}) : super(key: key);

  @override
  RadarrState createState() => RadarrState();
}

class RadarrState extends State<Radarr> {
  final TextEditingController _searchController = TextEditingController();
  List<MediaViewModel> mediaList = [];

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  void searchMedia(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => SearchResultsPage(
            fetcher: () =>
                Fetchers.searchMedia(MediaType.tv, _searchController.text, context)),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    var literals = Literals();
    return Scaffold(
      appBar: AppBar(
        title: const Text('Radarr'),
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
            onPressed: () {
              showDialog(
                context: context,
                builder: (context) {
                  return AlertDialog(
                    title: Text(literals.text.search),
                    content: TextField(
                      controller: _searchController,
                      decoration: InputDecoration(
                        labelText: literals.text.search,
                      ),
                    ),
                    actions: [
                      TextButton(
                        onPressed: () {
                          Navigator.pop(context);
                          searchMedia(context);
                        },
                        child: Text(literals.text.search),
                      ),
                    ],
                  );
                },
              );
            },
          ),
        ],
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.only(top: 16.0),
            child: Align(
              alignment: Alignment.topLeft,
              child: Wrap(
                crossAxisAlignment: WrapCrossAlignment.center,
                children: [
                  const SizedBox(width: 8.0),
                  const Icon(Icons.chevron_right, size: 28),
                  Text(
                    literals.text.watched,
                    style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),
                ],
              ),
            ),
          ),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: MediaList(
                fetcher: () => Fetchers.fetchWatched(MediaType.tv, context),
                itemHeight: MediaQuery.of(context).size.height / 3,
                itemWidth: MediaQuery.of(context).size.width / 3,
                key: const Key('movieWatched'),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 16.0),
            child: Align(
              alignment: Alignment.topLeft,
              child: Wrap(
                crossAxisAlignment: WrapCrossAlignment.center,
                children: [
                  const SizedBox(width: 8.0),
                  const Icon(Icons.chevron_right, size: 28),
                  Text(
                    literals.text.recommended,
                    style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),
                ],
              ),
            ),
          ),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: MediaList(
                fetcher: () => Fetchers.fetchRecommended(MediaType.tv, context),
                itemHeight: MediaQuery.of(context).size.height / 3,
                itemWidth: MediaQuery.of(context).size.width / 3,
                key: const Key('movieRecommended'),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
