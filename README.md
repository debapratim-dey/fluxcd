# fluxcd

sudo wget https://github.com/fluxcd/flux/releases/download/1.17.1/fluxctl_windows_amd64 -O /usr/bin/fluxctl && sudo chmod +x /usr/bin/fluxctl
$ fluxctl version\


helm upgrade -i flux fluxcd/flux --wait \
--namespace flux \
--set git.url=git@github.com:debapratim-dey/fluxcd

helm upgrade -i helm-operator fluxcd/helm-operator --wait \
--namespace flux \
--set git.ssh.secretName=flux-git-deploy \
--set helm.versions=v3

kubectl delete -f https://raw.githubusercontent.com/fluxcd/helm-operator/1.2.0/deploy/crds.yaml

docker image build -t deb0pratim/dummy_flask_app:1.0 .