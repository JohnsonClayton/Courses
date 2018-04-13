#include <iostream>
#include "MobilePiano.h"

namespace pianosegway {
  
  MobilePiano::MobilePiano()
    : Piano()
  {
		this._keycount = 32;
  }
  
  void MobilePiano::packUp() override{
	  this.pickUp();
  }
  
  MobilePiano::~MobilePiano() {
	  std::cout << "Mobile piano has been destroyed" << std::endl;
  }
}
