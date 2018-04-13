#include <iostream>
#include "MobileSegway.h"

namespace pianosegway {
	MobileSegway::MobileSegway() {
		this._maxspeed = 15; //Mph
		this._height = 6; //Inches
	}
    void MobileSegway::park() {
		this.pickUp();
	}
	MobileSegway::~MobileSegway() {
		std::cout<<"MobileSegway has been annihilated" << std::endl;
	}
}
