#version 150

#moj_import <vsh_util.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV2;

uniform sampler2D Sampler0;
uniform sampler2D Sampler2;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;

uniform vec3 Light0_Direction;
uniform vec3 Light1_Direction;

uniform float GameTime;

out float vertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;

void main() {
	vec3 offsetPosition = Position;
	vec4 finalColor = Color;
	// up lift
	ivec4 vertexTexel = ivec4(texture(Sampler0, UV0) * 255);
	if (vertexTexel.rgb == ivec3(1,3,5)) {
		mat3 WorldMat = getWorldMat(Light0_Direction, Light1_Direction);
		// value : height == 1 : 0.1
		if (vertexTexel.a == 255)  // head hp bar offset
			offsetPosition += WorldMat * vec3(0.0, Color.b * 25.5, 0.0);
		else if (vertexTexel.a == 1)  // text_display offset
			offsetPosition += WorldMat * vec3(0.0, Color.a * 25.5, 0.0);
		finalColor = vec4(1.0);
	}
	// damage number float and fade out
	else if (vertexTexel == ivec4(1,2,3,3)) {
		mat3 WorldMat = getWorldMat(Light0_Direction, Light1_Direction);
		
		float tickOffset = Color.b * 255;
		float tick = mod(mod(GameTime * 24000, 22.0) + 23.0 - tickOffset, 22.0);
		// 0.025 block per tick
		offsetPosition += WorldMat * vec3(0.0, tick * 0.025, 0.0);
		if (tick < 1.0 || tick > 20.0)
			finalColor = vec4(0.0);
		else if (tick > 7.0)
			finalColor = vec4(1.0, 1.0, 1.0, (20.0 - tick) / 13.0);
		else
			finalColor = vec4(1.0);
	}
	
	mat4 FixProjMat = fixProjMat(ProjMat);
	gl_Position = FixProjMat * ModelViewMat * vec4(offsetPosition, 1.0);

    vertexDistance = length((ModelViewMat * vec4(offsetPosition, 1.0)).xyz);
    vertexColor = finalColor;
    texCoord0 = UV0;
}
