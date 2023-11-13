//objmc
//https://github.com/Godlander/objmc

//default lighting
if (isCustom == 0) {
	#ifdef ENTITY
	if (ivec3(color.rgb * 255) == ivec3(0,1,0)) {
		if (isGUI == 0 || Light1_Direction.g < 0.5)  // (not gui) or (is inventory doll)
			color = vec4(0);
		else {
			float offset = mod(GameTime * 24000, 10);
			float selfPos = color.a * 10 - offset;
			if (selfPos > 0.0 && selfPos <= 1.0)
				color = vec4(1,1,0,selfPos);
			else
				color = vec4(0);
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