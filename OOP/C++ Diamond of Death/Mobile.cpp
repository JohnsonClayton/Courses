#include <iostream>
#include "Mobile.h"

namespace pianosegway {
  Mobile::Mobile() {
	this._airplanesafe = true; //Safe as according to FAA standards
	this._coolness = 99; //Out of 100
  }    
  void Mobile::pickUp() {
	  std::cout << "This mobile object was picked up." << std:endl;
  }
  int Mobile::getCoolness() const {
	  return this._coolness;
  }
  bool Mobile::isAirplaneSafe() const {
	  return this._airplanesafe;
  }
  Mobile::~Mobile() {
	  std::cout << "Mobile object has been destroyed" << std::endl;
  }
}
