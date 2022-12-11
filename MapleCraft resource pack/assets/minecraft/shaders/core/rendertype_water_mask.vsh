#version 150

#moj_import <vsh_util.glsl>

in vec3 Position;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;

void main() {
	mat4 FixProjMat = fixProjMat(ProjMat);
	gl_Position = FixProjMat * ModelViewMat * vec4(Position, 1.0);
}
