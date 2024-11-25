class Torrent {
  String id;
  String name;
  double progress;
  double downloadSpeed;
  double uploadSpeed;

  Torrent({
    required this.id,
    required this.name,
    required this.progress,
    required this.downloadSpeed,
    required this.uploadSpeed,
  });
}