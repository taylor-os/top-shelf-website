<?php
// Live subscriber count for the home page, read from the channel's public YouTube page.
// YouTube only publishes three significant figures (1.12M), so that is all there is to show.
// The channel id below is show.channelId in data.js.
// ponytail: scrapes the public page, cached 10 minutes. If YouTube changes the markup, switch to
// the Data API (channels.list?part=statistics) with a server-side key.
header('Content-Type: application/json');
header('Cache-Control: public, max-age=300');

$cache = sys_get_temp_dir() . '/mk-subs.json';
if (is_file($cache) && time() - filemtime($cache) < 600) { readfile($cache); exit; }

$ch = curl_init('https://www.youtube.com/channel/UC1gkLFIojYo1TGhZM84rZeQ/about');
curl_setopt_array($ch, [
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_TIMEOUT => 8,
  CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
  CURLOPT_HTTPHEADER => ['Accept-Language: en-US'],
]);
$html = curl_exec($ch);

if ($html && preg_match('/"subscriberCountText":"([\d.]+)([KM]?) subscribers"/', $html, $m)) {
  $scale = ['' => 1, 'K' => 1e3, 'M' => 1e6][$m[2]];
  $out = json_encode(['text' => $m[1] . $m[2], 'count' => (int) round((float) $m[1] * $scale), 'fetchedAt' => gmdate('c')]);
  file_put_contents($cache, $out, LOCK_EX);
  echo $out;
  exit;
}

if (is_file($cache)) { readfile($cache); exit; } // a stale count beats none
http_response_code(502);
echo '{"error":"unavailable"}';
