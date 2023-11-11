/*
 * Return proj matrix without fov and hurt rotation effect
 * Will not affect GUI display
 */
mat4 fixProjMat(mat4 ProjMat) {
	if (__isGUI(ProjMat))
		return ProjMat;
	
    return mat4(	0.5,	0.0,								0.0,			0.0,
					0.0,	0.888,	0.0,			0.0,
					0.0,	0.0,								ProjMat[2][2],	-1.0,
					0.0,	0.0,								ProjMat[3][2],	0.0		);
}