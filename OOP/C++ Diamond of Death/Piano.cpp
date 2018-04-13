#include "Piano.h"
#include <iostream>

namespace pianosegway {
  Piano::Piano() {
	  this._keycount = 88;
  }

  void Piano::packUp() {
      std::cout << "Piano is now packed up but is taking up a ton of space." << std::endl;
  }

  void Piano::getKeys() {
	  return this._keycount;
  }

  Piano::~Piano() { 
	std::cout << "Piano is now cleaned up, however is large." << std::endl;
	}
}
