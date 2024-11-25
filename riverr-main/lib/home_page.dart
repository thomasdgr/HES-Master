import 'package:flutter/material.dart';

import 'jackett.dart';
import 'radarr.dart';
import 'sonarr.dart';
import 'deluge.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  HomePageState createState() => HomePageState();
}

class HomePageState extends State<HomePage> {
  int _currentIndex = 2;

  final List<Widget> _pages = [
    Jackett(),
    Sonarr(),
    Radarr(),
    Deluge(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _pages[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.accessibility),
            label: 'Jackett',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings_input_antenna),
            label: 'Sonarr',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.radar),
            label: 'Radarr',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.umbrella_rounded),
            label: 'Deluge',
          ),
        ],
        selectedItemColor: Colors.blue,
        unselectedItemColor: Colors.black,
      ),
    );
  }
}
