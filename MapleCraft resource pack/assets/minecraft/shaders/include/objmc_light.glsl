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
				float offset = mod(GameTime * 24000, 10);
				float selfPos = color.a * 10 - offset;
				if (selfPos > 0.0 && selfPos <= 1.0)
					color = vec4(1,1,0,selfPos);
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