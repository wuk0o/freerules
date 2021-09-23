/**
 * Bypass Paywalls
 */

// console.log('==== Bypass Paywalls ====');
// console.log($request.url);
// console.log($request.method);
// console.log($request.headers);

let headers = $request.headers;
if (/https?:\/\/www\.wsj\.com/.test($request.url)) {
    // wsj.com
    headers['Cookie'] = '';
    headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/93.0.4577.39 Mobile/15E148 Safari/604.1';
    headers['Referer'] = 'https://www.google.com';
}

$done({ headers });