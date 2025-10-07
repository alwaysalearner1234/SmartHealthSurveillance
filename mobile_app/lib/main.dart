import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('ASHA Health Form')),
        body: Center(
          child: Column(
            children: [
              Text('Sample Input Form'),
              TextField(decoration: InputDecoration(labelText:'Village')),
              TextField(decoration: InputDecoration(labelText:'Diarrhea Cases')),
              ElevatedButton(onPressed: (){}, child: Text('Submit'))
            ],
          ),
        ),
      ),
    );
  }
}
