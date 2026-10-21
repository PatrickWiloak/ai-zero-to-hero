// ai.patrickwiloak.com -> ai.patricklukewilson.com (AI Zero to Hero), path and query kept.
// Owned by the ai-zero-to-hero repo (see its CLAUDE.md). Created 2026-10-21.
function handler(event) {
    var r = event.request;
    var q = Object.keys(r.querystring).map(function (k) {
        var v = r.querystring[k];
        return v.value === '' ? k : k + '=' + v.value;
    }).join('&');
    return {
        statusCode: 301,
        statusDescription: 'Moved Permanently',
        headers: { location: { value: 'https://ai.patricklukewilson.com' + r.uri + (q ? '?' + q : '') } }
    };
}
