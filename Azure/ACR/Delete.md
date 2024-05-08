# Delete

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-delete

## delete repo
```sh
az acr repository delete --name <acr-name> --repository <repo-name>
```

## delete by tag
```sh
az acr repository delete -n <acr-name> -t <repo-name>:<tag>
az acr repository delete --name <acr-name> --image <repo-name>:<tag>
```

## delte digests by timestamp
```sh
# Change to 'true' to enable image delete
ENABLE_DELETE=false

# Modify for your environment
REGISTRY=myregistry
REPOSITORY=myrepository
TIMESTAMP=2019-04-05

# Loop through command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -d)
            ENABLE_DELETE=true
            shift # past argument
            ;;
        -r|--registry)
            REGISTRY="$2"
            shift # past argument
            shift # past value
            ;;
        -p|--repository)
            REPOSITORY="$2"
            shift # past argument
            shift # past value
            ;;
        -t|--timestamp)
            TIMESTAMP="$2"
            shift # past argument
            shift # past value
            ;;
        *)    # unknown option
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done 

# Delete all images older than specified timestamp
if [ "$ENABLE_DELETE" = true ]
then
    az acr manifest list-metadata --name $REPOSITORY --registry $REGISTRY \
    --orderby time_asc --query "[?lastUpdateTime < '$TIMESTAMP'].digest" -o tsv \
    | xargs -I% az acr repository delete --name $REGISTRY --image $REPOSITORY@% --yes
else
    echo "No data deleted."
    echo "Set ENABLE_DELETE=true to enable deletion of these images in $REPOSITORY:"
    az acr manifest list-metadata --name $REPOSITORY --registry $REGISTRY \
    --orderby time_asc --query "[?lastUpdateTime < '$TIMESTAMP'].[digest, lastUpdateTime, imageSize, tags[:]]" -o table \
    | tail -n +3 | cut -d ' ' -f1,3- | awk '{split($2,a,"."); printf "%s %s %.2fGiB %s\n", $1, a[1], $3/1024/1024/1024, $4 }'
fi
```
