# Field Selector

https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/

```
kubectl get pods --field-selector status.phase=Running
kubectl get pods --field-selector=status.phase!=Running,spec.restartPolicy=Always
kubectl get services --all-namespaces --field-selector metadata.namespace!=default
kubectl get statefulsets,services --all-namespaces --field-selector metadata.namespace!=default
```
