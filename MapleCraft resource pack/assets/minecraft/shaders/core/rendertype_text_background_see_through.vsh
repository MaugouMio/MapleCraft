#version 150

#moj_import <vsh_util.glsl>

in vec3 Position;
in vec4 Color;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;

out vec4 vertexColor;

void main() {
	mat4 FixProjMat = fixProjMat(ProjMat);
    gl_Position = FixProjMat * ModelViewMat * vec4(Position, 1.0);

    vertexColor = Color;
}
