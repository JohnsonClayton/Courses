/*
author: Clayton Johnson
description:
	This is the combination of 2 beautiful objects: a piano and a segway. I couldn't think of anything more exciting
so I hope this works for the grader (Dr. MacEvoy). Please let me know if you would like to see anything else.
*/

#include <iostream>
#include "MobilePianoSegway.h"

namespace pianosegway {
    MobilePianoSegway::MobilePianoSegway()
       : MobileSegway(), MobilePiano()
    {
         this._height = 10; //Additional 4 inches originates from the piano
    }
	MobilePianoSegway::~MobilePianoSegway() {
		std::cout << "This amazing conglomeration of an object has been destroyed." << std::endl;
	}
}
