def collect(obj):
    arr = []
    for i in obj:
        if type(obj[i]) is str:
            arr.append(obj[i])
        if type(obj[i]) is dict:
            arr = arr + collect(obj[i])
    return arr




obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collect(obj))