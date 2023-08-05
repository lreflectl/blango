function resolvedCallback(data) {
  console.log('Resolved with data: ' + data)
}

function rejectedCallback(message) {
  console.warn('Rejected with message: ' + message)
}

function lazyAdd(a, b) {
  const doAdd = (resolve, reject) => {
    if (typeof a !== "number" || typeof b !== "number") {
      reject("a and b must both be numbers!")
    } else {
      const sum = a + b
      resolve(sum)
    }
  }

  return new Promise(doAdd)
}

const myPromise = lazyAdd(3, 5)
myPromise.then(resolvedCallback, rejectedCallback)

lazyAdd("foo", "bar").then(resolvedCallback, rejectedCallback)
