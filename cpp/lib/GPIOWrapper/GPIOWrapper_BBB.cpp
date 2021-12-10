#include "BeagleBoneBlack-GPIO/gpio/const.h"
#include "BeagleBoneBlack-GPIO/gpio/manager.h"
#include "GPIOWrapper.hpp"

namespace GPIOWrapper {

static beagle::gpio::GPIOManager* gp = beagle::gpio::GPIOManager::getInstance();

int getPin(std::string name) {
  return beagle::gpio::GPIOManager::getInstance()->getGpioByKey(name.c_str());
}

int setupPin(unsigned int pin) { return gp->exportPin(pin); }

int setupPin(std::string pin) {
  int p = beagle::gpio::GPIOManager::getInstance()->getGpioByKey(pin.c_str());
  return gp->exportPin(p);
}

int setupPin(unsigned int pin, PINMODE mode) {
  setupPin(pin);
  return setMode(pin, mode);
}

int setupPin(std::string pin, PINMODE mode) {
  int p = beagle::gpio::GPIOManager::getInstance()->getGpioByKey(pin.c_str());
  setupPin(p);
  return setMode(p, mode);
}

int closePin(unsigned int pin) { return gp->unexportPin(pin); }

int closePin(std::string pin) {
  int p = beagle::gpio::GPIOManager::getInstance()->getGpioByKey(pin.c_str());
  return gp->unexportPin(p);
}

int setMode(unsigned int pin, PINMODE mode) {
  if (mode == INPUT) {
    return gp->setDirection(pin, beagle::gpio::INPUT);
  } else {
    return gp->setDirection(pin, beagle::gpio::OUTPUT);
  }
}

int setMode(std::string pin, PINMODE mode) {
  int p = beagle::gpio::GPIOManager::getInstance()->getGpioByKey(pin.c_str());
  if (mode == INPUT) {
    return gp->setDirection(p, beagle::gpio::INPUT);
  } else {
    return gp->setDirection(p, beagle::gpio::OUTPUT);
  }
}

int getMode(unsigned int pin) { return gp->getDirection(pin); }

int getMode(std::string pin) {
  int p = beagle::gpio::GPIOManager::getInstance()->getGpioByKey(pin.c_str());
  return gp->getDirection(p);
}

int setValue(unsigned int pin, PINVALUE value) {
  if (value == HIGH) {
    return gp->setValue(pin, beagle::gpio::HIGH);
  } else {
    return gp->setValue(pin, beagle::gpio::LOW);
  }
}

int setValue(std::string pin, PINVALUE value) {
  int p = beagle::gpio::GPIOManager::getInstance()->getGpioByKey(pin.c_str());
  if (value == HIGH) {
    return gp->setValue(p, beagle::gpio::HIGH);
  } else {
    return gp->setValue(p, beagle::gpio::LOW);
  }
}

int getValue(unsigned int pin) { return gp->getValue(pin); }

int getValue(std::string pin) {
  int p = beagle::gpio::GPIOManager::getInstance()->getGpioByKey(pin.c_str());
  return gp->getValue(p);
}

int waitForEdge(unsigned int pin, EDGEVALUE edge) {
  if (edge == NONE) {
    gp->setEdge(pin, beagle::gpio::NONE);
    return gp->waitForEdge(PINVALUE);
  } else if (edge == RISING) {
    gp->setEdge(pin, beagle::gpio::RISING);
    return gp->waitForEdge(pin);
  } else if (edge == FALLING) {
    gp->setEdge(pin, beagle::gpio::FALLING);
    return gp->waitForEdge(pin);
  } else if (edge == BOTH) {
    gp->setEdge(pin, beagle::gpio::BOTH);
    return gp->waitForEdge(pin);
  }
}

// Not implemented by BBB GPIO library
int registerInterrupt(unsigned int pin, EDGEVALUE edge,
                      void (*function)(void)) {
  return -1;
};
}  // namespace GPIOWrapper
