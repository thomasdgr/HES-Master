import 'package:flutter/material.dart';

import '../backend/requests.dart';
import '../literals/literals.dart';
import 'tracker.dart';

class JackettContent extends StatefulWidget {
  const JackettContent({Key? key}) : super(key: key);

  @override
  _JackettContentState createState() => _JackettContentState();
}

class _JackettContentState extends State<JackettContent> {
  List<Tracker> trackers = [];

  @override
  void initState() {
    super.initState();
    fetchTrackers();
  }

  Future<void> fetchTrackers() async {
    List<Tracker> fetchedTrackers = await Requests.getTrackers();
    setState(() {
      trackers = fetchedTrackers;
    });
  }

  void updateUrl(BuildContext context, Tracker tracker) {
    TextEditingController urlController =
        TextEditingController(text: tracker.url);

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(Literals().text.updateUrl),
          content: TextField(
            controller: urlController,
            decoration:
                InputDecoration(labelText: Literals().text.updateTrackerHint),
          ),
          actions: <Widget>[
            TextButton(
              child: Text(Literals().text.cancel),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
            TextButton(
              child: Text(Literals().text.update),
              onPressed: () {
                String newUrl = urlController.text;
                Requests.wrapRequest(
                    () => Requests.updateTracker(tracker.id, newUrl),
                    Literals().text.updateTrackerSuccess,
                    Literals().text.updateTrackerError,
                    context);
                tracker.url = newUrl;
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Jackett'),
      ),
      body: ListView.builder(
        itemCount: trackers.length,
        itemBuilder: (context, index) {
          final tracker = trackers[index];
          return ListTile(
            title: Text(tracker.name),
            subtitle: Text(tracker.url),
            onLongPress: () {
              updateUrl(context, tracker);
            },
          );
        },
      ),
    );
  }
}
