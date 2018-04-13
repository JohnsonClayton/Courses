#pragma once

namespace pianosegway {
  class Piano {
	  protected: int _keycount;
	  public: Piano();
	  public: virtual void packUp();
	  public: virtual int getKeys();
	  public: virtual ~Piano();
  };
} 
