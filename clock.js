/*
Introduction
Implement a clock that handles times without dates.

You should be able to add and subtract minutes to it.

Two clocks that represent the same time should be equal to each other.
*/

class Clock {
  constructor(hours, minutes) {
    this.hours = hours
    this.minutes = minutes
  }

  addHours(hours) {
    let adjustedHours = hours % 24
    this.hours += adjustedHours
    if(this.hours > 24) {
      this.hours -= 24
    }
  }

  addMinutes(minutes) {
    let adjustedHours = Math.floor(minutes / 60)
    this.addHours(adjustedHours)
    let adjustedMinutes = minutes % 60
    this.minutes += adjustedMinutes
    if(this.minutes > 60) {
      this.hours += 1
      this.minutes -= 60
    }
  }

  logTime() {
    if(this.minutes < 10) {
      console.log(`The time is ${this.hours}:0${this.minutes}`)
    } else {
      console.log(`The time is ${this.hours}:${this.minutes}`)
    }
  }

}


const testClock = new Clock(8, 40)
testClock.addHours(25)
testClock.logTime()
testClock.addMinutes(121)
testClock.logTime()
