# Routines subordinate Charm
This charm can configure and execute routines.

To prepare this charm for deployment, run the following to install the
framework in to the `lib/` directory:

```
pip install -t lib/ https://github.com/canonical/operator
```

Link the framework:
```
ln -s ../mod/operator/ops lib/ops
```

Supposing you have deployed cs:ubuntu, deploy the routines charm using the application for identifaction: 

```
juju deploy . ubuntu-routines

```

And add a relation between them:
```
juju add-relation ubuntu ubuntu-routines
```

Configure the routines:
```
juju config ubuntu-routines routines="{ \"uname\": \"uname -a\"}"
```

Run the routine:
```
juju run-action ubuntu-routines/1 run routine=uname --wait
```