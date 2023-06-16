# Publish/subscribe

pub/sub events mode. can cause high memory usage in redis and sub can lost a little data.

commands
- `publish channel message`: publishe a message to channel
- `subscribe channel [channel ...]`: subscribe to channels
- `unsubscribe [channel [channel ...]]`: unsubscribe from channels
- `psubscribe pattern [pattern ...]`: subscribe to messages match given pattern
- `punsubscribe [pattern [pattern ...]]`: unsubscribe from provided patterns
