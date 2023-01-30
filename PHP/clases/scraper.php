<?php

class WebScraper {
    public function scrape($url) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $html = curl_exec($ch);
        curl_close($ch);
        
        // Use regular expressions or another library like DOMDocument to parse the HTML
        preg_match_all('/<p>(.*?)<\/p>/', $html, $matches);
        
        return $matches[1];
    }
}

$scraper = new WebScraper();
$paragraphs = $scraper->scrape('https://www.example.com');

foreach ($paragraphs as $p) {
    echo $p . "\n";
}
