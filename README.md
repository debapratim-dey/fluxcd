# Install Flux:

Create the namespace where all the flux resource will reside:
```sh
kubectl create ns flux
```

Apply the CustomResource of flux call `HelmRelease` which will do all the magic
```sh
kubectl apply -f https://raw.githubusercontent.com/fluxcd/helm-operator/1.2.0/deploy/crds.yaml
```

Using `helm`, first add the Flux CD Helm repository:
```sh
helm repo add fluxcd https://charts.fluxcd.io
```

Install the helm-operator, which will help manage the helm-charts:
```sh
helm upgrade -i helm-operator fluxcd/helm-operator \
    --namespace flux \
    --set helm.versions=v3
```

Now, link the repo you want to manage via FluxCD to flux:
```sh
helm upgrade -i flux fluxcd/flux --wait \
--namespace flux \
--set git.url=git@github.com:debapratim-dey/fluxcd
```

At this step, Flux will generate an `SSH key`. Grab that key by running the command given below and put it inside  
the `Settings > Deploy Keys` for that repo:
```sh
fluxctl identity --k8s-fwd-ns flux
```

Install Flux Helm Operator with Helm v3 support:
```sh
helm upgrade -i helm-operator fluxcd/helm-operator --wait \
--namespace flux \
--set git.ssh.secretName=flux-git-deploy \
--set helm.versions=v3
```

And we are good to go! :)
	
### _A Few basic commands:_

To install `fluxctl` on `WSL`:
```sh
sudo wget https://github.com/fluxcd/flux/releases/download/1.17.1/fluxctl_windows_amd64 -O /usr/bin/fluxctl && sudo chmod +x /usr/bin/fluxctl
$ fluxctl version\
```

	
To build a docker image:
```sh
docker image build -t deb0pratim/dummy_flask_app:1.0 .
```

