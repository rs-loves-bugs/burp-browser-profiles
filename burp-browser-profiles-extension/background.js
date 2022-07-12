var color = 'red';

chrome.webRequest.onBeforeSendHeaders.addListener(function(details){
  var headers = details.requestHeaders,
  blockingResponse = {};
  headers.push({
		name: 'X-PwnFox-Color',
		value: color,
  });
  blockingResponse.requestHeaders = headers;
  return blockingResponse;
},
{urls: [ "<all_urls>" ]},['requestHeaders','blocking','extraHeaders']);
