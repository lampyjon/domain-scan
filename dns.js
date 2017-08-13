const CDP = require('chrome-remote-interface');

var requested = 0;
var responded = 0;

CDP((client) => {
    const {Network, Page} = client;

    // setup handlers
    Network.requestWillBeSent((params) => {
        requested++;
        console.log(
            "Request " + requested + ": " +
            params.request.url
        );
    });
    Network.responseReceived((params) => {
        responded++;
        console.log(
            "Response " + responded + ": " +
            params.response.url
        );
    });

    // TODO: move to timeout or something other than pageload
    Page.loadEventFired(() => {
        console.log("Requests: " + requested);
        console.log("Responses: " + responded);
        client.close();
    });

    Promise.all([
        Network.enable(),
        Page.enable()
    ]).then(() => {
        return Page.navigate({url: 'https://github.com'});
    }).catch((err) => {
        console.error(err);
        client.close();
    });
}).on('error', (err) => {
    // cannot connect to the remote endpoint
    console.error(err);
});
