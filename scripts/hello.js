// http-request
console.log('test script');

let headers = $request.headers;
console.log(headers);

$done({ headers });