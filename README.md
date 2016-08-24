# ThePrepper

The script takes the list of names from the file or it uses harvester to grab the list from the LinkedIn.

It then creates the list of email addresses.

```
Usage:

./theprepper.py <email_domain> <mode> <optional_names_file>

modes:

1 - <first_initial><last_name>@domain
2 - <first_name><last_initial>@domain
3 - <first_name>.<last_name>@domain
4 - <first_name><last_name>@domain

Examples:

./theprepper.py somecompany.com 1 
./theprepper.py somecompany.com 2 full_names.txt
```
