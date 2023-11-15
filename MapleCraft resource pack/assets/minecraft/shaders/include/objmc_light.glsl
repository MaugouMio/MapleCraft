//objmc
//https://github.com/Godlander/objmc

//default lighting
if (isCustom == 0) {
	#ifdef ENTITY
	if (iconMode == 1) { // custom icon item - model
		if (isGUI == 1 && Light1_Direction.g > 0.5)  // is gui
			color = vec4(0);
	}
	else if (iconMode == 2) { // custom icon item - icon
		if (isGUI == 0 || Light1_Direction.g < 0.5) {  // (not gui) or (is inventory doll)
			color = vec4(0);
		}
		else {
			if (ivec3(color.rgb * 255) == ivec3(255,255,254)) {
				float offset = mod(GameTime * 24000, 20);
				float relativePos = mod(color.a * 20 - offset + 20, 20);
				if (relativePos > 0 && relativePos <= 3)
					color = vec4(1,1,0,relativePos/3);
				else if (relativePos > 10 && relativePos <= 13)
					color = vec4(1,1,0,(relativePos-10)/3);
				else if ((relativePos > 3 && relativePos <= 5) || (relativePos > 13 && relativePos <= 15))
					color = vec4(1,1,0,1);
				else
					color = vec4(0);
			}
		}
	}
	#endif
	color *= vertexColor;
}
//custom lighting
else if (noshadow == 0) {
    //normal from position derivatives
    vec3 normal = normalize(cross(dFdx(Pos), dFdy(Pos)));

    //block lighting
    #ifdef BLOCK
    color *= vec4(vec3(clamp(dot(normal, vec3(0.2,1,0)) * 0.5 + 0.6, 0.1,1)), 1.0);
    #endif

    //entity lighting
    #ifdef ENTITY
    //flip normal for gui
    if (isGUI == 1) normal.xz = -normal.xz;
    color *= minecraft_mix_light(Light0_Direction, Light1_Direction, normal, overlayColor);
    #endif
}
color *= lightColor * ColorModulator;