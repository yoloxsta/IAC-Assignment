## Day-03

```
❯ helm repo add gitlab https://charts.gitlab.io

❯ helm install gitlab-runner gitlab/gitlab-runner -n gitlab-runner -f gitlab-runner-value.yaml

---
gitlabUrl: https://gitlab.com/
runnerRegistrationToken: ""
concurrent: 10
rbac:
  create: true
serviceAccount:
  create: true

runners:
  config: |
    [[runners]]
      name = "k8s-dind-runner"
      executor = "kubernetes"
      shell = "bash"
      [runners.kubernetes]
        namespace = "gitlab-runner"
        privileged = true
        allow_privilege_escalation = true
        image = "docker:24.0"

        [runners.kubernetes.volumes]
          [[runners.kubernetes.volumes.empty_dir]]
            name = "build-cache"
            mount_path = "/cache"

      [runners.cache]
        Type = "empty_dir"
        Shared = true

```