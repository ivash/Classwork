/* 
 * File:   Move.cpp
 * Author: sunnypatel
 * 
 * Created on November 16, 2013, 4:21 PM
 */

#include "Move.h"

Move::Move() {
}

Move::Move(const Move& orig) {
}

Move::~Move() {
}

void Move::setPositions(int a, int b){
	this->pos1 = a;
	this->pos2 = b;
}