#version 150

#moj_import <fog.glsl>
#moj_import <vsh_util.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;
uniform mat4 TextureMat;
uniform int FogShape;

out float vertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;

void main() {
	mat4 FixProjMat = fixProjMat(ProjMat);
	gl_Position = FixProjMat * ModelViewMat * vec4(Position, 1.0);

    vertexDistance = fog_distance(ModelViewMat, Position, FogShape);
    vertexColor = Color;
    texCoord0 = (TextureMat * vec4(UV0, 0.0, 1.0)).xy;
}
