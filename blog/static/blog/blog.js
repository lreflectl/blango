class Greeter {
  constructor (name) {
    this.name = name
  }

  getGreeting () {
    if (this.name === undefined) {
      return "Hello, noname!"
    } else {
      return "Hello, " + this.name + "!"
    }
  }

  showGreeting (greetingMessage) {
    console.log(greetingMessage)
  }

  greet () {
    this.showGreeting(this.getGreeting())
  }
}

class DelayedGreeter extends Greeter {
  delay = 2000

  constructor (name, delay) {
    super(name)
    if (delay !== undefined) {
      this.delay = delay
    }
  }

  greet () {
    setTimeout(
      () => {
        this.showGreeting(this.getGreeting())
      }, this.delay
    )
  }
}

const delayedGreeter = new DelayedGreeter("Poppy", 1000)
delayedGreeter.greet()

const greeter2 = new Greeter("pecky")
greeter2.greet()
