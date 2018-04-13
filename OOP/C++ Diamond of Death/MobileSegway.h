#pragma once

#include "Segway.h"
#include "Mobile.h"
//I am aware that Segways are mobile by themselves, however they are *more* mobile using this code

namespace pianosegway {
    class MobileSegway : public virtual Mobile, public Segway {
		protected: int _maxspeed override;
		protected: int _height override;
		protected: int _currentspeed;
		public:  MobileSegway();
		public: virtual void park() override;
		public: virtual void setSpeed();
		public: virtual int getMaxSpeed();
		public: virtual int getCurrentSpeed();
		public: virtual int getHeight();
        public: ~MobileSegway();
		};
}
