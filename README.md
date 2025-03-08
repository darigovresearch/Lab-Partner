# Lab-Partner
Repository containing code for the low cost solution to manage experiment critical equipment

## Introduction
Very often in labs you need to monitor a particular device which has an old seven segment display or the like that if it falls outside of a given parameter the experiment is no longer valid. This includes -80's that keep things cool and prevents degradation of samples and incubators which are needed to grow samples for a specified amount of time. The idea of Lab Partner is to have a Raspberry Pi with a USB camera pointed at the display and it uses Machine Learning to
1. read the display to monitor this range to either let you know that this situation has occurred to tell you that you need to start again or
2. to notify you as it happens so you can salvage your experiment before it is unsalvageable.

## Documentation
Documentation for this project is currently being hosted here - https://darigovresearch.github.io/Lab-Partner/

### Editing the documentation

After cloning the repository if you wish to edit or make improvements to it, you need to edit the relevant files in the `docs_source` folder and when you want to build it, you run the following command from the root folder of the repository. The output will then be able to be opened locally from the `docs` folder.

```
sphinx-build docs_source/source docs
```

## Contributing
Pull requests, corrections, translations & fixes are welcome. Any contributions must be submitted under the same license that the original piece of work (see below). Take a look at any open issues or submit new ones if there is something that needs to be fixed or added.

Watch our video on how to contribute to open source for a complete overview -> [https://www.youtube.com/watch?v=UWA4wyacY2A](https://www.youtube.com/watch?v=UWA4wyacY2A)

## License
Unless otherwise specified, everything in this repository is covered by the following licence:

The license for this project is yet to be decided on, join the discussion [in this GitHub issue](https://github.com/darigovresearch/Lab-Partner/issues/16).

----

<b>
<div align="center">
    The creation, maintenance and continued development of this project is made possible
    <br>
    thanks to our <a href="http://patreon.com/darigovresearch">Patreon</a> and <a href="https://www.darigovresearch.com/donate">Direct</a> supporters!
    <br>
    Consider joining them if you think this project has earned it!
</div>
</b>
