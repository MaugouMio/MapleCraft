#version 150

#moj_import <projection.glsl>
#moj_import <vsh_util.glsl>

in vec3 Position;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;

out vec4 texProj0;

void main() {
	mat4 FixProjMat = fixProjMat(ProjMat);
	gl_Position = FixProjMat * ModelViewMat * vec4(Position, 1.0);

    texProj0 = projection_from_position(gl_Position);
}
