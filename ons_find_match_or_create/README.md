# some notes

## counts for ONS IRIs in OD metadata but not in ONS
*(only for selected collections)*  

- **TOTAL 289 FAILURES**
- 1 failed ONS IRIs in collection angelus
- 187 failed ONS IRIs in collection building-or
- 9 failed ONS IRIs in collection chinavine
- 0 failed ONS IRIs in collection fealy
- 22 failed ONS IRIs in collection lowenstam
- 2 failed ONS IRIs in collection marketing-photos
- 1 failed ONS IRIs in collection nosatsu
- 67 failed ONS IRIs in collection uo-arch-photos

## query time 
### [@e3240dd](https://github.com/briesenberg07/briesenb_scratchpaper/blob/e3240dd40533fa74595327f1fede11388436b78a/ons_find_match_or_create/1_ons_fails_from_dump.ipynb)
- angelus.ttl = 1m 23.5s
- building-or.ttl = 2m 5.1s
- chinavine.ttl = 1m 29.4s
- fealy.ttl = 2.9s
- lowenstam.ttl = ?
- marketing-photos.ttl = 1m 15.0s
- nosatsu.ttl = 46.1s
- uo-arch-photos.ttl = 2m 27.9s

## parse + retrieve label time 
### [@e3240dd](https://github.com/briesenberg07/briesenb_scratchpaper/blob/e3240dd40533fa74595327f1fede11388436b78a/ons_find_match_or_create/1_ons_fails_from_dump.ipynb)
- angelus.ttl = 2.2s
- building-or.ttl = ?
- chinavine.ttl = 1.6s
- fealy.ttl = 0.0s
- lowenstam.ttl = ?
- marketing-photos.ttl = 1.7s
- nosatsu.ttl = 0.2s
- uo-arch-photos.ttl = 1m 29.2s
