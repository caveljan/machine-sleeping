Consider a machine reading the pixels of an image

    ... 223, 132, 145, 123, 56, 233, ...

The awake phase would be reading, interpreting them, and when a feature is detected the daily budget is spent and an event is logged. When the budget is completely spent, the sleep phase begins, de-eventing (retracing/detracing the previous day's events). The scope of the de-eventing is to imagine, dream of new features, new possibilities of extraction, of different sources.


## Example

Considering that:

the image has 2 features (x's)

    |--------|
    |000x0000|
    |00000000|
    |000000x0|
    |--------|

the day starts with 952 debs (if the first day, it's a random number between 300 and 1000, for the other days the debs is computed based on the debs of the previous days)

the first feature is easier to extract than the second figure: 452 debs for the first, 260 for the second

952 - 712 (452+260) = 240 debs left at end of day (percent of which will be passed onto the next day, based on the historical trend of debs retention)

the machine sleeps after either:

    i. it spends all the debs

    or

    ii. the micro-task is finished (e.g. an image is read/interpreted)


## Questions

What kind of mechanism is the de-eventing? What kind of equations does it handle?

How is the context of the events re-membered: formed from the other events? To store somekind of meta-events? To have a mechanism for a remembering of a remembrance? Dreaming would then become a sort of chaining of de-eventings.

What kind of data structures are used?

    life_events = {
        current_day: event[]
        last_days: day[]
    }

    day = {
        events: event[]
        metadata: {
            day_start: number
        }
    }

    event = {
        cost: number
        action: string identifier?
    }
