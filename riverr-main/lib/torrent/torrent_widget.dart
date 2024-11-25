import 'package:flutter/material.dart';
import 'package:marquee/marquee.dart';

import '../backend/requests.dart';
import '../literals/literals.dart';
import 'torrent.dart';

class TorrentViewModel {
  Future<List<Torrent>> getTorrents() async {
    // Call the async method to fetch torrents
    List<Torrent> torrents = await Requests.getTorrents();
    torrents.sort((a, b) => a.progress > b.progress ? -1 : 1);
    return torrents;
  }

  List<DataRow> getTorrentRows(BuildContext context, List<Torrent> torrents) {
    return torrents.map((torrent) {
      return DataRow(
        cells: [
          DataCell(
            SizedBox(
              width: 150,
              height: 50,
              child: Marquee(
                  text: torrent.name,
                  scrollAxis: Axis.horizontal,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  blankSpace: 18.0,
                  velocity: 25.0),
            ),
          ),
          DataCell(
            LinearProgressIndicator(
              value: torrent.progress / 100,
              color: torrent.progress < 100 ? Colors.blue : Colors.green,
              // blue if downloading, green if seeding
            ),
          ),
          DataCell(Text(
              '${(torrent.downloadSpeed / 1000000).toStringAsFixed(1)} MB/s')),
          DataCell(Text(
              '${(torrent.uploadSpeed / 1000000).toStringAsFixed(1)} MB/s')),
        ],
        onLongPress: () => {
          // Open a dialog with pause/resume and delete options
          showDialog(
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                title: Text(torrent.name),
                actions: [
                  Row(
                    children: [
                      TextButton(
                        // Pause
                        onPressed: () {
                          Navigator.pop(context);
                          Requests.wrapRequest(() => Requests.pauseTorrent(torrent.id), Literals().text.torrentPauseSuccess, Literals().text.torrentPauseError, context);
                        },
                        child: Text(Literals().text.pause),
                      ),
                      TextButton(
                        // Resume
                        onPressed: () {
                          Navigator.pop(context);
                          Requests.wrapRequest(() => Requests.resumeTorrent(torrent.id), Literals().text.torrentResumeSuccess, Literals().text.torrentResumeError, context);
                        },
                        child: Text(Literals().text.resume),
                      ),
                      TextButton(
                        // Remove
                        onPressed: () {
                          Navigator.pop(context);
                          Requests.wrapRequest(() => Requests.removeTorrent(torrent.id), Literals().text.torrentRemoveSuccess, Literals().text.torrentRemoveError, context);
                        },
                        child: Text(Literals().text.remove),
                      ),
                      TextButton(
                        // Cancel
                        onPressed: () {
                          Navigator.pop(context);
                        },
                        child: Text(Literals().text.cancel),
                      ),
                    ],
                  )
                ],
              );
            },
          )
        },
      );
    }).toList();
  }
}
