import 'dart:ui';

import 'package:flutter/material.dart';
import 'home_page.dart';
import 'literals/literals.dart';

void main() {
  initLanguage();
  runApp(const MyApp());
}

void initLanguage() {
  var language = window.locale.languageCode; 
  Literals lit = Literals();
  lit.text = "fr" == language ? FrenchLiterals() : EnglishLiterals();
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Riverr',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
}