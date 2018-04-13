#pragma once

namespace pianosegway {
    class Segway {
		protected: int _height;
		protected: int _maxspeed;
		protected: int _currentspeed;
		public: Segway();
		public: virtual void park();
		public: virtual void setSpeed(int newSpeed) const;
		public: virtual ~Segway();
    };
}
