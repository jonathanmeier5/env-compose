# env-compose
A CLI utility for composing environment variables.

Sample usage:

Configure your env-compose.yaml
```
providers:
    - name: static
    - name: file
    - name: aws-secrets-manager
env:
    - provider: static
      key: FOO
      value: BAR
    - provider: file
      filename: ./local.env
```

Now execute, for instance, a docker-compose shell:

```
alias ec=env-compose
cd example/
ec run -- docker-compose run --rm app bash
```

And you will have a bash shell in a python docker image with your environment injected into it.
