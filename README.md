## HTTPS in the .gov world

Runs .gov domains through Ben Balter's [`site-inspector`](https://github.com/benbalter/site-inspector-ruby) to create a spreadsheet of data on HTTPS strength and adoption in the .gov world.

Can be used with the [official .gov domain list](https://catalog.data.gov/dataset/gov-domains-api).

For each .gov domain, this lists whether:

* HTTPS is enabled (correctly).
* HTTPS is forced (redirect `http://` to `https://`).
* HSTS ([Strict Transport Security](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) is enabled (tells the browser to never use `http://`).
* HSTS is enabled for **all subdomains** and a **long expiration** (needed to be [preloaded](https://hstspreload.appspot.com/) in browsers).


### Setup

The script is tested with Ruby 2.1, and should run on 1.9+.

Install dependencies:

```bash
gem install site-inspector oj
```

Run the script on the domain CSV:

```
./https-scan.rb domains.csv
```

Where `domains.csv` is a CSV in the format of the [official .gov domain list](https://catalog.data.gov/dataset/gov-domains-api).

Prepare for a `cache/` directory to be created, and for that directory to fill up with many `.json` files - one for each domain analyzed.


### TODO

Some of these are/may be [site-inspector](https://github.com/benbalter/site-inspector-ruby) todos.

* Save the certificate to disk.
* Show when a cert is installed but invalid.
* Who issues the cert?
* Loosen HSTS check to site-inspector.
* Easy serialization path for site-inspector results.
* Whether the cert is SHA-1 vs SHA-2.
