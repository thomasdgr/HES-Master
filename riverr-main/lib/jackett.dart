 import 'package:flutter/material.dart';

import 'torrent/tracker_widget.dart';

class Jackett extends StatelessWidget {
  const Jackett({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: JackettContent(),
    );
  }
}
