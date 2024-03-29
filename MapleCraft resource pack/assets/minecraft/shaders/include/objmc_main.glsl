//objmc
//https://github.com/Godlander/objmc

isCustom = 0;
int corner = gl_VertexID % 4;
ivec2 atlasSize = textureSize(Sampler0, 0);
vec2 onepixel = 1./atlasSize;
ivec2 uv = ivec2((UV0 * atlasSize));
vec3 posoffset = vec3(0);
vec3 rotation = vec3(0);
//read uv offset
ivec4 metauvoffset = ivec4(texelFetch(Sampler0, uv, 0) * 255);
ivec2 uvoffset = ivec2(metauvoffset.r*256 + metauvoffset.g,
                       metauvoffset.b+1); //no alpha due to optifine, max number of faces greatly limited (probably still a couple million more than needed)
//find and read topleft pixel
ivec2 topleft = uv - uvoffset;

#ifdef ENTITY
isGUI = int(__isGUI(ProjMat));
ivec3 colorByte = ivec3(Color.rgb * 255);
iconMode = 0;
#endif

//if topleft marker is correct
if (ivec4(texelFetch(Sampler0, topleft, 0)*255) == ivec4(12,34,56,78)) {
    isCustom = 1;
    //grab meta
    ivec4 meta = getmeta(topleft, 1);
    vec2 autorotate = vec2(getb(meta.r, 6), getb(meta.r, 5));
    noshadow = getb(meta.r, 7);
    //size
    ivec4 metasize = getmeta(topleft, 2);
    ivec2 size = ivec2(metasize.r*256 + metasize.g,
                       metasize.b*256 + metasize.a-128+geta(meta.a,6));
    //nvertices
    ivec4 metanvertices = getmeta(topleft, 3);
    int nvertices = metanvertices.r*16777216 + metanvertices.g*65536 + metanvertices.b*256 + metanvertices.a-128+geta(meta.a,5);
    //frames
    ivec4 metaanim = getmeta(topleft, 4);
    int nframes = clamp(metaanim.r, 1,255);
    int ntextures = clamp(metaanim.g, 1,255);
    float duration = float(metaanim.b + 1);
    bool autoplay = bool(getb(metaanim.a, 6));
    int easing = metaanim.a & 7;
    //data heights
    ivec4 metaheight = getmeta(topleft, 5);
    int vph = metaheight.r*256 + metaheight.g;
    int vth = metaheight.b*256 + metaheight.a-128+geta(meta.a,4);
    //time in ticks
    float time = GameTime * 24000;
    int tcolor = 0;
//colorbehavior
#ifdef ENTITY
    overlayColor = vec4(1);
    int colorbehavior = meta.b;
    if (colorbehavior == 243) { //animation frames 0-8388607
        tcolor = (colorByte.r*65536)%32768 + colorByte.g*256 + colorByte.b;
        //interpolation disabled past 8388608, suso's idea to define starting tick with color
        autoplay = (Color.r <= 0.5);
    } else {
        //bits from colorbehavior
        vec3 accuracy = vec3(255./256.);
        switch ((colorbehavior/64)%4) { //first byte of color
            case 0: rotation.x += colorByte.r; accuracy.r *= 256; break;
            case 1: rotation.y += colorByte.r; accuracy.g *= 256; break;
            case 2: rotation.z += colorByte.r; accuracy.b *= 256; break;
            case 3: tcolor = tcolor * 256 + colorByte.r; break;
        }
        switch ((colorbehavior/16)%4) { //second byte of color
            case 0: rotation.x += colorByte.g; accuracy.r *= 256; break;
            case 1: rotation.y += colorByte.g; accuracy.g *= 256; break;
            case 2: rotation.z += colorByte.g; accuracy.b *= 256; break;
            case 3: tcolor = tcolor * 256 + colorByte.g; break;
        }
        switch (colorbehavior%16) { //third byte of color
            case 0: rotation.x += colorByte.b; accuracy.r *= 256; break;
            case 1: rotation.y += colorByte.b; accuracy.g *= 256; break;
            case 2: rotation.z += colorByte.b; accuracy.b *= 256; break;
            case 3: tcolor = tcolor * 256 + colorByte.b; break;
            case 4: if (Color.b > 0) overlayColor = vec4(customOverlay(colorByte.b),1); break;
        }
        rotation = rotation/accuracy * 2*PI;
    }
#endif
    time = autoplay ? time + (nframes*duration) - mod(tcolor, nframes*duration) : tcolor;
    int frame = int(time/duration) % nframes;
    //relative vertex id from unique face uv
    int id = (((uvoffset.y-1) * size.x) + uvoffset.x) * 4 + corner;
    id += frame * nvertices;
    //calculate height offsets
    int headerheight = 1 + int(ceil(nvertices*0.25/size.x));
    int height = headerheight + (size.y);
    //read data
    ivec2 index = getvert(topleft, size.x, height+vph+vth, id);
    posoffset = getpos(topleft, size.x, height, index.x);
    texCoord = getuv(topleft, size.x, height+vph, index.y) * size;
    if (nframes > 1 && easing > 0) {
        int nids = (nframes * nvertices);
        //next frame
        id = (id+nvertices) % nids;
        index = getvert(topleft, size.x, height+vph+vth, id);
        vec3 posoffset2 = getpos(topleft, size.x, height, index.x);
        //interpolate
        transition = fract(time/duration);
        switch (easing) { //easing
            case 1: //linear
                posoffset = mix(posoffset, posoffset2, transition);
                break;
            case 2: //in-out cubic
                transition = transition < 0.5 ? 4 * transition * transition * transition : 1 - pow(-2 * transition + 2, 3) * 0.5;
                posoffset = mix(posoffset, posoffset2, transition);
                break;
            case 3: //4-point bezier
                //third point
                id = (id+nvertices) % nids;
                index = getvert(topleft, size.x, height+vph+vth, id);
                vec3 posoffset3 = getpos(topleft, size.x, height, index.x);
                //fourth point
                id = (id+nvertices) % nids;
                index = getvert(topleft, size.x, height+vph+vth, id);
                vec3 posoffset4 = getpos(topleft, size.x, height, index.x);
                //bezier
                posoffset = bezier(posoffset, posoffset2, posoffset3, posoffset4, transition);
                break;
        }
    }
//custom entity rotation
#ifdef ENTITY
    isHand = int(ishand(FogStart));
    if (any(greaterThan(autorotate,vec2(0))) && isGUI == 0) {
        //normal estimated rotation calculation from The Der Discohund
        vec3 local = IViewRotMat * Normal;
        float yaw = -atan(local.x, local.z);
        float pitch = -atan(local.y, length(local.xz));
        posoffset = rotate(vec3(vec2(pitch,yaw)*autorotate,0) + rotation) * posoffset * IViewRotMat;
    }
    //pure color rotation
    else if (isHand == 0) {
        posoffset = rotate(rotation) * posoffset * IViewRotMat;
    }
#endif
    //final pos and uv
    Pos += posoffset;
    texCoord = (vec2(topleft.x, topleft.y+headerheight) + texCoord)/atlasSize
                //make sure that faces with same uv beginning/ending renders
                + vec2(onepixel.x * 0.0001 * corner, onepixel.y * 0.0001 * ((corner + 1) % 4));
				
	// custom glowing effect
	ivec3 realVertexTexel = ivec3(texture(Sampler0, texCoord).rgb * 255);
	if (realVertexTexel == ivec3(1,3,5))
		lightColor = vec4(1);
}
// custom glowing effect
else if (metauvoffset.rgb == ivec3(1,3,5)) {
	lightColor = vec4(1);
#ifdef ENTITY
	if (alpha < 0.0)
		vertexColor = Color;
	else
#endif
		vertexColor = vec4(1);
}
// custom offset for billboard entity
#ifdef ENTITY
else if (metauvoffset.rgb == ivec3(1,2,3)) {
	// ignore alpha setting
	alpha = -1;
	lightColor = vec4(1);
	vertexColor = vec4(1);
	mat3 WorldMat = getWorldMat(Light0_Direction, Light1_Direction);
	// blue color : height == 1 : 0.1
	float height = Color.b * 25.5;
	// red color == theta (0.0 ~ 1.0 represents 0 ~ 360 degree)
	// green color : forward == 1 : 0.1
	Pos += WorldMat * vec3(-sin(Color.r*PI*2) * Color.g * 25.5, Color.b * 25.5, cos(Color.r*PI*2) * Color.g * 25.5);
}
// afterimage fade out effect (need to keep Color, but green used for time offset)
else if (metauvoffset.rgb == ivec3(1,2,4) && metauvoffset.a <= 2) {
	lightColor = vec4(1);
	if (metauvoffset.a == 2)  // represent white
		vertexColor = vec4(1);
	else
		vertexColor = vec4(Color.r, 0.0, Color.b, 1.0);
	
	float tickOffset = Color.g * 255;
	float tick = mod(GameTime * 24000, 6.0) - tickOffset;
	if (tick < 0.0) tick += 6.0;
	
	if (tick > 5.0)
		alpha = 0;
	else if (tick < 1.0)
		alpha = 1;
	else
		alpha = (5.0 - tick) / 4.0;
}
// custom icon item - model
else if (colorByte == ivec3(0,218,255)) {
	vertexColor = vec4(1);
	iconMode = 1;
}
// custom icon item - icon
else if (colorByte == ivec3(0,173,255)) {
	vertexColor = vec4(1);
	iconMode = 2;
}
#endif
//debug
//else {
//    posoffset = vec3(gl_VertexID % 4 - 2, gl_VertexID % 4 / 2 * 2, -(gl_VertexID % 4) + 2 * 2);
//    Pos += posoffset;
//    vertexColor = vec4(1.0,0.0,0.0,1.0);
//}