# System architecture
...

# Projections on write vs on read
Computed-at-read is selected with the following reasoning:
* Discord handles a majority of read operations (app view is only computed on update)
* Keeps database design simple and normalized
* Minimal writes
* Strong consistency

# Data model
## proto
* `ObjectInfo` - pure user-set metadata about an object
* `Object` - ObjectInfo + version + system-set discord metadata
* `ObjectView` - ObjectInfo + computed view data

# REST: FastAPI vs gRPC transcoding
* FastAPI is used for REST API
* gRPC is used for internal service-to-service communication
* gRPC transcoding is not used to ensure proper HTTP headers creation at the gateway level