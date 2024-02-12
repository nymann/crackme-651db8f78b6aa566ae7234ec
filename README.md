# Crackme 651db8f78b6aa566ae7234ec

```sh
# Create a new virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the program
make install
```

### Run

```sh
crackme_651db8f78b6aa566ae7234ec
```

You can generate multiple keys at a time (guaranteed to be uniqueu)

```sh
crackme_651db8f78b6aa566ae7234ec --keys-to-generate 100
```

### Test a key

```sh
docker build -f docker/Dockerfile --tag=crackme:651db8f78b6aa566ae7234ec .
docker run crackme:651db8f78b6aa566ae7234ec 'ABBB-CDCC-CCED-EEFE'                                                                                                                                1 ↵
Access granted!
```

## Development

For help getting started developing check [DEVELOPMENT.md](DEVELOPMENT.md)
