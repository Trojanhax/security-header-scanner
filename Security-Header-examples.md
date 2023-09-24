# security header examples
## Content Security Policy (CSP):

- Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline';
## X-Content-Type-Options:

- X-Content-Type-Options: nosniff
## X-Frame-Options:

- X-Frame-Options: DENY
- X-Frame-Options: SAMEORIGIN
## X-XSS-Protection:

- X-XSS-Protection: 1; mode=block
## Referrer-Policy:

- Referrer-Policy: strict-origin-when-cross-origin
## Content-Security-Policy-Report-Only:

- Content-Security-Policy-Report-Only: default-src 'self'; report-uri /report-endpoint
## Cross-Origin Resource Sharing (CORS):

- Access-Control-Allow-Origin: *
- Access-Control-Allow-Headers: Content-Type
- Access-Control-Allow-Methods: GET, POST, OPTIONS
## Feature-Policy:

- Feature-Policy: camera 'none'; geolocation 'self'
## Public Key Pinning Extension (HPKP):

- Public-Key-Pins: pin-sha256="base64=="; max-age=31536000; includeSubDomains
## Expect-CT:

- Expect-CT: enforce, max-age=30, report-uri="https://example.com/ct-report"
## Content-Encoding:

- Content-Encoding: gzip
## Content-Security-Policy-Report-Only:

- Content-Security-Policy-Report-Only: 
- default-src 'none'; report-uri /csp-report-endpoint/
## Access-Control-Allow-Origin:

- Access-Control-Allow-Origin: https://example.com
## Access-Control-Allow-Credentials:

- Access-Control-Allow-Credentials: true
## Access-Control-Expose-Headers:

- Access-Control-Expose-Headers: Authorization
## Access-Control-Max-Age:

- Access-Control-Max-Age: 3600
## Feature-Policy:

- Feature-Policy: vibrate 'self' https://example.com
## X-Permitted-Cross-Domain-Policies:

- X-Permitted-Cross-Domain-Policies: none
## X-Download-Options:

- X-Download-Options: noopen
## Content-Disposition:

- Content-Disposition: attachment; filename="example.pdf"
## Cache-Control:

- Cache-Control: no-store
## Pragma:

- Pragma: no-cache
## X-Robots-Tag:

- X-Robots-Tag: noindex, nofollow
## Feature-Policy:

- Feature-Policy: geolocation 'none'
## Expect-Staple:

- Expect-Staple: max-age=3600, report-uri="https://example.com/staple-report"
## Access-Control-Allow-Methods:

- Access-Control-Allow-Methods: GET, POST
## Access-Control-Allow-Headers:

- Access-Control-Allow-Headers: Content-Type, Authorization
## Access-Control-Allow-Origin:

- Access-Control-Allow-Origin: https://example.com
## Access-Control-Allow-Credentials:

- Access-Control-Allow-Credentials: true