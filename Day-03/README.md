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
--------------------
```
{
  "__inputs": [
    {
      "name": "DS_LOKI",
      "label": "loki",
      "description": "",
      "type": "datasource",
      "pluginId": "loki",
      "pluginName": "Loki"
    },
    {
      "name": "DS_PROMETHEUS",
      "label": "Prometheus",
      "description": "",
      "type": "datasource",
      "pluginId": "prometheus",
      "pluginName": "Prometheus"
    }
  ],
  "__elements": {},
  "__requires": [
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "11.1.0"
    },
    {
      "type": "panel",
      "id": "logs",
      "name": "Logs",
      "version": ""
    },
    {
      "type": "datasource",
      "id": "loki",
      "name": "Loki",
      "version": "1.0.0"
    },
    {
      "type": "datasource",
      "id": "prometheus",
      "name": "Prometheus",
      "version": "1.0.0"
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "datasource",
          "uid": "grafana"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "description": "Container/Pod Log Quick Search(Loki as DataSource)",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "gnetId": 16970,
  "graphTooltip": 0,
  "id": null,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "loki",
        "uid": "${DS_LOKI}"
      },
      "description": "",
      "gridPos": {
        "h": 24,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 2,
      "options": {
        "dedupStrategy": "none",
        "enableLogDetails": true,
        "prettifyLogMessage": false,
        "showCommonLabels": false,
        "showLabels": false,
        "showTime": true,
        "sortOrder": "Descending",
        "wrapLogMessage": false
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "{namespace=\"$namespace\", job=~\"$job\"} |~ \"(?i)$searchable_pattern\" ",
          "hide": false,
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Search Result",
      "type": "logs"
    }
  ],
  "refresh": "1m",
  "schemaVersion": 39,
  "tags": [
    "Loki",
    "logging"
  ],
  "templating": {
    "list": [
      {
        "allValue": ".*",
        "current": {},
        "datasource": {
          "type": "loki",
          "uid": "${DS_LOKI}"
        },
        "definition": "label_values({namespace=~\".+\"}, namespace)",
        "hide": 0,
        "includeAll": false,
        "label": "Namespace",
        "multi": false,
        "name": "namespace",
        "options": [],
        "query": "label_values({namespace=~\".+\"}, namespace)",
        "refresh": 2,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": ".*",
        "current": {},
        "datasource": {
          "type": "loki",
          "uid": "${DS_LOKI}"
        },
        "definition": "label_values({namespace=\"$namespace\"}, pod)",
        "hide": 0,
        "includeAll": true,
        "label": "job",
        "multi": false,
        "name": "job",
        "options": [],
        "query": {
          "label": "job",
          "refId": "LokiVariableQueryEditor-VariableQuery",
          "stream": "{namespace=\"$namespace\"}",
          "type": 1
        },
        "refresh": 2,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {
          "selected": true,
          "text": "",
          "value": ""
        },
        "hide": 0,
        "label": "Search (case insensitive)",
        "name": "searchable_pattern",
        "options": [
          {
            "selected": true,
            "text": "",
            "value": ""
          }
        ],
        "query": "",
        "skipUrlSync": false,
        "type": "textbox"
      }
    ]
  },
  "time": {
    "from": "now-1h",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ]
  },
  "timezone": "",
  "title": "Container Log Quick Search",
  "uid": "7ecZpUkRk",
  "version": 1,
  "weekStart": ""
}

---