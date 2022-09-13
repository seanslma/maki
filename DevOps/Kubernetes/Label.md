# Label and Annotation

https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/

https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/

- Labels can be used to `select objects` and to `find collections of objects` that satisfy certain conditions. 
- Annotations are not used to identify and select objects - to `attach arbitrary non-identifying metadata to objects`. 

## get node labels
```
kubectl get nodes --show-labels | sed 's/,/\n  /g'  #works
kubectl get nodes --show-labels | tr , '\n  '       #can't add space
```
