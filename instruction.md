There is an Apache-style access log at `/app/access.log`. Create a JSON summary report at `/app/report.json`.

The report must be a JSON object with exactly these keys:

- `total_requests`
- `unique_ips`
- `top_path`

Success criteria:

1. `/app/report.json` exists and contains valid JSON.
2. `total_requests` is the number of non-empty log lines in `/app/access.log`.
3. `unique_ips` is the number of distinct client IP addresses, using the first whitespace-separated field of each non-empty log line.
4. `top_path` is the most frequently requested URL path extracted from the quoted HTTP request. For example, the path in `"GET /index.html HTTP/1.1"` is `/index.html`.
