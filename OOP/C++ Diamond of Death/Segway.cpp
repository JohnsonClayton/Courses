#include "Segway.h"

#include <iostream>

namespace pianosegway {
  Segway::Segway() {
    this._height = 72; //Inches
	this._maxspeed = 12; //Mph
	this._currentspeed = 0; //Mph
  }
    void Segway::park() {
		std::cout << "Segway is parked and looks kind of obnoxious the way it is, frankly." << std:endl;
    }

    double Segway::setSpeed(int newSpeed) const {
        this._currentspeed = newSpeed;
    }

    Segway::~Segway() {
		std::cout << "Segway has been destroyed." << std::endl;
	}
}

