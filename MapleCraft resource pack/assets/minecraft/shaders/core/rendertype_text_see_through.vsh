#version 150

#moj_import <vsh_util.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;

uniform sampler2D Sampler0;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;

out vec4 vertexColor;
out vec2 texCoord0;

void main() {
	mat4 FixProjMat = fixProjMat(ProjMat);
	gl_Position = FixProjMat * ModelViewMat * vec4(Position, 1.0);

	// mob hp shadow
	ivec4 vertexTexel = ivec4(texture(Sampler0, UV0) * 255);
	if (vertexTexel == ivec4(1,3,5,255) || vertexTexel == ivec4(1,2,3,3))
		vertexColor = vec4(0.0);
	else
		vertexColor = Color;
	
    texCoord0 = UV0;
}
