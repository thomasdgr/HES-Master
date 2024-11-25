import 'dart:async';

import 'package:flutter/material.dart';
import 'package:riverr/backend/requests.dart';

import 'torrent/torrent_widget.dart';
import 'torrent/torrent.dart';
import 'literals/literals.dart';

class Deluge extends StatefulWidget {
  const Deluge({Key? key}) : super(key: key);

  @override
  DelugeState createState() => DelugeState();
}

class DelugeState extends State<Deluge> {
  late Future<List<Torrent>> _torrentsFuture;
  late TorrentViewModel _viewModel;
  late Timer _timer;

  @override
  void initState() {
    super.initState();
    _viewModel = TorrentViewModel();
    _torrentsFuture = _viewModel.getTorrents();
    _timer = Timer.periodic(const Duration(seconds: 5), (_) {
      setState(() {
        _torrentsFuture = _viewModel.getTorrents();
      });
    });
  }

  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    var literals = Literals();
    return Scaffold(
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            // Open a dialog with a text field to add a torrent magnet url
            TextEditingController urlController = TextEditingController();
            showDialog(
              context: context,
              builder: (context) {
                return AlertDialog(
                  title: Text(literals.text.addHint),
                  content: TextField(
                    controller: urlController,
                    decoration: InputDecoration(
                      labelText: literals.text.addHint,
                    ),
                  ),
                  actions: [
                    TextButton(
                      onPressed: () {
                        urlController.text = "";
                        Navigator.pop(context);
                      },
                      child: Text(literals.text.cancel),
                    ),
                    TextButton(
                      onPressed: () {
                        Navigator.pop(context);
                        Requests.wrapRequest(
                          () => Requests.addTorrent(urlController.text),
                          Literals().text.torrentAddSuccess,
                          Literals().text.torrentAddError,
                          context,
                        );
                      },
                      child: Text(literals.text.add),
                    ),
                  ],
                );
              },
            );
          },
          child: const Icon(Icons.add),
        ),
        appBar: AppBar(
          title: const Text('Deluge'),
        ),
        body: RefreshIndicator(
          onRefresh: () async {
            setState(() {
              _torrentsFuture = _viewModel.getTorrents();
            });
          },
          child: FutureBuilder<List<Torrent>>(
            future: _torrentsFuture,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting &&
                  !snapshot.hasData) {
                return const SingleChildScrollView(
                  physics: AlwaysScrollableScrollPhysics(),
                  child: Center(child: CircularProgressIndicator()),
                );
              } else if (snapshot.hasError) {
                return Center(child: Text('Error: ${snapshot.error}'));
              } else {
                List<Torrent> torrents = snapshot.data!;
                return SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: DataTable(
                    columns: [
                      DataColumn(label: Text(literals.text.name)),
                      DataColumn(label: Text(literals.text.progress)),
                      DataColumn(label: Text(literals.text.download)),
                      DataColumn(label: Text(literals.text.upload)),
                    ],
                    rows: _viewModel.getTorrentRows(context, torrents),
                  ),
                );
              }
            },
          ),
        ));
  }
}
