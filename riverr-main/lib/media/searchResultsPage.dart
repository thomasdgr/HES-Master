import 'package:flutter/material.dart';
import 'package:marquee/marquee.dart';

import 'media_widget.dart';

class SearchResultsPage extends StatelessWidget {
  final Future<List<MediaViewModel>> Function() fetcher;

  const SearchResultsPage({required this.fetcher, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Search Results'),
      ),
      body: SearchMediaList(
        fetcher: () => fetcher(),
        key: const Key('searchResultsPage'),
      ),
    );
  }
}

class SearchMediaList extends StatelessWidget {
  final Future<List<MediaViewModel>> Function() fetcher;

  const SearchMediaList({required this.fetcher, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final double itemWidth = MediaQuery.of(context).size.width / 2;

    return FutureBuilder<List<MediaViewModel>>(
      future: fetcher(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const CircularProgressIndicator();
        } else if (snapshot.hasError) {
          return Text('Error: ${snapshot.error}');
        } else {
          final List<MediaViewModel> movies = snapshot.data!;

          return GridView.builder(
            scrollDirection: Axis.vertical,
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,
              childAspectRatio: itemWidth / (itemWidth * 1.5),
            ),
            itemBuilder: (BuildContext context, int index) {
              final mediaViewModel = movies[index];

              return Padding(
                padding: const EdgeInsets.all(8.0),
                child: Column(
                  children: [
                    Expanded(
                      child: GestureDetector(
                        child: ClipRRect(
                          child: Image.network(
                            mediaViewModel.thumbnailUrl,
                            height: itemWidth * 1.5,
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
            itemCount: movies.length,
          );
        }
      },
    );
  }
}
