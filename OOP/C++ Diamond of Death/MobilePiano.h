#pragma once

#include "Piano.h"
#include "Mobile.h"

namespace pianosegway {
    class MobilePiano : public Piano, public virtual Mobile {
	    public: int _keycount override;
	    public: MobilePiano();
		public: virtual void packUp() override; //Maybe throw const in front of override
		public: virtual int getKeyCount();
		public: virtual ~MobilePiano();    
  };
} 
