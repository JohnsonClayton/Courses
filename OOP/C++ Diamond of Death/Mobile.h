#pragma once

namespace pianosegway {
    class Mobile {
		protected: int _coolness;
		protected: bool _airplanesafe;
		public:  Mobile();
		public:  virtual void pickUp();
		public:  virtual int getCoolness() const;
		public:  virtual bool isAirplaneSafe() const;
		public:  virtual ~Mobile();
    };
}
