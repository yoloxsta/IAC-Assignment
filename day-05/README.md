### Day-05

#### Gitlab-runner (docker execute)

```
docker --version
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker gitlab-runner
sudo systemctl restart gitlab-runner


---
concurrent = 1
check_interval = 0
connection_max_age = "15m0s"
shutdown_timeout = 0
 
[session_server]
  session_timeout = 1800
 
[[runners]]
  name = "arm-runner" #type is arm
  url = "https://wxyz"
  id = 16
  token = "token"
  token_obtained_at = date
  token_expires_at = date
  executor = "docker"
 
  remove_builds_after = "1h"  # Removes builds older than 1 hour
 
  [runners.custom_build_dir]
  [runners.cache]
    MaxUploadedArchiveSize = 0
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "docker:latest"
    privileged = true
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = true
    volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
    shm_size = 0
    network_mtu = 0
 
    pull_policy = "if-not-present"  # Prevent unnecessary image pulls
    auto_remove = true  # Automatically remove containers after each job
  [runners.machine]
    IdleCount = 0
    IdleScaleFactor = 0.0
    IdleCountMin = 0
    MachineDriver = ""
    MachineName = ""

---
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker gitlab-runner
sudo systemctl restart gitlab-runner

```

- https://youtu.be/9kGC2CrFJME?si=TURZP_yhaj-QJQIz

### curl pod 

```
 kubectl run curlpod -n music-uat --rm -it --image=curlimages/curl --restart=Never -- sh
```