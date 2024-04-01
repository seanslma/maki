# Function
https://helm.sh/docs/chart_template_guide/function_list/#trimprefix

## string
- trimPrefix
- lower

remove namespace from name:
- namespace: dev
- name: dev-test-app
- app: {{ trimPrefix (printf "%s-" .Values.namespace) .Chart.Name }}
