#version 150

#moj_import <light.glsl>
#moj_import <fog.glsl>

uniform sampler2D Sampler0;

uniform vec4 ColorModulator;
uniform float FogStart;
uniform float FogEnd;
uniform vec4 FogColor;
uniform float GameTime;

uniform vec3 Light0_Direction;
uniform vec3 Light1_Direction;

in float vertexDistance;
in vec4 vertexColor;
in vec4 lightColor;
in vec4 overlayColor;
in vec2 texCoord;
in vec2 texCoord2;
in vec3 Pos;
in float transition;
in float alpha;

flat in int isCustom;
flat in int isGUI;
flat in int isHand;
flat in int noshadow;
flat in int iconMode;

out vec4 fragColor;

void main() {
    vec4 color = texture(Sampler0, texCoord);
	
	//custom lighting
	#define ENTITY
	#moj_import<objmc_light.glsl>

	// alpha fade in
	if (alpha >= 0.0)
		color.a *= alpha;

    if (color.a < 0.02) discard;
    fragColor = linear_fog(color, vertexDistance, FogStart, FogEnd, FogColor);
}