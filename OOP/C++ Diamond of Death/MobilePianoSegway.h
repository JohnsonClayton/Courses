#pragma once

#include "MobilePiano.h"
#include "MobileSegway.h"

namespace pianosegway {
    class MobilePianoSegway : public MobilePiano, public MobileSegway {
		protected: int _keycount;
		protected: int _maxspeed;
		protected: int _currentspeed;
		protected: int _height override;
		protected: bool airplanesafe;
		protected: int _coolness;
		public: MobilePianoSegway();
		
		public: void packUp();
		public: void park();
		
		public: void setSpeed();
		
		public: int getMaxSpeed();
		public: int getCurrentSpeed();
		public: int getHeight();
		public: bool isAirplaneSafe();
		public: int getCoolness();
		
		public: ~MobilePianoSegway();
    };
}