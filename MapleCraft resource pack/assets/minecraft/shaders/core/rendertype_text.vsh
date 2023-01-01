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

out float vertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;

void main() {
	vec3 offsetPosition = Position;
	vec4 finalColor = Color;
	// mob hp up lift
	ivec4 vertexTexel = ivec4(texture(Sampler0, UV0) * 255);
	if (vertexTexel == ivec4(1,3,5,255) || vertexTexel == ivec4(0,255,0,255) || vertexTexel == ivec4(170,0,0,255)) {
		mat3 WorldMat = getWorldMat(Light0_Direction, Light1_Direction);
		// blue color : height == 1 : 0.2
		offsetPosition += WorldMat * vec3(0.0, Color.b * 51, 0.0);
		finalColor = vec4(1.0);
	}
	
	mat4 FixProjMat = fixProjMat(ProjMat);
	gl_Position = FixProjMat * ModelViewMat * vec4(offsetPosition, 1.0);

    vertexDistance = length((ModelViewMat * vec4(offsetPosition, 1.0)).xyz);
    vertexColor = finalColor;
    texCoord0 = UV0;
}
